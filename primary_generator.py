import time


def generator(limit):
    """ Generator is creating and printing primary numbers
    and time of the process

    Parameters:
        limit (int): Function breaks when limit is reched.
   
    """
    start = time.process_time()
    liczba = 1
    count = 1
    print("2 is a primary number")

    while liczba < limit:
        suma_dzielnikow = 0                   # reset liczby dzielnikow
        liczba += 2
        for dzielnik in range(3, liczba + 1, 2):
            if liczba % dzielnik == 0:
                suma_dzielnikow += 1
                if suma_dzielnikow > 1:       # przestaje szukac kolejnych
                    break                     # dzielnikow po osiagnieciu 2
                if dzielnik == liczba:
                    if suma_dzielnikow == 1:
                        print(liczba, "to liczba pierwsza")
                        count += 1
    finish = time.process_time()
    print(f'There are {count} primal numbers in range {limit}.\nProcess took {finish - start}s')


generator(20000)
