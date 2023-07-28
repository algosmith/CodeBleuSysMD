# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

# -*- coding:utf-8 -*-
import argparse
from bleu_nltk import compute_code_bleu
from weigh_n_gram import weighted_bleu
from grammar_sysmd import corpus_syntax_match, syntax_match

parser = argparse.ArgumentParser()
#parser.add_argument('--refs', type=str, nargs='+', required=True,
#                        help='reference files')

alpha = 0.33
beta = 0.33
gamma = 0.33

#args = parser.parse_args()

# preprocess inputs
candidate = 'LaptopParts::Keyboard hasA\nValue layout: String = \"QWERTY\",\nValue backlight: Boolean = true,\nValue language: String = \"English-US\".'
reference = 'LaptopParts::Keyboard hasA\nValue layout: String = \"QWERTY\",\nValue backlight: Boolean = true,\nValue language: String = \"English-US\".'

weighted_ngram_match_score = weighted_bleu(reference,candidate=candidate,max_n=4)
ngram_match_score = compute_code_bleu(reference,candidate)

# calculate syntax match
syntax_match_score = corpus_syntax_match(reference, candidate)

print('ngram match: {0}, weighted ngram match: {1}, syntax_match: {2}, '.\
                    format(ngram_match_score, weighted_ngram_match_score, syntax_match_score))

code_bleu_score = alpha*ngram_match_score\
                + beta*weighted_ngram_match_score\
                + gamma*syntax_match_score\
                
print('CodeBLEU score: ', code_bleu_score)




