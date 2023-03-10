#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        weight = [0] * N
        for i in range(N):
            if Edge[i] != -1:
                weight[Edge[i]] += i
        max_weight = max(weight)
        for i in range(N-1, -1, -1):
            if weight[i] == max_weight:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends
