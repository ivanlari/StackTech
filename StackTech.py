# ------------------------------------------------------------------------------------
# ---------------------------- StackTech v1.0 ----------------------------------------
# ------------------------------------------------------------------------------------

from tkinter import *
import numpy as np
import math
import os
import datetime
import time

# ------------------------------------------------------------------------------------
# ---------------------------- Directories -------------------------------------------
# ------------------------------------------------------------------------------------

# Save directory name:
directory = "StackTech"
    
# Parent directory path:
parent_dir = os.sep # C:\

# Save path:
save_path = os.path.join(parent_dir, directory) 

# ------------------------------------------------------------------------------------
# ---------------------------- Window definition -------------------------------------
# ------------------------------------------------------------------------------------

f = Tk()

f.title("StackTech 1.0")
f.geometry("750x550")
back_color = "#EDDA74"
f['background']=back_color

Titolo = Label(f, text="StackTech", font=("Arial", 18))
Titolo.config(bg=back_color)
Titolo.grid(row=0, column=1)

testo0 = Label(f, text="Lamina", font=("Arial", 15))
testo0.config(bg=back_color)
testo0.grid(row=6, column=1, pady=20)

testo1 = Label(f, text="E1 (MPa):", font=("Arial", 11))
testo1.grid(row=8, column=1)
testo1.config(bg=back_color)
e1 = Entry(f, borderwidth=2)
e1.grid(row=8, column=2)
e1.insert(0, 134000)

testo2 = Label(f, text="E2 (MPa):", font=("Arial", 11))
testo2.grid(row=9, column=1)
testo2.config(bg=back_color)
e2 = Entry(f, borderwidth=2)
e2.grid(row=9, column=2)
e2.insert(0, 7000)

testo3 = Label(f, text="ni12:", font=("Arial", 11))
testo3.grid(row=10, column=1)
testo3.config(bg=back_color)
e3 = Entry(f, borderwidth=2)
e3.grid(row=10, column=2)
e3.insert(0, 0.25)

testo4 = Label(f, text="G12 (MPa):", font=("Arial", 11))
testo4.grid(row=11, column=1)
testo4.config(bg=back_color)
e4 = Entry(f, borderwidth=2)
e4.grid(row=11, column=2)
e4.insert(0, 4200)

testo5 = Label(f, text="f1t (MPa):", font=("Arial", 11))
testo5.grid(row=8, column=4, padx=30)
testo5.config(bg=back_color)
e5 = Entry(f, borderwidth=2)
e5.grid(row=8, column=5)
e5.insert(0, 2500)

testo6 = Label(f, text="f1c (MPa):", font=("Arial", 11))
testo6.grid(row=9, column=4)
testo6.config(bg=back_color)
e6 = Entry(f, borderwidth=2)
e6.grid(row=9, column=5)
e6.insert(0, 1200)

testo7 = Label(f, text="f2t (MPa):", font=("Arial", 11))
testo7.grid(row=10, column=4)
testo7.config(bg=back_color)
e7 = Entry(f, borderwidth=2)
e7.grid(row=10, column=5)
e7.insert(0, 80)

testo8 = Label(f, text="f2c (MPa):", font=("Arial", 11))
testo8.grid(row=11, column=4)
testo8.config(bg=back_color)
e8 = Entry(f, borderwidth=2)
e8.grid(row=11, column=5)
e8.insert(0, 200)

testo9 = Label(f, text="f12 (MPa):", font=("Arial", 11))
testo9.grid(row=12, column=4)
testo9.config(bg=back_color)
e9 = Entry(f, borderwidth=2)
e9.grid(row=12, column=5)
e9.insert(0, 80)

testo10 = Label(f, text="Laminate", font=("Arial", 15))
testo10.grid(row=32, column=1, pady=20)
testo10.config(bg=back_color)

testo11 = Label(f, text="Thickness (mm):", font=("Arial", 11))
testo11.grid(row=33, column=1)
testo11.config(bg=back_color)
e11 = Entry(f, borderwidth=2)
e11.grid(row=33, column=2)
e11.insert(0, 1)

testo12 = Label(f, text="Plies:", font=("Arial", 11))
testo12.grid(row=34, column=1)
testo12.config(bg=back_color)
e12 = Entry(f, borderwidth=2)
e12.grid(row=34, column=2)
e12.insert(0, 4)

testo13 = Label(f, text="Loads", font=("Arial", 15))
testo13.grid(row=25, column=1, pady=20)
testo13.config(bg=back_color)

testo14 = Label(f, text="Nx (N/mm):", font=("Arial", 11))
testo14.grid(row=27, column=1)
testo14.config(bg=back_color)
e14 = Entry(f, borderwidth=2)
e14.grid(row=27, column=2)
e14.insert(0, 100)

testo15 = Label(f, text="Ny (N/mm):", font=("Arial", 11))
testo15.grid(row=28, column=1)
testo15.config(bg=back_color)
e15 = Entry(f, borderwidth=2)
e15.grid(row=28, column=2)
e15.insert(0, 0)

testo16 = Label(f, text="Ns (N/mm):", font=("Arial", 11))
testo16.grid(row=29, column=1)
testo16.config(bg=back_color)
e16 = Entry(f, borderwidth=2)
e16.grid(row=29, column=2)
e16.insert(0, 0)

testo17 = Label(f, text="Mx (N):", font=("Arial", 11))
testo17.grid(row=27, column=4)
testo17.config(bg=back_color)
e17 = Entry(f, borderwidth=2)
e17.grid(row=27, column=5)
e17.insert(0, 0)

testo18 = Label(f, text="My (N):", font=("Arial", 11))
testo18.grid(row=28, column=4)
testo18.config(bg=back_color)
e18 = Entry(f, borderwidth=2)
e18.grid(row=28, column=5)
e18.insert(0, 0)

testo19 = Label(f, text="Ms (N):", font=("Arial", 11))
testo19.grid(row=29, column=4)
testo19.config(bg=back_color)
e19 = Entry(f, borderwidth=2)
e19.grid(row=29, column=5)
e19.insert(0, 0)

# ------------------------------------------------------------------------------------
# ---------------------------- Start of script ---------------------------------------
# ------------------------------------------------------------------------------------

print("------------------------------------------------------")
print("------------------------------------------------------")
print("------------------- StackTech 1.0 --------------------   To begin, enter the requested data in the")
print("------------------------------------------------------   dedicated window and clic Compute.")
print("-------------- Developed by Ivan Lari ----------------")
print("--------------------- May 2021 -----------------------")
print("------------------------------------------------------")
print("------------------------------------------------------\n")

# Make save directory:
try: 
    os.mkdir(save_path) 
    print ("A directory called %s " % directory + "has been created in C:/.")
except OSError as error: 
    # print(error)
    print("A directory for this analysis already exist.") 

# Make save directory the current working directory:
os.chdir(save_path)
cwd = os.getcwd()
print("Current working directory:  %s" % cwd)
print(" ")

def clic1():

    # ************************************************************************************
    # ******************************** START OF SOLVER ***********************************
    # ************************************************************************************

    print("Computing...\n")

    # Get material properties
    E1 = int(e1.get())
    E2 = int(e2.get())
    ni12 = float(e3.get())
    G12 = int(e4.get())

    # Get allowables
    f1t = int(e5.get())
    f1c = int(e6.get())
    f2t = int(e7.get())
    f2c = int(e8.get())
    f12 = int(e9.get())

    # Get external loads
    Nx = int(e14.get())
    Ny = int(e15.get())
    Ns = int(e16.get())
    Mx = int(e17.get())
    My = int(e18.get())
    Ms = int(e19.get())

    # Get laminate properties
    N = int(e12.get())
    h = int(e11.get())

    # ------------------------------------------------------------------------------------
    # ---------------------------- Lamina stiffness matrix -------------------------------
    # ---------------------------- in lamina reference system ----------------------------
    # ------------------------------------------------------------------------------------

    ni21 = ni12 * E2 / E1
    b = 1 / (1 - ni12 * ni21)
    Q = np.array([[b * E1, b * ni12 * E2, 0], [b * ni12 * E2, b * E2, 0], [0, 0, G12]])
    print("---------------------------------------------------------------------------\n")
    print("The stiffness matrix of the lamina in the local reference system (1-2) is: \n")
    print(Q, "(MPa) \n")
    print("---------------------------------------------------------------------------\n")

    hl = h / N  # lamina thickness
    z = np.zeros(N + 1)
    for k in range(N + 1):
            z[k] = -h / 2 + k * hl

    # ------------------------------------------------------------------------------------
    # ---------------------------- Stacking sequence -------------------------------------
    # ------------------------------------------------------------------------------------
       
    print("Insert the stacking sequence of the plies (deg) and press Enter:")
    print("(from bottom to top, separated by a space, example: 45 90 90 0)\n")
    angles_entries = list(map(float, input().split()))
    c2 = np.array(angles_entries)

    # Rotation matrix
    R = lambda a: np.array([[(np.cos(a)) ** 2, (np.sin(a)) ** 2, -np.sin(a) * np.cos(a)],
                            [(np.sin(a)) ** 2, (np.cos(a)) ** 2, np.sin(a) * np.cos(a)],
                            [2 * np.sin(a) * np.cos(a), -2 * np.sin(a) * np.cos(a),
                             (np.cos(a)) ** 2 - (np.sin(a)) ** 2]])

    # ------------------------------------------------------------------------------------
    # ---------------------------- Laminas stiffness matrices ----------------------------
    # ---------------------------- in laminate reference system --------------------------
    # ------------------------------------------------------------------------------------

    a = np.zeros([3, 3 * N])
    j = 0
    c2_rad = np.deg2rad(c2)
    ni21 = ni12 * E2 / E1
    b = 1 / (1 - ni12 * ni21)
    Q = np.array([[b * E1, b * ni12 * E2, 0], [b * ni12 * E2, b * E2, 0], [0, 0, G12]])
    for i in range(N):
        t = c2_rad[i]
        Rt = R(t)
        o = np.linalg.inv(Rt)
        m = np.transpose(o)
        O = np.dot(Q, o)
        a[0:3, j:(j + 3)] = np.dot(m, O)
        j = j + 3

    # ------------------------------------------------------------------------------------
    # ---------------------------- A, B, D matrices --------------------------------------
    # ------------------------------------------------------------------------------------

    k = 0
    A = np.zeros([3, 3])
    B = np.zeros([3, 3])
    D = np.zeros([3, 3])

    for n in range(N):
        ti = -(z[n] - z[n + 1])
        ti2 = -((z[n]) ** 2 - (z[n + 1]) ** 2)
        ti3 = -((z[n]) ** 3 - (z[n + 1]) ** 3)
        As = a[0:3, k:(k + 3)] * ti
        Bs = 1 / 2 * a[0:3, k:(k + 3)] * ti2
        Ds = 1 / 3 * a[0:3, k:(k + 3)] * ti3
        k = k + 3
        A = A + As
        B = B + Bs
        D = D + Ds

    print(" ")
    print("---------------------------------------------------------------------------\n")
    print("Laminate matrices (laminate reference system (x-y))\n")
    print("Membrane matrix A (N/mm): \n")
    print(A, "\n")
    print("Membrane-bending coupling matrix B (N): \n")
    print(B, "\n")
    print("Bending matrix D (Nmm): \n")
    print(D, "\n")
    print("---------------------------------------------------------------------------\n")

    # ------------------------------------------------------------------------------------
    # ---------------------------- Solve system ------------------------------------------
    # ------------------------------------------------------------------------------------

    S = np.array([Nx, Ny, Ns, Mx, My, Ms])
    S.shape = (6, 1)
    C = np.zeros([6, 6])
    C[0:3, 0:3] = A
    C[0:3, 3:6] = B
    C[3:6, 0:3] = B
    C[3:6, 3:6] = D

    e = np.linalg.solve(C, S)

    e0 = np.array([e[0], e[1], e[2]])
    k = np.array([e[3], e[4], e[5]])

    # Total strain
    eps = lambda f: e0 + f * k

    print("Mean plane strain vector (epsilon 0) (x-y): \n")
    print(e0)
    print(" ")
    print("Mean plane curvature vector (k) (1/mm) (x-y): \n")
    print(k)
    print(" ")
    print("---------------------------------------------------------------------------\n")

    # ------------------------------------------------------------------------------------
    # ---------------------------- Start writing output ----------------------------------
    # ------------------------------------------------------------------------------------

    # Time and date variables
    localtime = time.localtime(time.time())
    timestring = time.strftime('%Y/%m/%d - %H:%M:%S')

    # Create results file
    with open('Results.txt', 'w') as f:
        f.write('************************************************************************************\n')
        f.write('************************************************************************************\n')
        f.write('             StackTech 1.0 - RESULTS DATABASE - ' + str(timestring) + ' \n')
        f.write('************************************************************************************\n')
        f.write('************************************************************************************\n')
        f.write(' \n')
        f.write('************************************************************************************\n')
        f.write('Stiffness matrix of the lamina in the local reference system (1-2) (MPa): \n')
        f.write(' \n')

        Q_mat = np.matrix(Q)
        A_mat = np.matrix(A)
        B_mat = np.matrix(B)
        D_mat = np.matrix(D)

        for line in Q_mat:
            np.savetxt(f, line, fmt='%.2f')

        f.write(' \n')
        f.write('************************************************************************************\n')
        f.write('Stacking sequence \n')
        f.write(' \n')
        np.savetxt(f, c2, fmt='%.2f')

        f.write(' \n')
        f.write('************************************************************************************\n')
        f.write('Laminate matrices (laminate reference system (x-y)) \n')
        f.write(' \n')
        f.write('Membrane matrix A (N/mm) \n')
        f.write(' \n')
        for line in A_mat:
            np.savetxt(f, line, fmt='%.2f')
        f.write(' \n')
        f.write('Membrane-bending coupling matrix B (N) \n')
        f.write(' \n')
        for line in B_mat:
            np.savetxt(f, line, fmt='%.2f')
        f.write(' \n')
        f.write('Bending matrix D (Nmm) \n')
        f.write(' \n')
        for line in D_mat:
            np.savetxt(f, line, fmt='%.2f')

        f.write(' \n')
        f.write('************************************************************************************\n')
        f.write('Mean plane strain vector (epsilon 0) (x-y) \n')
        f.write(' \n')
        np.savetxt(f, e0, fmt='%.6f')
        f.write(' \n')

        f.write('************************************************************************************\n')
        f.write('Mean plane curvature vector (k) (1/mm) (x-y) \n')
        f.write(' \n')
        np.savetxt(f, k, fmt='%.6f')
        f.write(' \n')

        f.write('************************************************************************************\n')
        f.write('Stresses and strains in the plies (lamina reference system (1-2)) \n')
        f.write(' \n')
    f.close()

    # ------------------------------------------------------------------------------------
    # ---------------------------- Stresses and strains ----------------------------------
    # ---------------------------- in the laminas ----------------------------------------
    # ------------------------------------------------------------------------------------

    print("Stresses and strains in the plies (lamina reference system (1-2))\n")

    v = np.zeros([3, N])
    y = np.zeros([3, N])
    d = len(z)

    if math.floor(d / 2) * 2 == d:
        z = z
    else:
        c = math.floor(d / 2)
        z = np.delete(z, c)

    for i in range(N):
        print("Ply", i + 1,":")
        print(" ")
        t = c2_rad[i]
        Rt = R(t)
        o = np.linalg.inv(Rt)
        x = z[i]
        w = eps(x)
        b = np.dot(o, w)
        v[0:3, i:i + 1] = b
        y[0:3, i:i + 1] = np.dot(Q, b)
        print("Epsilon:", v[:, i])
        print("Sigma:", y[:, i], "MPa \n")
        with open('Results.txt', 'a') as f:
            f.write('------------\n')
            f.write('\n')
            f.write('Ply ')
            f.write(str(i+1))
            f.write(' :\n')
            f.write('\n')
            f.write('Epsilon: \n')
            f.write('\n')
            np.savetxt(f, v[:, i], fmt='%.6f')
            f.write('\n')
            f.write('Sigma (MPa): \n')
            f.write('\n')
            np.savetxt(f, y[:, i], fmt='%.2f')
            f.write('\n')
        f.close()

    # ************************************************************************************
    # ******************************** FAILURE CRITERIONS ********************************
    # ************************************************************************************

    print("---------------------------------------------------------------------------\n")
    print("Failure criterions\n")

    with open('Results.txt', 'a') as f:
        f.write('************************************************************************************\n')
        f.write('Failure criterions \n')
        f.write('\n')
    f.close()

    zero = np.zeros(1)
    q5 = np.zeros(1)
    q5m = np.zeros(1)
    nov = np.zeros(1)

    for i in range(N):
        if c2[i] == 0:
            zero = np.append(zero, 1)
        elif c2[i] == 45:
            q5 = np.append(q5, 1)
        elif c2[i] == -45:
            q5m = np.append(q5m, 1)
        elif c2[i] == 90 or c2[i] == -90:
            nov = np.append(nov, 1)

    lam_0 = len(zero) - 1  # numero di lamine a 0 gradi
    lam_90 = len(nov) - 1
    lam_45 = len(q5) - 1
    lam_m45 = len(q5m) - 1

    p_lam_0 = lam_0 / N * 100  # % di lamine a 0 gradi
    p_lam_90 = lam_90 / N * 100
    p_lam_45 = lam_45 / N * 100
    p_lam_m45 = lam_m45 / N * 100
    p_lam_45s = p_lam_45 + p_lam_m45

    Fmxt = f1t * (p_lam_0 + 0.1 * (p_lam_90 + p_lam_45s)) / 100
    Fmxc = f1c * (p_lam_0 + 0.1 * (p_lam_90 + p_lam_45s)) / 100
    Fmyt = f1t * (p_lam_90 + 0.1 * (p_lam_0 + p_lam_45s)) / 100
    Fmyc = f1c * (p_lam_90 + 0.1 * (p_lam_0 + p_lam_45s)) / 100

    Fbxt = f1t * (p_lam_0 + 0.1 * p_lam_90 + 0.55 * p_lam_45s) / 100
    Fbxc = f1c * (p_lam_0 + 0.1 * p_lam_90 + 0.55 * p_lam_45s) / 100
    Fbyt = f1t * (p_lam_90 + 0.1 * p_lam_0 + 0.55 * p_lam_45s) / 100
    Fbyc = f1c * (p_lam_90 + 0.1 * p_lam_0 + 0.55 * p_lam_45s) / 100

    if f1t > f1c:
        Fsh = (0.05 + 0.225 * p_lam_45s / 100) * f1c
    else:
        Fsh = (0.05 + 0.225 * p_lam_45s / 100) * f1t

    if (p_lam_0 >= 10) and (p_lam_90 >= 10) and (p_lam_45 >= 10) and (p_lam_m45 >= 10):
        er = 1
    else:
        er = 0

    print("What lamina failure criterion would you like to be implemented?\n")
    print("                    S: Max Stress")
    print("                    T: Tsai-Hill")
    print("                    H: Hoffman")
    print("                    W: Tsai-Wu\n")
    L = str(input("(type the corresponding letter and press Enter): "))
    print(" ")

    if L == "S":

        # ------------------------------------------------------------------------------------
        # ---------------------------- Max stress criterion ----------------------------------
        # ------------------------------------------------------------------------------------

        print("Max Stress criterion")

        with open('Results.txt', 'a') as f:
            f.write('Max Stress criterion \n')
            f.write('\n')
        f.close()
        rf = np.zeros(N)
        for j in range(N):
            g = y[:, j]
            if g[0] > 0:
                f1 = f1t
            else:
                f1 = f1c
                g[0] = abs(g[0])
            if g[1] > 0:
                f2 = f2t
            else:
                f2 = f2c
                g[1] = abs(g[1])
            g[2] = abs(g[2])
            ms = np.array([f1 / g[0] - 1, f2 / g[1] - 1, f12 / g[2] - 1])
            ms = np.sort(ms)
            MS = ms[0]
            RF = MS + 1
            rf[j] = RF
            print(" ")
            print("Lamina", j + 1, ":", "MS =", MS, ",", "RF =", RF)
            with open('Results.txt', 'a') as f:
                f.write('Ply ')
                f.write(str(j+1))
                f.write(' -> ')
                f.write(' ')
                f.write('MS: ')
                f.write(str(MS))
                f.write('     ')
                f.write('RF: ')
                f.write(str(RF))
                f.write('\n')
            f.close()
        rf = np.sort(rf)
        print(" ")
        if rf[0] < 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is not verified.\n')
                f.write('(There is at least one lamina with a RF less than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is not verified.")
            print("(There is at least one lamina with a RF less than 1)")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is verified.\n')
                f.write('(All the RF are greater than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is verified.")
            print("(All the RF are greater than 1)")
        print(" ")
        print("The % of plies at 0, 90, 45 e -45 are:\n")
        print("0: ", p_lam_0, "%")
        print("90: ", p_lam_90, "%")
        print("45: ", p_lam_45, "%")
        print("-45: ", p_lam_m45, "%\n")
        with open('Results.txt', 'a') as f:
            f.write('The % of plies at 0, 90, 45 e -45 are:\n')
            f.write('\n')
            f.write('0: ')
            f.write(str(p_lam_0))
            f.write(' %\n')
            f.write('90: ')
            f.write(str(p_lam_90))
            f.write(' %\n')
            f.write('45: ')
            f.write(str(p_lam_45))
            f.write(' %\n')
            f.write('-45: ')
            f.write(str(p_lam_m45))
            f.write(' %\n')
        f.close()
        if er == 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n')
                f.write('Fmxt = ')
                f.write(str(Fmxt))
                f.write('   ')
                f.write('Fmxc = ')
                f.write(str(Fmxc))
                f.write('   ')
                f.write('Fmyt = ')
                f.write(str(Fmyt))
                f.write('   ')
                f.write('Fmyc = ')
                f.write(str(Fmyc))
                f.write('   \n')
                f.write('Fbxt = ')
                f.write(str(Fbxt))
                f.write('   ')
                f.write('Fbxc = ')
                f.write(str(Fbxc))
                f.write('   ')
                f.write('Fbyt = ')
                f.write(str(Fbyt))
                f.write('   ')
                f.write('Fbyc = ')
                f.write(str(Fbyc))
                f.write('   \n')
                f.write('Fsh = ')
                f.write(str(Fsh))
                f.write('   ')
            f.close()
            print("Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n")
            print("Fmxt =", Fmxt, " Fmxc =", Fmxc, " Fmyt =", Fmyt, " Fmyc =", Fmyc, " (MPa)")
            print("Fbxt =", Fbxt, " Fbxc =", Fbxc, " Fbyt =", Fbyt, " Fbyc =", Fbyc, " (MPa)")
            print("Fsh =", Fsh, " (MPa)\n")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is not applicable.\n')
                f.write('\n')
            f.close()
            print("Therefore the 10 % rule is not applicable.\n")
        # print("(Tempo di calcolo complessivo:", tov, "secondi)")
        print("---------------------------------------------------------------------------\n")
        print("Thanks for using StackTech!")
        with open('Results.txt', 'a') as f:
            f.write('Thanks for using StackTech!')
        f.close()

    elif L == "T":
        
        # ------------------------------------------------------------------------------------
        # ---------------------------- Tsai-Hill criterion -----------------------------------
        # ------------------------------------------------------------------------------------

        print("Tsai-Hill criterion")

        with open('Results.txt', 'a') as f:
            f.write('Tsai-Hill criterion \n')
            f.write('\n')
        f.close()
        rf = np.zeros(N)
        for j in range(N):
            g = y[:, j]
            if g[0] > 0:
                f1 = f1t
            else:
                f1 = f1c
                g[0] = abs(g[0])
            if g[1] > 0:
                f2 = f2t
            else:
                f2 = f2c
                g[1] = abs(g[1])
            g[2] = abs(g[2])
            MS = 1 / math.sqrt((g[0] / f1) ** 2 + (g[1] / f2) ** 2 - g[0] * g[1] / f1 ** 2 + (g[2] / f12) ** 2) - 1
            RF = MS + 1
            rf[j] = RF
            print(" ")
            print("Lamina", j + 1, ":", "MS =", MS, ",", "RF =", RF)
            with open('Results.txt', 'a') as f:
                f.write('Ply ')
                f.write(str(j+1))
                f.write(' -> ')
                f.write(' ')
                f.write('MS: ')
                f.write(str(MS))
                f.write('     ')
                f.write('RF: ')
                f.write(str(RF))
                f.write('\n')
            f.close()
        rf = np.sort(rf)
        print(" ")
        if rf[0] < 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is not verified.\n')
                f.write('(There is at least one lamina with a RF less than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is not verified.")
            print("(There is at least one lamina with a RF less than 1)")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is verified.\n')
                f.write('(All the RF are greater than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is verified.")
            print("(All the RF are greater than 1)")
        print(" ")
        print("The % of plies at 0, 90, 45 e -45 are:\n")
        print("0: ", p_lam_0, "%")
        print("90: ", p_lam_90, "%")
        print("45: ", p_lam_45, "%")
        print("-45: ", p_lam_m45, "%\n")
        with open('Results.txt', 'a') as f:
            f.write('The % of plies at 0, 90, 45 e -45 are:\n')
            f.write('\n')
            f.write('0: ')
            f.write(str(p_lam_0))
            f.write(' %\n')
            f.write('90: ')
            f.write(str(p_lam_90))
            f.write(' %\n')
            f.write('45: ')
            f.write(str(p_lam_45))
            f.write(' %\n')
            f.write('-45: ')
            f.write(str(p_lam_m45))
            f.write(' %\n')
        f.close()
        if er == 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n')
                f.write('Fmxt = ')
                f.write(str(Fmxt))
                f.write('   ')
                f.write('Fmxc = ')
                f.write(str(Fmxc))
                f.write('   ')
                f.write('Fmyt = ')
                f.write(str(Fmyt))
                f.write('   ')
                f.write('Fmyc = ')
                f.write(str(Fmyc))
                f.write('   \n')
                f.write('Fbxt = ')
                f.write(str(Fbxt))
                f.write('   ')
                f.write('Fbxc = ')
                f.write(str(Fbxc))
                f.write('   ')
                f.write('Fbyt = ')
                f.write(str(Fbyt))
                f.write('   ')
                f.write('Fbyc = ')
                f.write(str(Fbyc))
                f.write('   \n')
                f.write('Fsh = ')
                f.write(str(Fsh))
                f.write('   ')
            f.close()
            print("Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n")
            print("Fmxt =", Fmxt, " Fmxc =", Fmxc, " Fmyt =", Fmyt, " Fmyc =", Fmyc, " (MPa)")
            print("Fbxt =", Fbxt, " Fbxc =", Fbxc, " Fbyt =", Fbyt, " Fbyc =", Fbyc, " (MPa)")
            print("Fsh =", Fsh, " (MPa)\n")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is not applicable.\n')
                f.write('\n')
            f.close()
            print("Therefore the 10 % rule is not applicable.\n")
        # print("(Tempo di calcolo complessivo:", tov, "secondi)")
        print("---------------------------------------------------------------------------\n")
        print("Thanks for using StackTech!")
        with open('Results.txt', 'a') as f:
            f.write('Thanks for using StackTech!')
        f.close()

    elif L == "H":
        
        # ------------------------------------------------------------------------------------
        # ---------------------------- Hoffmann criterion ------------------------------------
        # ------------------------------------------------------------------------------------

        print("Hoffman criterion")

        with open('Results.txt', 'a') as f:
            f.write('Hoffman criterion \n')
            f.write('\n')
        f.close()
        F1 = 1 / f1t - 1 / f1c
        F11 = 1 / (f1t * f1c)
        F2 = 1 / f2t - 1 / f2c
        F22 = 1 / (f2t * f2c)
        F66 = 1 / f12 ** 2
        F12 = -1 / (2 * f1t * f1c)
        rf = np.zeros(N)
        for j in range(N):
            g = y[:, j]
            A = F1 * g[0] + F2 * g[1]
            B = F11 * (g[0]) ** 2 + F22 * (g[1]) ** 2 + F66 * (g[2]) ** 2 + 2 * F12 * g[0] * g[1]
            MS = 2 / (-A + math.sqrt(A ** 2 + 4 * B)) - 1
            RF = MS + 1
            rf[j] = RF
            print(" ")
            print("Lamina", j + 1, ":", "MS =", MS, ",", "RF =", RF)
            with open('Results.txt', 'a') as f:
                f.write('Ply ')
                f.write(str(j+1))
                f.write(' -> ')
                f.write(' ')
                f.write('MS: ')
                f.write(str(MS))
                f.write('     ')
                f.write('RF: ')
                f.write(str(RF))
                f.write('\n')
            f.close()
        rf = np.sort(rf)
        print(" ")
        if rf[0] < 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is not verified.\n')
                f.write('(There is at least one lamina with a RF less than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is not verified.")
            print("(There is at least one lamina with a RF less than 1)")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is verified.\n')
                f.write('(All the RF are greater than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is verified.")
            print("(All the RF are greater than 1)")
        print(" ")
        print("The % of plies at 0, 90, 45 e -45 are:\n")
        print("0: ", p_lam_0, "%")
        print("90: ", p_lam_90, "%")
        print("45: ", p_lam_45, "%")
        print("-45: ", p_lam_m45, "%\n")
        with open('Results.txt', 'a') as f:
            f.write('The % of plies at 0, 90, 45 e -45 are:\n')
            f.write('\n')
            f.write('0: ')
            f.write(str(p_lam_0))
            f.write(' %\n')
            f.write('90: ')
            f.write(str(p_lam_90))
            f.write(' %\n')
            f.write('45: ')
            f.write(str(p_lam_45))
            f.write(' %\n')
            f.write('-45: ')
            f.write(str(p_lam_m45))
            f.write(' %\n')
        f.close()
        if er == 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n')
                f.write('Fmxt = ')
                f.write(str(Fmxt))
                f.write('   ')
                f.write('Fmxc = ')
                f.write(str(Fmxc))
                f.write('   ')
                f.write('Fmyt = ')
                f.write(str(Fmyt))
                f.write('   ')
                f.write('Fmyc = ')
                f.write(str(Fmyc))
                f.write('   \n')
                f.write('Fbxt = ')
                f.write(str(Fbxt))
                f.write('   ')
                f.write('Fbxc = ')
                f.write(str(Fbxc))
                f.write('   ')
                f.write('Fbyt = ')
                f.write(str(Fbyt))
                f.write('   ')
                f.write('Fbyc = ')
                f.write(str(Fbyc))
                f.write('   \n')
                f.write('Fsh = ')
                f.write(str(Fsh))
                f.write('   ')
            f.close()
            print("Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n")
            print("Fmxt =", Fmxt, " Fmxc =", Fmxc, " Fmyt =", Fmyt, " Fmyc =", Fmyc, " (MPa)")
            print("Fbxt =", Fbxt, " Fbxc =", Fbxc, " Fbyt =", Fbyt, " Fbyc =", Fbyc, " (MPa)")
            print("Fsh =", Fsh, " (MPa)\n")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is not applicable.\n')
                f.write('\n')
            f.close()
            print("Therefore the 10 % rule is not applicable.\n")
        # print("(Tempo di calcolo complessivo:", tov, "secondi)")
        print("---------------------------------------------------------------------------\n")
        print("Thanks for using StackTech!")
        with open('Results.txt', 'a') as f:
            f.write('Thanks for using StackTech!')
        f.close()

    elif L == "W":
        
        # ------------------------------------------------------------------------------------
        # ---------------------------- Tsai-Wu criterion -------------------------------------
        # ------------------------------------------------------------------------------------

        print("Tsai-Wu criterion")

        with open('Results.txt', 'a') as f:
            f.write('Tsai-Wu criterion \n')
            f.write('\n')
        f.close()
        g1 = 1 / f1t - 1 / f1c
        F11 = 1 / (f1t * f1c)
        g2 = 1 / f2t - 1 / f2c
        F22 = 1 / (f2t * f2c)
        F66 = 1 / f12 ** 2
        B_ = -1 / 2 * math.sqrt(f1t * f1c) / math.sqrt(f2t * f2c)
        F12 = B_ / (f1t * f1c)
        rf = np.zeros(N)
        for j in range(N):
            g = y[:, j]
            A = g1 * g[0] + g2 * g[1]
            B = F11 * (g[0]) ** 2 + F22 * (g[1]) ** 2 + F66 * (g[2]) ** 2 + 2 * F12 * g[0] * g[1]
            MS = 2 / (-A + math.sqrt(A ** 2 + 4 * B)) - 1
            RF = MS + 1
            rf[j] = RF
            print(" ")
            print("Lamina", j + 1, ":", "MS =", MS, ",", "RF =", RF)
            with open('Results.txt', 'a') as f:
                f.write('Ply ')
                f.write(str(j+1))
                f.write(' -> ')
                f.write(' ')
                f.write('MS: ')
                f.write(str(MS))
                f.write('     ')
                f.write('RF: ')
                f.write(str(RF))
                f.write('\n')
            f.close()
        rf = np.sort(rf)
        print(" ")
        if rf[0] < 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is not verified.\n')
                f.write('(There is at least one lamina with a RF less than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is not verified.")
            print("(There is at least one lamina with a RF less than 1)")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore, according to the criterion of First Ply Failure the laminate is verified.\n')
                f.write('(All the RF are greater than 1)\n')
                f.write('\n')
            f.close()
            print("Therefore, according to the criterion of 'First Ply Failure' the laminate is verified.")
            print("(All the RF are greater than 1)")
        print(" ")
        print("The % of plies at 0, 90, 45 e -45 are:\n")
        print("0: ", p_lam_0, "%")
        print("90: ", p_lam_90, "%")
        print("45: ", p_lam_45, "%")
        print("-45: ", p_lam_m45, "%\n")
        with open('Results.txt', 'a') as f:
            f.write('The % of plies at 0, 90, 45 e -45 are:\n')
            f.write('\n')
            f.write('0: ')
            f.write(str(p_lam_0))
            f.write(' %\n')
            f.write('90: ')
            f.write(str(p_lam_90))
            f.write(' %\n')
            f.write('45: ')
            f.write(str(p_lam_45))
            f.write(' %\n')
            f.write('-45: ')
            f.write(str(p_lam_m45))
            f.write(' %\n')
        f.close()
        if er == 1:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n')
                f.write('Fmxt = ')
                f.write(str(Fmxt))
                f.write('   ')
                f.write('Fmxc = ')
                f.write(str(Fmxc))
                f.write('   ')
                f.write('Fmyt = ')
                f.write(str(Fmyt))
                f.write('   ')
                f.write('Fmyc = ')
                f.write(str(Fmyc))
                f.write('   \n')
                f.write('Fbxt = ')
                f.write(str(Fbxt))
                f.write('   ')
                f.write('Fbxc = ')
                f.write(str(Fbxc))
                f.write('   ')
                f.write('Fbyt = ')
                f.write(str(Fbyt))
                f.write('   ')
                f.write('Fbyc = ')
                f.write(str(Fbyc))
                f.write('   \n')
                f.write('Fsh = ')
                f.write(str(Fsh))
                f.write('   ')
            f.close()
            print("Therefore the 10 % rule is applicable and the allowable values of the laminate are:\n")
            print("Fmxt =", Fmxt, " Fmxc =", Fmxc, " Fmyt =", Fmyt, " Fmyc =", Fmyc, " (MPa)")
            print("Fbxt =", Fbxt, " Fbxc =", Fbxc, " Fbyt =", Fbyt, " Fbyc =", Fbyc, " (MPa)")
            print("Fsh =", Fsh, " (MPa)\n")
        else:
            with open('Results.txt', 'a') as f:
                f.write('\n')
                f.write('Therefore the 10 % rule is not applicable.\n')
                f.write('\n')
            f.close()
            print("Therefore the 10 % rule is not applicable.\n")
        # print("(Tempo di calcolo complessivo:", tov, "secondi)")
        print("---------------------------------------------------------------------------\n")
        print("Thanks for using StackTech!")
        with open('Results.txt', 'a') as f:
            f.write('Thanks for using StackTech!')
        f.close()

    # ************************************************************************************
    # ******************************** END OF SOLVER *************************************
    # ************************************************************************************

    print("A result text file has been generated in C:\StackTech.\n")
    print("Clic Compute to perform another analysis, Results to view the output file or Quit to exit the program.")

def clic2():
    if os.path.isfile("Results.txt") == True: # check if results file exists
        os.system("Results.txt")
    else:
        print("An output file is not present in the working directory.")
        print("Run an analysis before viewing the results.\n")
        print(" ")

# ------------------------------------------------------------------------------------
# ---------------------------- Buttons definition ------------------------------------
# ------------------------------------------------------------------------------------

button1 = Button(f, command=clic1, text="Compute", height=3, width=15)
button1.grid(row=35, column=5)

button2 = Button(f, text="Quit", command=f.quit, height=3, width=15)
button2.grid(row=35, column=7)

button3 = Button(f, text="Results", command=clic2, height=3, width=15)
button3.grid(row=35, column=6)

# ------------------------------------------------------------------------------------
# ---------------------------- End of script -----------------------------------------
# ------------------------------------------------------------------------------------

f.mainloop()