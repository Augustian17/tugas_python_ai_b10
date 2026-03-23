# Tugas 4 - Coding: Python Data Structures
# 1 - List – akses & manipulasi

my_list = [10, "apple", 3.14, "banana", 42, "orange"]

first_element = my_list[0]
last_element = my_list[-1]

sliced_list = my_list[1:5:2]

print("Sebelum operasi append, insert, extend, pop, remove:")
print(my_list)

my_list.append("grape")
my_list.insert(2, "kiwi")
my_list.extend([100, "pear"])
popped_element = my_list.pop()
my_list.remove("apple")

print("Setelah operasi append, insert, extend, pop, remove:")
print(my_list)


# 2 - Tuple – immutability & unpacking

my_tuple = (1, "hi", 3.5, True, "world")

tuple_length = len(my_tuple)
second_element = my_tuple[1]

a, b, *rest = my_tuple

print("Panjang tuple:", tuple_length)
print("Elemen kedua:", second_element)
print("Unpacking:", a, b, rest)


# 3 - Set – keunikan & operasi himpunan

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b
symmetric_difference_set = set_a ^ set_b

set_with_duplicates = {1, 2, 2, 3}

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Set dengan duplikat:", set_with_duplicates)


# 4 - Dictionary – key/value dasar

student_data = {
    "nama": "Xiao",
    "nim": "123456",
    "angkatan": 2022,
    "kota": "Surabaya"
}

student_data["email"] = "xiaoganteng@gmail.com"
student_data["angkatan"] = 2023
del student_data["nim"]

print("Keys:", student_data.keys())
print("Values:", student_data.values())
print("Items:", student_data.items())

for key, value in student_data.items():
    print(f"{key}: {value}")


# 5 - Nested structures

chara = [
    {"nama": "Hutao", "game": "genshin", "tahun": 18},
    {"nama": "Xiao", "game": "genshin", "tahun": 20},
    {"nama": "Nahida", "game": "genshin", "tahun": 1000},
    {"nama": "Ganyu", "game": "genshin", "tahun": 500},
]

# Loop print nama
for c in chara:
    print("nama:", c["nama"])

# Filter (misalnya karakter dengan umur >= 100)
filtered_charas = [c for c in chara if c["tahun"] >= 100]

print("Karakter dengan umur >= 100:", filtered_charas)


# 6 - Comprehension & utilitas

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
squared_numbers = [x ** 2 for x in range(1, 21)]

number_mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}

sentence = "Hello World"
unique_lowercase_letters = {char.lower() for char in sentence if char.isalpha()}

print("List genap:", even_numbers)
print("List kuadrat:", squared_numbers)
print("Mapping angka:", number_mapping)
print("Huruf unik (lowercase):", unique_lowercase_letters)


# 7 - Keanggotaan & pencarian sederhana

item_to_check = "banana"
membership_check = item_to_check in my_list

position = my_list.index("orange") if "orange" in my_list else None

print("Keanggotaan:", membership_check)
print("Posisi 'orange':", position)