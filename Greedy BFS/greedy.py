SuccList ={ 'S':[['A',9],['B',7],['C',8]],
            'A':[['D',8],['B',7]],
            'B':[['D',8],['H',6]],
            'C':[['L',6]],
            'D':[['F',6]],'H':[['F',6],['G',3]],
            'L':[['I',4],['J',4]],
            'G':[['E',0]],
            'I':[['K',3]],
            'J':[['K',3]]
          } 
Start='A'
Goal='E'
Closed = list()
SUCCESS=True
FAILURE=False
State=FAILURE

#Find child or successor of N
def MOVEGEN(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	
	return New_list
	
#Check whether is N our goal    
def GOALTEST(N):
	if N == Goal:
		return True
	else:
		return False
#Remove childs from open and close list, and return appended list
def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list

#Sort list L based on heuristic value of nodes
def SORT(L):
	L.sort(key = lambda x: x[1]) 
	return L 

#Call search algorithm	
def GreedyBestFirstSearch():
	OPEN=[[Start,5]]
	CLOSED=list()
	global State
	global Closed
	while (len(OPEN) != 0) and (State != SUCCESS):
		print("------------")

        #Pick first node N from Open
		N= OPEN[0]
		print("N=",N)
		del OPEN[0] #delete the node we picked
		
		if GOALTEST(N[0])==True:
			State = SUCCESS
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)
		else:
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)

            #Find child of N
			CHILD = MOVEGEN(N[0])
			print("CHILD=",CHILD)

            #Delete child from open and closed list
			for val in CLOSED:
				if val in CHILD:
					CHILD.remove(val)
			for val in OPEN:
				if val in CHILD:
					CHILD.remove(val)
			OPEN = APPEND(CHILD,OPEN) #append movegen elements to OPEN
			print("Unsorted OPEN=",OPEN)
			SORT(OPEN)
			print("Sorted OPEN=",OPEN)
			
	Closed=CLOSED
	return State
	
result=GreedyBestFirstSearch() #call search algorithm
print(Closed,result)