import matplotlib.pyplot as plt

a = 3.57728614907441140518e-136
b = 3.53234992160629284088e-78
alpha = 3.872e-117
beta = 9.557e-59
D = 2.4233920160704021815e-10
kT_2 = 2.07e-21

L1 = 7e-10
dx = 1e-13



def get_energy_atomic(x):
    out = 0
    
    for y_ind in range(-10, 10):
        for z_ind in range(-10, 10):
            r2 = x**2 + (y_ind * D)**2 + (z_ind * D)**2
            
            out += a / r2**6 - b / r2**3
    
    return out

def get_energy_smooth(x):
    return alpha / x**10 - beta / x**4



atomic_xlist = []
atomic_elist = []
x = L1
relative_energy = 0
while(relative_energy < 3):
    atomic_xlist.append(x)
    
    relative_energy = get_energy_atomic(x) / kT_2
    atomic_elist.append(relative_energy)
    
    x -= dx
    
smooth_xlist = []
smooth_elist = []
x = L1
relative_energy = 0
while(relative_energy < 3):
    smooth_xlist.append(x)
    
    relative_energy = get_energy_smooth(x) / kT_2
    smooth_elist.append(relative_energy)
    
    x -= dx
    
plt.plot(atomic_xlist, atomic_elist)
plt.plot(smooth_xlist, smooth_elist)
plt.xlabel('distance, m')
plt.ylabel('potential energy, 1/2kT')
plt.title('Interraction of a hydrogen atom\nwith a sodium wall')
plt.legend(('calculated with atomic model', 'calculated with smooth surface model'),
           loc='lower right')
plt.show()