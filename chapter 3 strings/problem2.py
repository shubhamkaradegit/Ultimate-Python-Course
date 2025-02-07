letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>", "Shubham").replace("<|DATE|>", "12-12-2050"))