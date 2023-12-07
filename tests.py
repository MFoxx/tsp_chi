from algorithm import find_path

import os, sys

class HiddenPrints:
    def __init__(self, e):
        self.e = e
    
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open('logs/log--{}.txt'.format(self.e), 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def test():
    inputs = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20']
    outputs = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'r16', 'r17', 'r18', 'r19', 'r20']
    test_cases = 20
    failed = 0
    print('🧪 TESTING {} CASES: '.format(test_cases))
    for i in range(test_cases):
        expected_o = process_output(outputs[i])
        with HiddenPrints(inputs[i]):
            results = find_path('data/'+inputs[i]+'.txt')
        if expected_o[0] == results[1]:
            print('✅ T{} EXPECTED WEIGHT CORRECT'.format(i + 1))
        else:
            print('❌ T{} EXPECTED WEIGHT INCORRECT: Expected {}; Found: {}; Test Case Input: {}'.format(
                i + 1,
                expected_o[0],
                results[1],
                inputs[i]
            ))

        if expected_o[1] == results[0]:
            print('✅ T{} EXPECTED PATH CORRECT'.format(i + 1))
        else:
            print('❌ T{} EXPECTED PATH INCORRECT: Expected: {}; Found: {}; Test Case Input: {}'.format(
                i + 1,
                expected_o[1],
                results[0],
                inputs[i]
            ))
            failed += 1


    if failed == 0:
        print("✅ ALL CASES PASSED")
    else:
        print("❌ {} FAILED".format(failed))


def process_output(path):
    with open('data/expected_results/'+path+'.txt') as f:
        weight = int(f.readline().strip())
        v = f.readline().strip().split(',')
        values = [int(x) for x in v]

    return weight, values


if __name__ == '__main__':
    test()

