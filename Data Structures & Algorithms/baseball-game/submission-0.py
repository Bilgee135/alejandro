class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
                sum += record[-1]
            elif op == 'D':
                record.append(record[-1] * 2)
                sum += record[-1]
            elif op == 'C':
                sum -= record[-1]
                record.pop()
            else:
                record.append(int(op))
                sum += record[-1]

        return sum
