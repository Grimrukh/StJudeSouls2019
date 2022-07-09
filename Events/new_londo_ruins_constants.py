import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Rickert = 6220
    Sif = 1600452
    MaleGhost1 = 1600200
    MaleGhost2 = 1600201
    MaleGhost3 = 1600301
    MaleGhost4 = 1600302
    FemaleGhost = 1600300


class SPEFFECT(dt.IntEnum):
    RingOfTheAlpha = 4704
    SifReward = 4807


class FLAG(dt.Flag):
    SifRecruited = 1907


class TEXT(dt.Text):
    ExtendHand = 10010360
    SifAccepts = 10010361
    SifRejects = 10010362
