class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1

        while(i <= len(numbers)-1):

            diff = target - numbers[i]

            if diff < numbers[j] :
                j -= 1
            
            if diff > numbers[j] : 
                i += 1
                j = len(numbers) - 1

            if diff == numbers[j] :
                return [i+1 , j+1]
        

           
