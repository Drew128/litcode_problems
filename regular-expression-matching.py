class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pairs = [[s, p]]
        for _ in range(100):
            new_pairs = []
            for pair in pairs:
                if pair[1][1:2] == '*':
                    new_pairs.append([pair[0], pair[1][2:]])                 # add pattern where * means 0
                    if pair[1][0] == '.' or pair[0][0:1] == pair[1][0:1]:
                        new_one = [pair[0][1:], pair[1]]
                        if '|'.join(new_one) not in {'|'.join(each) for each in new_pairs}:
                                                                             # check if pattern not in the list
                            new_pairs.append([pair[0][1:], pair[1]])         # add pattern where * match at least once
                elif pair[1][0] == '.' or pair[0][0] == pair[1][0]:
                    new_pairs.append([pair[0][1:], pair[1][1:]])             # delete one element if matching
            if [each for each in new_pairs if each == ['', '']]:             # when we get a first match
                return True
            else:
                new_pairs = [v for i, v in enumerate(new_pairs) if (v[0] and v[1]) or v[1][1:2] == '*']  
                                                                             # delete empty pattern or string
            if not new_pairs:
                return False                                                 # where there is no suitable pattern
            pairs = new_pairs
