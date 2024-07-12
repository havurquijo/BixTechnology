import numpy as np


def score(confution_matrix_var:np.ndarray)->float:
    true_positive = confution_matrix_var[1,1]
    false_positive = confution_matrix_var[0,1]
    false_negative = confution_matrix_var[1,0]

    return true_positive*25.0 + false_positive*10.0 + false_negative*500.0

def f2_score(confution_matrix_var:np.ndarray)->float:
    beta=2
    true_positive = confution_matrix_var[1,1]
    false_positive = confution_matrix_var[0,1]
    false_negative = confution_matrix_var[1,0]
    return (1+beta**2)*true_positive/((1+beta**2)*true_positive+false_positive+beta**2*false_negative)

def weigthedScore(confution_matrix_var:np.ndarray)->float:
    true_positive = confution_matrix_var[1,1]
    false_positive = confution_matrix_var[0,1]
    false_negative = confution_matrix_var[1,0]
    
    total = 25+10+500
    w_tp = 25/total
    w_fp = 10/total
    w_fn = 500/total
    return true_positive*w_tp + false_positive*w_fp + false_negative*w_fn
