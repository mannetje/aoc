with open('../input/01/input.txt', 'r') as input_text:
    input_arr = [int(line) for line in input_text]
    #Short:
    print([x * y for x in input_arr for y in input_arr if x + y == 2020][0])

    #More efficient:
    for i in range(0, len(input_arr)-1):
        for j in range(i+1, len(input_arr)):
            if input_arr[i]+input_arr[j]==2020:
                print(input_arr[i]*input_arr[j])
                break