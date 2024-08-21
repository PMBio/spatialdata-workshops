##
# this script has been used to keep only the metadata from the "slice file" of the Visium HD datset
import h5py

f = 'Visium_HD_Mouse_Small_Intestine_feature_slice.h5 old'

with h5py.File(f, 'r') as infile:
    with h5py.File('Visium_HD_Mouse_Small_Intestine_feature_slice.h5', 'w') as outfile:
        for k in dict(infile.attrs).keys():
            outfile.attrs[k] = infile.attrs[k]