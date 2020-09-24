import numpy as np
import matplotlib.pyplot as plt

def main():
    # create the lists of cosine and sine to plot. Since range accepts only integers, I made the list go 0 to 80 and then
    # divide by 10 when computing the sine/cosine. This allows me to get more points on the graph for a smoother plot.
    cos_lst = [np.cos(x/10) for x in range(0, 80)]
    sin_lst = [np.sin(x/10) for x in range(0, 80)]
    tan_lst = [np.tan(x/10) for x in range(0, 80)]

    # create the x-list to plot with each list of y's
    x_lst = [x/10 for x in range(0, 80)]

    plt.plot(x_lst, cos_lst)
    plt.plot(x_lst, sin_lst)
    plt.plot(x_lst, tan_lst)

    # Since the range of x values goes from 0-7, I set the x limit to 2*pi as per the requirements of the assignment
    plt.xlim(0, np.pi*2)

    # Adding labels to the graph per suggestion from team member Lucas Fan
    plt.title("Trig Functions Graph")
    plt.legend(['Sin', 'Cos', 'Tan'])
    # Also adding y-lim like I did in my addition of Lucas' code
    plt.ylim(-4,4)

    plt.show()
    #Great code. I would just put it all in a main function. 
if __name__ == '__main__':
    main() 
    

