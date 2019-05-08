from inference import infer

def defuzzifyCoG(variables, ans):
    '''Defuzzify using the Centre of Gravity method
    Parameters: variables, ans
    Output: the defuzzified value
    '''
    finalAns = 0
    for var in ans:
        denominator = 0
        nominator = 0
        for description in ans[var]:
            if ans[var][description] != 0:
                area = (-2*variables[var][description]['a'] + variables[var][description]['alfa'] + 2*variables[var][description]['b'] + variables[var][description]['beta'])/2.0
                missing = ((1-ans[var][description])*((1 - ans[var][description])*100 + variables[var][description]['b'] - variables[var][description]['a']))/2.0
                missing = (1-ans[var][description])*((1-ans[var][description])*(variables[var][description]['b'] + variables[var][description]['beta'] - variables[var][description]['a'] + variables[var][description]['alfa']))/2
                area -= missing
                denominator += area
                nominator += (area*(variables[var][description]['a'] - variables[var][description]['alfa'] + variables[var][description]['b'] + variables[var][description]['beta']))/2
    if denominator == 0:
        return 0
    finalAns = nominator/denominator
    return finalAns

def defuzzifyDoA(variables, ans):
    '''Defuzzify using the Dilation of the Aggregate method
    Parameters: variables, ans
    Output: the defuzzified value
    '''
    finalAns = 0
    for var in ans:
        denominator = 0
        nominator = 0
        for description in ans[var]:
            if ans[var][description] != 0:
                area = ((-variables[var][description]['a'] + variables[var][description]['alfa'] + variables[var][description]['b'] + variables[var][description]['beta'])*ans[var][description])/2
                denominator += area
                nominator += (area*(variables[var][description]['a'] - variables[var][description]['alfa'] + variables[var][description]['b'] + variables[var][description]['beta']))/2
    if denominator == 0:
        return 0
    finalAns = nominator/denominator
    return finalAns
