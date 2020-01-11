import sys



ARRAY = sys.argv[4:]


def QuickSortA(arr):
    Temp1 = []
    Pivot = []
    count = 0

    for j in range(len(arr)):
        count = j
        for i in range (0 , len(arr) -1):
            arr[i] = int(arr[i])
            Pivot = arr[i]
            if Pivot >= int(arr[i+1]):
                Temp1 = Pivot
                arr[i] = int(arr[i+1])
                arr[i+1] = Temp1
            
            elif Pivot < int(arr[i+1]):
               
                int(arr[i])
                pass

            else : pass
    print("리스트내 숫자의 개수 :" , count + 1)


    
def QuickSortD(arr):
    Temp1 = []
    Pivot = []
    count = 0

    for j in range(len(arr)):
        count = j
        for i in range (0 , len(arr) -1):
            Pivot = int(arr[i])
            if Pivot <= int(arr[i+1]):
                Temp1 = Pivot
                arr[i] = int(arr[i+1])
                arr[i+1] = Temp1
            
            elif Pivot > int(arr[i+1]):
                pass

            else : pass

    print("리스트내 숫자의 개수 :" , count + 1)


if sys.argv[1] == "-o" :
    if sys.argv[2] == "A" : 
        
        print("정렬 전 리스트 :" , ARRAY)
        QuickSortA(ARRAY)
        print("정렬 후 리스트 :" , ARRAY)

    elif sys.argv[2] == "D" : 
        
        print("정렬 전 리스트 :" , ARRAY)
        QuickSortD(ARRAY)
        print("정렬 후 리스트 :" , ARRAY)

    else :
        print("입력인자를 잘 못입력하셨습니다.")


else :
    print("입력인자를 잘못입력하셨습니다.")