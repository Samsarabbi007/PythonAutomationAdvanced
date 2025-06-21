from basics.Dictionaries.DistionaryLoop import my_dict

my_dict = {
    "name": "Suborno",
    "Company": "KAZ",
    "University" : "DU",
    "Phone" : "01784919174",
    "Batch" : "09"
}

Copied_dist = my_dict.copy()
print(f"Copied_dist = {Copied_dist}")

copied_dist2 = dict(my_dict)
print(f"copied_dist2 = {copied_dist2}")