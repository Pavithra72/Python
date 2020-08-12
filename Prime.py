val =0
for j in range(2,100,1):
    for i in range(2,100,1):
        if j%i==0:
            val=val+1
            if val == 2:
                break

    if val == 1:
        print(j)

    val=0
