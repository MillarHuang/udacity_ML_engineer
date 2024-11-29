"""
The test code to get the mean of test scores and its relevant number
"""
import math
import numpy as np

best = 10


def test_code(test_scores):
    """
    The test code to get the mean of test scores and its relevant number

    Argument:
    test_scores:list. the list of scores

    Return:
    no return
    """
    print(np.mean(test_scores))
    curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
    print(np.mean(curved_test_scores))


if __name__ == '__main__':
    test_scores_trial = [88, 92, 79, 93, 85]
    test_code(test_scores_trial)
    print("Here it is!")
