n=int(input("Enter No. of Movies you like:"))
i=1
movies=[]
while i<=n:
    m=str(input("Enter Movie: "))
    movies.append(m)
    i+=1
print(movies)