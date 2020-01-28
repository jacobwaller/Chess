import random
import math
import numpy

'''
Hyperbolic tangent activation function
'''
def tanh(sum): 
    return numpy.tanh(sum)

def relu(sum):
    if sum>0:
        return 1
    return 0

class NeuralNet:
    def __init__(self,dense_layer_nums,activation_functions):
        self.layers = []

        #Fill self.layers with Nodes
        for i in range(0,len(dense_layer_nums)):
            self.layers.append([])
            for j in range(0,dense_layer_nums[i]):
                self.layers[i].append(Node(activation_functions[i]))
        pass

        #Fully connect the nodes
        for i in range(0,len(self.layers)-1):
            for in_node in self.layers[i]:
                for out_node in self.layers[i+1]:
                    e = Edge(in_node,out_node,random.random()*2-1) #Initialize edges with random weights
                    in_node.outputs.append(e)
                    out_node.inputs.append(e)

    def fit(self, training_features, training_labels, batch_size=50):
        if len(training_features) != len(self.layers[0]):
            print("Expected training feature of length",len(self.layers[0]))
            return
        if len(training_labels) != len(self.layers[len(self.layers)-1]):
            print("Expected training labels of length",len(self.layers[len(self.layers)-1]))
            return

    def loadParams(self, filename):
        file = open(filename,"r")
        fileStr = file.readline()
        strArr = fileStr.split(" ")
        floatArr = []

        for string in strArr:
            if(len(string) != 0):
                floatArr.append(float(string))
        


        arr = floatArr

        cnt = 0

        for layer in self.layers:
            for node in layer:
                node.bias = arr[cnt]
                cnt += 1

        for layer in self.layers:
            for node in layer:
                for edge in node.outputs:
                    edge.weight = arr[cnt]
                    cnt += 1



    def saveParams(self, filename):
        file = open(filename,"w")
        for layer in self.layers:
            for node in layer:
                file.write(str(node.bias) + " ")

        for layer in self.layers:
            for node in layer:
                for edge in node.outputs:
                    file.write(str(edge.weight) + " ")



    def wiggle(self, amount=0.1):
        for layer in self.layers:
            for node in layer:
                node.bias += random.random() * amount
                for outputEdge in node.outputs:
                    outputEdge.weight += random.random() * amount


        

    def predict(self, input_values):
        input_layer = self.layers[0]

        for i,t_node in enumerate(input_values):
            input_layer[i].value = t_node

        length = len(self.layers)

        for i in range(1,length):
            for node in self.layers[i]:
                sum = 0.0
                for input_edge in node.inputs:
                    sum += input_edge.weight * input_edge.from_node.value
                sum += node.bias

                node.value = node.activation_function(sum)

        return self.layers[len(self.layers)-1]


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.to_node = to_node
        self.from_node = from_node
        self.weight = weight
        pass

class Node:
    def __init__(self, activation_function):
        self.value = 0.0
        self.bias = random.random()*2-1
        self.inputs = []
        self.outputs = []
        self.activation_function = activation_function
        pass

    def calculate_value(self):
        pass
        return 0.0



