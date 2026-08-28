class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd:
                return ""
            mid_char = ""
        else:
            if len(odd) != 1:
                return ""
            mid_char = chr(odd[0] + 97)

        p = [c // 2 for c in cnt]
        h = n // 2

        # states[k] = remaining pair-counts after matching target[0:k] exactly
        states = [p[:]]
        for k in range(h):
            idx = ord(target[k]) - 97
            cur = states[-1]
            if cur[idx] > 0:
                nxt = cur[:]
                nxt[idx] -= 1
                states.append(nxt)
            else:
                break
        K = len(states) - 1  # longest feasible exact-match prefix

        # Case: entire first half can exactly match target -> check the (later) forced tail
        if K == h:
            half = target[:h]
            if n % 2 == 1:
                m = target[h]
                if mid_char > m:
                    return half + mid_char + half[::-1]
                elif mid_char == m:
                    rev = half[::-1]
                    suffix = target[h + 1:]
                    if rev > suffix:
                        return half + mid_char + rev
            else:
                rev = half[::-1]
                suffix = target[h:]
                if rev > suffix:
                    return half + rev

        # General pivot search in the free half, rightmost first
        start = min(K, h - 1)
        for i in range(start, -1, -1):
            cur = states[i]
            ti = ord(target[i]) - 97
            chosen = -1
            for idx in range(ti + 1, 26):
                if cur[idx] > 0:
                    chosen = idx
                    break
            if chosen != -1:
                rem = cur[:]
                rem[chosen] -= 1
                left = list(target[:i])
                left.append(chr(chosen + 97))
                for idx in range(26):
                    if rem[idx]:
                        left.append(chr(idx + 97) * rem[idx])
                L = "".join(left)
                if n % 2 == 1:
                    return L + mid_char + L[::-1]
                else:
                    return L + L[::-1]

        return ""