class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda y: (abs(y-x),x))
        return sorted((arr[0:k]))
        