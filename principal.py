import orbit_cy
import orbit_py
import time

ini_time = time.time()


planet = orbit_cy.Planet()
orbit_cy.step_time_cy(planet,1,1000000)

fin_time = time.time()


time_cython = fin_time-ini_time


ini_time = time.time()

planet = orbit_py.Planet()
orbit_py.step_time_py(planet,1,1000000)

fin_time = time.time()

time_python = fin_time-ini_time

print("Cython Time: ",time_cython)
print("Python Time: ",time_python)

print("Cython es: ",time_cython/time_python," mas rapido")