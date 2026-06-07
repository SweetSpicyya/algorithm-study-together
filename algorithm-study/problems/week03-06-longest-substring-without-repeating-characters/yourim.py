class Solution:
    def lengthOfLongestSubstring_nav(self, s: str) -> int:
        result = {}
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                print(sub, j)
                if s[j] in sub:
                    result[sub] = len(sub)
                    break
                sub = sub + s[j]

        print(result)

        return max(i for i in result.values())

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 문자의 마지막 위치를 저장할 딕셔너리
        char_map = {}
        max_length = 0
        start = 0  # 윈도우의 시작 지점

        for end in range(len(s)):
            # 만약 현재 문자가 이미 윈도우 안에 있다면, start 지점을 옮김
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1

            # 현재 문자의 위치를 갱신
            char_map[s[end]] = end

            # 현재 윈도우의 길이(end - start + 1)와 최댓값 비교
            max_length = max(max_length, end - start + 1)

        return max_length



sol = Solution()
s = "pwwkew"

a = sol.lengthOfLongestSubstring(s)
print(a)