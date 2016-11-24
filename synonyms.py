'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math, time


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    ''' Return the cosine similaryt of two vectors stored as dictionaries
        Assume all dictionary values are integers'''
        
    dot_prod = 0
    for a in vec1:
        if a in vec2:
            dot_prod += vec1[a] * vec2[a]
    magnitude_prod = norm(vec1) * norm(vec2)
    
    if dot_prod == 0:
        return -1
        
    return dot_prod/magnitude_prod


def build_semantic_descriptors(sentences):
    #Convential method; test against (try and except) to compare run times
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d:
                d[word] = {}
            for accomp_word in sentence:
                if accomp_word != word:
                    if accomp_word in d[word]:
                        d[word][accomp_word] += 1
                    else:
                        d[word][accomp_word] = 1
    return d
    



# def build_semantic_descriptors_from_files(filenames):
#     sentences = []
#     start = time.time()
#     for n in range(len(filenames)):
#         file = open(filenames[n], encoding="latin1").read().lower()
#         file = file.replace('!', " ").replace('.', ' ').replace('?', ' ')
#         file = file.split()
#         sentences.append(file)
#     #print(sentences)
#     dictionary = build_semantic_descriptors(sentences)
#     #print(dictionary['pride'])
#     print(time.time() - start)
#     #return dictionary


def build_semantic_descriptors_from_files(filenames):
    sentences = []
    start = time.time()
    for text in filenames:
        file = open(text, encoding="utf8").read().lower().replace("\n", " ").replace(',', ' ').replace('-',' ').replace('--', ' ').replace(':',' ').replace(';',' ').split('.')
        for i in range(len(file)):
            file[i] = file[i].split('!')
            for j in range(len(file[i])):
                file[i][j] = file[i][j].split('?')
                for k in range(len(file[i][j])):
                    file[i][j][k] = file[i][j][k].split()
                    sentences.append(file[i][j][k])
    print("success, building descriptors")
    dictionary = build_semantic_descriptors(sentences)
    print(time.time() - start)
    return dictionary

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    scores = []
    if word not in semantic_descriptors:
        return -1
    for choice in choices:
        if choice not in semantic_descriptors:
            scores.append(-1)
            continue
        scores.append(similarity_fn(semantic_descriptors[word], semantic_descriptors[choice]))
    return choices[scores.index(max(scores))]
    

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    
    file = open(filename, encoding="latin1").read().split("\n")
    for i in range(len(file)):
        file[i] = file[i].split()
        if len(file[i]) == 0:
            del file[i]
            i -= 1
            continue
        if file[i][1] == most_similar_word(file[i][0], file[i][2:], semantic_descriptors, cosine_similarity):
            correct += 1
    
    return correct/len(file)

if __name__ == "__main__":
    filenames = ["swann.txt", "war_and_peace.txt"]
    # semantic_descriptors = build_semantic_descriptors_from_files(filenames)
    
    # choices = ['him', 'her', 'woman', 'prejudice']
    # print(most_similar_word(man, choices, semantic_descriptors, cosine_similary))
    
    