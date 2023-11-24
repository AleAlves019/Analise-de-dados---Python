from matplotlib import pyplot as plt
import random 

dado1 = random.sample(range(100), k =20)

dado2 = random.sample(range(100), k =20)

plt.plot(dado1, dado2)

plt.show()