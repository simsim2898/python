h, m = map(int, input().split())
tt = h * 60 + m - 45  
if tt < 0:  
    tt += 24 * 60
ah = tt // 60 
am = tt % 60  
print(ah, am)