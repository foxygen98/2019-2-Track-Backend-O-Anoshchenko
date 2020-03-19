#! /usr/bin/env python

import boto3

if __name__=="__main__":
    session = boto3.session.Session()
    s3_client = session.client(service_name='s3',
			       endpoint_url='http://hb.bizmrg.com',
			       aws_access_key_id='shbHSMGMH3z9M5pZuz5rTK',
			       aws_secret_access_key='hECFe4Cq1UDQipSPDhv1PNGmLdEbpoQDGZWohESPtSi')
    print("Successfully init")
