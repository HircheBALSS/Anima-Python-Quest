def solution(n):
    # TODO convert int to roman string
    
 roman_num = ""
        
 moman_let = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV":4, "I":1}

 for i in roman_let:
        while n >= roman_let[i]:
            roman_num += i
            n -= roman_let[i]
 return roman_num