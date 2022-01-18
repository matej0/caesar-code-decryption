def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = str(input("xd: ")).strip() ##remove spaces
    offset = 0
    for i in range(len(alphabet)):
        decrypted = ""
        for j in encrypted:
            if (j in alphabet): #python easy
                offset = alphabet.find(j)
                decrypted += alphabet[(offset - i) % len(alphabet)]
            else:
                decrypted += j #should never happen, but never say never!
        print("key %d: %s" % (i, decrypted))

if __name__ == "__main__":
     main()
