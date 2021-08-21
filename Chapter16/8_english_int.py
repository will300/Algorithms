num2word = {"1": ("One", ), "2": ("Two", "Twenty"), "3": ("Three", "Thirty"), 
            "4": ("Four", "Forty"), "5": ("Five", "Fifty"), "6": ("Six", "Sixty"), 
            "7": ("Seven", "Seventy"), "8": ("Eight", "Eighty"), "9": ("Nine", "Ninety"),
            "10": ("Ten", ), "11": ("Eleven", ), "12": ("Twelve", ), "13": ("Thirteen", ),
            "14": ("Fourteen", ), "15": ("Fifteen", ), "16": ("Sixteen", ), 
            "17": ("Seventeen", ), "18": ("Eighteen", ), "19": ("Nineteen", )} 

order2word = {2: "Hundred", 3: "Thousand", 6: "Million", 9: "Billion"} 

def covert_to_english(num):
    num = str(num)
    order = len(str(num))
    output = ""
    for char in num:
        order -= 1
        if order == 0:
            output += num2word[char][0]
        elif order == 1:
            if int(char) > 1:
                output += num2word[char][1]
            else:
                
        if char != "0":
            output += num2word[char][0] + " "
            output += order2word[order]
    return output


def test_case(num, solution, test_func):

    output = test_func(num)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(300, "Three Hundred", covert_to_english)
