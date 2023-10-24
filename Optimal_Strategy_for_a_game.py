# Python3 code to implement the approach 

def optimalStrategyOfGame(arr, n): 
	memo = {} 

	# recursive top down memoized solution 
	def solve(i, j): 
		if i > j or i >= n or j < 0: 
			return 0

		k = (i, j) 
		if k in memo: 
			return memo[k] 

		# if the user chooses ith coin, the opponent can choose from i+1th or jth coin. 
		# if he chooses i+1th coin, user is left with [i+2,j] range. 
		# if opp chooses jth coin, then user is left with [i+1,j-1] range to choose from. 
		# Also opponent tries to choose 
		# in such a way that the user has minimum value left. 
		option1 = arr[i] + min(solve(i+2, j), solve(i+1, j-1)) 

		# if user chooses jth coin, opponent can choose ith coin or j-1th coin. 
		# if opp chooses ith coin,user can choose in range [i+1,j-1]. 
		# if opp chooses j-1th coin, user can choose in range [i,j-2]. 
		option2 = arr[j] + min(solve(i+1, j-1), solve(i, j-2)) 

		# since the user wants to get maximum money 
		memo[k] = max(option1, option2) 
		return memo[k] 

	return solve(0, n-1) 

	
# Driver Code 
arr1 = [8, 15, 3, 7] 
n = len(arr1) 
print(optimalStrategyOfGame(arr1, n)) 

arr2 = [2, 2, 2, 2] 
n = len(arr2) 
print(optimalStrategyOfGame(arr2, n)) 

arr3 = [20, 30, 2, 2, 2, 10] 
n = len(arr3) 
print(optimalStrategyOfGame(arr3, n)) 
