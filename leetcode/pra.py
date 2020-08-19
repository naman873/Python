class Solution:
    def addBinary(self, a, b):
        remainder = 0

        alen = len(a)
        blen = len(b)
        totalsum = ""

        if alen > blen:
            maxlen = alen
        else:
            maxlen = blen

        for i in range(maxlen):

            if a[i] != " " and b[i] != " ":
                if remainder == 0:
                    if (a[i] == "1") and (b[i] == "1"):
                        totalsum = totalsum + "0"
                        remainder = 1

                    elif (a[i] == "1") or (b[i] == "1"):
                        totalsum = totalsum + "1"

                    else:
                        totalsum = totalsum + "0"

                else:
                    if (a[i] == "1") and (b[i] == "1"):
                        totalsum = totalsum + "1"
                        remainder = 1

                    elif (a[i] == "1") or (b[i] == "1"):
                        totalsum = totalsum + "0"
                        remainder = 1

                    else:
                        totalsum = totalsum + "1"
                        remainder = 0


            elif a[i] != " " and b[i] == " ":
                if remainder == 0:
                    totalsum = totalsum + a[i]

                else:
                    if a[i] == "1":
                        totalsum = totalsum + "0"
                        remainder = 1

                    else:
                        totalsum = totalsum + "1"
                        remainder = 0



            elif b[i] != " " and a[i] == " ":
                if remainder == 0:
                    totalsum = totalsum + b[i]

                else:
                    if b[i] == "1":
                        totalsum = totalsum + "0"
                        remainder = 1

                    else:
                        totalsum = totalsum + "1"
                        remainder = 0

            if i == maxlen - 1:
                if remainder == 1:
                    totalsum = "1" + totalsum

        return totalsum, remainder


a=Solution()

a.addBinary("101","111")
