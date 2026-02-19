#list
marks=[75, 80, 90, 80, 75, 85]
print("List:",marks)
total=len(marks)
print("Total marks:",total)
#tuple
marks_tuple=tuple(marks)
print("Tuple:",marks_tuple)
highest=max(marks_tuple)
print("highest mark:",highest)
#set
marks_set=set(marks)
print("set:",marks_set)
unique_count=len(marks_set)
print("Unique mark:",unique_count)
#dictionary
student={"Alice":75,"Bob": 80,"Charlie": 90,"David": 80,"David": 80,"Eva": 75,"Frank": 85}
print("Dictionary:",student)
print("charlie's mark:",student["Charlie"])
student["Bob"]=88
print("Updated dictionary:",student)
