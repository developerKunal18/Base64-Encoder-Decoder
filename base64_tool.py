import base64

print("1. Encode")
print("2. Decode")

choice = input("Choose option: ")

if choice == "1":
    text = input("Enter text: ")
    encoded = base64.b64encode(text.encode()).decode()
    print("Encoded:", encoded)

elif choice == "2":
    text = input("Enter Base64 text: ")
    decoded = base64.b64decode(text.encode()).decode()
    print("Decoded:", decoded)

else:
    print("Invalid choice")
