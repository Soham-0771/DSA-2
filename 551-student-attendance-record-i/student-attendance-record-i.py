class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for ch in s:
            if ch == 'A':
                absent += 1
                late = 0
                if absent >= 2:
                    return False
            elif ch == 'L':
                late += 1
                if late >= 3:
                    return False
            else:  # 'P'
                late = 0

        return True