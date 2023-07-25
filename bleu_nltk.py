from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction

def compute_code_bleu(candidate_code, reference_code):
    """
    Compute the CodeBLEU score.
    
    :param candidate_code: The generated code as a list of tokens.
    :param reference_code: The reference code as a list of tokens.
    :return: The CodeBLEU score.
    """
    # We use the smoothing function to avoid division by zero
    smoothing = SmoothingFunction().method1

    return sentence_bleu([reference_code], candidate_code, smoothing_function=smoothing)



if __name__ == '__main__':
    # Use the function
    candidate_code = 'print("Hello, World!")'.split()
    reference_code = 'print("Hello, World!")'.split()

    score = compute_code_bleu(candidate_code, reference_code)
    print(f"CodeBLEU score: {score}")
