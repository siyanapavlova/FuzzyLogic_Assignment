from fuzzify import fuzzify

def infer(rules, mfs):
    '''Takes a rules array with a structure provided by the readData module and a
    membership functions dictionary with a structure as provided by the fuzzifier module.
    Sample results for the inference engine can be seen in ​ inferenceSampleOutput.txt ​ .
    '''
    ans = {}
    for rule in rules:
        if ans == {}:
            ans[rule['result']['name']] = {}
        if rule['connective'] == ' or ' or rule['connective'] == None:
            value = 0
            for var in rule['variables']:
                value = max(value, mfs[var][rule['variables'][var]])
        if rule['connective'] == ' and ':
            value = 1
            for var in rule['variables']:
                value = min(value, mfs[var][rule['variables'][var]])
        if ans[rule['result']['name']].get(rule['result']['value']):
            ans[rule['result']['name']][rule['result']['value']] = max(ans[rule['result']['name']][rule['result']['value']],value)
        else:
            ans[rule['result']['name']][rule['result']['value']] = value
    return ans
