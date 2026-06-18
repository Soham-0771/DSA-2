class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        prev = 1

        for k in range(1, rowIndex + 1):
            prev = prev * (rowIndex - k + 1) // k
            row.append(prev)

        return row