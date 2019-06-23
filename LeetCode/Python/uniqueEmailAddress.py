class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            temp = email.split('@')
            local = temp[0]
            domain = temp[1]
            plusIdx = local.find('+')
            if plusIdx != -1:
                local = local[:plusIdx]
            local = local.replace(".", "")
            unique.add(local + "@" + domain)

        return len(unique)
