import soulstruct.emevd.ds_types as dt


class FLAG(dt.Flag):
    SolaireCellOpen = 11810102
    SiegmeyerCellOpen = 11810101
    PatchesCellOpen = 11810100


class CHR(dt.Character):
    Solaire = 6005
    Siegmeyer = 6285
    Patches = 6325
    Frampt = 1810800


class SPEFFECT(dt.IntEnum):
    OpenChurchDoor = 4709
