marks = {
    "Harry": 98,
    "Kapil": 80,
    "Rohan": 70,
     0: "Girish"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 90, "Yash": 100}) # We can add also like "Yash": 100
print(marks)
print(marks.get("Shivika")) # Prints None because it is not present
print(marks.get("Harry"))
print(marks["Harry"])

# # Interview Question
print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error
n = marks.pop("Kapil")
print(n)
# m = marks.popitem()
# print(m)
# print("Updated dictionary:", marks)
print(marks.items())
