import sys


def CKY_parse(grammarMap: dict, sentence: str):
    tokens = sentence.split(" ")
    N = len(tokens)
    dp = [[list() for _ in range(N)] for _ in range(N)]

    for col in range(N):
        for row in range(col, -1, -1):
            # Add valid parses to dp for the this word
            if row == col:
                word = tokens[row]
                parents = grammarMap[word]

                # [parent, (row, col, index) of children that form this parent]
                items = [[parent, []] for parent in parents]

                # Push all tags to current cell
                dp[row][col].extend(items)
            else:
                # Traverse all possible substrings that can combine
                for k in range(row, col):
                    firstPossibilities = dp[row][k]
                    secondPossibilities = dp[k+1][col]

                    for i in range(len(firstPossibilities)):
                        firstChild = firstPossibilities[i]
                        firstNodeName = firstChild[0]

                        for j in range(len(secondPossibilities)):
                            secondChild = secondPossibilities[j]
                            secondNodeName = secondChild[0]

                            # Get new parent from the two children
                            print(firstNodeName, secondNodeName)
                            key = ' '.join([firstNodeName, secondNodeName])

                            if key not in grammarMap:
                                continue

                            newParents = grammarMap[key]

                            # Push new parent tag to current cell
                            firstChildPtr = (row, k, i)
                            secondChildPtr = (k+1, col, j)
                            for newParent in newParents:
                                dp[row][col].append([
                                    newParent,
                                    [firstChildPtr, secondChildPtr]
                                ])

    # TEST
    print()
    for row in dp:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

    return dp


def walkback(sentence, dp, row, col, idx, compact=True):
    tokens = sentence.split(" ")

    def dfs(curR, curC, curIdx, depth=0):
        result = ''
        indent = '  ' * depth if not compact else ''
        newline = '\n' if not compact else ''
        space = ' ' if compact else ''

        # [parent, (row, col, index) of children that form this parent]
        parent, children = dp[curR][curC][curIdx]

        # Leaf node
        if len(children) == 0:
            return '%s[%s %s]%s' % (indent, parent, tokens[curC], newline)
        else:
            for child in children:
                childR, childC, childIdx = child
                tag = dfs(childR, childC, childIdx, depth+1)
                result += space + tag

        return '%s[%s%s%s%s]%s' % (indent, parent, newline, result, indent, newline)

    return dfs(row, col, idx)


def main():
    CNF_file_path = sys.argv[1]

    mode = sys.argv[2] if len(
        sys.argv) >= 3 else "expand"  # compact vs. expand

    sentences = [
        "Sales of the company to return to normalcy .",
        "The new products and services contributed to increase revenue .",
        "Dow falls as recession indicator flashed red and economical worries continue through the month .",
        "Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal ."
    ]
    # sentence = input("Input sentence: ")
    sentence = sentences[1]

    lines = []

    # TEST
    print()
    print("Sentence:", sentence)
    print()

    with open(CNF_file_path, 'r') as reader:
        while line := reader.readline():
            lines.append(line.strip())

    # key = value or pair of literals -> value = list of possible parent literals
    grammarMap = dict()

    for line in lines:
        line: str
        tokens = line.split(' ', maxsplit=1)
        parent, children = tokens

        if children not in grammarMap:
            grammarMap[children] = set()
        else:
            # TEST
            # print("Repeated children:", children)
            pass

        grammarMap[children].add(parent)

    # TEST
    # print()
    # print("Grammer size vs Lines size:", len(grammarMap), len(lines))
    # print()

    # TEST
    # print("All lines:")
    # for line in lines:
    #     print(line)
    # print()

    # Do a forward CKY parse
    dp = CKY_parse(grammarMap, sentence)
    print("Sentence:", sentence)
    print("Parses:", dp[0][-1])
    print("Number of parses:", len(dp[0][-1]))

    for i in range(len(dp[0][-1])):
        print(walkback(sentence, dp, 0, len(dp)-1, i, compact=(mode == "compact")))


main()
