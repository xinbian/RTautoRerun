#this code delete some fields from hdf5 file
#this can be used to delete "blow up results"

import h5py
import os
import os.path

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath,os.pardir))
parentDir = os.path.abspath(os.path.join(curDir,os.pardir)) 

inFile='tests_single_new.h5'
mylist = [parentDir,'/',inFile]
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
f = open('parameter.d', 'r')
lines = f.readlines()
lines[36-1] = False
f.close()

f = open('parameter.d', 'w')
lines = f.writelines()
f.close()

#line 38 change timestep
f = open('parameter.d', 'r')
lines = f.readlines()
lines[38-1] = timestep
f.close()

f = open('parameter.d', 'w')
lines = f.writelines()
f.close()


H5File.close()
