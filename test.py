# # import itertools
# # from typing import List
# # from typing import List
# from itertools import permutations
# from itertools import combinations_with_replacement
# from os import close
# list1 = [1,2,3,4,5,6]
# # l = list[a,b,c,d,e,f,d,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
# ll = ['a','b','c','d','e','f','d','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# # for i in range(1,10):
# #     a = list(itertools.combinations(ll,6))
# # for i in range (1,230230):
# #     for result in permutations(ll,i):
# #         print (result)
# ff = open ('test1.py','a+')
# for c in combinations_with_replacement(ll,1):
#     ff.write(f" {c} \n")
#     # print >> f , c + '\n'    
#     print (c)
# ff.close()
# # print (ll[1])
# # print [a]

dict = {'Name': 'Runoob', 'Age': 27}
print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))
