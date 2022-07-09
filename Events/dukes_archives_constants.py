import soulstruct.emevd.ds_types as dt


"""
Mimics info:
    - They have special effect 5421 when they are closed and waiting to eat you.
    - Warp player to Mimic model point 100 and force animation 7521.
    - Issue Mimic AI command 10 (slot 0), replan, wait 0.1 seconds, and revert to command -1 (slot 0).
    - This should work if the Mimic is hostile to whoever is opening it.
    - Make Mimic invincible so it can't be disturbed. 
"""

"""
Looter positions:
    1. Patrols on ground floor of first room. Mimic is next to rotating stairs pillar.
    2. Patrols on ground floor of second room. Chest is somewhere.
    3. Patrols on upper floors of first room. Chest is at one end.
    4. Patrols on upper floors of second room. Chest is at one end.
    5. Patrols along route to prison. Mimic is in the little room in the middle.
    6. Patrols in dark part near stairs to exterior. Chest is in the dark room.
"""


class CHR(dt.Character):
    Logan = 6030
    LoganTalk = 6032
    Havel = 6580
    NakedHavel = 6581
    Crow = 1700675

    Looter1 = 1700600
    Looter2 = 1700601
    Looter3 = 1700602
    Looter4 = 1700603
    Looter5 = 1700604
    Looter6 = 1700605

    LoganMimic1 = 1700410
    LoganMimic2 = 1700411
    LoganMimic3 = 1700412
    LoganMimic4 = 1700413
    LoganMimic5 = 1700414
    LoganMimic6 = 1700415

    HungryMimic1 = 1700400
    HungryMimic2 = 1700401
    HungryMimic3 = 1700402
    HungryMimic4 = 1700403
    HungryMimic5 = 1700404
    HungryMimic6 = 1700405


class FLAG(dt.Flag):
    LoganRecruited = 1904
    HavelRecruited = 1905

    MimicRingGiven = 11702003
    HavelGearReturned = 11702007
    PisacasAllDead = 11702005
    GiantCellOpened = 11700320
    GiantCellIsOpen = 61700320

    Mimic1Fed = 11702020
    Mimic2Fed = 11702021
    Mimic3Fed = 11702022
    Mimic4Fed = 11702023
    Mimic5Fed = 11702024
    Mimic6Fed = 11702025


class OBJECT(dt.Object):
    Chest1 = 1701650
    Chest2 = 1701651
    Chest3 = 1701652
    Chest4 = 1701653
    Chest5 = 1701654
    Chest6 = 1701655

    GiantCellDoor = 1701506


class WEAPON(dt.Weapon):
    DragonTooth = 854000
    HavelsGreatshield = 1505000


class ARMOR(dt.Armor):
    HavelsHelm = 440000
    HavelsArmor = 441000
    HavelsGauntlets = 442000
    HavelsLeggings = 443000


class ITEMLOT(dt.ItemLot):
    MimicRing = 4620


class REGION(dt.Region):
    Mimic1 = 1702740
    Mimic2 = 1702741
    Mimic3 = 1702742
    Mimic4 = 1702743
    Mimic5 = 1702744
    Mimic6 = 1702745


class TEXT(dt.Text):
    ReturnToFirelink = 10010140
    Talk = 10010200
    SummonMimic = 10010350
    MimicSatiated = 10010351
    LoganInstructions = 10010352
    ReturnHavelGear = 10010353
    MissingHavelGear = 10010354
    Caught = 10010355


class SPEFFECT(dt.IntEnum):
    MimicRing = 4706
    MimicRingStealth = 4707
    HavelHealth = 4716
    LoganReward = 4804
    HavelReward = 4805
