# coding=utf-8

import os
import matplotlib.pyplot as plt
import numpy as np

dirname = os.path.dirname(__file__)

n = 2000

Y, X = np.mgrid[-1.5:1.5:3 / n, -2:1:3 / n]

C = X + 1j * Y

# pic = np.random.randn(n, n)
# ans = np.random.randn(n, n)

pic = np.zeros((n, n))
ans = np.zeros((n, n))

for i in range(100):
    pic = pic**2 + C
    ans += np.float32(np.abs(pic) < 100)

plt.axis('off')
plt.imshow(ans, cmap="Blues")

plt.savefig(os.path.join(dirname, 'images/figure.png'), dpi=1000, bbox_inches='tight', pad_inches=0)
# plt.show()
