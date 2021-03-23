# import os
# from email.parser import Parser
# for root, dirs, files in os.walk('enron_email_corpus_1'):
#      for file in files:
#         print(root)
#         print(dirs)
#         print("files",file)
# champ_ids = [0, 36, 85]

# champ_dict = {"Bob" :[85,0] , "Carly": [22,45], "Freddy" : 85, "Megan" : 14, "Dilbert" : 69}
# for k, v in champ_dict.items():
#    try:
#       for i in v:
#          print("v",v)
#          if i in champ_ids:
#             print("i",i)
#             print(k)
#    except:
#       if v in champ_ids:
#          print("k_",k)




# red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
# "skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}

# from_ = "jeff.skilling@enron.com"
# for k, v in red_flags.items():
#       try:
#          for i in v:
#             if i == from_:
#                print("i",i)
#             else:
#                pass
#       except:
#             pass
A=[]
A = ['gmarmol@gmarmol.com,kenneth.lay@enron.com'] 
to_new = [s.replace(',', '') for s in A]
print(to_new)