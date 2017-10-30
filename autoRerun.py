
import h5py
import os
import os.path


inFile='tests_single_new.h5'
mylist = inFile
delimiter = ''
filepath = delimiter.join(mylist)

variable = ['PVz','PVy','PVx','PPress','Prho']
H5File = h5py.File(filepath,'r+')
Fields = H5File.get('Fields').values()

def get_timestepstr(dset):

    return os.path.split(dset.name)[1]

def get_LatestTime(Fields):

    maxtstep = 0

    for grp in Fields:
        dsets = grp.values()

        for dset in dsets:
            dTimestep = int(get_timestepstr(dset))
            if dTimestep > maxtstep:
                maxtstep = dTimestep

    return maxtstep

timestep = get_LatestTime(Fields)

#line 36 change boolen rerun
f = open('parameter_2D.d', 'r')
lines = f.readlines()
lines[36-1] = '.false.\n'
f.close()

f = open('parameter_2D.d', 'w')
f.writelines(lines)
f.close()

#line 38 change timestep
f = open('parameter_2D.d', 'r')
lines = f.readlines()
lines[38-1] = str(timestep)+'\n'
f.close()

f = open('parameter_2D.d', 'w')
f.writelines(lines)
f.close()


H5File.close()
