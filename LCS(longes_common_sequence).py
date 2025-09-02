def LCS(str1,str2):
    m=len(str1)
    n=len(str2)
    l=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]
str1=str(input("Enter first string:"))
str2=str(input("Enter second string:"))
print("Length of Longest Common Subsequence is:",LCS(str1,str2)) 

