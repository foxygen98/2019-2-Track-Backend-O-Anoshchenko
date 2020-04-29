from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from chats.models import Chat, Message, Attachment
from users.models import User, Member
from chats.form import MessageForm, ChatForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
import cProfile, pstats
from chats.tasks import send_email
from cent import Client

@login_required
def chat_list(request, user_id):
    if request.method == "GET":
        user = get_object_or_404(User, id=user_id)
        chats_id = Member.objects.filter(user=user_id).values('chat_id')
        return JsonResponse({'chats' : list(chats_id)})
    return HttpResponseNotAllowed(['GET'])

@login_required
def one_chat(request, chat_id):
    if request.method == "GET":
        chat = Chat.objects.all()
        chat = chat.get(id=chat_id)
        return JsonResponse({'chat': chat.id, 'topic': chat.topic, 'last message': chat.last_message})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
# @login_required
def create_chat(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        user_id = request.POST.get('user')
        if form.is_valid():
            chat = form.save()
            user = User.objects.get(id=user_id)
            member = Member.objects.create(user=user, chat=chat)
            send_email.delay([user.email])
            return JsonResponse({'status': 'success!', 'id': chat.id, 'user_email': user.email})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            CentrifugeClient.publish(message)
            return JsonResponse({'user' : message.user_id, 'message': message.content})
        return JsonResponse({'errors' : form.errors})
    return HttpResponseNotAllowed(['POST'])


@login_required
def list_messages(request, chat_id):
    if "GET" == request.method:
        messages = Message.objects.values('chat', 'user', 'content', 'added_at')
        messages = messages.filter(chat=chat_id)
        return JsonResponse({'messages': list(messages)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
@login_required
def read_message(request):
    if request.method == "POST":
        member_id = request.POST.get('member')
        member = get_object_or_404(Member, id = member_id)
        chat_id = member.chat.id
        messages = Message.objects.all().filter(chat_id = chat_id).order_by('added_at')
        member.last_read_message_id = messages.last().id
        return JsonResponse({'last_message' : member.last_read_message_id})
    return HttpResponseNotAllowed(['POST'])


@login_required
def upload_file (file):
    openfile = FileField(open(file, 'rb'))
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id='shbHSMGMH3z9M5pZuz5rTK',
        aws_secret_access_key='hECFe4Cq1UDQipSPDhv1PNGmLdEbpoQDGZWohESPtSi')
    return s3_client.put_object(Bucket=AWS_STORAGE_BUCKET_NAME, key='attachment', body=openfile.read())

class ChatViewSet(viewsets.ModelViewSet):
    
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def get_serializer_class(self):
        if self.action == 'chat_list':
            return MemberSerializer
        return ChatSerializer

    @action(detail=True, methods=['GET'])
    def one_chat(self, request, pk):
        chats = self.get_queryset()
        chat = get_object_or_404(chats, id=pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(chat, many=False)
        return Response({'chat': serializer.data})

    @action(detail=True, methods=['GET'])
    def chat_list(self, request, pk):
        members = Member.objects.filter(user_id=pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(members, many=True)
        return Response({'chats': serializer.data})

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    def create_chat(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'successfully'})
        return Response({'errors' : serializer.errors})

class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    @action(detail=True, methods=['GET'])
    def list_messages(self, request, pk):
        messages = self.get_queryset().filter(chat_id=pk)
        serializer_class = self.get_serializer_class()
        serializers = serializer_class(messages, many=True)
        return Response({'messages': serializers.data})

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    def send_message(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.POST)
        if serializer.is_valid():
            message = serializer.save()
            CentrifugeClient.publish(message)
            return Response({'status': 'successfully'})
        return Response({'errors' : serializer.errors})

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    def read_message(self, request):
        member_id = request.POST.get('member')
        member = get_object_or_404(Member, id=member_id)
        chat_id = member.chat.id
        messages = self.get_queryset().filter(chat_id=chat_id).order_by('added_at')
        member.last_read_message_id = messages.last().id
        return Response({'status': 'successfully'})

class CentrifugeClient():
    url = 'http://localhost:8001'
    api_key = '7ce4568b-accc-4bb9-9daa-a5ec09c2f8c2'
    channel = 'centrifuge'
    client = Client(url, api_key, timeout=1)

    @classmethod
    def publish(cls, message):
        data = {
            'status': 'ok',
            'message': {
                'id': message.id,
                'user': message.user_id,
                'content': message.content,
            }
        }
        cls.client.publish(cls.channel, data)
