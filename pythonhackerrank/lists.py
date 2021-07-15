if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0, N):
        store_str = input()
        store_str_arr = store_str.strip().split(" ")
        command = store_str_arr[0]
        if command == "print":
            print(arr)
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()
        # elif command == "count":
        #     #value = int(store_command_arr[1])
        #     arr.count()
        # elif command == "index":
        elif command == "insert":
            position = int(store_str_arr[1])
            value = int(store_str_arr[2])
            arr.insert(position, value)
        elif command == "append":
            value = int(store_str_arr[1])
            arr.append(value)
        elif command == "remove":
            value = int(store_str_arr[1])
            arr.remove(value)
