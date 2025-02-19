from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        par = [i for i, _ in enumerate(accounts)]
        rank = [1] * len(accounts)

        def find(n1):
            cur = n1
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur

        def union(n1, n2):
            par1, par2 = find(n1), find(n2)

            if par1 == par2:
                return False

            if rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par2] = par1
                rank[par1] += rank[par2]

            return True

        email2acc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email2acc:
                    union(i, email2acc[email])
                else:
                    email2acc[email] = i

        email_groups = defaultdict(list)

        for email, acc_id in email2acc.items():
            leader = find(acc_id)
            email_groups[leader].append(email)

        result = []
        for i, emails in email_groups.items():
            name = accounts[i][0]
            result.append([name] + sorted(emails))

        return result
