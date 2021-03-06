# -*- coding: cp949 -*-
import cv2
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import ImageGrab
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors.nearest_centroid import NearestCentroid
import scipy.integrate as integrate
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def d3plot(arr1, arr2, arr3):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax = fig.gca(projection = '3d')
    ax.title.set_text('integral result')
    my_data = genfromtxt('twrite\presult1.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    t1_line = np.full((len(result), 1), 1)
    t1_line = np.concatenate((t1_line, result[:, np.newaxis, 3]), axis = 1)
    t1_lineFor = t1_line
    nppie = np.arange(1, 6, 0.05)
    for i in nppie:
        print (i)
        integ = integrate.quad(lambda x: np.tan(x), 0, i/np.pi)
        nptempp = (t1_lineFor * integ[0])
        nptempp[:, 0] = i
        print (nptempp)
        t1_line = np.concatenate((t1_line, nptempp), axis = 0)
    t1_line = np.concatenate((t1_line, arr1[:, np.newaxis, 1]), axis = 1)
    ax.scatter(t1_line[:,1], t1_line[:, 2], t1_line[:, 0], 'r', label = 'speci')
    #ax.plot_surface(t1_line[:,2], t1_line[:, 1], t1_line[:, 0], rstride=8, cstride=8, alpha=0.3, label = 'test')
    #cset = ax.contour(t1_line[:,0], t1_line[:, 1], (t1_line[:, 1], t1_line[:, 0]), zdir='z', offset=-80000, cmap=cm.coolwarm)
    #cset = ax.contour(t1_line[:,2], t1_line[:, 0], t1_line[:, 1], zdir='x', offset=-40, cmap=cm.coolwarm)
    #cset = ax.contour(t1_line[:,2], t1_line[:, 0], t1_line[:, 1], zdir='y', offset=40, cmap=cm.coolwarm)
    ax.legend()
    ax.set_xlabel('int(0 ^ x)tan(dx/pi)')
    ax.set_ylabel('lim[x](tan(x)/pi)')
    ax.set_zlabel('arnge_x')
    print (arr1[1485])
    print (t1_line[1485])
    plt.show()

def cvsreader():
    fig = plt.figure(1)
    splot = fig.add_subplot(221)
    splot.title.set_text('linearReg_sep')
    my_data = genfromtxt('C:\data\ppcvs.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    aline = np.full((len(result), 1), 1, dtype = np.float64)
    aline = np.concatenate((aline, result[:, np.newaxis, 0]), axis = 1)
    bline = np.full((len(result), 1), 2, dtype = np.float64)
    bline = np.concatenate((bline, result[:, np.newaxis, 1]), axis = 1)
    cline = np.full((len(result), 1), 3, dtype = np.float64)
    cline = np.concatenate((cline, result[:, np.newaxis, 2]), axis = 1)
    dline = np.full((len(result), 1), 4, dtype = np.float64)
    dline = np.concatenate((dline, result[:, np.newaxis, 3]), axis = 1)
    total = np.concatenate((aline, bline, cline, dline), axis = 0)
    sa = splot.scatter(aline[:, 0],aline[:, 1],30,'b','o')
    sb = splot.scatter(bline[:, 0],bline[:, 1],30,'r','o')
    sc = splot.scatter(cline[:, 0],cline[:, 1],30,'y','o')
    sd = splot.scatter(dline[:, 0],dline[:, 1],30,'g','o')
    splot.set_xlabel('grade')
    splot.set_ylabel('credit')
    splot.legend((sa, sb, sc, sd), ('1st', '2nd', '3rd', '4th'), scatterpoints = 1, fontsize =10)
    reg = linear_model.LinearRegression()
    reg.fit(total[:, np.newaxis, 0], total[:, np.newaxis, 1])
    prex = np.arange(1, 5)
    a = prex[:, np.newaxis]
    prey = reg.predict(a)
    splot.plot(a, prey, color = 'blue', linewidth = 3)
    splot.text(a[0], prey[0] + 7.8, 'coef %s' %reg.coef_, fontsize = 11)
    splot.text(a[0], prey[0] + 9.5, 'intercept  %s' %reg.intercept_, fontsize = 11)
    ay = fig.add_subplot(222)
    ay.title.set_text('Credit_total')
    my_data = genfromtxt('C:\data\ppresult.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    ayline = np.full((len(result), 1), 1, dtype = np.float64)
    ayline = np.concatenate((ayline, result[:, np.newaxis, 0]), axis = 1)
    byline = np.full((len(result), 1), 2, dtype = np.float64)
    byline = np.concatenate((byline, result[:, np.newaxis, 1]), axis = 1)
    cyline = np.full((len(result), 1), 3, dtype = np.float64)
    cyline = np.concatenate((cyline, result[:, np.newaxis, 2]), axis = 1)
    dyline = np.full((len(result), 1), 4, dtype = np.float64)
    dyline = np.concatenate((dyline, result[:, np.newaxis, 3]), axis = 1)
    aytotal = np.concatenate((ayline, byline, cyline, dyline), axis = 0)
    aya = ay.scatter(ayline[:, 0],ayline[:, 1],30,'b','o')
    ayb = ay.scatter(byline[:, 0],byline[:, 1],30,'r','o')
    ayc = ay.scatter(cyline[:, 0],cyline[:, 1],30,'y','o')
    ayd = ay.scatter(dyline[:, 0],dyline[:, 1],30,'g','o')
    ay.legend((aya, ayb, ayc, ayd), ('1st', '2nd', '3rd', '4th'), scatterpoints = 1, fontsize =10)
    az = fig.add_subplot(212)
    az.title.set_text('SVM_plot(4th grade_nonlim)')
    az.set_xlim([1, 5])
    #az.set_ylim([0, 2000])
    my_data = genfromtxt('C:\data\presult1.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    t1_line = np.full((len(result), 1), 1)
    t1_line = np.concatenate((t1_line, result[:, np.newaxis, 3]), axis = 1)
    t1_lineFor = t1_line
    nppie = np.arange(0, 5, 0.05)
    for i in nppie:
        print (i)
        nptempp = (t1_lineFor * (np.tan(i/np.pi)))
        nptempp[:, 0] = i
        print (nptempp)
        t1_line = np.concatenate((t1_line, nptempp), axis = 0)
    my_data = genfromtxt('C:\data\presult2.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    t2_line = np.full((len(result), 1), 1)
    t2_line = np.concatenate((t2_line, result[:, np.newaxis, 3]), axis = 1)
    t2_lineFor = t2_line
    nppie = np.arange(0, 5, 0.05)
    for i in nppie:
        print (i)
        nptempp = (t2_lineFor * (np.tan(i/np.pi)))
        nptempp[:, 0] = i
        print (nptempp)
        t2_line = np.concatenate((t2_line, nptempp), axis = 0)
    my_data = genfromtxt('C:\data\presult3.csv', delimiter = ',')
    result = my_data[1:len(my_data)]
    t3_line = np.full((len(result), 1), 1)
    t3_line = np.concatenate((t3_line, result[:, np.newaxis, 3]), axis = 1)
    t3_lineFor = t3_line
    nppie = np.arange(0, 5, 0.05)
    for i in nppie:
        print (i)
        nptempp = (t3_lineFor * (np.tan(i/np.pi)))
        nptempp[:, 0] = i
        print (nptempp)
        t3_line = np.concatenate((t3_line, nptempp), axis = 0)
    '''
    for i in range(2, 5):
        nptemp = np.full((len(result), 1), i, dtype = np.float64)
        t1_line = np.concatenate((t1_line, nptemp), axis = 0)
    result = result.reshape((len(result)) * 4, 1)
    t1_line = np.concatenate((t1_line, result), axis = 1)
    '''
    
    linefive = np.arange(0, 6, 1)
    fifty = np.full((6, 1), 57, dtype = np.float64)
    linefive = linefive.reshape(6, 1)
    linefive = np.concatenate((linefive, fifty), axis = 1)
    print (linefive)
    print (t1_line[:, 1])
    az.set_xlabel('arnge_x')
    az.set_ylabel('lim[x](tan(x)/π)')
    aza = az.scatter(t1_line[:, 0], t1_line[:, 1], 5, 'r', 'o')
    azb = az.scatter(t2_line[:, 0], t2_line[:, 1], 5, 'b', 'o')
    azc = az.scatter(t3_line[:, 0], t3_line[:, 1], 5, 'y', 'o')
    az.plot(linefive[:, 0], linefive[:, 1], color = 'blue', linewidth = 3)
    linefive = np.arange(0, 6, 1)
    fifty = np.full((6, 1), 96, dtype = np.float64)
    linefive = linefive.reshape(6, 1)
    linefive = np.concatenate((linefive, fifty), axis = 1)
    az.plot(linefive[:, 0], linefive[:, 1], color = 'pink', linewidth = 3)
    az.legend((aza, azb, azc), ('speci', 'arch', 'nonarch'), scatterpoints = 1, fontsize =10)
    print (reg.coef_)
    print (reg.intercept_)
    plt.show(block=False)
    plt.savefig('C:\data\poo.png')
    print ('complete')

    
