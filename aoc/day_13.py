"""Processing for Day 13"""

def point_of_incidence(patterns: str, smudges: bool) -> int:
    """Take the patterns and return the appropriate value"""

    summary = 0

    maxs = int(smudges)

    for pattern in patterns.strip().split("\n\n"):
        temp = 0

        for i in range(4):
            if i == 0:
                lines = pattern.splitlines()
            elif i == 2:
                lines = ["".join([line[c_idx] for line in lines]) for c_idx in range(len(lines[0]))]
            elif i in [1, 3]:
                lines = lines[::-1]

            l_idx = len(lines)
            while l_idx > 1 and temp == 0:
                l_idx -= 1
                num_smudges = sum((c1 != c2 for c1, c2 in zip(lines[l_idx], lines[0])))
                if num_smudges > maxs:
                    continue
                for m_idx in range(1, l_idx + 1):
                    if (num_smudges == maxs) and (m_idx > l_idx - m_idx) and (l_idx % 2):
                        temp = m_idx
                        break
                    if (num_smudges == maxs) and (lines[m_idx] != lines[l_idx-m_idx]):
                        break
                    if sum((c1 != c2 for c1, c2 in zip(lines[m_idx], lines[l_idx-m_idx]))) == maxs:
                        num_smudges = maxs

            if temp != 0:
                temp = (i % 2) * (len(lines) - temp) + (not i % 2) * temp
                summary += temp * 100**(i < 2)
                break

    return summary
