def average(array):
    Avg = sum(set(array))/len(set(array))
    return Avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)