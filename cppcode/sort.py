def solve(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp


if __name__ == '__main__':
    arr = [3, 5, 1, 4, 2]
    solve(arr)
    print(arr)
