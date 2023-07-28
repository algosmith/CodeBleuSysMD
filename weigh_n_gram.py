import nltk
from collections import Counter
import numpy as np

KEYWORDS = set(['def', 'for', 'while', 'if', 'else', 'class', 'try', 'except'])  # Replace with your keywords

def ngram_counts(code, n):
    words = nltk.word_tokenize(code)
    return Counter(nltk.ngrams(words, n))

def weighted_precision(reference, candidate, n):
    ref_counts = ngram_counts(reference, n)
    cand_counts = ngram_counts(candidate, n)

    match_count = 0
    total_count = 0
    for ngram, count in cand_counts.items():
        total_count += count
        match_count += min(count, ref_counts[ngram]) * ngram_weight(ngram)

    return match_count / total_count if total_count > 0 else 0

def ngram_weight(ngram):
    return 1.5 if any(word in KEYWORDS for word in ngram) else 1

def brevity_penalty(reference, candidate):
    ref_words = nltk.word_tokenize(reference)
    cand_words = nltk.word_tokenize(candidate)

    if len(cand_words) > len(ref_words):
        return 1
    else:
        return np.exp(1 - len(ref_words) / len(cand_words))

def bleu(reference, candidate, max_n):
    precisions = [weighted_precision(reference, candidate, n) for n in range(1, max_n + 1)]
    return brevity_penalty(reference, candidate) * np.exp(np.mean(np.log(precisions)))
