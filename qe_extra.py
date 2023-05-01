import os

def printheader(self):
    self.write("""&CONTROL
  calculation = 'vc-relax',
  restart_mode = 'from_scratch',
  prefix = 'NAME',
  verbosity = 'high',
  etot_conv_thr = 2.0D-6,
  forc_conv_thr = 6.0D-4,
  nstep = 250,
/
&SYSTEM
  ibrav = 14,
  ntyp = 7,
""")

def print_second(self):
     self.write("""
  ecutwfc = 50.000000,
  ecutrho = 550.000000,
  vdw_corr = 'XDM',
  xdm_a1 = 0.6512,
  xdm_a2 = 1.4633,
/
&ELECTRONS
  electron_maxstep = 1500,
  conv_thr = 1.D-8,
  scf_must_converge = .TRUE.,
  mixing_beta = 0.5D0,
/
&IONS
  ion_dynamics = 'bfgs',
/
&CELL
  cell_dynamics = 'bfgs',
/
ATOMIC_SPECIES
 H 1.00 H.b86bpbe.UPF
 C 12.0 C.b86bpbe.UPF
 O 16.0 O.b86bpbe.UPF
 N 14.0 N.b86bpbe.UPF
 S 32.0 S.b86bpbe.UPF
 Cl 35.0 Cl.b86bpbe.UPF
 F 19.0 N.b86bpbe.UPF

K_POINTS automatic
""")

def lines_that_contain(string, fp):
         return [line for line in fp if string in line]

def findvalue(self,name):
     with open(self,"r+") as f:
        for line in lines_that_contain(name,f):
            line = line.split()
            final = line[1]
            return final
        
def grab_variables(self):
    a = float(findvalue(self,"_cell_length_a"))
    b = float(findvalue(self,"_cell_length_b")) 
    c = float(findvalue(self,"_cell_length_c"))
    alpha = float(findvalue(self,"_cell_angle_alpha"))
    beta = float(findvalue(self,"_cell_angle_beta"))
    gamma = float(findvalue(self,"_cell_angle_gamma"))
    return a,b,c,alpha,beta,gamma 
