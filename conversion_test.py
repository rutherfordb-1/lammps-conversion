import mbuild as m
import foyer as fo
cer_ns = m.load("ucer2.mol2")
water = m.load("SOL.mol2")
for particle in cer_ns.particles():
    particle.name = "_"+particle.name
for particle in water.particles():
    particle.name = "_"+particle.name
ff = fo.Forcefield(forcefield_files="foyer_charmm.xml")
bilayer = ff.apply(cer_ns,assert_dihedral_params=False)
sol = ff.apply(water,assert_dihedral_params=False)
