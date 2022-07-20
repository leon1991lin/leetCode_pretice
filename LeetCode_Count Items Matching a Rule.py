'''
1773. Count Items Matching a Rule

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color,
and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
'''
def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    columns, ans = ['type', 'color', 'name'], 0
    for i in range(len(items)):
        if items[i][columns.index(ruleKey)] == ruleValue:
            ans += 1
    return ans

if __name__ == "__main__":
    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(countMatches(items,ruleKey,ruleValue))

    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
             ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    print(countMatches(items,ruleKey,ruleValue))