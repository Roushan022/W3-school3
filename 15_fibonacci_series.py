n=int(input("Enter the number"))
main_num=0
next_num=1
for i in range(n):
    print(main_num,end=" ")
    temp=main_num
    main_num=next_num
    next_num+=temp
    
