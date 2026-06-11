class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            leftVal = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, leftVal)

        return arr



        
            



        print(arr)

                

        