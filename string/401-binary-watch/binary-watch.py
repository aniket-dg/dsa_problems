class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hour in range(12):
            hour_bits = bin(hour).count("1")
            print(hour_bits)
            for min in range(60):
                min_bits = bin(min).count("1")
                if hour_bits + min_bits == turnedOn:
                    res.append(f"{hour}:{str(min).zfill(2)}")
        return res