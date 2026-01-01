#broot force
# n=[1,2,3,4,2,5,6,7,6,10]
# m=[1,10,22,111,4,6,7,5,3]
# for i in range(len(m)):
#     count=0
#     for j in range(len(n)):
#         if m[i]==n[j]:
#             count+=1
#     print(count)
# #optimal approch
# dict={}

s="aasdadhfuhuleaa"
b=["a","b","c","s","d","g","f","n"]
for i in  b:
    count=0
    for j in s:
        if j==i:
            count+=1
    print(i ,"=", count)