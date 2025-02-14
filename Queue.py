def Enqueue(data):
    global front 
    global rear 
    if front==rear== -1:
        queue.append(data)
        front=0; rear=0
        print(queue[rear],"is Enqueued into Queue")
   
    else:
        rear +=1
        queue.append(data)
        print(queue[front],"is Enqueued into Queue")
       
def Dequeue():
    global front
    global rear
    if front==rear== -1:
        print("Queue is empty")
    
    elif front==rear== 0:
        print(queue[front],"is Dequeued from Queue")
        queue.pop(0)
        front = -1
        rear = -1
    
    else:
        print(queue[front],"is Dequeued into Queue")
        queue.pop(0)
        rear -= 1

def Display():
    if queue:
        print(queue)
    else:
        print("Queue is Empty")

if __name__=="__main__":
    queue = []
    front = -1;
    rear = -1;

    print("\n**********WELCOME TO STACK OPERATIONS***********")
    print("Enter 1 to Enqueue an element into Queue")
    print("Enter 2 to Dequeue an element from Queue")
    print("Enter 3 to Display all elements in Queue")
    print("Enter 4 to EXIT\n")

    while(True):
        ip = int(input("Enter your Choice :-  "))
        if ip==1:
            data = int(input("Enter your push value :- "))
            Enqueue(data)
        elif ip==2:
            Dequeue()
        elif ip==3:
            Display()
        elif ip==4:
            print("You have Exited the Program")
            break
        else:
            print("Invalid Choice ")
