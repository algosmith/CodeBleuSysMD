# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

# -*- coding:utf-8 -*-
import argparse
from bleu_nltk import compute_code_bleu
from weigh_n_gram import weighted_bleu
from grammar_sysmd import syntax_match

parser = argparse.ArgumentParser()
parser.add_argument('--refs', type=str, nargs='+', required=True,
                        help='reference files')

alpha = 0.33
beta = 0.33
gamma = 0.33

args = parser.parse_args()

# preprocess inputs
pre_references = [[x.strip() for x in open(file, 'r', encoding='utf-8').readlines()] \
                for file in args.refs]
hypothesis = [x.strip() for x in open(args.hyp, 'r', encoding='utf-8').readlines()]

# calculate ngram match (BLEU)
tokenized_hyps = [x.split() for x in hypothesis]
tokenized_refs = [[x.split() for x in reference] for reference in references]

ngram_match_score = compute_code_bleu(tokenized_refs,tokenized_hyps)

# calculate weighted ngram match
keywords = [x.strip() for x in open('keywords/'+args.lang+'.txt', 'r', encoding='utf-8').readlines()]
def make_weights(reference_tokens, key_word_list):
    return {token:1 if token in key_word_list else 0.2 \
            for token in reference_tokens}
tokenized_refs_with_weights = [[[reference_tokens, make_weights(reference_tokens, keywords)]\
            for reference_tokens in reference] for reference in tokenized_refs]

weighted_ngram_match_score = weighted_bleu(references,candidate=candidate,max_n=4)

# calculate syntax match
syntax_match_score = syntax_match.corpus_syntax_match(references, hypothesis, args.lang)

print('ngram match: {0}, weighted ngram match: {1}, syntax_match: {2}, '.\
                    format(ngram_match_score, weighted_ngram_match_score, syntax_match_score))

code_bleu_score = alpha*ngram_match_score\
                + beta*weighted_ngram_match_score\
                + gamma*syntax_match_score\
                
print('CodeBLEU score: ', code_bleu_score)




