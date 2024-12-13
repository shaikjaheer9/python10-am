# names={'val':{10:20,2:3}}
# print(names['val'][2])

# dct={'a':20,'n':3}
# for x,y in dct.items():
#     print(x,y)

# v={}
# v['name']='arjun'
# v['age']=22
# print(v)

ticktes=[1,2,3,4,5,6]
print('avilable tickets',ticktes)
q=int(input('enter how many ticktes you want'))
val={}
for x in range(q):
    q=int(input('enter seat number'))
    ticktes.remove(q)
    name=input('enter name')
    val[q]=name
    print(val)
    print('avilable tickets',ticktes)






