from GetEmailStrings import getEmails
from parseEmail import entities_text
from Samsort import samsort
from building import buildings_dict
import re
import json

dlist = []
bdict = buildings_dict()
emails_dict = getEmails()

i=1
for email in emails_dict:
    print("Email "+str(i)+": success")
    edict = entities_text(email['body'])
    edict['event'] = email['subject'].split(': ')[1]

    sdict = samsort(email['body'])
    if sdict['time']:
        edict['time'] = sdict['time']
    if sdict['date']:
        edict['date'] = sdict['date']
    if sdict['location']:
        for key, value in bdict.items():
            if key == sdict['location'].split(" ")[0]:
                edict['address'] = value
        edict['location'] = sdict['location']
    dlist.append(edict)
    i = i+1
print("All info sucessfully collected.")
with open('data.json', 'w') as outfile:
    json.dump(dlist, outfile)
