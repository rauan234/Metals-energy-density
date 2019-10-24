import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from numpy import sqrt, exp, log, pi, power
import numpy



saturated_vapor_table = ''''Li'	'solid'	5.667	-8310	0	0	453
'Li'	'liquid'	5.055	-8023	0	0	0
'Na'	'solid'	5.298	-5603	0	0	371
'Na'	'liquid'	4.704	-5377	0	0	0
'K'	'solid'	4.961	-4646	0	0	336
'K'	'liquid'	4.402	-4453	0	0	0
'Rb'	'solid'	4.5857	-4215	0	0	313
'Rb'	'liquid'	4.312	-4040	0	0	0
'Cs'	'solid'	4.711	-3999	0	0	301.6
'Cs'	'liquid'	4.165	-3830	0	0	0
'Be'	'solid'	8.042	-17020	-0.444	0	1560
'Be'	'liquid'	5.786	-15731	0	0	0
'Mg'	'solid'	8.489	-7813	-0.8253	0	923
'Mg'	'liquid'	0	0	0	0	0
'Ca'	'solid'	10.127	-9517	-1.403	0	1112
'Ca'	'liquid'	0	0	0	0	0
'Sr'	'solid'	9.226	-8572	-1.1926	0	1042
'Sr'	'liquid'	0	0	0	0	0
'Ba'	'solid'	12.405	-9690	-2.289	0	1002
'Ba'	'liquid'	4.007	-8163	0	0	0
'Al'	'solid'	9.459	-17342	-0.7927	0	933
'Al'	'liquid'	5.911	-16211	0	0	0
'Ga'	'solid'	6.657	-14208	0	0	302.9
'Ga'	'liquid'	6.754	-13984	-0.3413	0	0
'In'	'solid'	5.991	-12548	0	0	429
'In'	'liquid'	5.374	-12276	0	0	0
'Tl'	'solid'	5.971	-9447	0	0	577
'Tl'	'liquid'	5.259	-9037	0	0	0
'Sn'	'solid'	6.036	-15710	0	0	508
'Sn'	'liquid'	5.262	-15332	0	0	0
'Pb'	'solid'	5.643	-10143	0	0	601
'Pb'	'liquid'	4.911	-9701	0	0	0
'Sc'	'solid'	6.65	-19721	0.2885	-0.3663	1812
'Sc'	'liquid'	5.795	-17681	0	0	0
'Y'	'solid'	9.735	-22306	-0.8705	0	1799
'Y'	'liquid'	5.795	-20341	0	0	0
'La'	'solid'	7.463	-22551	-0.3142	0	1190
'La'	'liquid'	5.911	-21855	0	0	0
'Ti'	'solid'	11.925	-24991	-1.3376	0	1930
'Ti'	'liquid'	6.358	-22747	0	0	0
'Zr'	'solid'	10.008	-31512	-0.789	0	2125
'Zr'	'liquid'	6.806	-30295	0	0	0
'Hf'	'solid'	9.445	-32482	-0.6735	0	2500
'Hf'	'liquid'	0	0	0	0	0
'V'	'solid'	9.744	-27132	-0.5501	0	2175
'V'	'liquid'	6.929	-25011	0	0	0
'Nb'	'solid'	8.822	-37818	-0.2575	0	2741
'Nb'	'liquid'	0	0	0	0	0
'Ta'	'solid'	16.807	-41346	-3.2152	0.7437	3269
'Ta'	'liquid'	0	0	0	0	0
'Cr'	'solid'	6.8	-20733	0.4391	-0.4094	2130
'Cr'	'liquid'	0	0	0	0	0
'Mo'	'solid'	11.529	-34626	-1.1331	0	2890
'Mo'	'liquid'	0	0	0	0	0
'W'	'solid'	2.945	-44094	1.3677	0	3695
'W'	'solid2'	-54.527	-57687	-12.2231	0	0
'Mn'	'solid'	12.805	-15097	-1.7896	0	1519
'Mn'	'liquid'	0	0	0	0	0
'Re'	'solid'	11.543	-40726	-1.1629	0	3450
'Re'	'liquid'	0	0	0	0	0
'Fe'	'solid'	7.1	-21723	0.4536	-0.5846	1808
'Fe'	'liquid'	6.347	-19574	0	0	0
'Ru'	'solid'	9.755	-34154	-0.4723	0	2520
'Ru'	'liquid'	0	0	0	0	0
'Os'	'solid'	9.419	-41198	-0.3896	0	3300
'Os'	'liquid'	0	0	0	0	0
'Co'	'solid'	10.976	-22576	-1.028	0	1768
'Co'	'liquid'	6.488	-20578	0	0	0
'Rh'	'solid'	10.168	-29010	-0.7068	0	2239
'Rh'	'liquid'	6.802	-26792	0	0	0
'Ir'	'solid'	10.506	-35099	-0.75	0	2716
'Ir'	'liquid'	0	0	0	00	0
'Ni'	'solid'	10.557	-22606	-0.8717	0	1726
'Ni'	'liquid'	6.666	-20765	0	0	0
'Pd'	'solid'	9.502	-19813	-0.9258	0	1825
'Pd'	'liquid'	5.426	-17899	0	0	0
'Pt'	'solid'	4.882	-29387	1.1039	-0.4527	2045
'Pt'	'liquid'	6.386	-26856	0	0	0
'Cu'	'solid'	9.123	-17748	-0.7317	0	1358
'Cu'	'liquid'	5.849	-16415	0	0	0
'Ag'	'solid'	9.127	-14999	-0.7845	0	1234
'Ag'	'liquid'	5.752	-13827	0	0	0
'Au'	'solid'	9.52	-19343	-0.7479	0	1337
'Au'	'liquid'	5.832	-18024	0	0	0
'Zn'	'solid'	6.102	-6776	0	0	692
'Zn'	'liquid'	5.378	-6286	0	0	0
'Cd'	'solid'	5.939	-5799	0	0	594
'Cd'	'liquid'	5.242	-5392	0	0	0
'Hg'	'solid'	0	0	0	0	234
'Hg'	'liquid'	5.116	-3190	0	0	0
'Ce'	'solid'	6.139	-21752	0	0	1071
'Ce'	'liquid'	5.611	-21200	0	0	0
'Pr'	'solid'	8.859	-18720	-0.9512	0	1204
'Pr'	'liquid'	4.772	-17315	0	0	0
'Nd'	'solid'	8.996	-17264	-0.9519	0	1016
'Nd'	'liquid'	4.912	-15824	0	0	0
'Sm'	'solid'	9.6988	-11034	-1.287	0	1345
'Sm'	'liquid'	0	0	0	0	0
'Eu'	'solid'	9.24	-9459	-1.1661	0	1095
'Eu'	'liquid'	0	0	0	0	0
'Gd'	'solid'	8.344	-20861	-0.5775	0	1585
'Gd'	'liquid'	5.557	-19389	0	0	0
'Tb'	'solid'	9.51	-20457	-0.9247	0	1630
'Tb'	'liquid'	5.411	-18639	0	0	0
'Dy'	'solid'	9.579	-15336	-1.1114	0	1680
'Dy'	'liquid'	0	0	0	0	0
'Ho'	'solid'	9.785	-15899	-1.1753	0	1740
'Ho'	'liquid'	0	0	0	0	0
'Er'	'solid'	9.916	-16642	-1.2154	0	1795
'Er'	'liquid'	4.668	-14380	0	0	0
'Tm'	'solid'	8.882	-1227	-0.9564	0	1818
'Tm'	'liquid'	0	0	0	0	0
'Yb'	'solid'	9.111	-8111	-1.0849	0	1097
'Yb'	'liquid'	0	0	0	0	0
'Lu'	'solid'	8.793	-22423	-0.62	0	1936
'Lu'	'liquid'	5.648	-20302	0	0	0
'Th'	'solid'	8.668	-31483	-0.5288	0	2028
'Th'	'liquid'	-18.453	-24569	6.6473	0	0
'Pa'	'solid'	10.552	0.34869	-1.0075	0	1870
'Pa'	'liquid'	6.177	32874	0	0	0'''

young_modulus_table = '''Aluminum	10008	10008	69	69	3481	3481	24	24
	Beryllium	15954	16679	110	115	15954	15954	110	110
	Bronze	13924	17405	96	120	6505	6505	44.85	44.85
	Cadmium	7252	7252	50	50	2751	2751	18.97	18.97
	Iron (grey)	18855	18855	130	130	10008	24511	69	169
	Chromium	40466	40466	279	279	16613	16613	114.54	114.54
	Cobalt	30603	30603	211	211	10878	10878	75	75
	Copper	15954	17405	110	120	5802	6817	40	47
	Gold (24K) Pure	11385	11385	78.5	78.5	3916	3916	27	27
	Iron	30458	30458	210	210	4641	10008	32	69
	Iron (Cast)	12038	24656	83	170	10878	10878	75	75
	Iron (Wrought)	30603	30603	211	211	11893	11893	82	82
	Lead	2335	2335	16.1	16.1	1921	1921	13.248	13.248
	Magnesium	6527	6527	45	45	2392	2392	16.491	16.491
	Nickel	24656	30458	170	210	11603	11603	80	80
	Platinum	21306	21306	146.9	146.9	40030	40030	276	276
	Silver	10443	11023	72	76	4032	4032	27.8	27.8
	Steel (Carbon)	30458	30458	210	210	11168	11168	77	77
	Tin	6005	6498	41.4	44.8	2611	2611	18	18
	Titanium	17434	17434	120.2	120.2	5656	6382	39	44
	Tungsten	59611	59611	411	411	23518	23518	162.15	162.15
	Zinc	12000	12000	82.737	82.737	6105	6105	42.09	42.09'''

density_table = '''0.0899 g/L 	Hydrogen 	H 	1
0.1785 g/L 	Helium 	He 	2
0.9 g/L 	Neon 	Ne 	10
1.2506 g/L 	Nitrogen 	N 	7
1.429 g/L 	Oxygen 	O 	8
1.696 g/L 	Fluorine 	F 	9
1.7824 g/L 	Argon 	Ar 	18
3.214 g/L 	Chlorine 	Cl 	17
3.75 g/L 	Krypton 	Kr 	36
5.9 g/L 	Xenon 	Xe 	54
9.73 g/L 	Radon 	Rn 	86
0.534 g/cc 	Lithium 	Li 	3
0.862 g/cc 	Potassium 	K 	19
0.971 g/cc 	Sodium 	Na 	11
1.55 g/cc 	Calcium 	Ca 	20
1.63 g/cc 	Rubidium 	Rb 	37
1.738 g/cc 	Magnesium 	Mg 	12
1.82 g/cc 	Phosphorus 	P 	15
1.848 g/cc 	Beryllium 	Be 	4
1.873 g/cc 	Cesium 	Cs 	55
2.07 g/cc 	Sulfur 	S 	16
2.26 g/cc 	Carbon 	C 	6
2.33 g/cc 	Silicon 	Si 	14
2.34 g/cc 	Boron 	B 	5
2.54 g/cc 	Strontium 	Sr 	38
2.702 g/cc 	Aluminum 	Al 	13
2.99 g/cc 	Scandium 	Sc 	21
3.119 g/cc 	Bromine 	Br 	35
3.59 g/cc 	Barium 	Ba 	56
4.47 g/cc 	Yttrium 	Y 	39
4.54 g/cc 	Titanium 	Ti 	22
4.79 g/cc 	Selenium 	Se 	34
4.93 g/cc 	Iodine 	I 	53
5.24 g/cc 	Europium 	Eu 	63
5.323 g/cc 	Germanium 	Ge 	32
5.5 g/cc 	Radium 	Ra 	88
5.72 g/cc 	Arsenic 	As 	33
5.907 g/cc 	Gallium 	Ga 	31
6.11 g/cc 	Vanadium 	V 	23
6.15 g/cc 	Lanthanum 	La 	57
6.24 g/cc 	Tellurium 	Te 	52
6.51 g/cc 	Zirconium 	Zr 	40
6.684 g/cc 	Antimony 	Sb 	51
6.77 g/cc 	Praseodymium 	Pr 	59
6.77 g/cc 	Cerium 	Ce 	58
6.9 g/cc 	Ytterbium 	Yb 	70
7.01 g/cc 	Neodymium 	Nd 	60
7.13 g/cc 	Zinc 	Zn 	30
7.19 g/cc 	Chromium 	Cr 	24
7.3 g/cc 	Promethium 	Pm 	61
7.31 g/cc 	Indium 	In 	49
7.31 g/cc 	Tin 	Sn 	50
7.43 g/cc 	Manganese 	Mn 	25
7.52 g/cc 	Samarium 	Sm 	62
7.874 g/cc 	Iron 	Fe 	26
7.895 g/cc 	Gadolinium 	Gd 	64
8.23 g/cc 	Terbium 	Tb 	65
8.55 g/cc 	Dysprosium 	Dy 	66
8.57 g/cc 	Niobium 	Nb 	41
8.65 g/cc 	Cadmium 	Cd 	48
8.8 g/cc 	Holmium 	Ho 	67
8.9 g/cc 	Cobalt 	Co 	27
8.9 g/cc 	Nickel 	Ni 	28
8.96 g/cc 	Copper 	Cu 	29
9.07 g/cc 	Erbium 	Er 	68
9.3 g/cc 	Polonium 	Po 	84
9.32 g/cc 	Thulium 	Tm 	69
9.75 g/cc 	Bismuth 	Bi 	83
9.84 g/cc 	Lutetium 	Lu 	71
10.07 g/cc 	Actinium 	Ac 	89
10.22 g/cc 	Molybdenum 	Mo 	42
10.5 g/cc 	Silver 	Ag 	47
11.35 g/cc 	Lead 	Pb 	82
11.5 g/cc 	Technetium 	Tc 	43
11.724 g/cc 	Thorium 	Th 	90
11.85 g/cc 	Thallium 	Tl 	81
12.02 g/cc 	Palladium 	Pd 	46
12.37 g/cc 	Ruthenium 	Ru 	44
12.41 g/cc 	Rhodium\tRh\t45
13.31 g/cc 	Hafnium 	Hf 	72
13.5 g/cc 	Curium 	Cm 	96
13.546 g/cc 	Mercury 	Hg 	80
13.67 g/cc 	Americium 	Am 	95
14.78 g/cc 	Berkelium 	Bk 	97
15.1 g/cc 	Californium 	Cf 	98
15.4 g/cc 	Protactinium 	Pa 	91
16.65 g/cc 	Tantalum 	Ta 	73
18.95 g/cc 	Uranium 	U 	92
19.32 g/cc 	Gold 	Au 	79
19.35 g/cc 	Tungsten 	W 	74
19.84 g/cc 	Plutonium 	Pu 	94
20.2 g/cc 	Neptunium 	Np 	93
21.04 g/cc 	Rhenium 	Re 	75
21.45 g/cc 	Platinum 	Pt 	78
22.4 g/cc 	Iridium 	Ir 	77
22.6 g/cc 	Osmium 	Os 	76'''

molar_mass_table = '''1.0079 	Hydrogen 	H 	1
4.0026 	Helium 	He 	2
6.941 	Lithium 	Li 	3
9.0122 	Beryllium 	Be 	4
10.811 	Boron 	B 	5
12.0107 	Carbon 	C 	6
14.0067 	Nitrogen 	N 	7
15.9994 	Oxygen 	O 	8
18.9984 	Fluorine 	F 	9
20.1797 	Neon 	Ne 	10
22.9897 	Sodium 	Na 	11
24.305 	Magnesium 	Mg 	12
26.9815 	Aluminum 	Al 	13
28.0855 	Silicon 	Si 	14
30.9738 	Phosphorus 	P 	15
32.065 	Sulfur 	S 	16
35.453 	Chlorine 	Cl 	17
39.0983 	Potassium 	K 	19
39.948 	Argon 	Ar 	18
40.078 	Calcium 	Ca 	20
44.9559 	Scandium 	Sc 	21
47.867 	Titanium 	Ti 	22
50.9415 	Vanadium 	V 	23
51.9961 	Chromium 	Cr 	24
54.938 	Manganese 	Mn 	25
55.845 	Iron 	Fe 	26
58.6934 	Nickel 	Ni 	28
58.9332 	Cobalt 	Co 	27
63.546 	Copper 	Cu 	29
65.39 	Zinc 	Zn 	30
69.723 	Gallium 	Ga 	31
72.64 	Germanium 	Ge 	32
74.9216 	Arsenic 	As 	33
78.96 	Selenium 	Se 	34
	79.904 	Bromine 	Br 	35
83.8 	Krypton 	Kr 	36
85.4678 	Rubidium 	Rb 	37
87.62 	Strontium 	Sr 	38
88.9059 	Yttrium 	Y 	39
91.224 	Zirconium 	Zr 	40
92.9064 	Niobium 	Nb 	41
95.94 	Molybdenum 	Mo 	42
98 	Technetium 	Tc 	43
101.07 	Ruthenium 	Ru 	44
102.9055 	Rhodium 	Rh 	45
106.42 	Palladium 	Pd 	46
107.8682 	Silver 	Ag 	47
112.411 	Cadmium 	Cd 	48
114.818 	Indium 	In 	49
118.71 	Tin 	Sn 	50
121.76 	Antimony 	Sb 	51
126.9045 	Iodine 	I 	53
127.6 	Tellurium 	Te 	52
131.293 	Xenon 	Xe 	54
132.9055 	Cesium 	Cs 	55
	137.327 	Barium 	Ba 	56
	138.9055 	Lanthanum 	La 	57
	140.116 	Cerium 	Ce 	58
	140.9077 	Praseodymium 	Pr 	59
	144.24 	Neodymium 	Nd 	60
	145 	Promethium 	Pm 	61
	150.36 	Samarium 	Sm 	62
	151.964 	Europium 	Eu 	63
	157.25 	Gadolinium 	Gd 	64
	158.9253 	Terbium 	Tb 	65
	162.5 	Dysprosium 	Dy 	66
	164.9303 	Holmium 	Ho 	67
	167.259 	Erbium 	Er 	68
	168.9342 	Thulium 	Tm 	69
	173.04 	Ytterbium 	Yb 	70
	174.967 	Lutetium 	Lu 	71
	178.49 	Hafnium 	Hf 	72
	180.9479 	Tantalum 	Ta 	73
	183.84 	Tungsten 	W 	74
	186.207 	Rhenium 	Re 	75
	190.23 	Osmium 	Os 	76
	192.217 	Iridium 	Ir 	77
	195.078 	Platinum 	Pt 	78
	196.9665 	Gold 	Au 	79
	200.59 	Mercury 	Hg 	80
	204.3833 	Thallium 	Tl 	81
	207.2 	Lead 	Pb 	82
	208.9804 	Bismuth 	Bi 	83
	209 	Polonium 	Po 	84
	210 	Astatine 	At 	85
	222 	Radon 	Rn 	86
	223 	Francium 	Fr 	87
	226 	Radium 	Ra 	88
	227 	Actinium 	Ac 	89
	231.0359 	Protactinium 	Pa 	91
	232.0381 	Thorium 	Th 	90
	237 	Neptunium 	Np 	93
	238.0289 	Uranium 	U 	92
	243 	Americium 	Am 	95
	244 	Plutonium 	Pu 	94
	247 	Curium 	Cm 	96
	247 	Berkelium 	Bk 	97
	251 	Californium 	Cf 	98
	252 	Einsteinium 	Es 	99
	257 	Fermium 	Fm 	100
	258 	Mendelevium 	Md 	101
	259 	Nobelium 	No 	102
	261 	Rutherfordium 	Rf 	104
	262 	Lawrencium 	Lr 	103
	262 	Dubnium 	Db 	105
	264 	Bohrium 	Bh 	107
	266 	Seaborgium 	Sg 	106
	268 	Meitnerium 	Mt 	109
	272 	Roentgenium 	Rg 	111
	277 	Hassium 	Hs 	108
	'''

letters = 'qwertyuiopasdfghjklzxcvbnm'

k = 1.38 * 10**-23
F = 0.9107
Na = 6.022 * 10**23



T_room = 300
P = 101 * 10**3



def complete_str(inp, l):
    return ' ' * (l - len(str(inp))) + str(inp)

def leave_letters(inp):
    out = ''

    for char in inp:
        if(char in letters):
            out += char

    return out

def show_metals(metals):
    print('------ Metals full data   ------')
    print(complete_str('index', 8), end='')
    print(complete_str('density', 16), end='')
    print(complete_str('young`s modulus', 21), end='')
    print(complete_str('A', 16), end='')
    print(complete_str('B', 16), end='')
    print(complete_str('C', 16), end='')
    print(complete_str('D', 16), end='')
    print(complete_str('number', 16), end='')
    print(complete_str('molar mass', 16), end='')
    print(complete_str('t_melt', 12), end='')
    print()

    for m in metals:
        m.show_compact()

    print()
    print()

def calculate_energy(metals):
    print('------ Metals surface energy density data   ------')
    print(complete_str('index', 8), end='')
    print(complete_str('t_melt', 12), end='')
    print(complete_str('T used', 12), end='')
    print(complete_str('saturated vapor pressure', 32), end='')
    print(complete_str('surface energy density', 32))
        
    for m in metals:
        m.calc_coeffs()
        m.calc_energydensity()

        m.show_compact_energydensity()

def show_scheme(metals):
    dct = {}
    for m in metals:
        dct[m.index] = m.energydensity
    lst = [(k, dct[k]) for k in sorted(dct, key=dct.get, reverse=True)]
    
    indecies = []
    edensities = []
    for elm in lst:
        indecies.append(elm[0][0].upper() + elm[0][1:])
        edensities.append(elm[1])

    y_pos = numpy.arange(len(indecies))

    plt.bar(y_pos, edensities, align='center', color='#f7c500')
    plt.xticks(y_pos, indecies)
    plt.ylabel('energy density')
    plt.xlabel('metal')
    plt.title('Surface energy density\nof metals` saturation vapors')
    plt.yscale('log')
    plt.show()



class Metal_a:
    def __init__(self, description):
        lst = description.lower().split('\t')
        
        self.index = lst[0].strip("'")
        self.state = lst[1].strip("'").replace('liquid', 'L').replace('solid', 'S')
        self.A = float(lst[2])
        self.B = float(lst[3])
        self.C = float(lst[4])
        self.D = float(lst[5])
        self.T_melt = float(lst[6])

        self.show_compact()

    def show_compact(self):
        print(complete_str(self.index, 2), end='')
        print(complete_str(self.state, 7),  end='')
        print(complete_str(self.A, 12), end='')
        print(complete_str(self.B, 12), end='')
        print(complete_str(self.C, 12), end='')
        print(complete_str(self.D, 12), end='')
        print(complete_str(self.T_melt, 12), end='')
        print()

    def is_solid(self):
        return (self.state == 'S') and (self.T_melt > T_room)

class Metal_b:
    def __init__(self, description):
        description = description.lower().strip('\t')
        lst = description.split('\t')

        self.name = lst[0].split(' ')[0]
        self.young_modulus = float(lst[4])

        self.show_compact()

    def show_compact(self):
        print(complete_str(self.name, 24), end='')
        print(complete_str(self.young_modulus, 12), end='')
        print()

class Metal_c():
    def __init__(self, description):
        description = description.lower().strip('\t')
        
        lst = description.split('\t')

        self.name = leave_letters(lst[1])
        self.index = leave_letters(lst[2])
        self.density = float(lst[0].split(' ')[0])
        self.number = int(lst[3])

        if(lst[0].split(' ')[1] == 'g/cc'):
            self.density *= 1000

        self.show_compact()

    def show_compact(self):
        print(complete_str(self.index, 2), end='')
        print(complete_str(self.name, 24), end='')
        print(complete_str(self.density, 12), end='')
        print()

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

class Metal:
    def __init__(self, index):
        self.index = index
        
        self.density =         None
        self.young_modulus =   None
        self.A =               None
        self.B =               None
        self.C =               None
        self.D =               None
        self.number =          None
        self.t_melt =          None

    def show_compact(self):
        print(complete_str(self.index[0].upper() + self.index[1:], 8), end='')
        print(complete_str(self.density, 16), end='')
        print(complete_str(self.young_modulus, 21), end='')
        print(complete_str(self.A, 16), end='')
        print(complete_str(self.B, 16), end='')
        print(complete_str(self.C, 16), end='')
        print(complete_str(self.D, 16), end='')
        print(complete_str(self.number, 16), end='')
        print(complete_str(mass_dict[self.number], 16), end='')
        print(complete_str(self.t_melt, 12), end='')
        print()

    def show_compact_energydensity(self):
        print(complete_str(self.index[0].upper() + self.index[1:], 8), end='')
        print(complete_str(round(self.t_melt), 12), end='')
        print(complete_str(round(self.t_used), 12), end='')
        print(complete_str(self.vapor_pressure, 32), end='')
        print(complete_str(self.energydensity, 32))
              
    def is_full(self):
        if(self.index == None):
            return False
        if(self.density == None):
            return False
        if(self.young_modulus == None):
            return False
        if(self.A == None):
            return False
        if(self.B == None):
            return False
        if(self.C == None):
            return False
        if(self.D == None):
            return False
        if(self.number == None):
            return False
        if(self.t_melt == None):
            return False

        return True

    def calc_coeffs(self):
        self.alpha = pi / 5 * self.young_modulus / 72 * (mass_dict[self.number] / Na / self.density)**(13/3)
        self.beta =  pi / 2 * self.young_modulus / 36 * (mass_dict[self.number] / Na / self.density)**(7/3)

        self.t_used = self.t_melt * 0.95
        self.vapor_pressure = exp((log(10) * (5.006 + self.A + self.B / self.t_used + self.C * log(self.t_used)/log(10) + self.D * power(self.t_used, -3))))

    def calc_energydensity(self):
        self.energydensity = 2 * F / (3 * sqrt(pi)) * (self.beta**4 / self.alpha)**(1/6) * self.vapor_pressure / sqrt(k * self.t_used)
        
        return self.energydensity



mass_dict = {}
for line in molar_mass_table.split('\n'):
    try:
        line = line.replace(' ', '\t')
        while('\t\t' in line):
            line = line.replace('\t\t', '\t')
        line = line.strip('\t')
        lst = line.split('\t')

        mass = float(lst[0])
        number = int(lst[3])
        mass_dict[number] = mass
    except Exception:
        pass

print('------   Saturated vapor data   ------')
sv_inplist = saturated_vapor_table.split('\n')
metal_a_list = list(map(lambda a: Metal_a(a), sv_inplist))
solid_malist = filter(lambda m: m.is_solid(), metal_a_list)
print()
print()

print('------   Young`s modulus data   ------')
younglist = young_modulus_table.split('\n')
metal_b_list = list(map(lambda a: Metal_b(a), younglist))
metal_b_list.append(Metal_b('Osmium\t\t\t\t550'))
print()
print()

print('------   Density data   ------')
densitylist = density_table.split('\n')
metal_c_list = list(map(lambda a: Metal_c(a), densitylist))
print()
print()

mendeleev_table = {}
indexlist = []
for m in metal_c_list:
    name = m.get_name()

    if(name not in mendeleev_table):
        mendeleev_table[name] = m.get_index()
        indexlist.append(m.get_index())

metals = []
for index in indexlist:
    m = Metal(index)

    for mc in metal_c_list:
        if(mc.index == index):
            m.density = mc.density
            m.number = mc.number
            break

    for mb in metal_b_list:
        try:
            if(mendeleev_table[mb.name] == index):
                if((m.young_modulus == None) or (mb.young_modulus > m.young_modulus)):
                    m.young_modulus = mb.young_modulus
        except Exception:
            pass

    for ma in metal_a_list:
        if(ma.index == index):
            if((m.t_melt == None) or (ma.T_melt > m.t_melt)):
                m.t_melt = ma.T_melt

                m.A = ma.A
                m.B = ma.B
                m.C = ma.C
                m.D = ma.D

    if(m.is_full()):
        metals.append(m)

show_metals(metals)

calculate_energy(metals)

show_scheme(metals)
