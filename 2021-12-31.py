"""
Togetherness of a Family
In the world of magic land, there is a park in which a group of people are playing a game. Every person in the group is a child of one another person in the group except one person who is the parent of all the people in the group. Here, each person is represented by a number that if there are ‘n’ persons in the group then they are represented by numbers 1 to 7. The direct and indirect child relationship is defined as follows:

(i) A person ‘b’ is said to be direct child of ‘a’ if ‘a’ is parent of ‘b’.

(ii) Person is ‘c’ is said to be indirect child of ‘a’ when ‘c’ is child of ‘b’ and ‘b’ is child of ‘a’.

(iii) A indirect child ‘i’ of a person ‘p’ is also an indirect child of parent of ‘p’.

In the game, everyone is given a token which has a number written on it and to test the togetherness of the family, the family is given some queries.

In one query, a number representing a person is given and it is asked to find the number of direct and indirect children of the person who have prime number in the token given to them.

For more clarifications see the example below.

There are seven person in the group and the tokens assigned to each of them are:

Person

Token Number

1

1

2

2

3

3

4

4

5

5

6

6

7

7

We are given 2 queries:

Query1: The person numbered as 1 is given and we need to findout the number of children(both direct and indirect under 1) which have a token with prime number value:

Answer: 4.

Explanation:

For the person numbered as 1, its direct children are persons numbered as 2 and 3 and they have tokens 2 and 3 respectively which are prime numbers.

The person numbered as 5 and 7 are also children (indirect) of the person number 1 hence they also added up to the count and hence there are a total of 4 people who are children of person number 1 and have a prime number token.

Query2: The person numbered as 6 is given

Answer: 0.

Explanation:

The person with number 6 has no children and hence there are 0 children under him having tokens with prime number values.

Input Format:

First line of the input contains N, the number of persons playing in the park

Second line contains token numbers assigned for the persons and they are separated by a space ith number in the line contains the value of the token assigned to the ith person.

Next N-1 lines contains two integers Xi and Yi separated by a space and indicates that Xi is the parent of Yi.

The next line contains the number of queries, Q

Next Q lines contain the person queried

Note: The persons are indexed from 1.

Output Format:

Output Q lines, each containing only 1 integer, the number of children for the given node, which have their token value as a prime number

Example:

Input:

7

1 2 3 4 5 6 7

1 2

1 3

2 4

2 5

3 6

3 7

2

1

6

Output:

4

0

As can be seen

1 is the parent of both 2 and 3.

2 is the parent of 4 and 5.

3 is the parent of 6 and 7


print("checker")
Input
7
1 2 3 4 5 6 7
1 2
1 3
2 4
2 5
3 6
3 7
2
1
6
Expected output
4
0
Your Program Output
4
0
checker

"""
import math
# Number of people
n = int(input())
tokens = [] # For storing tokens
tree = [] # For storing adjacency list in tree, check https://youtu.be/09zltCNaRF8 for more
result = [] # For storing the results


#Slightly improved logic to check if a number is prime or not
def isPrime(number):
    if(number <= 1): return False
    if(number <= 3): return True

    if(number % 2 == 0 or number % 3 == 0):
        return False
    
    for i in range(5, math.ceil(math.sqrt(number)) + 1, 6):
        if(number % i == 0 or (number % (i + 2) == 0)):
            return False

    return True

# Depth first traversal as explained:https://youtu.be/pEwTw97BS2c?t=340
def depth_first_traversal(source):
    for child in tree[source]:
        #Go deep into the branch
        depth_first_traversal(child)
    #While coming up, bubble up the results from children to the parent
    for child in tree[source]:
        if(isPrime(tokens[child-1])):
            result[source] += 1
        result[source] += result[child]

#Get all the tokens
tokens = list(map(int, input().split()))
#Initialise tree and results
for i in range(n+1):
    tree.append([])
    result.append(0)
#Store the tree as adjacency list
for i in range(n-1):
    x,y = map(int, input().split())
    tree[x].append(y)
#Perform depth first traversal and build the results list,
#this operation only needs to run once
depth_first_traversal(1)
#Answer all the queries
q = int(input())
for _ in range(q):
    x = int(input())
    print(result[x])