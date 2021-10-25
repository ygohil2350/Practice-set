'''
Sorting Boxes
The parcel section of the Head Post Office is in a mess.  The parcels that need to be loaded to the vans have been lined up in a row in an arbitrary order of weights.  The Head Post Master wants them to be sorted in the increasing order of the weights of the parcels, with one exception.  He wants the heaviest (and presumably the most valuable) parcel kept nearest his office.

Problem Description
The parcel section of the Head Post Office is in a mess.  The parcels that need to be loaded to the vans have been lined up in a row in an arbitrary order of weights.  The Head Post Master wants them to be sorted in the increasing order of the weights of the parcels, with one exception.  He wants the heaviest (and presumably the most valuable) parcel kept nearest his office.
You and your friend try to sort these boxes and you decide to sort them by interchanging two boxes at a time.  Such an interchange needs effort equals to the product of the weights of the two boxes. 
The objective is to reposition the boxes as required with minimum effort.

Input
The first line consists of two space separated positive integers giving the number of boxes (N) and the position of the Head Post Masterâ€™s office (k) where the heaviest box must be.
The second line consists of N space separated positive integers giving the weights of the boxes.  You may assume that no two weights are equal.

Output
The output is one line giving the total effort taken to get the boxes in sorted order, and the heaviest in position k.
Constraints
N<=50
Weights <= 1000
Difficulty Level
Complex
Time Limit (secs)
1
Examples
Example 1
Input
5 2
20 50 30 80 70
Output
3600
Explanation
There are 5 boxes (N=5) and the heaviest box must be in position 2 (k=2).  If we look at the final order (sorted, with the heaviest at position 2), it should be 20 80 30 50 70.  If we look at this, we notice that only the 50 and the 80 parcels need to be exchanged.  As this takes effort of the product of the weights, the effort is 4000.   
Further reduction can be obtained if we use the smallest package (20) as an intermediary.  If we exchange 20 with 50 (effort 1000), then with 80 (effort 1600) and back with 50 again (effort 1000), the effect is the same, with a total effort of 3600 (less th an the effort obtained by the direct move)an the effort
The results after the optimal sequence of exchanges are
50 20 30 80 70
50 80 30 20 70
20 80 30 80 70
As this takes an effort of 3600, the output is 3600.
Example 2
Input
6 3
30 20 40 80 70 60
Output
7600
Explanation
There are 6 parcels, and the heaviest should be at position 3.  Hence the final order needs to be 20 30 80 40 60 70.  If we look at the initial position, we see that 20 and 30 need to be exchanged (effort 600), 40 and 80 need to be exchanged (effort 3200) and 60 and 70 need to be exchanged (effort 4200).  Hence the total effort is 600+3200+4200=8000. 
If we use the same approach as in Example 1, we get the following efforts
(600)   20 30 40 80 70 60
(3200) 20 30 80 40 70 60   
(1200) 60 30 80 40 70 20
(1400) 60 30 80 40 20 70
(1200) 20 30 80 40 60 70
A total effort of 7600 is obtained rather than an effort of 8000, which is the outpu
'''



n,k = map(int,input().split())
lst = list(map(int,input().split()))
eff=0
if(lst[0]!=min(lst)):
    temp=min(lst)
    eff=eff+(lst[0]*temp)
    lst[lst.index(min(lst))]=lst[0]
    lst[0]=temp

if(lst[k-1]!=max(lst)  and  (lst[k-1]*max(lst)  <  (2*(lst[0]*lst[k-1])+lst[0]*max(lst)))):
    temp=max(lst)
    eff=eff+(lst[k-1]*max(lst))
    lst[lst.index(max(lst))]=lst[k-1]
    lst[k-1]=temp
    
else:
    eff=eff+( 2*(lst[0]*lst[k-1]) + lst[0]*max(lst) )
    temp=max(lst)
    lst[lst.index(max(lst))]=lst[k-1]
    lst[k-1]=temp


for i in range(len(lst)):
   for j in range(i,len(lst)):
        if(i==k-1 or j==k-1):
            continue
        elif(lst[i]>lst[j]):
            if((lst[i]*lst[j])>(lst[i]*lst[0]+lst[j]*lst[0])):
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
                eff=eff+(2*(lst[i]*lst[0])+(lst[j]*lst[0]))
            else:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
                eff=eff+(lst[i]*lst[j])

print(eff)
