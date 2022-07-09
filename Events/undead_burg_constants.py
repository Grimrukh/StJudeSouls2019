import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Solaire = 6000
    UndeadMerchant = 6230
    Hellkite = 1010300
    HellkiteTail = 1010301
    HellkiteFirstEncounter = 1010302
    TaurusDemon = 1010700
    CapraDemon = 1010750
    ACOG = 6190  # Andre
    Soy = 6010  # Darkmoon Knightess
    Lan = 6300  # Lautrec
    Lobrocop = 6370  # Oswald
    LobrocopHollow1 = 1010400
    LobrocopHollow2 = 1010401
    LobrocopHollow3 = 1010402
    LobrocopHollow4 = 1010403
    LobrocopHollow5 = 1010404
    LobrocopHollow6 = 1010405
    LobrocopHollow7 = 1010406


class FLAG(dt.Flag):
    SolaireRecruited = 1900
    UndeadMerchantDead = 11012002
    LanHostile = 11012003
    LanDead = 11012004
    SoyHostile = 11012005
    SoyDead = 11012006
    LobrocopDead = 11012007
    ACOGDead = 11012010

    SoyChestOpened = 11010650
    LanChestOpened = 11010651
    LobrocopTrigger = 51010510  # Corpse in barrel in Lower Burg house.

    TaurusDemonDead = 11010901
    CapraDemonDead = 11010902

    HellkiteFirstEncounterDone = 11010790
    HellkiteBridgeSwoopDone = 11010791
    HellkiteIsFrustrated = 11015305
    HellkiteFrustrationTimerOn = 11015306
    HellkiteBridgeAttackTriggered = 11015310
    HellkiteDownOnBridge = 11015311
    HellkiteAttacked = 11015317
    HellkiteDead = 11010900


class GOOD(dt.Good):
    LansKey = 2021  # Formerly Residence Key.
    LowerBurgKey = 2017  # Formerly Mystery Key.
    SoysKey = 2001  # Formerly Basement Key.
    LobrocopsKey = 2014  # Formerly Key to the Depths.
    WatchtowerKey = 2019
    RemoteFirebomb = 298
    RemoteDetonator = 299


class ARMOR(dt.Armor):
    HavelsHelm = 440000
    HavelsArmor = 441000
    HavelsGauntlets = 442000
    HavelsLeggings = 443000


class WEAPON(dt.Weapon):
    HavelsGreatshield = 1505000


class ITEMLOT(dt.ItemLot):
    HellkiteWyvernGift = 4630
    UndeadMerchantDrop = 25100100  # Havel's Shield.
    LanDrop = 6300  # Watchtower Basement Key and Undercity Key.
    SoyDrop = 6010  # Fire Keeper Soyl.
    LobrocopDrop = 6370  # Key to Lobos' Lair.
    ACOGDrop = 26400000  # Havel's Leggings and clarinet guide.


class SPEFFECT(dt.IntEnum):
    SolaireReward = 4800
    SuperFast = 4702
    UsedRemoteDetonator = 4703
    WhisperingDragonRing = 4705
    HavelHelmEquipped = 4710
    HavelArmorEquipped = 4711
    HavelGauntletsEquipped = 4712
    HavelLeggingsEquipped = 4713
    HavelShieldEquipped = 4714
    HavelFireproof = 4715


class FX(dt.IntEnum):
    RemoteFirebombExplosion = 20286


class TEXT(dt.Text):
    Listen = 10010201
    Rescue = 10010153
    ReturnToFirelink = 10010140
    UndercityKeyUsed = 10010876
    LansKeyUsed = 10010881
    SoysKeyUsed = 10010860
    LobosKeyUsed = 10010873


class REGION(dt.Region):
    HellkiteWyvernTalk = 1012675
