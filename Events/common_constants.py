import soulstruct.emevd.ds_types as dt


class FLAG(dt.Flag):
    BoulderLauncherNotPointingDownOutsideRamp = 11500803  # This flag is fully logically negated.
    BoulderLauncherPointingOutside = 11500812


class SPEFFECT(dt.IntEnum):
    SerpentSoulEaten = 4760
