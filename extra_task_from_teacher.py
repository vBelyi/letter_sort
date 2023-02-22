#задача сгенерувати список букв і відсортувати їх
import random

#тут ми генеруэмо випадковий список букв
letter_list = []
for n in range(100):
    i = chr(random.randint(97,122))
    letter_list.append(i)
print(letter_list)
#тут ми перетворюємо цей список букв на список їх юнікодів щоб відсортувати
ord_list = []
for i in letter_list:
    n = ord(i)
    ord_list.append(n)



#тут ми за допомогою insertion sort сортуэмо
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#на виході юнікоди знов перетворюємо на букви і отримуємо результат
insertion_sort(ord_list)
final_list = []
for i in ord_list:
    n = chr(i)
    final_list.append(n)
print(final_list)






