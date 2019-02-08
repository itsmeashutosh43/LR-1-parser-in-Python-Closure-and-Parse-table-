from first import first

def checkValidity(i):
	if i[0][-1]=='.':
		return False
	return True


def preProcessStates(states):
	l=[]
	for i in states:
		if checkValidity(i):
			l.append(''.join(i).replace(' ',''))

	if len(l)!=0:
		return(l)
		

def is_nonterminal(symbol):
	return symbol.isupper()
def shiftPos(item):
	Item=''.join(item).replace(' ','')
	listItem=list(Item)
	index=listItem.index('.')
	if len(listItem[index:])!=1:
		return (Item[:index]+''+Item[index+1]+'.'+Item[index+2:])
	return item
def check(item,N):
	Item=''.join(item).replace(' ','')
	listItem=list(Item)
	try:
		index=listItem.index('.')
		#index1=listItem.index('=')
		if N ==listItem[index+1]:
			return True
		if ' '== listItem[index+1]:
			return False
	except:
		return False
def GOTO(I,N):
	J=[]
	for i in I:
		if check(i,N):
			new=shiftPos(i)
			J.append(new)

	if len(J)==0:
		return([])

	return(findClosure([J]))

def allGrammarSymbol(item):
	l=[]
	for i in item:
		for k in i:
			if k.isalpha():
				l.append(k)
	
	return set(l)


def findProduction(B):
	
	if B=='$':
		return 1
	if B not in entryOfGram.keys():
		return 1
	return entryOfGram[B]

def findTerminalsOf(gram):
	newList={}
	for i in gram:
		n=i.replace(' ', '').split('::=')
		if n[0] not in newList.keys():
			newList[n[0]]=[''.join(n[1])]
		else:
			newList[n[0]].append(''.join(n[1]))
	return newList


def nextDotPos(item):
	Item=item.replace(' ','')
	listItem=list(Item)
	try:
		index=listItem.index('.')
		return listItem[index+1]
	except:
		return '$'

def followOf(item):
	Item=item.replace(' ','')
	listItem=list(Item)
	try:
		index=listItem.index('.')
		return listItem[index+2]
	except IndexError:
		return '$'

def findClosure(I):
	add=1
	while (add!=0):
		add=0
		for item in I:
			element=item[0]
			giveElement=nextDotPos(element)
			findPr=findProduction(nextDotPos(element))
			if findPr==1:
				pass
			else:				
				for productions in findPr:
					for b in first[followOf(element)]:
						elem=[giveElement+'::=.'+productions+''+b]
						if elem not in I:
							I.append(elem)
							add=1
		return(I)
		break

gram=(
    '^::=S$',
    'S::=CC',
    'C::=cC',
    'C::=d'
)
entryOfGram=findTerminalsOf(gram)
I=[findClosure([['^::=.S$']])]
#findClosure(GOTO(I[0],'d'))

X=allGrammarSymbol(gram)

allItems={}
ItemsAll=[]
new_item=True
while new_item:
	new_item=False
	i=1
	for item in I:
		i+=1
		for g in X:
			if len(GOTO(item,g))!=0:
				goto=GOTO(item,g)
				flat_list = [[item] for sublist in goto for item in sublist]
				if flat_list not in I:
					index='I'+str(i)
					if index not in allItems.keys():
						allItems[index]=[g]
					else:
						allItems[index].append(g)	
					I.append(flat_list)
					Z=preProcessStates(flat_list)
					if (Z):
						ItemsAll.append(flat_list)
					
					new_item=True		

	new_item=False

ItemsAll.insert(0,findClosure([['^::=.S$']]))
i=0
ACTION={}
#print(ItemsAll)
print('*********************')
for item in ItemsAll:
	i+=1
	for num in item:
		x=list(num[0]).index('.')+2
		y=len(num[0])
		if x<y:
			elem=list(num[0]).index('.')+1
			gotoElem=list(num[0])[elem]
			IJ= GOTO(num,gotoElem)
			#print(IJ)
			if IJ in ItemsAll:
				#print('aa')
				#print(num)
				index=ItemsAll.index(IJ)
				last=list(num[0])[len(num[0])-1]
				ACTION[str(i-1)+'+'+gotoElem]="shift "+str(index)
		else:
			listy=list(num[0]).index('.')
			el=num[0][listy+1]
			ACTION[str(i-1)+'+'+el]="reduce "+num[0][:listy]

		#print(num[0])
	
print(ACTION)
print('*************************')


print('**** All States Are ****')
for i in ItemsAll:
	print('State ',ItemsAll.index(i))
	print(i)
	print('*********************')





