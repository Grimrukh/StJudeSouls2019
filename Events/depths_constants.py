import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Quelana = 6170

    Butcher1 = 1000450
    Butcher2 = 1000451
    Butcher3 = 1000452

    HeadStoneDrake = 1000400
    TorsoStoneDrake = 1000401
    BesiegedDragon = 1000800
    BesiegedDragonTail = 1000801
    SilverKnightSword1 = 1000810
    SilverKnightSword2 = 1000811
    SilverKnightSpear1 = 1000812
    SilverKnightSpear2 = 1000813
    Artorias = 1000820


class FLAG(dt.Flag):
    QuelanaRecruited = 1906

    BesiegedDragonKilledOnce = 11000001
    WhisperingRingReceived = 11002000
    HeadStoneObtained = 11002001
    TorsoStoneObtained = 11002002
    ArtoriasDead = 11002003

    BossFogEntered = 11005393


class REGION(dt.Region):
    QuelanaAppearanceTrigger = 1002460  # Just before arena entrance.
    QuelanaAppearanceFirestorm = 1002461
    QuelanaRewardTrigger = 1002470  # Inside arena, near fog.
    QuelanaRewardFirestorm = 1002471
    BesiegedDragonArena = 1002999

    ButcherTrigger1 = 1002450
    ButcherTrigger2 = 1002451
    ButcherTrigger3 = 1002452

    ReturnToFirelink = 1002675


class TEXT(dt.Text):
    ReturnToFirelink = 10010140
    Talk = 10010200
    Listen = 10010201
    CycleOfTormentContinues = 10010152
    BesiegedDragonName = 5260
    ArtoriasName = 4100


class ITEMLOT(dt.ItemLot):
    QuelanaGift = 4530  # Whispering Dragon Ring
    HeadStoneDrakeGift = 4540  # Dragon Head Stone
    TorsoStoneDrakeGift = 4550  # Dragon Torso Stone


class SPEFFECT(dt.IntEnum):
    WhisperingRing = 4705
    DragonTransformation = 1530
    DragonBreath = 4726
    QuelanaSoulReward = 4806


class FX(dt.IntEnum):
    FirestormPillar = 20160
