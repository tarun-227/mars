
encrypted_message = input("Enter the encoded message: ")

encrypted_message = encrypted_message.upper()  # converting all letters to uppercase
decoded_message = ""

index_shifts = [] #list that stores by how much shuld each letter be shifted in the message
for i in range(len(encrypted_message)):
    index_shifts.append(i + 1)  #create a list of shifts

for i in range(len(encrypted_message)):
    decoded_ascii = ord(encrypted_message[i]) - index_shifts[i]  #shifting each letter by its index+1

    # Ensure circular shift within A to Z
    if decoded_ascii < ord('A'):
        decoded_ascii += 26

    decoded_message += chr(decoded_ascii)

print("Decoded message:", decoded_message)
