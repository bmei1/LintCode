class Solution:
    """
    @param: s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        ips = []
        self.dfs(s, 0, ips, '')
        return ips
    
    def dfs(self, s, sub, ips, ip):
        if sub == 4:                # should be 4 parts
            if s == '':
                ips.append(ip[1:])  # remove first '.'
            return
        for i in range(1, 4):
            if i <= len(s):         # if i > len(s), s[:i] will make false!!!!
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                if s[0] == '0':
                    break