import os
from soulstruct import DCX
from soulstruct.emevd import *


DSR_EMEVD_DIRECTORY = 'G:/Steam/steamapps/common/DARK SOULS REMASTERED/event'


def compile_emevd():

    print('\nCompiling EMEVD...\n')

    for game_map in [COMMON, DEPTHS, UNDEAD_BURG, FIRELINK_SHRINE, OOLACILE, CATACOMBS, SENS_FORTRESS,
                     ANOR_LONDO, NEW_LONDO_RUINS, DUKES_ARCHIVES, UNDEAD_ASYLUM]:
        try:
            emevd_name = game_map.file_name
        except AttributeError:
            emevd_name = game_map

        evs_path = os.path.join(os.path.dirname(__file__), emevd_name + '.evs')
        emevd_path = os.path.join(DSR_EMEVD_DIRECTORY, emevd_name + '.emevd.dcx')

        emevd = EMEVD(evs_path)
        emevd.write_numeric(os.path.join('built_numeric', emevd_name + '.numeric.txt'))
        emevd.write_verbose(os.path.join('built_verbose', emevd_name + '.verbose.txt'))
        emevd_dcx = DCX(emevd.pack())
        emevd_dcx.write(emevd_path)

        print(f'Compiled {emevd_name}.')

    print('\nAll EMEVD compiled.')


if __name__ == '__main__':
    compile_emevd()
