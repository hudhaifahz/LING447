from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

def load_training_data(path):
    file = open(path)
    lines = [line.strip() for line in file]
    file.close()
    inputs = list()
    outputs = list()
    for line in lines:
        line = line.strip('-')
        line = line.split(',')
        code = create_input(line[0])
        inputs.append(code)
        outputs.append([float(n) for n in line[1:]])
    return inputs, outputs

def create_input(word):
    code = list()
    for letter in word:
        if letter=="c" or letter=="h" or letter=="i":
            code.append(1.0)
        elif letter=="o":
            code.append(1.0)
        elif letter=="p" or letter=="t" or letter=="s" or letter=="k":
            code.append(1.0)
        elif letter=="b" or letter=="d" or letter=="z" or letter=="g":
            code.append(0.0)
        else:
            code.append(0.0)
    return code

def fill_pattern(inputs, longest):
    for codeArray in inputs:
        i = codeArray
        j = 0
        while len(codeArray) < longest:
            codeArray.append(i[j])
            j = j + 1
    print(inputs)
    return inputs

'''
def add_zeroes(inputs, longest):
    for i in inputs:
        while len(i) < longest:
            i.append(0.)
    return inputs
'''

def find_longest(inputs):
    longest = 0
    for i in inputs:
        if len(i) > longest:
            longest = len(i)
    return longest


#Load input and output values
path = r'/Users/hudhaifahz/Desktop/LING447/Assignment5/list.txt'
inputs,outputs = load_training_data(path)
#print(inputs,outputs)
#Add in any extra 0 that are needed
longest = find_longest(inputs)
inputs = fill_pattern(inputs, longest)

#Create a dataset from pybrain
dataset = SupervisedDataSet(longest, 4)
#the first argument is the number of input nodes
#the second argument is the number of output nodes

for index in range(len(inputs)):
    dataset.addSample(tuple(inputs[index]), tuple(outputs[index]))
    #the first argument is the activation values of the input nodes
    #the second argument is the activation value of the output nodes
    #the arguments are lists that are are cast to tuples
    #(tuples are like lists, except they are immutable)
    #the casting happens because the function requires tuples

#Build a network that uses backpropogration
network = buildNetwork(longest, longest+1, 4)
#the first argument is the number of input nodes
#the second argument is the number of hidden nodes
#the third argument is the number of output nodes

#Train the network with 50 examples of each training item
trainer = BackpropTrainer(network, dataset)
for j in range(1000):
    trainer.train()

#Test the network
test_words = ['nono', 'chiyuchiyu', 'zaza', 'gugu', 'dadadada','barabara','chibi-chibi','karakara','noronoro',]
#inputs = [word+word for word in test_words if len()]
inputs = [create_input(word) for word in test_words]
inputs = fill_pattern(inputs, longest)
for index, input_ in enumerate(inputs):
    results  = network.activate(input_)
    #the activation function activates the inputs nodes, sending a signal
    #that results in an output, but it doesn't cause the network to do any
    #backpropogation (its weights don't change) so it doesn't learn anything
    print(results)
    #the results are a list of activation values of each output node
    highest = max(results)
    #we are going to treat the output roughly as probabilities
    #higher activation values for an output node represent a greater probability
    #that the input word belongs to the category associated with that node
    #we'll say that the network has categorized the input as whichever node has
    #the highest value
    if highest == results[0]:
        category = 'small quick'
    elif highest == results[1]:
        category = 'big slow'
    elif highest == results[2]:
        category = 'high pitched'
    else:
        category = 'low pitched'
    print (test_words[index], 'is probably a', category)
print ("expected bigslow,smallquick,4xlowpitch,smallquick,highpitch,bigslow")
