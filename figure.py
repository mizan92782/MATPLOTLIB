import matplotlib.pyplot as plt

def plot1():

    a = [5, 2, 3, 4]
    b = [3,6,7,19]
    c=[5,9,2,4,6,4]
    d=[9,2,4,13,3,2,85,99]



    '''figure use for crete multiple figure in a plot'''
    fig = plt.figure(figsize=(10,10))
    
    '''sub plots'''
    sub1=plt.subplot(2,2,1)
    sub2=plt.subplot(2,2,2)
    sub3=plt.subplot(2,2,3)
    sub4=plt.subplot(2,2,4)



    
    sub1.plot(a)
    sub1.plot(a, 'sb')
    
    # sets how the display subplot 
    # x axis values advances by 1
    # within the specified range
    sub1.set_xticks(list(range(0,10, 1)))
    sub1.set_title('1st Rep')






    sub2.plot(b)
    sub2.plot(b, 'or')
    
    # sets how the display subplot x axis
    # values advances by 2 within the
    # specified range
    sub2.set_xticks(list(range(0, 10, 1)))
    sub2.set_title('2nd Rep')
        






    # can directly pass a list in the plot
    # function instead adding the reference

    sub3.plot(c)
    sub3.plot(c, 'vg')
    sub3.set_xticks(list(range(0, 10, 1)))
    sub3.set_title('3rd Rep')
    






    sub4.plot(d, 'Dm')
    
    # similarly we can set the ticks for 
    # the y-axis range(start(inclusive),
    # end(exclusive), step)
    sub4.set_yticks(list(range(0, 10, 10)))
    sub4.set_title('4th Rep')




    
    plt.show()

    
  




def main():
    plot1()




__name__=='__main__'
main()
