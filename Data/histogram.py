import matplotlib.pyplot as plt
import numpy as np

# 히스토그램

gaussian_numbers = np.random.randn(100000)
plt.hist(gaussian_numbers, bins=10)

plt.title('Gaussian Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()

# 산점도

num_friends = [41, 26, 90, 50, 18, 124, 152, 88, 72, 51]
phone_time = [4.1, 3.3, 5.7, 4.2, 3.2, 6.4, 6.0, 5.1, 6.2, 3.7]

plt.scatter(num_friends, phone_time)

plt.show()
