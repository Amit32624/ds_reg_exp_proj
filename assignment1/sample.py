A ='''
     Marriage of MARY ROCHE
    in 1880
    Group Registration ID	N/R
    SR District/Reg Area	Cork
    Returns Year	1880
    Returns Quarter	4
    Returns Volume No	5
    Returns Page No	0110
        Marriage of MARY ROCHE
    in 1880
    Group Registration ID	N/R
    SR District/Reg Area	Enniscorthy
    Returns Year	1880
    Returns Quarter	3
    Returns Volume No	4
    Returns Page No	276
    '''
# print(A)

import re
import collections
nameRegex = re.compile(r'Marriage of (.*?)',re.DOTALL)
m = nameRegex.findall(A)
B = (re.sub(r"[\s]*", "", A))
print('B',B)
lines1_common =(re.split("Marriageof",B ))
print("lines1_common",lines1_common)
remove_space = [elem for elem in lines1_common if elem.strip()]
print(remove_space)




#############
info = []
info.clear()
county_name = []
for i in remove_space:
          county_name.clear()
          name = re.findall('^[A-Z]+', i)
          print("name",name)
          num = re.findall('[0-9]+', i)
          print("num",num)
          district = re.findall('(?<=RegArea).*(?=ReturnsYear)', i)
          print("county_district",district)
          str1 = ''.join(district)
          print("str1",str1)
          str1=re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', str1)
          print("str1",str1)
          county_name.append(str1)
          name.extend(num)
          print("name",name)
          name[2:2] = county_name
          print("countttttt",county_name)
          info.append(name)

print("info",info)
calB =info
print(type(calB))
# calB.append(info)
print("calB",calB)
string = 'Cork'
print(re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', string))
count =0
for i in info:  ##  using finditer to find possible match
    count += 1
    str1 = ''.join(i[1:])
    print("new",str1)
    count_m =0
    for j in calB:
        count_m += 1
        str2 = ''.join(j[1:])
        print("str2",str2)

        if collections.Counter(str1) == collections.Counter(str2):

        # for match in re.finditer(str1,str2):
        #     print("macth")

