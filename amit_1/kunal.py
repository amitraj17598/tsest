


first = input ( " enter first number : " )
operator = input ( " enter operetor ( + , - , * , / , % ) : " )
second = input ( " enter second number : " )

first = int ( first )
second = int ( second )

print(f"operator: {operator}")


if operator ==  '+' :
    print ( first + second )
elif operator == '-' :
     print ( first - second ) 
elif operator == '*' :
     print ( first * second )
elif operator == '/'  :
     print ( first / second )
elif operator == '%' :
     print ( first % second )
else:
    print ( " invalid opretion " )

