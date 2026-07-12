class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for i in range(1, 4):
                if start + i > len(s):
                    break

                part = s[start:start + i]

                # Skip numbers with leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                # Skip numbers greater than 255
                if int(part) > 255:
                    continue

                backtrack(start + i, path + [part])

        backtrack(0, [])
        return result