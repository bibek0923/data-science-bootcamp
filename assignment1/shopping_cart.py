wishlist=["tshirt" , "pants" ,"shoes"]
for item in wishlist:
    print(item)


print("after appending")
wishlist.append("cap")

for item in wishlist:
    print(item)
    
print("after extending") 
itemsToBeAdded=["keyboard","monitor"]
wishlist.extend(itemsToBeAdded)
for item in wishlist:
    print(item)

print("dictionaries")
product = {"name":"tshirt","price":1000}
# for item in product.values():
#     print(item)

# for item in product.keys():
#     print(item)
    
for key,value in product.items():
    print(f"key:{key}, value: {value}")
    
    
print("after adding key value pair")
#update for adding multiple value
#setdefault
#simple method


product["location"]="anamnagar"

for key,value in product.items():
    print(f"key:{key}, value: {value}")

