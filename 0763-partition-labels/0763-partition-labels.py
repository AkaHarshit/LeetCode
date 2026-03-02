class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        lst=[]
        st=0
        ed=0
        for i in range(len(s)):
            ed=max(ed, d[s[i]])
            if i==ed:
                lst.append(ed-st+1)
                st=i+1
        return lst