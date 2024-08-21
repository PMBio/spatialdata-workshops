# ##
# from spatialdata_io import visium
# sdata = visium('data/visium_2.1.0_2_io_subset')
# sdata.write('data/visium_2.1.0_2_io_subset.zarr', overwrite=True)
#
# ##
# from spatialdata_io import xenium
# sdata = xenium('data/xenium_2.0.0_io_subset')
# sdata.write('data/xenium_2.0.0_io_subset.zarr', overwrite=True)
#
# ##
# from spatialdata_io import visium_hd
# sdata = visium_hd('data/visium_hd_3.0.0_io_subset')
# sdata.write('data/visium_hd_3.0.0_io_subset.zarr', overwrite=True)

##
# print(sdata)
from napari_spatialdata import Interactive
import spatialdata as sd
sdata = sd.read_zarr("data/visium_2.1.0_2_io_subset.zarr")
Interactive(sdata)
