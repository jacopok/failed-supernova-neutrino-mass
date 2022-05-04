from gw_mock import read_file_and_resample, make_wavable
from scipy.io.wavfile import write
import astropy.units as u

filenames = [
    's10.0.swbj15.horo.3d.gw.dat',
    's15.0.swbj16.horo.3d.gw.dat',
    's11.0.swbj15.horo.3d.gw.dat',
    's19.0.swbj15.horo.3d.gw.dat',
    's12.0.swbj15.horo.3d.gw.dat',
    's25.0.swh18.horo.3d.gw.dat',
    's13.0.swbj15.horo.3d.gw.dat',
    's60.0.swbj15.horo.3d.gw.dat',
    's14.0.swbj16.horo.3d.gw.dat',
    's9.0.swbj15.horo.3d.gw.dat',
]

for filename in filenames:
    srate = 2**18
    time, hplus = read_file_and_resample('GW_strains/'+filename, srate, 10 *u.kpc) 
    mass_str = filename.split('.0.')[0][1:]
    
    write(f'sounds/signal_{mass_str}.wav', srate, make_wavable(hplus))