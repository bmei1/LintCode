class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if len(numbers) <= 1:
            return False
        temp = {} 
        for i in range(len(numbers)):
            if numbers[i] in temp:
                return [temp[numbers[i]], i+1]
            else:
                temp[target - numbers[i]] = i+1