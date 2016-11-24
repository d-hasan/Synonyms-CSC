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
    dot_prod = 0
    for a in vec1:
        if a in vec2:
            dot_prod += vec1[a] * vec2[a]
    magnitude_prod = norm(vec1) + norm(vec2)
    return dot_prod/magnitude_prod


def build_semantic_descriptors(sentences):
    #Convential method; test against (try and except) to compare run times
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d:
                d[word] = {}
            for i in sentence:
                if i != word:
                    if i in d[word]:
                        d[word][i] += 1
                    else:
                        d[word][i] = 1
    return d
    



def build_semantic_descriptors_from_files(filenames):
    sentences = []
    start = time.time()
    for n in range(len(filenames)):
        file = open(filenames[n], encoding="latin1").read().lower()
        file = file.replace('!', " ").replace('.', ' ').replace('?', ' ')
        file = file.split()
        sentences.append(file)
    #print(sentences)
    #dictionary = build_semantic_descriptors(sentences)
    #print(dictionary['pride'])
    print(time.time() - start)
    #return dictionary




def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    scores = []
    for i in choices:
        scores.append(cosine_similarity(semantic_descriptors[word],semantic_descriptors[i]))
    

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    filenames = ["swann.txt", "war_and_peace.txt"]
    semantic_descriptors = build_semantic_descriptors_from_files(filenames)
    
    # choices = ['him', 'her', 'woman', 'prejudice']
    # print(most_similar_word(man, choices, semantic_descriptors, cosine_similary))
    
    