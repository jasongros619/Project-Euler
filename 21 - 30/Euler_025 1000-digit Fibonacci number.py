import time
start=time.clock()

import math
phi=math.sqrt(5)/2+0.5 #1.618...

#F_n = phi^n / sqrt(5)
#solving for n,
#n = log_phi_( 10^999 * sqrt( 5 ) )
#n = 999 * log_phi_( 10 ) + 0.5 * log_phi_( 5 )
n = 999 * math.log(10, phi) + 0.5 * math.log(5, phi)

print(math.ceil(n),(time.clock()-start)*1000,"ms")
