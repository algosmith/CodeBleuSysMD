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
candidate = 'Vehicle isA Any\nPassengerCar isA Vehicle\nSportsCar isA PassengerCar\nLuxuryCar isA PassengerCar\nFamilyCar isA PassengerCar\nSmallCars isA PassengerCar\nSUV isA PassengerCar\nPetrolCar isA PassengerCar\nDieselCar isA PassengerCar\nBEV isA PassengerCar\nCNGCar isA PassengerCar\nHEV isA PassengerCar\nPHEV isA PassengerCar\nAlternateFuelCar isA PassengerCar\nPassengerCar imports Drivetrains, Frame, Chassis, LubricationSystems, Sensors\nPassengerCar hasA\nnoAutomation: NoAutomation,\ndriverAssistance: DriverAssistance,\npartialAutomation: PartialAutomation,\nconditionalAutomation: ConditionalAutomation,\nhighAutomation: HighAutomation,\nfullAutomation: FullAutomation EOF'
reference = 'Vehicle isA Any\nPassengerCar isA Vehicle\nSportsCar isA PassengerCar\nLuxuryCar isA PassengerCar\nFamilyCar isA PassengerCar\nSmallCars isA PassengerCar\nSUV isA PassengerCar\nPetrolCar isA PassengerCar\nDieselCar isA PassengerCar\nBEV isA PassengerCar\nCNGCar isA PassengerCar\nHEV isA PassengerCar\nPHEV isA PassengerCar\nAlternateFuelCar isA PassengerCar\nPassengerCar imports Drivetrains, Frame, Chassis, LubricationSystems, Sensors\nPassengerCar hasA\nnoAutomation: NoAutomation EOF'

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




