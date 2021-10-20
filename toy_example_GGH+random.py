from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
q = 2^10
n = 150 #
A = matrix(ZZ, n, n)
for i in range(n):
	for j in range(n):
		if i == j:
			A[i, j] = 1
		else:
			A[i, j] = ZZ.random_element(1, 10)
A.rank()
A.determinant()
U1 = matrix(ZZ, n, n)
U2 = matrix(ZZ, n, n)
for i in range(n):
	U1[i, i] = 1
	U2[i, i] = 1
for i in range(n):
	for j in range(i + 1, n):
		U1[i, j] = ZZ.random_element(0, q)
for i in range(n):
	for j in range(0, i):
		U2[i, j] = ZZ.random_element(0, q)
pub_matrix = A * U1 * U2
#for i in range(n):
#	for j in range(n):
#		pub_matrix[i, j] = pub_matrix[i ,j].powermod(1,q)
pub_matrix.str()
target = matrix(ZZ, n, 1)
for i in range(n):
	target[i, 0] = ZZ.random_element(0, q)
print("target point", target)
coeff =  A.inverse() * target
#print("coeff", coeff)
sigma = 3
decoding_coeff  =  matrix(ZZ, n, 1)
for i in range(n):
	D = DiscreteGaussianDistributionIntegerSampler(sigma=sigma, c= coeff[i, 0])
	decoding_coeff[i, 0] = D()
#print("decoding_coeff", decoding_coeff)
print("near point", A * decoding_coeff)
A.str()
pub_matrix.LLL().str()