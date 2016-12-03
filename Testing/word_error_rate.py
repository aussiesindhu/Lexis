import numpy

# Program to calculate error rate between 2 words
def word_error_rate(first, second):

    w = numpy.zeros((len(first)+1)*(len(second)+1), dtype=numpy.uint8)
    w = w.reshape((len(first)+1, len(second)+1))
    for i in range(len(first)+1):
        for j in range(len(second)+1):
            if i == 0:
                w[0][j] = j
            elif j == 0:
                w[i][0] = i

    # computation of error rate
    for i in range(1, len(first)+1):
        for j in range(1, len(second)+1):
            if first[i-1] == second[j-1]:
                w[i][j] = w[i-1][j-1]
            else:
                sub = w[i-1][j-1] + 1
                ins    = w[i][j-1] + 1
                dele    = w[i-1][j] + 1
                w[i][j] = (sub+ ins + dele)/(max(len(first),len(second)))
    return w[len(first)][len(second)]

def accuracy(first,second):
    err=word_error_rate(first,second);
    return (1-err)*100
    
    
    

#enter the 2 question pattern to compare
"""
Example for analyzing the word error rate for a question that is recon=gnized differently between
2 models  i.e. Sphynx and Siri

LEXUS: "Tall es mantain"
Siri: "Tallest mountain in US"

The above code returns the error rate as 0.698z

"""
word_error_rate("who is there".split(), "is there".split())
accuracy("who is there".split(), "is there".split())


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
