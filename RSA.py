# RSA Python Implementation

# Here are our imports
import random
import math

def checkprime(n):
    # We can check if a number is prime by checking if its divisible by numbers from 2 to n/2
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

def primegen():
    # We're gonna generate primes from 100 to 500
    prime = random.randint(100, 500)

    # Check if that number really is prime
    while not checkprime(prime):
        prime = random.randint(100, 500)

    return prime

def keygen_priv(e, phi):
    # Calculate d, the inverse congruent modulo of phi(n)
    # e * d mod phi(n) = 1
    for i in range(0, n):
        if (i * e) % phi == 1 and e != i:   # gotta make sure we don't have the same keys
            return i

def enc(e, n):
    m = input("Please enter your message: ")

    # Converting acsii to int
    encoded = []
    for i in m:
        encoded.append(ord(i))

    # Making ciphertext
    # m^e mod n
    ciphertext = []
    for i in encoded:
        ciphertext.append(pow(i, e, n))
    print("Your ciphertext is: ", ciphertext)
    return ciphertext

def dec(c, d, n):
    # format user input into a list
    formatted = c.split()

    # c^d mod n
    decoded = []
    for i in formatted:
        decoded.append(pow(int(i), d, n))

    # Convert the message back to ascii
    message = ""
    for i in decoded:
        message += chr(i)
    print("Your decrypted message is: ", message)
    return message


# MAIN
print("Calculating keys...")

# Pick two primes, p and q
p = primegen()
q = primegen()

# Make sure p and q aren't the same
while p == q:
    p = primegen()

# Calculate n
n = p * q

# Calculate phi(n)
phi = (p - 1) * (q - 1)

# Choose e, a relative prime of phi(n)
# Relative prime: GCD = 1, 1 < e < phi(n)
e = random.randint(1, phi - 1)

# Make sure the GCD is 1
while math.gcd(e, phi) != 1:
    e = random.randint(1, phi - 1)

d = keygen_priv(e, phi)

print("Finished!")
print("Public key = {", e, ", ", n, "}")
print("Private key = {", d, ", ", n, "}")

print("What would you like to do?")
print("1: Encrypt message using generated keys")
print("2: Decrypt message using user-inputted values")

choice = input("Your choice: ")
if choice == "1":
    c = enc(e, n)
if choice == "2":
    u_cipher = input("Enter ciphertext seperated by whitespace (e.g. 231245 131256 463754): ")
    u_d = int(input("Enter 'd' value of private key: "))
    u_n = int(input("Enter 'n' value of private key: "))
    dec(u_cipher, u_d, u_n)
