# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0 - TODO
## defining our data structures
class Node: # NOT given to students
    # TODO
    letter: str
    count: int
    left: any
    right: any
    
    def __init__(self, letter: str, count: int, left: any, right: any):
        self.letter = letter
        self.count = count
        self.left = left
        self.right = right

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None: # if 'TODO': # TODO
        coding[v.letter] = None # TODO
    else:
        retrieve_codes(None, None) # TODO
        retrieve_codes(None, None) # TODO

# STEP 1
## counting the frequencies - 
def count_freq(message):
    for letter in message:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1

count_freq(message)


# STEP 2
## initialize the nodes - 
def init_nodes():
    nodes = list()
    #nodes.append(Node(0, 'a'))
    for letter, count in freq.items():
        nodes.append(Node(count, letter))

init_nodes()


# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    #combined: Node = None # TODO
    new_freq = min_a.count + min_b.count
    combined: Node = Node(min_a.letter, new_freq, min_a, min_b)

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
result: str = str() # TODO (hint coding[letter] -> code)
# coding[v.letter]

# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')