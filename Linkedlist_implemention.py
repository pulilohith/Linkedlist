class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class LL:
    def __init__(self):
        self.head=self.tail=None 
    def add(self,data):
        N1=Node(data)
        if(self.head==None):
            self.head=self.tail=N1
        else:
            self.tail.next=N1
            self.tail=N1
    def addatbeginning(self,data):
        N1=Node(data)
        if(self.head==None):
            self.head=self.tail=N1
        else:
            N1.next=self.head
            self.head=N1
    def prints(self,head):
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
    def find(self,data):
        temp=self.head
        while(temp!=None):
            if(temp.data==data):
                return temp
            temp=temp.next 
    def insertion(self,data,databefore):
        N1=Node(data)
        temp=self.find(databefore)
        if(temp!=None): 
            N1.next=temp.next
            temp.next=N1
            if(self.tail==temp):
                self.tail=N1
        else:
            return "No element"
    def deletion(self,data):
        if(self.head==None):
            return "LL is empty"
        temp=self.find(data)
        if(temp!=None):
            if(self.head==temp):
                self.head=temp.next 
                if(self.tail==temp):
                    self.tail=None
            else:
                temp1=self.head
                while(temp1!=None):
                    if(temp1.next==temp):
                        temp1.next=temp.next
                        break
                    temp1=temp1.next
                if(self.tail==temp):
                    self.tail=temp1
        else:
            return "No element"   
    def mid(self,head):
        if(not head):
            return
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next 
        return slow 
    def mergeutil(self,left,right):
        result=None
        if(left==None):
            return right 
        if(right==None):
            return left
        if(left.data<right.data):
            result=left
            result.next=self.mergeutil(left.next,right)
        else:
            result=right
            result.next=self.mergeutil(left,right.next)
        return result
    def mergesort(self,head):
        if(head.next==None or head==None):
            return head
        middle=self.mid(head) 
        midnex=middle.next
        middle.next=None
        left=self.mergesort(head)
        right=self.mergesort(midnex)
        result=self.mergeutil(left,right) 
        return result 
    def partition(self,head,end):
        if(head==end or head==None or end==None):
            return head
        current=head 
        prev=head
        pivot=end.data 
        while(head!=end):
            if(head.data<pivot):
                prev=current
                current.data,head.data=head.data,current.data
                current=current.next
            head=head.next
        current.data,end.data=end.data,current.data
        return prev
    def quicksort(self,head,end):
        if(head==end):
            return 
        part=self.partition(head,end) 
        self.quicksort(head,part)
        if(part!=None and part==head):
            self.quicksort(part.next,end)
        elif(part!=None and part.next!=None): 
            self.quicksort(part.next.next,end) 
    def loopdetection(self,head):
        if(not head):
            return
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            if(slow==fast):
                break
            slow=slow.next
            fast=fast.next.next 
        slow=head
        prev=fast
        while(slow.next!=fast.next):
            slow=slow.next
            fast=fast.next
    def swap2num(self,head):
        while(head!=None and head.next!=None):
            head.data,head.next.data=head.next.data,head.data
            head=head.next.next  
    def revknodex(self,head,k):
        prev=None
        current=head
        nex=None
        count=0
        
        while(count<k and current!=None):
           
            nex=current.next
            current.next=prev
            prev=current
            current=nex  
            count+=1 
        if (nex):
            head.next=self.revknodex(nex,k)
        return prev
    def swapknode(self,head,k):
        no_of_elements=0 
        temp=head
        while(head!=None):
            no_of_elements+=1 
            head=head.next 
        no_of_elements-=k-1
        count=0
        while(temp!=None):
            count+=1 
            if(count==k):
                node1=temp
            if(count==no_of_elements):
                node2=temp
            temp=temp.next
        node1.data,node2.data=node2.data,node1.data 
    def deletduplicates(self,head):
        while(head!=None):
            j=head
            while(j.next and j.data==j.next.data):
                j=j.next 
            head.next=j.next  
            head=head.next
        self.prints(head)
            
        
L1=LL() 
L1.add(78)

L1.insertion(32,78)
L1.add(89)
L1.add(89)
L1.add(90)
L1.add(789)
L1.add(789)
print(L1.deletion(34))
L1.prints(L1.head)
print() 
L1.deletduplicates(L1.head)
L1.prints(L1.head)
print()
L1.swap2num(L1.head) 
L1.prints(L1.head)
print()
L1.swapknode(L1.head,2)
L1.prints(L1.head)
print()
L1.prints(L1.revknodex(L1.head,3))
print()
L1.prints(L1.mergesort(L1.head))
print() 



L1.swapknum(L1.head,3)
temp=L1.head
while(temp.next!=None):
    temp=temp.next  
L1.quicksort(L1.head,temp)
L1.prints(L1.head) 





