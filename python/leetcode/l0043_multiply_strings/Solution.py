class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        products = 0
        for p1 in range(len(num1) - 1, -1, -1):
            n1 = int(num1[p1])
            register = 0
            running_product = 0
            place = 10 ** (len(num1) - p1 - 1)
            for p2 in range(len(num2) - 1, -1, -1):
                n2 = int(num2[p2])
                product = n1 * n2 + register
                register = 0

                if product >= 10:
                    tens_place = (product // 10) * 10
                    register = tens_place // 10
                    product -= tens_place

                running_product += product * place 
                place *= 10

            if register != 0:
                running_product += register * place
                register = 0

            products += running_product

        return str(products)




print(Solution().multiply("21", "98"))



