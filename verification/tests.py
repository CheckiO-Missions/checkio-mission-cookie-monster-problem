"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3]],
            "answer": [2, 1],
        },
        {
            "input": [[1, 2, 3, 4, 5, 6]],
            "answer": [4, 2, 1],
        },
        {
            "input": [[2, 3, 5, 8, 13, 21, 34, 55, 89]],
            "answer": [55, 21, 8, 3, 2],
        },
        {
            "input": [[1, 10, 17, 34, 43, 46]],
            "answer": [46, 34, 17, 9, 1],
        },
    ],
    "Extra": [
        {
            "input": [[11, 26, 37, 44, 49, 52, 68, 75, 87, 102]],
            "answer": [37, 31, 15, 12, 7, 4],
        },
        {
            "input": [[2**n for n in range(10)]],
            "answer": [512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
        },
    ]
}
