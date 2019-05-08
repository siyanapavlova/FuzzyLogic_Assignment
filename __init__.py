from readData import readData
from fuzzify import fuzzify
from inference import infer
from defuzzify import defuzzifyCoG, defuzzifyDoA
import pprint

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    rules, variables, given = readData("tippingRulebase.txt")

    # pp.pprint(rules)
    # pp.pprint(variables)
    # pp.pprint(given)

    mfs = fuzzify(variables, given)

    # pp.pprint(mfs)

    ans = infer(rules, mfs)
    cog = defuzzifyCoG(variables, ans)
    doa = defuzzifyDoA(variables, ans)

    # pp.pprint(ans)

    print "Result by using Centre of Gravity         = ", cog
    print "Result by using Dilation of the Aggregate = ", doa
