import monkdata as m
import dtree
import random
import matplotlib.pyplot as plt
import drawtree_qt5

tree1 = dtree.buildTree(m.monk1, m.attributes)
tree2 = dtree.buildTree(m.monk2, m.attributes)
tree3 = dtree.buildTree(m.monk3, m.attributes)

drawtree_qt5.drawTree(tree2)

fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def getPartition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def getTrees(root_tree):
    return dtree.allPruned(root_tree)

def getVariance(mean, values):
    N = len(values)
    variance = 0
    for i in range(N):
        variance += (values[i] - mean)**2
    return variance / N

def getBestPartition(means): 
    return fractions[means.index(max(means))]

def calcBestTree(dataset, fraction):
    train, validation = getPartition(dataset, fraction)
    root_tree = dtree.buildTree(train, m.attributes)
    trees = getTrees(root_tree)

    best_val = 0
    for tree in trees: 
        value =  dtree.check(tree, validation)
        if value > best_val: 
            best_val = value
            best_tree = tree
    return best_val, best_tree


def check_fractions(dataset, testset, partitions):

    means = []
    variances = []
    test_error_means = []
    iterations = 100
    for fraction in partitions:
        
        best_vals = []
        test_results = []
        for _ in range(iterations):
            best_val, best_tree = calcBestTree(dataset, fraction)
            test_error = 1 - dtree.check(best_tree, testset)
            test_results.append(test_error)
            best_vals.append(best_val)

        mean = sum(best_vals) / len(best_vals)
        means.append(mean)
        variances.append(getVariance(mean, best_vals))
        test_error_mean = sum(test_results) / len(test_results)
        test_error_means.append(test_error_mean)
        
    return means, variances, test_error_means

means1, variances1, test_error_means1 = check_fractions(m.monk1, m.monk1test, fractions)
means2, variances2, test_error_means2 = check_fractions(m.monk2, m.monk2test, fractions)
means3, variances3, test_error_means3 = check_fractions(m.monk3, m.monk3test, fractions)

#print(f"Best partition for Monk1: {getBestPartition(means1)}")
#print(f"Best partition for Monk2: {getBestPartition(means2)}")
#print(f"Best partition for Monk3: {getBestPartition(means3)}")

plt.figure()
plt.plot(fractions, test_error_means1, label="MONK-1", color="orange",  marker=".")
plt.plot(fractions, test_error_means3, label="MONK-3", color="blue", marker=".")

plt.title("Test error over partition size")
plt.xlabel("Partition size")
plt.ylabel("Mean Test Error")

plt.grid(alpha=0.4)
plt.legend()
plt.show()