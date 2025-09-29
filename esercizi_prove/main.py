import sys
numeratore = int(sys.argv[1])
denominatore = int(sys.argv[2])

try:
    quoziente = numeratore/denominatore

except ZeroDivisionError:
    print("Except")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])

else:
    print("Quoziente uguale a: ", quoziente)

finally:
    print("finished")
