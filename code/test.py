

import matplotlib.pyplot as plt
import numpy as np

def main():

    from Tkinter import Tk
    from tkFileDialog import askopenfilename
    
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)

    epoch = 2
    costs = [1,2,3]
    Ws = [3,4,5]
    vbiases = [5,6,7]
    hbiases = [7,8,9]

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(221)
    ax2 = fig1.add_subplot(222)
    ax3 = fig1.add_subplot(223)
    ax4 = fig1.add_subplot(224)
    
    while(True):  
        #fig1.clear()
        np.add(costs,[1,1,1])
        np.add(Ws, [1,1,1])
        np.add(vbiases,[1,1,1])
        np.add(hbiases,[1,1,1])
        ax1.plot(range(epoch+1), costs)
        ax1.set_title('costs')
        ax2.plot(range(epoch+1), Ws)
        ax2.set_title('W')
        ax3.plot(range(epoch+1), vbiases)
        ax3.set_title('vb')
        ax4.plot(range(epoch+1), hbiases)
        ax4.set_title('hb')
        #plt.draw()
        plt.show(block=False)

if (False):
    fig = PLT.figure()
    
    ax1 = fig.add_subplot(211)
    ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])
    
    ax2 = fig.add_subplot(212)
    ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])
    
    PLT.show()


if (False):                     
    x = [1,2,3]
    y = [4,5,6]        
    f, axarr = plt.subplots(2, 2)
    axarr[0, 0].plot(x, y)
    axarr[0, 0].set_title('Axis [0,0]')
    axarr[0, 1].scatter(x, y)
    axarr[0, 1].set_title('Axis [0,1]')
    axarr[1, 0].plot(x, y)
    axarr[1, 0].set_title('Axis [1,0]')
    axarr[1, 1].scatter(x, y)
    axarr[1, 1].set_title('Axis [1,1]')
    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
    plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
    plt.show()

                         
main()