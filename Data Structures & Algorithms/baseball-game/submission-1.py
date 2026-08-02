class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+" and len(record) >= 2:
                a = record.pop()
                b = record.pop()
                record.append(b)
                record.append(a)
                record.append(a+b)
            elif op == "C":
                record.pop()
            elif op == "D":
                a = record.pop()
                record.append(a)
                record.append(2*a)
            else:
                record.append(int(op))
        return sum(record)
