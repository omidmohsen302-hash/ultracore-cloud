memory = {}

def store(key, value):
    memory[key] = value

def recall(key):
    return memory.get(key, "یافت نشد")

store("هدف", "توسعه روی فضای ابری")
print(recall("هدف"))