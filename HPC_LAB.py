#print "hello"
import pandas as pd
x=pd.read_csv('reservation.csv')
print x
a=['1','2','3','4','5']
maxtemp=0
for i in range(0,4):
    temp=0
    for j in a:
        if (x.loc[i,j]=='x'):
            temp+=1;
    if (temp>maxtemp):
        maxtemp=temp
print maxtemp
        
#a=['1','2','3','4','5']
#maxtemp=0
l=[]
for i in range(0,4):
    temp=-1
    for j in a:
        if (x.loc[i,j]=='x' and temp==-1):
            temp=j;
        elif (x.loc[i,j]=='x' and temp!=-1):
            temp=int(j)-int(temp)
            if (temp not in l):
                l.append(temp)
l.sort()
print l
            
size=l[-1]
collision_vect=[0]*size
for i in l:
    collision_vect[-i]=1
coll_vect=""    
for i in collision_vect:
    coll_vect+=str(i)
#coll_vect=int(coll_vect)
print coll_vect



test=int(coll_vect,2)
states=[test]
tempp=0
final=[]
while 1:
    varlen=len(states)
    if (tempp==varlen):
        break
    else:
        tempfinal=[]
        tempb=bin(states[tempp])[2:]
        #print tempb
        for xf in range(0,len(tempb)):
            if tempb[xf]=='0':
                #print xf
                trtr=((states[tempp]>>(len(tempb)-xf)) | test)
                #print trtr,"here"
                tempfinal.append(trtr)
                tempfinal.append(len(tempb)-xf)
                if (trtr not in states):    
                    states.append(trtr)
        final.append(tempfinal)
        tempp+=1
        #print "tempp is ",tempp
for i in range(0,len(states)):
    states[i]=bin(states[i])[2:]
        
#print final
new_final=[]
for k in final:
    tempnew_final=[coll_vect,len(coll_vect)+1]
    for i in range(0,len(k)):
        if (i%2==0):
            tata=k[i]
            #print tata
            tempnew_final.append(bin(tata)[2:])
        else:
            tempnew_final.append(k[i])
    new_final.append(tempnew_final)
#print "final graph is ",new_final
my_dict={}
for i in range(0,len(states)):
    my_dict[states[i]]=new_final[i]
   
print "final graph is ", my_dict


visited=[states[0]]
#cur_sum=0
def findGREEDY(qq,cur_sum,tot,minn):
    #print visited
    pp=my_dict[qq]
    if (len(pp)==0):
        return minn;
    for op in range(0,len(pp),2):
        if (pp[op] not in visited):
            visited.append(pp[op])
            minn=min(minn,findGREEDY(pp[op],cur_sum+pp[op+1],tot+1,minn))
            visited.remove(pp[op])
        else:
            visited.append(pp[op])
            print visited
            visited.remove(pp[op])
            cur_sum=cur_sum+pp[op+1]
            tot+=1
            #print "here",pp[op],cur_sum,tot
            #minn=cur_sum/tot
            minn= cur_sum/tot
            print "latency is",cur_sum/tot
    return minn
minn=1000
findGREEDY(states[0],0,0,minn)
#print minn