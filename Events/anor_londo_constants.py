import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Griggs = 6040
    Crow = 1510675
    GoodOrnstein = 1510800
    EvilOrnstein = 1510801
    GoodOrnsteinRevived = 1510802
    GiantEvilOrnstein = 1510810
    DarkmoonKnight1 = 6640
    DarkmoonKnight2 = 6650
    TitaniteDemon = 1510250
    GiantRat = 1510820
    Gargoyle = 1510450
    Ester = 1510676


class FLAG(dt.Flag):
    OrnsteinRecruited = 1903
    EvilOrnsteinKilled = 11512003
    GoodOrnsteinKilled = 11512004
    GriggsDead = 11512001
    OrnsteinBattleDone = 11512002
    TitaniteDemonDead = 11512006


class GOOD(dt.Good):
    GriggsLetter = 320
    SoulOfAKing = 326


class REGION(dt.Region):
    ChapelAltar = 1512675  # Unused.
    ScornsteinBed = 1512676
    MornsteinBed = 1512677
    MornsteinFireplace = 1512678
    BlacksmithAnvil = 1512679
    ScornsteinFireplace = 1512680
    DragonHead = 1512681
    LowerLeftFireplace = 1512682
    LowerRightFireplace = 1512683
    BasementPrison = 1512684


class ITEMLOT(dt.ItemLot):
    GriggsDrop = 4560  # Griggs' Letter
    EsterDrop = 4570
    FireplaceNote = 4580
    BlacksmithNote = 4590
    EtchedRock = 4600
    GiantEvilOrnsteinDrop = 4610


class TEXT(dt.Text):
    GiantRatName = 1202
    GoodOrnsteinName = 5270
    EvilOrnsteinName = 5271
    GiantEvilOrnsteinName = 5272

    Examine = 10010100
    ReturnToFirelink = 10010140
    MakeAccusation = 10010310
    GoodOrnsteinKilledByRat = 10010311
    AllyLost = 10010312
    PresentSoulOfAKing = 10010313

    DragonHeadMessage = 10010450
    CageUnderBed = 10010451
    NothingUnderBed = 10010452
    FireplaceEmpty = 10010453
    PrisonFurTraces = 10010454


class SPEFFECT(dt.IntEnum):
    KingslayerAxe = 4730
    WeakenGiantRat = 4731
    OrnsteinReward = 4803
