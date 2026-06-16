
def fibonacci(n):
	"""Generate Fibonacci series up to n terms as a list."""
	if n <= 0:
		return []
	if n == 1:
		return 0
	seq = [0, 1]
	print(len(seq))
	while len(seq) < n: #2<5
		seq.append(seq[-1] + seq[-2])
	return seq


if __name__ == "__main__":
	try:
		n = int(input("Enter number of terms: "))
	except Exception:
		print("Invalid input")
	else:
		print(fibonacci(n))
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    try:
        limit = int(input("Enter the upper limit for prime numbers: "))
        primes = generate_primes(limit)
        print(f"Prime numbers up to {limit}: {primes}")
    except Exception:
        print("Invalid input")