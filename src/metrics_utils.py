from rouge_score import rouge_scorer
from sklearn.metrics import accuracy_score

def calcular_exactitud(y_verdadero, y_predicho):
    return accuracy_score(y_verdadero, y_predicho)

def calcular_rouge(y_verdadero, y_predicho):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, pred)['rougeL'].fmeasure for ref, pred in zip(y_verdadero, y_predicho)]
    return sum(scores) / len(scores)