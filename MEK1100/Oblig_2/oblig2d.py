from oblig2 import*

#divergence function
def div(F,G):
    return gradient(F,axis=1)+gradient(G,axis=0)
#Contour plot
verdier = linspace(-600,600,9)
contourf(x,y,div(u,v),verdier)
colorbar()
#Seperate flat
plot(xit,yit,'*',color='black')
#Rectangles
def rektangel(xi,yi,xj,yj):
    x1 = x[yi][xi]; x2 = x[yj][xj]
    y1 = y[yi][xi]; y2 = y[yj][xj]
    plot([x1,x2],[y1,y1], color='red')
    plot([x2,x1],[y2,y2], color='blue')
    plot([x1,x1],[y1,y2], color='black')
    plot([x2,x2],[y2,y1], color='green')
rektangel(34,159,69,169)
rektangel(34,84,69,99)
rektangel(34,49,69,59)  
#Giving name to the akses and sets a title
xlabel('X-akse')
ylabel('Y-akse')
title('Divergens')
savefig('div.png')
show()
