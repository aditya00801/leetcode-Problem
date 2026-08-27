class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();
        vector<int> cnt(26, 0);

        for (char c : s)
            cnt[c - 'a']++;

        // We try to make the answer equal to target
        // for as long as possible.
        for (int i = 0; i < n; i++) {
            int x = target[i] - 'a';

            // If we can use target[i], use it.
            if (cnt[x] > 0) {
                cnt[x]--;
            } 
            else {
                // We cannot make the prefix equal anymore.
                // Try a character greater than target[i].
                for (int c = x + 1; c < 26; c++) {
                    if (cnt[c] > 0) {
                        string ans = target.substr(0, i);
                        ans += char('a' + c);
                        cnt[c]--;

                        // Fill the rest with smallest characters.
                        for (int k = 0; k < 26; k++) {
                            ans.append(cnt[k], char('a' + k));
                        }

                        return ans;
                    }
                }

                // No character greater at this position.
                // We need to backtrack.
                break;
            }
        }

        // Rebuild counts and perform proper backtracking.
        fill(cnt.begin(), cnt.end(), 0);
        for (char c : s)
            cnt[c - 'a']++;

        // Match target prefix while possible.
        int i = 0;
        while (i < n && cnt[target[i] - 'a'] > 0) {
            cnt[target[i] - 'a']--;
            i++;
        }

        // Try changing a previous position.
        for (int j = i - 1; j >= 0; j--) {
            // Restore target[j]
            cnt[target[j] - 'a']++;

            int x = target[j] - 'a';

            // Find smallest character > target[j]
            for (int c = x + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string ans = target.substr(0, j);
                    ans += char('a' + c);
                    cnt[c]--;

                    // Smallest possible suffix
                    for (int k = 0; k < 26; k++) {
                        ans.append(cnt[k], char('a' + k));
                    }

                    return ans;
                }
            }
        }

        return "";
    }
};