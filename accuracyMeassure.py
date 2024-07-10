from numpy import ndarray
from sklearn.metrics import confusion_matrix
from scoreValidator import score
def accuracyMeassure(y_true:ndarray,y_predict:ndarray)->float:
    confusion_matrix_var = confusion_matrix(y_true,y_predict)
    return score(confution_matrix_var=confusion_matrix_var)