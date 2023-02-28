val=1
while(val):
	print("=======MENU======")
	print(" 1.string \n 2.tuple \n 3.exit\n")
	ch=int(input("enter your choice"))
	if(ch == 1):
		str=input("enter the string")
		print("1.length \n 2.upper \n 3.lower \n 4.title \n 5.find \n 6.count \n 7.reverse \n 8.replace \n 9.swapcase \n 10.strip \n 11.exit \n")
		val=1
		while(val):
			choice=int(input("enter the choice"))
			if(choice == 1):
				print("length of the string =",len(str))
			elif(choice == 2):
				print("string upper form=",str.upper())
			elif(choice == 3):
				print("string lower form=",str.lower())
			elif(choice == 4):
				print("string title=",str.title())
			elif(choice == 5):
				char=input("enter the character to find")
				print("character position is=",str.find(char))
			elif(choice == 6):
				char=input("enter the character to find count")
				print("character count is=",str.count(char))
			elif(choice == 7):
				print("string reverse form is=",str[::-1])
			elif(choice == 8):
				str1=input("enter string to replace")
				str2=input("enter replacing string")
				print("new string is=",str.replace(str1,str2))
			elif(choice == 9):
				print("string fter swapped=",str.swapcase())
			elif(choice == 10):
				str1=input("enter string to remove")
				print("string after stripped=",str.strip(str1))
			else:
				print("enter valid option")
				ch=0
				break
	elif(ch == 2):
		t=tuple(input("enter the tuple"))
		print("1.extract \n 2.length \n 3.combine \n 4.count \n 5.repetion \n 6.max value \n 7.min value \n 8.convert to list \n 9.last element \n 10.extract part of tuple \n 11.exit")
		val=1
		while(val):
			print("=======MENU======")
			choice=int(input("enter the choice"))
			if(choice == 1):
				c=int(input("enter the location"))
				print(t[c])
			elif(choice == 2):
				print(len(t));
			elif(choice == 3):
				t1=tuple(input("enter the tuple"))
				print(t+t1)
			elif(choice == 4):
				t1=int(input("enter a number"))
				print(t*t1)
			elif(choice == 5):
				i=input("enter the element to count")
				print(t.count(i))
			elif(choice == 6):
				print(max(t))
			elif(choice == 7):
				print(min(t))
			elif(choice == 8):
				l=list(t)
				print(l)
			elif(choice == 9):
				print(t[-1])
			elif(choice == 10):
				s=int(input("enter the starting point of tuple"))
				e=int(input("enter the ending point of tuple"))
				print(t[s:e])
			else:
				print("enter valid option")
				choice=0
				break
