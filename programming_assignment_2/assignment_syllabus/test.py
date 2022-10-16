import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('results.json', 'w') as f:
        JSONTestRunner(visibility='visible', verbosity=2, buffer=True, stream=f).run(suite)

    import json
    with open('results.json', 'r') as f:
      data = json.load(f)
    tests = sorted(data['tests'], key=lambda item: item['name'])
    for test in tests:
        if test['score']==test['max_score']:
            print(bcolors.OKGREEN+'-'*10)
        else:
            print(bcolors.FAIL+'-'*10)
        for k,v in test.items():
            print(f"{k}: {v}")


    print(bcolors.HEADER + bcolors.BOLD + f"Your final score: {round(data['score'],2)}/18")
    print(bcolors.ENDC)
