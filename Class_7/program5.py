# items() 	Returns a list containing a tuple for each key value pair
phone = {
  "company": "Apple",
  "model": "15 plus",
  "year": 2023
}

store = phone.items()

phone['year'] = 2024
print(store)
