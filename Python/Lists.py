if __name__ == '__main__':
    N = int(input())

    opr_arr = []
    main_arr = []
    for i in range(N):
        arr = input().split()
        main_arr.append(arr)
        arr=[]
        
    #print(main_arr)

    for j in range(len(main_arr)):

        if main_arr[j][0] == 'insert':
            ind = int(main_arr[j][1])
            val = int(main_arr[j][2])
            #print(ind,val)
            opr_arr.insert(ind,val)

        elif main_arr[j][0] == 'print':
            print(opr_arr)

        elif main_arr[j][0] == 'remove':
            opr_arr.remove(int(main_arr[j][1]))

        elif main_arr[j][0] == 'append':
            opr_arr.append(int(main_arr[j][1]))

        elif main_arr[j][0] == 'sort':
            opr_arr.sort()
        
        elif main_arr[j][0] == 'pop':
            opr_arr.pop()

        elif main_arr[j][0] == 'reverse':
            opr_arr.reverse()
        



