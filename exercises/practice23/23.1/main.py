# Ecrire un générateur qui génére des nombres premiers dans un intervale spécifique

def gen_primes(limit):
    for dividend in range(2, limit + 1):
        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                break
        else:
            yield dividend


primes = gen_primes(101) # Limite à 100

for num in primes:
    print(num)