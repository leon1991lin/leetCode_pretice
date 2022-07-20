'''
1832. Check if the Sentence Is Pangram
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
'''
def checkIfPangram(sentence: str) -> bool:
    # ans = []
    # for c in sentence:
    #     if c not in ans:
    #         ans.append(c)
    # return len(ans)==26
    
    return len(set(sentence))==26

if __name__ == "__main__":
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence))

    sentence = "leetcode"
    print(checkIfPangram(sentence))

