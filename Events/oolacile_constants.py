import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Solaire = 6000
    Logan = 6030
    Quelana = 6170
    Siegmeyer = 6280
    Patches = 6320
    Havel = 6580
    Ornstein = 6998
    Sif = 6999
    BlackEyeGough = 1210100
    BlackKnightSword = 1210101
    BlackKnightGreatsword = 1210102
    BlackKnightAxe = 1210103
    BlackKnightHalberd = 1210104
    BlackKnightPool = 1210105
    FramptBoss = 1210401
    FramptSwoop = 1210402


class FLAG(dt.Flag):
    AlliesKilled = 1910
    PatchesDead = 1911
    KalameetShotDown = 11210535

    BattleStarted = 11212001


class TEXT(dt.Text):
    GoughName = 4110
    FramptName = 4510
    LegionName = 2790
    PatchesName = 6320

    RingBurns = 10010380
    HollowVictory = 10010384


class ITEMLOT(dt.ItemLot):
    SerpentSoul = 4700


class SPEFFECT(dt.IntEnum):
    RingOfStJude = 4750
    RingOfStJudeAlly = 4751
    RingOfStJudeStrong1 = 4752
    RingOfStJudeStrong2 = 4753
    RingOfStJudeStrong3 = 4754
    RingOfStJudeStrong4 = 4755
    RingOfStJudeStrong5 = 4756
    PatchesBuff = 4761

