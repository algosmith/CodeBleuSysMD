from nltk import ngrams
from collections import Counter

def weighted_ngram_match(seq1, seq2, n):
    # Generate n-grams for each sequence
    ngrams1 = Counter(ngrams(seq1, n))
    ngrams2 = Counter(ngrams(seq2, n))

    # Compute the weighted intersection of n-grams
    intersection = ngrams1 & ngrams2
    intersection_count = sum((count * len(gram)) for gram, count in intersection.items())

    # Compute the total weighted count of n-grams
    total_count = sum((count * len(gram)) for gram, count in ngrams1.items()) + sum((count * len(gram)) for gram, count in ngrams2.items())

    # Return the weighted Jaccard index
    return intersection_count / total_count if total_count != 0 else 0



if __name__ == '__main__':
    seq1 = ["CarBodyParts::SideMirror", "hasA", "Value", "visibility:", "String", "=", "\"Wide-angle\""]
    seq2 = ["CarBodyParts::SideMirror", "hasA", "Value", "visibility:", "String", "=", "\"Wide-angle\""]
    print(weighted_ngram_match(seq1, seq2, 2))  # This would output 1.0, since seq1 and seq2 are identical