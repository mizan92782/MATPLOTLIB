import matplotlib.pyplot as plt

def plot1():

    a = [5, 2, 3, 4, 5]
    b = [10, 0.6, 0.2, 15, 10, 8, 16, 21]
    c = [0,0.2, 4, 7, 9, 18, 20]


    '''drawing  plots individually  ,y axis'''
    plt.plot(a)
    plt.plot(b)
    plt.plot(c)
    plt.plot(list(range(1,20,2)))




    '''
      drawing red dor in y points
      # o is for circles and r is
        g ->green 
      # r->red


      shape:
      Here are some commonly used marker styles:

'o': Circles (default)
's': Squares
'D': Diamonds
'+': Plus signs
'x': X marks
'*': Asterisks
'.': Dots

    
    '''
    
    plt.plot(b, "or")
    plt.plot(a, "sg")
    plt.plot(c, label = '4th Rep')



    '''use for works with current plot,ax is the obj of current plot'''
    ax = plt.gca()
  
    '''set either will show plot boundary at different side'''
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # set the data show apart from left boundary
    ax.spines['left'].set_bounds(-3, 40)


    """ set the x axis interval or length"""
    plt.xticks(list(range(-3, 10)))
    plt.yticks(list(range(-10, 20, 3)))

    # legend denotes that what color 
    # signifies what
    ax.legend(['a', 'b', 'c',"list"])


    # annotate command helps to write
    # ON THE GRAPH any text xy denotes 
    # the position on the graph
    plt.annotate('plot/  four', xy = (1.01, -5.15))
    
   
    
    plt.show()

    
  




def main():
    plot1()




__name__=='__main__'
main()
