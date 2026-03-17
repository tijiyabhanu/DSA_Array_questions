class Solution:
    def isValid(self, s: str) -> bool:
    
        st=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                else:
                    ch = st[-1]
                    st.pop()
                    if (i==')' and ch=='(') or (i==']' and ch=='[') or (i=='}' and ch == '{'):
                        continue
                    else:
                        return False

        if len(st)==0:
            return True
        else:
            return False
