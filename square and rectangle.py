print('khurram khalil')
print('enter the function of square and rectangle which you want to create')
def shape(x):
    if x=='square':
        b=int(input('enter the length of the square: '))
        if b>7:
            print (". "*b)
            for _ in range(b-2):
                print (". " + "  " * (b - 2) + ".")
                def shape(rectangle):
                print (". "*b)

            
                
        else:
            print('your desired square is so small in length')
    elif x=='rectangle' or x==upper() or x==lower() or x==title():
        length= int(input('enter the length of the square: '))
        width= int(input('enter the width of the square: '))
        if (width>=length+6) and (length>=7) and (width>=9):
            print('YOUR RECTANGLE IS DRAWN BELOW')
            for i in range(0,length):
                i='* '*width
                print(i)
    else:
        print('enter the shape name which you want to draw from SQUARE OR RECTANGLE in ALPHABETS')
                
    
