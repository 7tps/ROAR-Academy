import matplotlib.pyplot as plt

x = [1.0, 2.0, 3.0]
y = [2.0, 4.0, 1.0]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-')

plt.title('Sample graph!')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)

plt.xticks([1.0, 1.5, 2.0, 2.5, 3.0])

plt.grid(True)

plt.show()