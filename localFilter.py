import numpy as np
import pandas as pd

def filterZeros(dataFrameIn)->pd.DataFrame:
    df = pd.DataFrame()
    return df

def isRemovable(dfColumn,conditionPercentage,checkFor="zeros")->bool:
    response = False
    cp = conditionPercentage
    #quantity of zeros
    colLength = len(dfColumn)
    qBad = []
    match checkFor:
        case "zeros":
            qBad = np.sum([dfColumn[i]==0 for i in range(0,colLength)])
        case "nan":
            qBad = np.sum(np.isnan(dfColumn[i]) for i in range(0,colLength))
            
    if qBad>cp/100*colLength:
        return True
    return response

    
