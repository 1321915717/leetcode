# encoding='utf-8'

'''
   author:zhangyu
   date:2019.7.24
   description: 在一个数组中找出两个数的和为一个固定值
'''
def get_two_number(arr, sum):
    
    dict = {}
    count = 0
    for i in arr:
        dict[i] = count
        count += 1
    for i in range(len(arr)):
        number = arr[i]
        if dict.keys().__contains__(sum - number) and dict[sum - number] > i:
            return number, sum - number

if __name__ == '__main__':
    arr = [2, 4, 5, 8]
    sum = 7
    num = get_two_number(arr, sum)
    print(num)
