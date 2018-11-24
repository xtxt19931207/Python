while True:
	print("\n1、加法\n2、减法\n3、乘法\n4、除法\n5、退出")
	a=input("请选择要进行的操作（1/2/3/4/5）：")
	if a=="":
		break
	elif int(a)==5:
		break
	elif int(a)<5:
		b=float(input("请输入第一个数："))
		c=float(input("请输入第二个数："))
		a=int(a)
		if a==1:
		    d=b+c
		    print(str(b)+"+"+str(c)+"="+str(d))
		elif a==2:
			e=b-c
			print(str(b)+"-"+str(c)+"="+str(e))
		elif a==3:
			f=b*c
			print(str(b)+"*"+str(c)+"="+str(f))
		elif a==4:
			if c!=0:
			    g=b/c
			    print(str(b)+"/"+str(c)+"="+str(g))
			else :
			    print("分母不能为0")
	else:
		print("输入无效，请输入1/2/3/4/5")
		