import json
filejson = json.load(open('message_1.json'))
messages = []
for message in filejson['messages']:
    print(message)
    if message['is_unsent'] == False:
        try:
            messages.append("{}: {}".format(message['sender_name'], message['content']))
        except:
            try:
                for i in range(0,len(message['photos'])):
                    messages.append("{}: {}".format(message['sender_name'], message['photos'][i]['uri']))
            except:
                try:
                    for i in range(0,len(message['files'])):
                        messages.append("{}: {}".format(message['sender_name'], message['files'][i]['uri']))
                except:
                    try:
                        for i in range(0,len(message['audio_files'])):
                            messages.append("{}: {}".format(message['sender_name'], message['audio_files'][i]['uri']))
                    except:
                        try:
                            for i in range(0,len(message['videos'])):
                                messages.append("{}: {}".format(message['sender_name'], message['videos'][i]['uri']))
                        except:
                            try:
                                messages.append("{}: {}".format(message['sender_name'], message['sticker']['uri']))
                            except:
                                for i in range(0,len(message['gifs'])):
                                    messages.append("{}: {}".format(message['sender_name'], message['gifs'][i]['uri']))
                                
                            
    else:
        pass
messages.reverse() #we have to do this because facebook is dumb and provides messages in reverse order... for some reason
with open('fixed_messages.txt', 'w') as f:
    for i in messages:
        f.write(i+'\n')
