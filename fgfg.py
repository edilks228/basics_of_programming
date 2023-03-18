class Solution:
    def __init__(self, x: int) -> bool:
        r = 0
        while(x>0):
            fd = x % 10
            r = r * 10 + fd
            x = x // 10
        if r == x:
            print('true')
        else:
            print('false')


a = Solution(121)