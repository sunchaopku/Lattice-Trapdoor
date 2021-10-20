from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
q = 2^10
n = 5 #
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
target = matrix(ZZ, 1, n)
for i in range(n):
	target[0, i] = ZZ.random_element(0, q)
print("target point", target)
coeff =  target *  A.inverse() 
#print("coeff", coeff)
sigma = 3
decoding_coeff  =  matrix(ZZ, 1, n)
for i in range(n):
	D = DiscreteGaussianDistributionIntegerSampler(sigma=sigma, c= coeff[ 0, i])
	decoding_coeff[ 0, i] = D()
#print("decoding_coeff", decoding_coeff)
print("near point", decoding_coeff * A)
near_point = decoding_coeff * A
signature = near_point - target
print("signature", signature)
print("norm of signature", norm(signature))
pub_matrix.LLL().str()
block_B = matrix(ZZ, n,1, [0] * n)
block_D = matrix(ZZ, 1, 1, q)
C = block_matrix([ [pub_matrix, block_B],[target, block_D] ])
print("C", C)
print("A", A)
M = C.BKZ(block_size = 20)
print("M", M)
forge = 0
for i in range(n):
	forge = forge + M[n, i] * M[n, i]
forge = RR(sqrt(forge))
print("norm of forge", forge)