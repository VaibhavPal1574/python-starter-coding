# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(None, list1))
print(res)