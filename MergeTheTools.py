def merge_the_tools(string, k):
    # first get all substrings
    lista=[string[i:i+k] for i in range(0,len(string),k)]
    
    #check each one and copy only unique letters
    for a in range(len(lista)):
        done=[]
        s=""
        for i in range(len(lista[a])):
            if lista[a][i] not in done:
                s+=lista[a][i]
                done.append(lista[a][i])
        lista[a]=s
    print(*lista,sep="\n")    
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""HERE GOES THE PROBLEM DESCRIPTION!
Consider the following:
A string, S, of length N where S=c0c1...cn-1.
An integer, K, where K is a factor of N.
We can split S into N/K substrings where each subtring, Ti, consists of a contiguous block of K characters in S. Then, use each Ti to create string Ui such that:

*The characters in Ui are a subsequence of the characters in Ti.
*Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once. In other words, if the character at some index j 
  in Ti occurs at a previous index<j in Ti, then do not include the character in string Ui.

Given S and K, print N/K lines where each line i denotes string Ui.

Example
S="AAABCADDE"
K=3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. 
The first substring is all 'A' characters, so U1="A". 
The second substring has all distinct characters, so U2="BCA". 
The third substring has 2 different characters, so U3="DE". 
Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description
Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:
*string s: the string to analyze
*int k: the size of substrings to analyze

Prints
Print each subsequence on a new line. There will be N/K of them. No return value is expected.

Input Format

The first line contains a single string, S.
The second line contains an integer, K, the length of each substring.

Constraints
*1<=N<=10^4, where N is the length of S.
*1<=K<=N
*It is guaranteed that N is a multiple of K.

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output
AB
CA
AD"""
