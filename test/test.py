
class MyClass(object):
    """work"""
    def __init__(self, ans2):
        """work"""
        self.num = ans2
    def boajritjaitjtijerpte(self):
        """work"""
        for i in self.num:
            for j in i:
                if len(self.num) != 4 or not j.isdigit() or (i.isdigit() and int(i) > 255):
                    return print("Invalid IPv4 address")
        print(*[int(i) for i in self.num], sep=".")
    def ans2(self):
        """work"""
        self.num = self.num


def main():
    ans2 = input().split(".")
    ans = MyClass(ans2)
    ans.boajritjaitjtijerpte()
main()
