from inspect import currentframe as cf
from functools import wraps
import functools
import string
import random

# ======================== 2020/08/09 - APIBENDRINIMAS - STRUKTURA ====================


"""
Dekoratorius funkcijos iskvietejas ir argumentu laikiklis
Kad nereiketu sekti kiek argumentu naudojame tada naudojame *args
"""


def kita_funcioja(argumentas):
    def upper_wrap(func):
        def wrapper(*args):
            # print(f"Line: {cf().f_lineno} type(args) {type(args)}")
            # print(f"Line: {cf().f_lineno} type(args) {args[1]}")
            rez = func(*args) + 100 + argumentas
            return rez
        return wrapper
    return upper_wrap


@kita_funcioja(10)
def decoruojama_fun(a,c,b):
    return 100 * a

# 1. Funcija
# 2. Sukurtume kita funcija
# 3. Pridedam decotariu i funcija
# 4. Pakeiciam perduodamos funcijos output
# 5. Graziname rez
# 6. Grazinam wraperi kad galetume kviesti funcija
# a) Jei naudojam argumentus pagrindinei funcijoj i wrapperi pridedam a arba *args
# b) Atitinkamai perduodam argumenta i apdirbamos funcijos parametrus
# 7. Jei norim argumentu decoratoriuje, ivelkam paprasta dekoratoriu i papildoma funkcija


x = decoruojama_fun(5, 3, 4)
print(x)

# ======================== 2020/08/09 - Exercise v.2 su input =========================

"""Parametru perdavimas per dekoratoriu"""

# from inspect import currentframe as cf
# import math
# import time
#
#
# def time_calc_dec(daugiklis):
#     print(f"Line {cf().f_lineno}: daugiklis {daugiklis}")
#
#     def upper_wrap(func):
#         def wrapper(*args):
#             print(f"Line {cf().f_lineno}: argsai {args}")
#             start = time.time()
#             func(*args)
#             end = time.time()
#             print(f"Line {cf().f_lineno}: uztruko {end - start}")
#             rez = (end - start) * daugiklis
#             print(f"Line {cf().f_lineno}: reultatas padaugintas is daugiklio {rez}")
#             return rez
#         return wrapper
#     return upper_wrap
#
#
# # Susikuriam funckija kuria dekoruojam + per pati dekoratoriu perduodame parametra "10", t.y. daugikli
# @time_calc_dec(10)
# def million_powers(skaicius, kelintuoju):
#     print(f"Line {cf().f_lineno}: skaicius {skaicius}")
#     print(f"Line {cf().f_lineno}: kelintuoju {kelintuoju}")
#     return [math.pow(skaicius, kelintuoju) for _ in range(100000)]
#
#
# x, y = int(input("Iveskite pirma skaiciu: ")), int(input("Iveskite antra skaiciu: "))
# rez = million_powers(x, y)
# print(x)

# ======================== 2020/08/09 - Exercise v.2 ==================================

"""Parametru perdavimas per dekoratoriu"""

# from inspect import currentframe as cf
# import math
# import time
# 
# 
# def time_calc_dec(daugiklis):
#     print(f"Line {cf().f_lineno}: daugiklis {daugiklis}")
# 
#     def upper_wrap(func):
#         def wrapper(*args):
#             print(f"Line {cf().f_lineno}: argsai {args}")
#             start = time.time()
#             func(*args)
#             end = time.time()
#             print(f"Line {cf().f_lineno}: uztruko {end - start}")
#             rez = (end - start) * daugiklis
#             return rez
#         return wrapper
#     return upper_wrap
# 
# 
# # Susikuriam funckija kuria dekoruojam + per pati dekoratoriu perduodame parametra "10", t.y. daugikli
# @time_calc_dec(10)
# def million_powers(skaicius, kelintuoju):
#     print(f"Line {cf().f_lineno}: skaicius {skaicius}")
#     print(f"Line {cf().f_lineno}: kelintuoju {kelintuoju}")
#     return [math.pow(skaicius, kelintuoju) for _ in range(100000)]
# 
# 
# x = million_powers(100, 60)
# print(x)

# ======================== 2020/08/09 - Exercise v.1 ======================================

"""
Given function power(x, y), which calculates x to the power of y 1 million times:
1. Write a class-based decorator which measures time it took to execute wrapped
function and prints it
2. Hint: use time() function from time library
3. Call power() with large numbers to see the results (15.0 and 60.0 will do fine)
"""

# import math
# import time
#
#
# class TimeCalc:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         self.func(*args, **kwargs)
#         end = time.time()
#         rez = end - start
#         return rez
#
#
# @TimeCalc
# def million_powers(skaicius, kelintuoju):
#     return [math.pow(skaicius, kelintuoju) for i in range(100000)]
#
#
# x = million_powers(15, 60)
# print(x)

# ======================== 2020/08/08 - 6 dalis - Exercise 2 ======================================

# class HTMLheader:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, a):
#         print(f"Line: {cf().f_lineno} a arg = {a}")
#         return f"<h1> {self.func(a)} </h1>"
# @HTMLheader
# def prep_header(title):
#     print(f"Line: {cf().f_lineno} {title}")
#     return title
# x = prep_header('Python')
# print(x)


# ======================== 2020/08/08 - 5 dalis - Exercise 1 ======================================

# print(string.ascii_letters)
# print(string.digits)
#
# letters = string.ascii_letters
# def lower(func):
#     print(f"Line: {cf().f_lineno} Paleidom lower funcija")
#     def wrapper():
#         print(f"Line: {cf().f_lineno} Paleidom wrapper funcija")
#         random_letters = func().lower()
#         return random_letters
#     return wrapper
# def trumpina(func):
#     print(f"Line: {cf().f_lineno} Paleidom trumpina funcija")
#     def wrapper():
#         print(f"Line: {cf().f_lineno} Paleidom wrapper funcija")
#         # func() = 'sdsdsadadasdsafgrg'
#         sutrumpintas = func()[:10]
#         return sutrumpintas
#     return wrapper
# def upper(func):
#     print(f"Line: {cf().f_lineno} Paleidom trumpina funcija")
#     def wrapper():
#         print(f"Line: {cf().f_lineno} Paleidom wrapper funcija")
#         # func() = 'sdsdsadadasdsafgrg'
#         sutrumpintas = func() * 5
#         return sutrumpintas
#     return wrapper
# @lower
# @trumpina
# @upper
# def random_string():
#     random_501 = "".join(random.choice(letters) for i in range(50))
#     return random_501
# x = random_string()
# print(x)

# ======================== 2020/08/08 - 4 dalis ======================================

# # func = another
# def dec_fun(func):
#     print(f"Line: {cf().f_lineno} pati funcija: {func}")
#     @functools.wraps(func)
#     def vidine_func(*args, **kwargs):
#         print(f"Line: {cf().f_lineno} argsai {args}, kwargs {kwargs}")
#         print(f"Line: {cf().f_lineno} grazintas rezultatas {func(*args, **kwargs)}")
#         result = func(*args, **kwargs) * 100
#         return result
#     return vidine_func
# @dec_fun
# def another(argumenta):
#     print(f"Line: {cf().f_lineno} Paleidom another funcija")
#     return argumenta
# # Galim kviest nes grazinam funcija 9 eilutej
# x = another(100)
# # rezultatas nes padauginam is 100 7 eilutej
# print(f"Line: {cf().f_lineno} {x}")

# ======================== 2020/08/08 - 3 dalis ======================================

# def dec_fun(func):
#     print(f"Line: {cf().f_lineno} pati funckija: {func}")
#     print(f"super_func rezultatas: {func()}")
#     result = func() * 3
#     print(f"Line: {cf().f_lineno} rezultatas: {result}")
#     return result
#
# @dec_fun
# def super_func():
#     print(f"Paleidom super func")
#     return 1
#
# # x = super_func
# print(super_func)

# ======================== 2020/08/08 - 2 dalis ======================================

# def example_decorator(func):
#     print(f"Line: {cf().f_lineno} {func}")
#     def wrapper():
#         print(f"Line: {cf().f_lineno} *args yra: {args}, **kwargs yra: {kwargs}")
#         result = func() * 3
#         print(f"Line: {cf().f_lineno} rezultatas yra: {result}")
#         return result
#     return wrapper
#
#
# @example_decorator # dekoratorius paima po juo esancia funkcija ir ja galima panaudoti auksciau funkcijoje
# def greetings():
#     return 1000
#
# x = greetings()
# print(x)
#

# ======================== 2020/08/08 - 1 dalis ======================================

# class Singleton:
#
#     def __init__(self, name):
#         print(f"Line: {cf().f_lineno} esame instance:")
#         self.name = name
#         print(f"Line: {cf().f_lineno} self.name yra: {self.name} name yra: {name}")
#
#     @property # tai yra dekoratorius. Dekoratorius tampa funckija ir grazina ta funkcija kura norime naudopti
#     def printer(self):
#         print(f"Line: {cf().f_lineno} esame printer metode:")
#         return self.name
#
#
# s1 = Singleton("Kazkas")
# print(s1.printer)