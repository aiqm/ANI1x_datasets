import dataloader as dl

# Path to the ANI-1x data set
path_to_h5file = '/home/jujuman/Scratch/Research/ANI-1x1ccx/FINAL_CLEANED_DATA/ani1x-20190925_rz.h5'

# List of keys to point to requested data
data_keys = ['wb97x_dz.energy','wb97x_dz.forces'] # Original ANI-1x data (https://doi.org/10.1063/1.5023802)
#data_keys = ['wb97x_tz.energy','wb97x_tz.forces'] # CHNO portion of the data set used in AIM-Net (https://doi.org/10.1126/sciadv.aav6490)
#data_keys = ['ccsd(t)_cbs.energy'] # The coupled cluster ANI-1ccx data set (https://doi.org/10.1038/s41467-019-10827-4)
#data_keys = ['wb97x_dz.dipoles'] # A subset of this data was used for training the ACA charge model (https://doi.org/10.1021/acs.jpclett.8b01939)


# Example for extracting DFT/DZ energies and forces
for data in dl.iter_data_buckets(path_to_h5file,keys=data_keys):
    X = data['coordinates']
    Z = data['atomic_numbers']
    E = data['wb97x_dz.energy']
    F = data['wb97x_dz.forces']
