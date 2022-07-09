import random
from soulstruct.emevd.pydses import shift


""" 
First two rows are each seven Undead Soldiers (alternating sword and spear).
Third row is seven Balder Knights (alternating shield and rapier).
Fourth row is Undead Soldiers mixed with two Berenike Knights.
Fifth row is seven Undead Soldiers again.

"""


PLAYER_SPAWN = (808.09, 750.98)
ALLY_GAP = 2.5

ANGLE = 160
FRONT_CENTER = (811.62, 717.02)
GAP_WITHIN = 3.5
GAP_BETWEEN = 4.5
NOISE_RANGE = (0, 1.15)


if __name__ == '__main__':

    ally_positions = []
    for i in [-4, -3, -2, 4, 3, 2, 1, -1]:
        ally_positions.append(shift(random.uniform(0, 1.15), i * ALLY_GAP + random.uniform(0, 1.15),
                                    origin=PLAYER_SPAWN, rotation=-5))

    print('ALLY POSITIONS:')
    [print(f'{p[0]:.2f}\t-371.5\t{p[1]:.2f}') for p in ally_positions]

    print()

    positions = []
    ids = []
    entity_id = 1210000
    for j in range(2, -6, -1):  # Eight rows
        for i in range(-3, 4):
            positions.append(shift(j * GAP_BETWEEN + random.uniform(*NOISE_RANGE),
                                   i * GAP_WITHIN + random.uniform(*NOISE_RANGE),
                                   origin=FRONT_CENTER, rotation=ANGLE))
            ids.append(entity_id)
            entity_id += 1

    [print(f'{p[0]:.2f}\t-371.5\t{p[1]:.2f}') for p in positions]
    # [print(e) for e in ids]
