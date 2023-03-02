def linear_search(data, key):
    position = 0
    end = len(data) -1
    steps = 1
    while position <= end:
        if data[position] == key:
            return steps, position
        steps += 1
        position += 1
    return steps, -1

def binary_search(data, key):
    start = 0
    end = len(data) -1
    steps = 1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == key:
            return steps, middle
        elif data[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        steps += 1
    return steps, -1

def search(title, data, func):
    print(title)
    max_steps = 1
    for key in data:
        steps, pos = func(data, key)
        if max_steps < steps:
            max_steps = steps
        print(f"key:{key} positon:{pos} steps:{steps}")
    print(f"最大ステップ数:{max_steps}\n")
    return

if __name__=="__main__":
    data = [1,3,7,13,17,21,74]
    length = len(data)
    print(f"探索データ:{data}\n長さ:{length}\n")
    search("線形探索", data, linear_search)
    search("2分木探索", data, binary_search)