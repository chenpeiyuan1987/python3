# 判断字符串是否为数字

def isNumber(s) :
    try:
        float(s);
        return True;
    except ValueError :
        pass

    try :
        import unicodedata;
        unicodedata.numeric(s);
        return True;
    except (TypeError, ValueError) :
        pass
      
    return False;  

print(isNumber("foo"));  
print(isNumber("1"));  
print(isNumber("1.3"));  
print(isNumber("-1.37"));  
print(isNumber("1e3"));
