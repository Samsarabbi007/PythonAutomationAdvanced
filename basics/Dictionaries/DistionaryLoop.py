my_dict = {
    "name": "Suborno",
    "Company": "KAZ",
    "University" : "DU",
    "Phone" : "01784919174",
    "Batch" : "09"
}

for key in my_dict:
    print(f"{key},: {my_dict[key]}")

#items with value
for key, value in my_dict.items():
    print(f"{key},: {value}")