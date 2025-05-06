def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
dizi=[5,2,6,1,93,4,7,8,9,0,3,12,45,23,56,78,90,34,21,11,10]
print("Sıralanmadan önceki dizi:",dizi)
print("Sıralandıktan sonraki dizi:",buble_sort(dizi))

def insertion_sort(arr):
    n=len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("Sıralandıktan sonraki dizi:",insertion_sort(dizi))
def merge_sort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return arr
print("Sıralandıktan sonraki dizi:",merge_sort(dizi))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) +  quick_sort(middle) + quick_sort(right)
print("Sıralandıktan sonraki dizi:",quick_sort(dizi))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
aranan=int(input("Aranacak sayıyı girin:"))
sonuc=binary_search(dizi, aranan)
if sonuc !=-1:
    print((aranan) ,"sayının indeksi:",(sonuc))
else:
    print("eleman dizide bulunamadı")