import numpy as np

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Layer:
    def __init__(self, name,top,bot):
        self.name = name
        self.top = float(top)
        self.bot =  float(bot)
        self.thickness = float(abs(top - bot))
        self.gamma_top = 0.0
        self.gamma_bot = 0.0
        self.C_top = 0.0
        self.C_bot = 0.0
        self.Fi_top = 0.0
        self.Fi_bot = 0.0
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
    def a_gamma(self, gamma1, gamma2 = -9999):
        self.gamma_top = gamma1
        if gamma2 == -9999:
            self.gamma_bot = gamma1
        else:
            self.gamma_bot = gamma2
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
    def a_C(self, C1, C2 = -9999):
        self.C_top = C1
        if C2 == -9999:
            self.C_bot = C1
        else:
            self.C_bot = C2
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
    def a_Fi(self, Fi1, Fi2 = -9999):
        self.Fi_top = Fi1
        if Fi2 == -9999:
            self.Fi_bot = Fi1
        else:
            self.Fi_bot = Fi2
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
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Profile:
    def __init__(self, name):
        self.name = name
        self.top = 0.0
        self.bot =  0.0
        self.gwt = 0.0
        self.layer_names = {}
        self.layers_count=0

    def addLayer(self,l):
        self.layers_count = self.layers_count +1
        self.layer_names[self.layers_count] = l
        pass
  





if __name__ == "__main__":

    p1 = Layer("Sand",0,-10)
    p1.a_gamma(17,19)
    p1.a_C(20)
    print((p1.gamma(h=7)))
    print(p1.C())
    print(p1.Fi())
    p2 = p1.after("Clay",7)
    print(p2.__dict__)

    pr = Profile("Profile_1")
    pr.addLayer(p1)
    print(pr.__dict__)
    print(pr.layer_names[1].__dict__)