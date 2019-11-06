import datetime

def handler(environ, start_response):
    now = datetime.datetime.now()
    now_string = now.strftime('%d-%m-%Y %H:%M')
    result = b'Current date and time: ' + str.encode(now_string) + b'\n'
    headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(result)))]
    start_response('200 OK', headers)
    return [result]
