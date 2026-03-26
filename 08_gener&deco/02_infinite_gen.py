def infinitechai():
    count = 1
    while True:
        yield f"refill {count}"
        count += 1

refill = infinitechai()
user2=infinitechai()

for _ in range(3):
    print(next(refill))

for _ in range(6):
    print(next(user2))