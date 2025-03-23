def lenght(s):
    w=s.split(" ")
    lenght=int(len(w))
    print(f"The total words in the sentences are : {lenght}")
s=str(input("Enter a sentence : "))
lenght(s)