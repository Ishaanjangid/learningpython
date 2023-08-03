def ReturnsTrue():
    print("ReturnsTrue() was called.")
    return True

def ReturnsFalse():
    print("ReturnsFalse() was called.")
    return False

# print(ReturnsTrue() or ReturnsFalse())
# print(ReturnsFalse() or ReturnsTrue())

print(ReturnsTrue() and ReturnsFalse())