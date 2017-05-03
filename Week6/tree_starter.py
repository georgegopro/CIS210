import argparse 


def readTree (inputFile):
	"""
	readTree reads the lines in the input file, and forms a tree using dictionaries.
	The result tree is a dictionary, whose keys are the indexes of nodes and the values of the dictionary are pairs of the value of nodes and the list of their children. For example tree[1] = (15, [2, 4]) means that node 1 has value 15 and it has two children with indexes of 2 and 4.
	Also, tree[2] = (20, [] ) means that node 2 has value 20, and it has no children (it is a leaf).
	"""
	tree = {}
	for line in inputFile:
		items = line.split();
		id = int(items[0]);
		value = int(items[1]);
		childrenList = [];
		if len(items) > 2:
			for it in items[2:]:
				child = int(it);
				childrenList.append(child);
		tree[id] = (value, childrenList);				 

	return tree

def printTree(tree, index, level):
	"""
		printTree prints the tree in the given format.
		index is the index of the current node in the tree 
		and level is the level of the current node.
	"""
	#FIX_ME


		
def main():	
	parser = argparse.ArgumentParser(description="Print a tree illustration of the given input data")
	parser.add_argument("treefile", type=argparse.FileType('r'), help="tree data file")
	args = parser.parse_args();
	tree = readTree(args.treefile)
	#We suppose that the root of the tree has index 1 and level 0.
	printTree(tree, 1, 0);

if __name__ == "__main__":
	main();
