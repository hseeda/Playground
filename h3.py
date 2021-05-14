import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Layer:
    def __init__(self, name ,top ,bot=-9999 , thickness = -9999 ):
        self.name = name
        self.top = float(top)
        if bot != -9999:
            self.bot =  float(bot)
        elif thickness != -9999:
            self.bot = self.top - thickness
        self.thickness = float(self.top - self.bot)

        self.gamma_top = 0.0
        self.gamma_bot = 0.0
        self.gamma_inc = 0.0

        self.C_top = 0.0
        self.C_bot = 0.0
        self.C_inc = 0.0

        self.Fi_top = 0.0
        self.Fi_bot = 0.0
        self.Fi_inc = 0.0

    # ---------------------------------------------------
    def a_d(self,d,vt,vb):
        if d > self.top:
            return float(vt)
        elif d < self.bot:
            return float(vb)
        else:
            return vt + (vb-vt) / self.thickness * (self.top-d)
    # ---------------------------------------------------
    def a_h(self,h,vt,vb):
        if h < 0:
            return float(vt)
        elif h > self.thickness:
            return float(vb)
        else:
            return vt + (vb-vt) / self.thickness * h
    # ---------------------------------------------------
    def set_gamma(self, gamma1, gamma2 = -9999, inc = -9999):
        self.gamma_top = gamma1
        if gamma2 == -9999:
            self.gamma_bot = gamma1
            self.gamma_inc = 0.0
        else:
            self.gamma_bot = gamma2
            self.gamma_inc = (self.gamma_bot - self.gamma_top)/self.thickness
        if inc != -9999:
            self.gamma_bot = self.gamma_top + inc * self.thickness
            self.gamma_inc = inc
    # ---------------------------------------------------
    def gamma(self,d=-9999,h=-9999):
        if h == -9999:
            if d == -9999:
                return self.gamma_top
            else:
                return self.a_d(d,self.gamma_top,self.gamma_bot)
        else:
            return self.a_h(h,self.gamma_top,self.gamma_bot)
    # ---------------------------------------------------
    def set_C(self, C1, C2 = -9999, inc = -9999):
        self.C_top = C1
        if C2 == -9999:
            self.C_bot = C1
            self.C_inc = 0.0
        else:
            self.C_bot = C2
            self.C_inc = (self.C_bot - self.C_top)/self.thickness
        if inc != -9999:
            self.C_bot = self.C_top + inc * self.thickness
            self.C_inc = inc
    # ---------------------------------------------------
    def C(self,d=-9999,h=-9999):
        if h == -9999:
            if d == -9999:
                return self.C_top
            else:
                return self.a_d(d,self.C_top,self.C_bot)
        else:
            return self.a_h(h,self.C_top,self.C_bot)
    # ---------------------------------------------------
    def set_Fi(self, Fi1, Fi2 = -9999, inc = -9999):
        self.Fi_top = Fi1
        if Fi2 == -9999:
            self.Fi_bot = Fi1
            self.Fi_inc = 0.0
        else:
            self.Fi_bot = Fi2
            self.Fi_inc = (self.Fi_bot - self.Fi_top)/self.thickness
        if inc != -9999:
            self.Fi_bot = self.Fi_top + inc * self.thickness
            self.Fi_inc = inc
    # ---------------------------------------------------
    def Fi(self,d=-9999,h=-9999):
        if h == -9999:
            if d == -9999:
                return self.Fi_top
            else:
                return self.a_d(d,self.Fi_top,self.Fi_bot)
        else:
            return self.a_h(h,self.Fi_top,self.Fi_bot)
    # ---------------------------------------------------
    def after(self,cname, c_thickness):
        return Layer(cname, self.bot, self.bot - c_thickness)
    # ---------------------------------------------------
    def shift(self,distance):
        self.top += distance
        self.bot += distance
        return
    # ---------------------------------------------------
    def print(self):
        gs="\u03B3sat: {:.1f},{:.1f},{:.1f}".format(self.gamma_top,self.gamma_bot,self.gamma_inc)
        sus = "Su: {:.1f},{:.1f},{:.1f}".format(self.C_top,self.C_bot,self.C_inc)
        fs="\u03C6: {:.1f},{:.1f},{:.1f}".format(self.Fi_top,self.Fi_bot,self.Fi_inc)

        # print("top: {:.1f} \tbot: {:.1f}\tthickness: {:.1f}\t\t\u03B3sat: {:.1f},{:.1f},{:.1f}\tSu: {:.1f},{:.1f},{:.1f}\t\u03C6: {:.1f},{:.1f},{:.1f}"
        # .format(self.top,self.bot,self.thickness,
        # self.gamma_top,self.gamma_bot,self.gamma_inc,
        # self.C_top,self.C_bot,self.C_inc,
        # self.Fi_top,self.Fi_bot,self.Fi_inc))
        print("{}\ttop: {:.1f} \tbot: {:.1f}\tthickness: {:.1f}\t\t{}{}{}"
        .format(self.name.ljust(12), self.top,self.bot,self.thickness,
        gs.ljust(24),
        sus.ljust(24),
        fs.ljust(24)))

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Profile:
    def __init__(self, name="default"):
        self.name = name
        self.top = 0.0
        self.bot =  0.0
        self.gwt = 0.0
        self.layers = {}
        self.layers_count=0

        self.depth = []
        self.p = []
        self.p_ = []
        self.g  = []
        self.C  = []
        self.Fi = []
# ----------------------------------------------------------------
    def setTop(self,v):
        h = self.top - self.bot
        self.top = v
        self.bot = self.top - h
# ----------------------------------------------------------------
    def addLayer(self, lname, lthickness):
        self.layers_count += 1
        l=Layer(lname, self.bot,thickness=lthickness)
        self.current_layer = l

        self.layers[self.layers_count] = l
        self.bot = l.bot
# ----------------------------------------------------------------
    def print(self):
        for n,l in self.layers.items():
            print("{}".format(str(n).ljust(3)),end="")
            l.print()
# ----------------------------------------------------------------
    def getLayer(self,depth):
        for l in self.layers.values():
            if depth >= l.bot and depth <= l.top:
                return l
# ----------------------------------------------------------------
    def setDepth(self, inc):
        d=self.top
        flag = True
        while flag:
            self.depth.append(d)
            d=d+inc
            if d < self.bot or d > self.top:
                flag=False
        return
# ----------------------------------------------------------------
    def setP0(self):
        pcum=0.0; p_cum=0.0
        g=0.0; gg=0.0
        
        inc = 0
        dold = self.depth[0]
        for d in self.depth:
            print(d)
            inc = abs(dold - d)
            pcum  += g * inc; 
            p_cum += gg * inc
            dold = d
            l = self.getLayer(d)
            g = l.gamma(d)
            if d <= self.gwt:
                gg = g - 9.81
            else:
                gg=g
            self.g.append(gg)
            self.C.append(l.C(d))
            self.Fi.append(l.Fi(d))           
            self.p.append(pcum)
            self.p_.append(p_cum)
    # ---------------------------------------------------
            print("{:.2f}\t{:.2f}\t{:.2f}".format(d,g,pcum))
    # ---------------------------------------------------
        plt.plot(self.p,self.depth)
        plt.plot(self.p_,self.depth)
        plt.ylabel('Depth, m')
        plt.xlabel('Po, kPa')
        plt.grid()
        plt.show()
     # ---------------------------------------------------
        plt.plot(self.C,self.depth)
        plt.plot(self.Fi,self.depth)
        plt.ylabel('Depth, m')
        plt.xlabel('Po, kPa')
        plt.grid()
        plt.show()       
        return
# ----------------------------------------------------------------
    def setProps(self):
        pcum=0.0; p_cum=0.0
        g=0.0; gg=0.0
        
        inc = 0
        dold = self.depth[0]
        for d in self.depth:
            inc = abs(dold - d)
            pcum  += g * inc; 
            p_cum += gg * inc
            dold = d
            l = self.getLayer(d)
            g = l.gamma(d)


            self.g.append(g)
            self.C.append(l.C())
            self.Fi.append(l.Fi())

            if d <= self.gwt:
                gg = g - 9.81
            else:
                gg=g
    # ---------------------------------------------------
            print("{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(d,g,l.C(),l.Fi()))
    # ---------------------------------------------------
        plt.plot(self.C,self.depth)
        plt.plot(self.Fi,self.depth)
        plt.ylabel('Depth, m')
        plt.xlabel('Po, kPa')
        plt.grid()
        plt.show()
        return
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

if __name__ == "__main__":

    # p1 = Layer("Sand",0,-10)
    # p1.set_gamma(17,19)
    # p1.set_C(20,90)

    # p1.shift(5)
    # print((p1.gamma(h=7)))
    # print(p1.C())
    # print(p1.Fi())
    # p2 = p1.after("Clay",7)
    # print(p2.__dict__)

    pr = Profile("Profile_1")
    pr.addLayer("Sand_1",5)
    pr.current_layer.set_gamma(17,19)
    pr.current_layer.set_Fi(30,inc=.5)
    pr.addLayer("Clay",5)
    
    pr.current_layer.set_gamma(14,17)
    pr.current_layer.set_C(20,inc=5)

    pr.addLayer("Sand_2",8)
    pr.current_layer.set_gamma(18,19)

    pr.current_layer.set_Fi(33,inc=.5)
    pr.gwt = -3
    pr.print()
    pr.setDepth(-.1)
    pr.setP0()
