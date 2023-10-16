class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for cur_day, cur_temp in enumerate(temperatures):   # 날짜 계산위해 enumerate
            while stack and cur_temp > stack[-1][1]:
                prev_day, _ = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
            
        return answer