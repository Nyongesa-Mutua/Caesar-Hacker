import pyperclip
Symbols = "abcdefghijklmnopqrstuvwxyz"

print("This code can hack the caesar cypher code even if you do not have the key.")
print("As long as you know all symbols concerned in making the code .")
print ("It displays all possible outcomes of the code.")

text = str(input('enter the text you need decrypted  '))


for kent in range(len(Symbols)): # Loop through every possible key.
    traned = ""
# Decrypt each symbol in the message:
    for symbol in text:
        b = Symbols.find(symbol)
        if symbol in Symbols:
            num = Symbols.find(symbol) # Get the number of the symbol.
            num = num - kent # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(Symbols)

            # Add decrypted number's symbol to translated:
            traned = traned + Symbols[num]
        else:

            traned = traned + symbol

 # Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(kent, traned))
