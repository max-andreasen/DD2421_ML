import monkdata as m
import dtree
import random
import matplotlib.pyplot as plt

tree1 = dtree.buildTree(m.monk1, m.attributes)
tree2 = dtree.buildTree(m.monk2, m.attributes)
tree3 = dtree.buildTree(m.monk3, m.attributes)

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
    return fractions[means1.index(max(means))]

def calcBestVal(dataset, fraction):
    train, validation = getPartition(dataset, fraction)
    root_tree = dtree.buildTree(train, m.attributes)
    trees = getTrees(root_tree)

    best_val = 0
    for tree in trees: 
        value =  dtree.check(tree, validation)
        if value > best_val: 
            best_val = value
    return best_val


def check_fractions(dataset, partitions):

    means = []
    variances = []
    iterations = 100
    for fraction in partitions:
        
        best_vals = []
        for _ in range(iterations):
            best_vals.append(calcBestVal(dataset, fraction))

        mean = sum(best_vals) / len(best_vals)
        means.append(mean)
        variances.append(getVariance(mean, best_vals))
        
    return means, variances

means1, variances1 = check_fractions(m.monk1, fractions)
means2, variances2  = check_fractions(m.monk2, fractions)
means3, variances3  = check_fractions(m.monk2, fractions)

print(f"Best partition for Monk1: {getBestPartition(means1)}")
print(f"Best partition for Monk2: {getBestPartition(means2)}")
print(f"Best partition for Monk3: {getBestPartition(means3)}")