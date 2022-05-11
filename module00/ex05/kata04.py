kata = (0, 4, 132.42222, 10000, 12345.67)

module = "module_{:02d}".format(kata[0])
ex = "ex_{:02d}".format(kata[1])
decimal = "{:.2f}".format(kata[2])
sci_1 = "{:.2e}".format(kata[3])
sci_2 = "{:.2e}".format(kata[4])
print(module + ", " + ex + " : " + decimal + ", " + sci_1 + ", " + sci_2)
