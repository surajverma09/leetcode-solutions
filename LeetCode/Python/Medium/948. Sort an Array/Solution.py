class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr)<=1:
            return arr
        
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = self.sortArray(left)
        right = self.sortArray(right)
        return self.merge(left,right)

    def merge(self, left, right):
        i = 0
        j = 0
        arr2 = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr2.append(left[i])
                i += 1
            else:
                arr2.append(right[j])
                j += 1
        
        arr2.extend(left[i:])
        arr2.extend(right[j:])
        return arr2
