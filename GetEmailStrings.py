from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import json

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def getEmails():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    results = service.users().messages().list(userId='me', q='from:alangcha@usc.edu').execute()
    msg_ids = [item['id'] for item in results['messages']]

    email_strings = []

    for msg_id in msg_ids:
        message = service.users().messages().get(userId='me', id=msg_id).execute()
        try:
            data = message['payload']['parts'][0]['body']['data']
        except KeyError:
            pass
        try:
            data = message['payload']['parts'][0]['parts'][0]['body']['data']
        except KeyError:
            pass
        clean_one = data.replace("-","+") # decoding from Base64 to UTF-8
        clean_one = clean_one.replace("_","/") # decoding from Base64 to UTF-8
        clean_two = base64.b64decode (bytes(clean_one, 'UTF-8')) # decoding from Base64 to UTF-8
        soup = BeautifulSoup(clean_two , "lxml" )
        mssg_body = str(soup.body())
        lines = mssg_body.split('\n')
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line!='']
        lines = [line for line in lines if line[:5]!='<http']
        lines = [line for line in lines if line[:6]!='</http']
        sub = lines[3]
        lines = lines[5:]
        lines = " ".join(lines)
        dict = {}
        dict['subject'] = sub
        dict['body'] = lines
        email_strings.append(dict)
    return email_strings
