#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("James", "mwangi")
say_my_name("Walter", "Whitehouse")
say_my_name("Banny")
try:
    say_my_name(12, "Whitehouse")
except Exception as e:
    print(e)

