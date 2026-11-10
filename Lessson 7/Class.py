classmates={"Aarav", "Priya", "Rahul", "Sneha", "Dev"}
print("Class list: ", classmates)
print("Total students: ", len(classmates))
print("First student: ", classmates[0])
print("Last student: ", classmates[-1])
print("First three: ", classmates[:3])
classmates.appened("Meera")
print("/nAfter adding Meera: ", classmates)
classmates.sort()
print("Sorted alphabetically: ", classmates)
classmates.reverse()
print("Reversed: ", classmates)
teacher= {"name": "Mr. Sharma", "subject" : "Python", "expirence" : 5 }
print("/nTeacher profile: ", teacher)
print("Subject: ", teacher["subject"])
print("Expirence: ", teacher.get("expirence", "Not found"))
teacher["expirence"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("expirence")
print("Updated teacher profile: ", teacher)
roll_numbers = [1, 2, 3, 4, 5,]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("/nStudent Directory: ", student_directory)
print("Student at roll 3: ", student_directory[3])