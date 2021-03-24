from email.parser import Parser
from email.policy import default

red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
"skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
import os
for root, dirs, files in os.walk('zufferli-j'):
    
    for file in files:
        # print(root)
        # print("files",file)
        with open(os.path.join(root, file), "r") as auto:
            headers = Parser().parse(auto)
            to =[]
            # print("headers",headers.email.message.message)
            # print('To: %s' % headers['to'])
            # to_raw = (headers['to']).split()
            # to_new = [s.replace(',', '') for s in to_raw]
            from_raw =(headers['from'])
            from_ = from_raw
            for key, val in red_flags.items():
                try:
                    for i in val:
                        if i ==from_:
                            # print("from",i)
                            to_raw = (headers['to']).split()
                            # print("to_raw",to_raw)
                            to_new = [s.replace(',', '') for s in to_raw]
                            # print(to_new)
                            for k, v in red_flags.items():
                                try:
                                    for l in v:
                                        if l in to_new:
                                            print(file)
                                            # print("i",i)
                                            print('Date: %s' % headers['Date'])
                                            print('From: %s' % headers['from'])
                                            print('To:%s' % headers['To'])
                                            print('Subject: %s' % headers['subject'])
                                            print("Email",headers.email.message.message)

                                            # print(headers.get_payload())
                                except:
                                    if v in to_new:
                                        print("Random",i)
                                        print('Date: %s' % headers['Date'])
                                        print('From: %s' % headers['from'])
                                        print('To:%s' % headers['To'])
                                        print('Subject: %s' % headers['subject'])
                                        # print(headers.get_payload())
                                        
                        else:
                            pass
                except:
                    pass

 

