class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        tmp = sum(1 for idx, charr in enumerate(s) if (idx % 2 == 0) == (charr == '0'))
        res = min(tmp, n - tmp)
        if n % 2 == 1:
            for charr in s:
                if charr == '0':
                    tmp = n+1-tmp
                else:
                    tmp = n-1-tmp
                res = min(res, tmp, n-tmp)

        return res
