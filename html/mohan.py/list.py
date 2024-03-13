x=['ramesh','mohan','prem','suresh','mayil']
for i in x:
    #print(i)
    m=i.endswith('sh')
   # print(m)
    if m==True:
        x.remove(i)
print(x)
        
        