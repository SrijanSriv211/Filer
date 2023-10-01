from vendor.AND.AND import AND

rng = AND()
for _ in range(10):
    print(rng.gen()*10)
