f = open("itc.py", 'w+')
f.write("# hello world")
f.seek(0)
r = f.read()
print(r)