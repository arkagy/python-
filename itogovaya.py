import tkinter as tk
from tkinter import messagebox
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def sort_sequence():
    try:
        # Получаем введенную последовательность чисел
        sequence = entry.get()

        # Проверяем, что введена хотя бы одна запятая
        if ',' not in sequence:
            messagebox.showerror('Ошибка', 'Последовательность чисел должна быть разделена запятыми')
            return

        # Разделяем последовательность по запятым и преобразуем в список чисел
        numbers = [int(num.strip()) for num in sequence.split(',')]

        # Получаем выбранный вариант сортировки
        sorting_method = var.get()

        # Проверяем, что выбран хотя бы один вариант сортировки
        if sorting_method == '':
            messagebox.showerror('Ошибка', 'Выберите вариант сортировки')
            return

        # Сортируем последовательность
        start_time = time.time()
        if sorting_method == 'Сортировка выбором':
            selection_sort(numbers)
        elif sorting_method == 'Сортировка пузырьком':
            bubble_sort(numbers)
        elif sorting_method == 'Сортировка вставками':
            insertion_sort(numbers)
        elif sorting_method == 'Сортировка слиянием':
            merge_sort(numbers)
        elif sorting_method == 'Быстрая сортировка':
            numbers = quick_sort(numbers)
        end_time = time.time()

        # Выводим отсортированную последовательность и время затраченное на сортировку
        output.delete('1.0', tk.END)
        output.insert(tk.END, 'Отсортированная последовательность: ')
        output.insert(tk.END, ', '.join(str(num) for num in numbers))
        output.insert(tk.END, '\nВремя затраченное на сортировку: {:.6f} секунд'.format(end_time - start_time))

    except ValueError:
        messagebox.showerror('Ошибка', 'Последовательность должна содержать только числа')
    except Exception as e:
        messagebox.showerror('Ошибка', str(e))

# Создаем графическое окно
window = tk.Tk()
window.title('Графическая программа')

# Создаем метку и поле ввода для последовательности чисел
label = tk.Label(window, text='Введите последовательность чисел:')
label.pack()
entry = tk.Entry(window)
entry.pack()

# Создаем раскрывающийся список для выбора варианта сортировки
label = tk.Label(window, text='Выберите вариант сортировки:')
label.pack()
var = tk.StringVar(window)
var.set('')  # По умолчанию не выбран ни один вариант
sorting_options = ['Сортировка выбором', 'Сортировка пузырьком', 'Сортировка вставками', 'Сортировка слиянием', 'Быстрая сортировка']
dropdown = tk.OptionMenu(window, var, *sorting_options)
dropdown.pack()

# Создаем кнопку для запуска сортировки
button = tk.Button(window, text='Start', command=sort_sequence)
button.pack()

# Создаем кнопку для очистки
def clear():
    output.delete('1.0', tk.END)
    entry.delete(0, 'end')

button = tk.Button(text='Очистить', command=clear)
button.pack()

# Создаем текстовое поле вывода
output = tk.Text(window, height=5, width=50)
output.pack()

# Запускаем главный цикл программы
window.mainloop()
