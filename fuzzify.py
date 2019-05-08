from readData import readData

def fuzzify(variables, given):
    '''Takes a variables dictionary with a structure as provided by the readData module
    and a "given" array and produces a membership functions dictionary.
    '''
    mfs = {}
    for var in given:
        if variables.get(var['name']):
            mf = {}
            for description in variables[var['name']]:
                mf[description] = 0
                if var['value'] < variables[var['name']][description]['a'] - variables[var['name']][description]['alfa'] or var['value'] > variables[var['name']][description]['b'] + variables[var['name']][description]['beta']:
                    mf[description] = 0
                    continue
                if var['value'] < variables[var['name']][description]['a']:
                    mf[description] = (var['value']-variables[var['name']][description]['a']+variables[var['name']][description]['alfa'])/variables[var['name']][description]['alfa']
                else:
                    if var['value'] > variables[var['name']][description]['b']:
                        mf[description] = (variables[var['name']][description]['b']+variables[var['name']][description]['beta']-var['value'])/variables[var['name']][description]['beta']
                    else:
                        mf[description] = 1
            mfs[var['name']] = mf
    return mfs
