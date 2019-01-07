import re

def string_similarity(s1, s2):
    s1 = re.sub(r'\s+', '', s1)
    s2 = re.sub(r'\s+', '', s2)

    if s1 == "" and s2 == "":
        return 1.

    if len(s1) == 0 or len(s2) == 0:
        return 0.

    if s1 == s2:
        return 1.

    if len(s1) == 1 or len(s2) == 1:
        return 0.

    bigrams = {}
    for i in range(len(s1)-1):
        bigram = s1[i:i+2]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1

    intersection = 0
    for i in range(len(s2)-1):
        bigram = s2[i:i+2]
        if bigram in bigrams and bigrams[bigram] > 0:
            bigrams[bigram] -= 1
            intersection += 1

    return (2. * intersection) / (len(s1) + len(s2) - 2)

def string_similarity_test():
    tests = [{ 'first': 'french', 'second': 'quebec', 'expected': 0 },
      { 'first': 'france', 'second': 'france', 'expected': 1 },
      { 'first': 'fRaNce', 'second': 'france', 'expected': 0.2 },
      { 'first': 'healed', 'second': 'sealed', 'expected': 0.8 },
      { 'first': 'web applications', 'second': 'applications of the web', 'expected': 0.7878787878787878 },
      { 'first': 'this will have a typo somewhere', 'second': 'this will huve a typo somewhere', 'expected': 0.92 },
      { 'first': 'Olive-green table for sale, in extremely good condition.', 'second': 'For sale: table in very good  condition, olive green in colour.', 'expected': 0.6060606060606061 },
      { 'first': 'Olive-green table for sale, in extremely good condition.', 'second': 'For sale: green Subaru Impreza, 210,000 miles', 'expected': 0.2558139534883721 },
      { 'first': 'Olive-green table for sale, in extremely good condition.', 'second': 'Wanted: mountain bike with at least 21 gears.', 'expected': 0.1411764705882353 },
      { 'first': 'this has one extra word', 'second': 'this has one word', 'expected': 0.7741935483870968 },
      { 'first': 'a', 'second': 'a', 'expected': 1 },
      { 'first': 'a', 'second': 'b', 'expected': 0 },
      { 'first': '', 'second': '', 'expected': 1 },
      { 'first': 'a', 'second': '', 'expected': 0 },
      { 'first': '', 'second': 'a', 'expected': 0 },
      { 'first': 'apple event', 'second': 'apple    event', 'expected': 1 },
      { 'first': 'iphone', 'second': 'iphone x', 'expected': 0.9090909090909091 }]

    for test in tests:
        result = string_similarity(test['first'], test['second'])
        assert abs(result - test['expected']) < 1e-9

    print("PASSED.")

if __name__ == "__main__":
    string_similarity_test()
