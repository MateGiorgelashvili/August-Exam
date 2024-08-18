#1 Classy Extentions

# from preloaded import Animal

# class Cat(Animal):
#     def speak(self):
#         return self.name + " meows.

#2 Adam and Eve

#first version რომელიც კლაებზე აკონკრეტებს სტრინგი მნიშვნელობის არსებობას

# class Human:
#     pass
    
# class Man(Human):
#     def __str__(self):
#         return "Man"
    
# class Woman(Human):
#     def __str__(self):
#         return "Woman"
# def God():
#     return [Man(), Woman()]

#version 2

# class Human:
#     pass
    
# class Man(Human):
#     pass
    
# class Woman(Human):
#     pass
# def God():
#     return [Man(), Woman()]



#Currying functions: multiply all elements in an array

# def multiply_all(arr):
#     def one_int(num):
#         return [i * num for i in arr]
#     return one_int


#Is n divisible by (...)

#first version

# def is_divisible(num, *othernums):
#     for nums in othernums:
#         if num % nums != 0:
#             return False
#     return True


#second version + ემატება სიცარიელის შემოწმება

# def is_divisible(num, *othernums):
#     if not othernums:
#         return True
#     for nums in othernums:
#         if num % nums != 0:
#             return False
#     return True



#pete the baker

# def cakes(recipe, available):
#     if len(available) < len(recipe):
#         return 0
    
#     cakes = float('inf')
#     for i,b in recipe.items():
#         if i not in available:
#             return 0
        
#         max = available[i] // b
        
#         if max < cakes:
#             cakes = max
#     return cakes