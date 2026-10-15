class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
                total += record[-1]
            elif op == 'D':
                record.append(record[-1] * 2)
                total += record[-1]
            elif op == 'C':
                total -= record[-1]
                record.pop()
            else:
                record.append(int(op))
                total += record[-1]

        return total
