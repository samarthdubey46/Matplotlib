import matplotlib.pyplot as plt
min = [x for x in range(1,10)]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
l = ["p1","p2","p3"]
base =['zero', 'sym', 'wiggle', 'weighted_wiggle']
plt.stackplot(min,player1,player2,player3,labels=l)
plt.legend(loc=(0.07,0.05))
plt.tight_layout()
plt.show()