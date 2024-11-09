class Person:  
    def __init__(self, name, age, gender):  
        self.name = name        # Attribute for person's name  
        self.age = age          # Attribute for person's age  
        self.gender = gender    # Attribute for person's gender  

    def introduce(self):  
        # Method to introduce the person  
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")  

# Creating an instance of the Person class  
person1 = Person("Austin", 34, "Male")  

# Calling the introduce method to display the person's information  
person1.introduce()  # Output: Hello! My name is Alice, I am 30 years old, and I am female.