
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
