while True:
	print("1.list \n 2.sets \n 3.exit")
	ch=int(input("enter your choice"))
	if(ch == 1): 
		l=list(input("enter the list").split(" "))
		while True:
			print("1.append \n 2.insert \n3.pop \n4.remove \n5.length \n6.count \n7.min max \n8.sort \n9.revrse \n10.clear")
			ch=int(input("Enter the choice"))
			if ch==1:
				e=int(input("Enter ele"))
				l.append(e)
				print("ele",e,"is appended successsfully")
				print(l)
			elif ch==2:
				e=int(input("Enter ele"))
				p=int(input("Enter position"))
				l.insert(p,e)
				print(e,"is inserted at ",p)
				print(l)
			elif ch==3:
				print("popped ele=",l.pop())
			elif ch==4:
				v=input("Enter value to remove")
				l.remove(v)
				print(l)
			elif ch==5:
				print(len(l))
			elif ch==6:
				e=int(input("Enter ele"))
				print(l.count(e))
			elif ch==7:
				print(min(l),max(l))
			elif ch==8:
				l.sort()
				print(l)
			elif ch==9:
				l.reverse()
				print(l)
			elif ch==10:
				l.clear()
			else:
				break
				print()

	elif(ch == 2):
		print("1.size of set")
		print("2.length of set")
		print("3.add of set")
		print("4.intersection of set")
		print("5.diffrence of set")
		print("6.symmetric diffrence of set")
		print("7.check for a element of set")
		print("8.pop of set")
		print("9.clearing of set")
		print("10.deletion of set")
		print("0.exit")
		while True:
			ch=int(input("enter your choice"))
			if ch==1:
				set1=set(input("enter the set"))
				print(set1.__sizeof__())
			elif ch==2:
				set1=set(input("enter the set"))
				print(len(set1))
			elif ch==3:
				set1=set(input("enter the set"))
				set1.add(7)
				print(set1)
			elif ch==4:
				set1=set(input("enter the set1"))
				set2=set(input("enter the set2"))
				print(set1.intersection(set2))
			elif ch==5:
				set1=set(input("enter the set1"))
				set2=set(input("enter the set2"))
				print(set1-set2)
			elif ch==6:
				set1=set(input("enter the set1"))
				set2=set(input("enter the set2"))
				print(set1^set2)
			elif ch==7:
				set1=set(input("enter the set"))
				print(set1.__contains__(8))
			elif ch==8:
				set1=set(input("enter the set"))
				set1.pop()
			elif ch==9:
				set1=set(input("enter the set"))
				set1.clear()
			elif ch==10:
				set1=set(input("enter the set"))
				del(set1)
	elif ch==0:
		exit()
		break
