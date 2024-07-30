def sumita_range(l_range, u_range):
    sumita = 0
    for x in range(l_range, u_range):
        sumita += x
    return sumita

if __name__ == "__main__":
    sumitommo = sumita_range(2, 100)
    print(sumitommo)