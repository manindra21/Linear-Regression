import matplotlib.pyplot as plt
import sympy as sym
import numpy as np

def training(x, y):
	cov_mat_0 = np.stack((x, y), axis=0)

	a = np.sum(x)
	b = np.size(x)
	c = np.sum(y)

	d = np.sum(np.square(x))
	e = np.sum(x)
	f = np.sum(np.multiply(x, y))

	r = np.cov(cov_mat_0)[0, 1]

	corcof = 1.96 / (np.sqrt(np.size(x)))

	if corcof <= r:
		A = np.array([[a, b], [d, e]])
		B = np.array([[c], [f]])
		arr = np.linalg.inv(A) @ B
		m = arr[0, 0]
		c = arr[1, 0]


		q = np.linspace(-10, 150, 100)
		plt.scatter(x, y)

		p = m * q + c

		plt.plot(q, p, '-r')

		plt.xlabel('Hours')
		plt.ylabel('Weight(KG')
		plt.grid()
		plt.show()

		return m, c

	else:
		print("please use some another model as there is no linear relationship.")


def prediction(m, c, check):
	y = m * check + c
	print("Predicted value is {}.".format(y))


x = [100, 75, 80, 90, 60, 50, 25, 40]
y = [15, 11, 15, 14, 8, 9, 2, 5]

check = input("Input the Hours to check the weight loss\n\n")

m, c = training(x, y)

prediction(m, c, float(check))






