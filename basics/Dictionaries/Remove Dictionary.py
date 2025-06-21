my_dict = {
    "name": "Suborno",
    "Company": "KAZ",
    "University" : "DU",
    "Phone" : "01784919174",
    "Batch" : "09"
}

#pop
my_dict.pop("Company")
print(my_dict)

#popitem()->last inserted item
my_dict.popitem()
print(my_dict)

#delete
del my_dict["Phone"]
print(my_dict)

#clear
my_dict.clear()
print(my_dict)
