def readData(filename):
    ''' Takes the name of a text file, e.g. ‘example.txt’, parses the file
    and creates a rules array, a variables dictionary and a given array.
    '''
    f = open(filename, "r")
    print "\nReading file", filename, '...\n'

    rules = []
    variables = {}
    given = []

    f.readline()

    while True:
        x = f.readline().lower()
        if x == '':
            break
        if x[0:4] == 'rule':
            var = {}
            r = x.split(' then ')[0].split('if ')[1]
            connective = None
            if ' or ' in r:
                connective = ' or '
            if ' and ' in r:
                connective = ' and '
            if connective == None:
                nextRule = r
                name = nextRule.split(' is ')[0].strip()
                if 'the ' in name:
                    name = name.split('the ')[1].strip()
                value = nextRule.split(' is ')[1].strip()
                var[name] = value
            else:
                for nextRule in r.split(connective):
                    name = nextRule.split(' is ')[0].strip()
                    if 'the ' in name:
                        name = name.split('the ')[1].strip()
                    value = nextRule.split(' is ')[1].strip()
                    var[name] = value
            result = x.split(' then ')[1].strip()
            name = result.split(' is ')[0].strip()
            if 'the ' in name:
                name = name.split('the ')[1].strip()
            value = result.split(' is ')[1].strip()
            res = {'name':name,'value':value}
            rules.append({'connective':connective, 'variables': var, 'result':res})
        else:
            if len(x) > 1 and len(x.split(' ')) == 1 and '=' not in x:
                values = {}
                line = f.readline()
                while True:
                    line = f.readline()
                    if len(line.split(' ')) == 5:
                        values[line.split(' ')[0].strip()] = {
                                        'a':float(line.split(' ')[1].strip()),
                                        'b':float(line.split(' ')[2].strip()),
                                        'alfa':float(line.split(' ')[3].strip()),
                                        'beta':float(line.split(' ')[4].strip())}
                    else:
                        break
                variables[x.strip()] = values
            else:
                if '=' in x:
                    given.append({'name':x.split('=')[0].strip(), 'value':float(x.split('=')[1].strip())})

    f.close()
    return rules, variables, given
