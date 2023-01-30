def find_primes(n: int):
    '''
    Return set of prime numbers not exceeding n
    '''
    # Sieve of Eratosthenes

    # Place zeros to non-prime numbers
    arr = [i for i in range(n+1)]
    arr[1] = 0

    # Start from 3
    i = 2
    while i <= n:
        if arr[i] != 0:
            j = i + i
            while j <= n:
                arr[j] = 0
                j = j + i
        i += 1

    # Remove all zeroes
    arr = set(arr)
    arr.remove(0)

    return arr


if __name__ == '__main__':
    n = int(input("Enter n: "))
    print(find_primes(n))
