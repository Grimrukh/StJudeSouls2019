import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Siegmeyer = 6280
    BombGiant = 1500100
    BoulderGiant = 1500101
    GateGiant = 1500102
    IronGolem1 = 1500800
    IronGolem2 = 1500801

    BoulderFodderSerpent = 1500110

    UndeadAssassin1 = 1500400  # Dead end at end of first bridge.
    UndeadAssassin2 = 1500401  # At first chest. (Small delay.)
    UndeadAssassin3 = 1500402  # At second chest.
    UndeadAssassin4 = 1500403  # Before multi ramps.
    UndeadAssassin5 = 1500404  # In broken cell.
    UndeadAssassin6 = 1500405  # In locked cell.
    UndeadAssassin7 = 1500406  # Above outdoor boulder ramp.
    UndeadAssassin8 = 1500407  # Before horizontal dart trap.
    UndeadAssassin9 = 1500408  # Before packed pendulum bridge.
    UndeadAssassin10 = 1500409  # Near ladder to gate Giant.
    UndeadAssassin11 = 1500410  # Dead end with item after packed pendulum bridge.
    UndeadAssassin12 = 1500411  # Dead end with chest near Balder Knights.
    BlackIronTarkus = 1500412  # Inside Ricard's tower.

    ChainedPrisoner = 1500700


class REGION(dt.Region):
    FirstBoulderTrigger = 1502110

    ReturnToFirelink = 1502675

    TriggerUndeadAssassin1 = 1502400  # Dead end at end of first bridge.
    TriggerUndeadAssassin2 = 1502401  # At first chest. (Small delay.)
    TriggerUndeadAssassin3 = 1502402  # At second chest.
    TriggerUndeadAssassin4 = 1502403  # Before multi ramps.
    TriggerUndeadAssassin5 = 1502404  # In broken cell.
    TriggerUndeadAssassin6 = 1502405  # In locked cell.
    TriggerUndeadAssassin7 = 1502406  # Above outdoor boulder ramp.
    TriggerUndeadAssassin8 = 1502407  # Before horizontal dart trap.
    TriggerUndeadAssassin9 = 1502408  # Before packed pendulum bridge.
    TriggerUndeadAssassin10 = 1502409  # Near ladder to gate Giant.
    TriggerUndeadAssassin11 = 1502410  # Dead end with item after packed pendulum bridge.
    TriggerUndeadAssassin12 = 1502411  # Dead end with chest near Balder Knights.
    TriggerBlackIronTarkus = 1502412  # Inside Ricard's tower.


class FLAG(dt.Flag):
    IronGolemsDead = 11

    SiegmeyerRecruited = 1901
    SiegmeyerCageOpen = 11500112

    BoulderGiantAwake = 11502004

    FirstBoulderTriggered = 11500791
    BoulderStackingAllowed = 11500830
    BoulderGiantAggravated = 11505050
    TriggerBoulderGiantLoading = 11505052
    Boulder1Used = 11505210
    Boulder2Used = 11505211
    Boulder3Used = 11505212
    Boulder4Used = 11505213
    BoulderLauncherIsRotating = 11505250

    # Launcher starts pointing outside (in Common one-time event).
    BoulderLauncherNotPointingDownOutsideRamp = 11500803  # This flag is fully logically negated.
    BoulderLauncherPointingToCages = 11500806
    BoulderLauncherPointingDownMultiRamp = 11500809
    BoulderLauncherPointingOutside = 11500812

    OneBoulderStacked = 11500821
    TwoBouldersStacked = 11500822
    ThreeBouldersStacked = 11500823

    LaunchBoulder1 = 11505220
    TriggerBoulderLaunch2 = 11505221
    TriggerBoulderLaunch3 = 11505222
    TriggerBoulderLaunch4 = 11505223


class ITEMLOT(dt.ItemLot):
    ChainedPrisonerDrop = 41800000
    AssembledClarinet = 4500


class GOOD(dt.Good):
    CageKey = 2003
    IronKey = 2007
    Clarinet = 385
    ClarinetPiece1 = 386
    ClarinetPiece2 = 387
    ClarinetPiece3 = 388
    ACOGInstructions = 300


class OBJECT(dt.Object):
    LoadingBoulder = 1501800
    StackingBoulder1 = 1501801
    StackingBoulder2 = 1501802
    StackingBoulder3 = 1501803
    RollingBoulder1 = 1501804
    RollingBoulder2 = 1501805
    RollingBoulder3 = 1501806
    RollingBoulder4 = 1501807


class BOULDER_ANIM(dt.IntEnum):
    BoulderFallsIntoTrap = 0
    BoulderRollsOutside = 12


class SPEFFECT(dt.IntEnum):
    SiegmeyerSoulReward = 4801
    PlayClarinet = 4700


class TEXT(dt.Text):
    Examine = 10010100
    ReturnToFirelink = 10010140
    YourClarinetIsAssembled = 10010150
    FastAsleep = 10010151
    LockedBySomeContraption = 10010160
