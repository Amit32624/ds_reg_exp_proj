from email.parser import Parser
from email.policy import default

red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
"skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
# red_flags = {"lay-k":"klay@enron.com",
# "skilling-j": "jeff.skilling@enron.com"}
import os
for root, dirs, files in os.walk('enron_email_corpus'):
    for file in files:
        # print(root)
        # print("files",file)
        # print(dirs)
        with open(os.path.join(root, file), "r") as auto:
            headers = Parser().parse(auto)
            to =[]
            from_raw =(headers['from'])
            from_ = from_raw
            # print(from_)
            for key, val in red_flags.items():
                try:
                    for i in val:
                        if i ==from_:
                            # print(i)
                            # print("from",i)
                            to_raw = (headers['to']).split()
                            # print("to_raw",to_raw)
                            to_new = [s.replace(',', '') for s in to_raw]
                            # print(to_new)
                            for k, v in red_flags.items():
                                try:
                                    for l in v:
                                        if l in to_new:
                                            # print(l)
                                            # m =[]
                                            m = (headers['to']).split()
                                            m1 = [s.replace(',', '') for s in m]
                                            # print(m1)
                                            # print(len(m1))
                                            if len(m1) <= 20 :
                                                print(file)
                                                print('Date: %s' % headers['Date'])
                                                print('From: %s' % headers['from'])
                                                # print('To:%s' % headers['To'])
                                                print('To:',l)
                                                print('Subject: %s' % headers['subject'])
                                                print("Email",headers.email.message.message)
                                            else:
                                                pass
                                        else:
                                            if v in to_new:
                                                print("Random",i)
                                                print('Date: %s' % headers['Date'])
                                                print('From: %s' % headers['from'])
                                                print('To:%s' % headers['To'])
                                                print('Subject: %s' % headers['subject'])
                                            # print(headers.get_payload())
                                except:
                                    pass
                                        
                        else:
                            pass
                except:
                    pass

 

