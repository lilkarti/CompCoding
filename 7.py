class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = 0
        a = 0
        if (x>0):
            while(x != 0):
                print("This is x!",x)
                a = x%10
                temp = temp*10+a
                print(temp)
                x = x/10
            if(temp<(-2)**31):
                return 0
            else:
                return temp
        elif(x<0):
            x = x*(-1) 
            while(x != 0):
                print("This is x!",x)
                a = x%10
                temp = temp*10+a
                print(temp)
                x = x/10
            temp = temp*(-1)
            if (x>2**31):
                return 0
            else:
                return temp
        elif(x==0):
            return 0
