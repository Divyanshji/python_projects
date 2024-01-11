start_num = int(input("enter a start for prime number print- "));
end_num = int(input("enter a till where you want to see - "));

if(start_num<=end_num):     # to make sure start nnumber is less than end number
    for i in range(start_num, end_num + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
else:
    print("enter correct numbers.")