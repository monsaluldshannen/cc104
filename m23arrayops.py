arr = [10, 20, 30, 40, 50]
print("First element:", arr[0])
print("Last element:", arr[-1])
for x in arr:
    print(x)

arr.insert(0, 5)
print("After insertion:", arr)
arr.remove(30)
print("After deletion:", arr)