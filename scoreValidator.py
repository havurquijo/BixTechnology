import numpy as np


def score(confution_matrix_var:np.ndarray)->float:
    true_positive = confution_matrix_var[1,1]
    false_positive = confution_matrix_var[0,1]
    false_negative = confution_matrix_var[1,0]

    return true_positive*25.0 + false_positive*10.0 + false_negative*500.0