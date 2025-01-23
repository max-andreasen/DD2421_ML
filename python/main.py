import monkdata as m
import dtree


print(dtree.entropy(m.monk2))


tree1 = dtree.buildTree(m.monk1, m.attributes)
print(f"Tree 1 (training data) error: {1 - dtree.check(tree1, m.monk1)}")
print(f"Tree 1 (test data) error: {1 - dtree.check(tree1, m.monk1test)}")

tree2 = dtree.buildTree(m.monk2, m.attributes)
print(f"Tree 2 (training data) error: {1 - dtree.check(tree2, m.monk2)}")
print(f"Tree 2 (test data) error: {1 - dtree.check(tree2, m.monk2test)}")

tree3 = dtree.buildTree(m.monk3, m.attributes)
print(f"Tree 3 (training data) error: {1 - dtree.check(tree3, m.monk3)}")
print(f"Tree 3 (test data) error: {1 - dtree.check(tree3, m.monk3test)}")
