class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums_dict = {}
        # 딕셔너리 세팅, 중복제거의 이유도 있다
        for num in nums:
            nums_dict[num] = True

        for num in nums_dict:
            if num-1 not in nums_dict:  # 시작점을 찾고, 괜한 반복문 안돌릴려고
                to_find = num+1
                count = 1
                while to_find in nums_dict: # 찾는값이 있으면 다음 값으로 업데이트 (계속 찾아감)
                    count += 1
                    to_find += 1
                answer = max(answer, count) # 결과 업데이트
        return answer