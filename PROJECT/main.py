


class math :
    def __init__(self, number):
        self.number= number

    def armstrong(self,number):
        temp=self.number
        result=0
        while(temp!=0):
            rem = temp% 10
            result +=rem**3
            temp//=10
        if self.number ==result :
            print(self.number," is armstrong number")
        else :
            print(self.number," is not armstrong number")

number=156
check=math(number)

check.armstrong(number)


