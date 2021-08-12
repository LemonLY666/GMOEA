from GMOEA import *
from global_parameter import *
from IMMOEA_pro import *
from EAreal import *


if __name__ == '__main__':

    gp = GlobalParameter(operator=ea_real, pro=IMMOEA_F1, run=1)
    gmoea = GMOEA(gp=gp)

    gmoea.run()