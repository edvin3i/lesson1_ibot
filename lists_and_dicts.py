list1 = list(range(2, 8))
list1.append('Python')
print(len(list1))
print(list1[0])
print(list1[-1])
print(list1[1:4])
list1.remove('Python')

dict1 = {"city": "Москва", "temperature": "20"}
print(dict1.get("city", "Unknown"))
dict1["temperature"] = int(dict1.get("temperature")) - 5
print(dict1)
country_in = "country" in dict1
dict1.get("country", "Россия")
dict1["date"] = "27.05.2017"
print(len(dict1))