from soulstruct.emevd import *
from .dukes_archives_constants import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    # RegisterBonfire(11700984, obj=1701961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11700976, obj=1701962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=1701140)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=1701141)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=1701142)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701143)
    RegisterStatue(1701900, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701901, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701902, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701903, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701904, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701905, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701906, DUKES_ARCHIVES, StatueType.crystal)
    RegisterStatue(1701907, DUKES_ARCHIVES, StatueType.crystal)

    SkipLinesIfClient(5)
    EnableFlag(405)
    DisableObject(1701994)
    DeleteFX(1701995, erase_root_only=False)
    DisableObject(1701996)
    DeleteFX(1701997, erase_root_only=False)

    # If prison door is open, disable Tower Seath.
    SkipLinesIfFlagOff(1, 11700140)
    DisableFlag(405)

    # Pisaca gate is always open.
    EndOfAnimation(1701410, 0)

    # Checkpoint fog (just before garden). Leave.
    RunEvent(11700083, slot=0, args=(1701706, 1701707, 1702606, 1702607))
    RunEvent(11700085)  # Controls golden fog. Leave.

    # Gravelord.
    RunEvent(11705080)
    RunEvent(11705081)
    RunEvent(11705082)

    # Tower Seath. Just deletes fog, disables music, and clears crystal mass.
    DisableMapSound(1703801)
    DisableObject(1701050)
    DisableObject(1701890)
    DeleteFX(1701891, erase_root_only=False)

    RunEvent(11700110)  # Descending staircase before garden.

    # Moving bookshelves.
    RunEvent(11700120, slot=0, args=(11700120, 1701120, 1701121, 0, 0))
    EndOfAnimation(1701125, 1)  # Shortcut between rooms already open.

    # Elevator/staircase stuff. Leave.
    RunEvent(11700160, slot=0, args=(11700100, 1701100, 11700210, 11700211, 11705090, 11705180, 11705181))
    RunEvent(11700105, slot=0, args=(11700100, 1701100, 1701101, 1701102, 11705090, 11705180, 11705181))
    # RunEvent(11700160, slot=1, args=(11700102, 1701130, 11700220, 11700221, 11705091, 11705182, 11705183))
    # RunEvent(11700105, slot=2, args=(11700102, 1701130, 1701131, 1701132, 11705091, 11705182, 11705183))
    EndOfAnimation(1701130, 11)
    DisableObjectActivation(1701131, objact_param_id=-1)
    DisableObjectActivation(1701132, objact_param_id=-1)
    RunEvent(11700090, slot=0, args=(11700100, 0, 1701101, 11705090), arg_types='iBii')
    RunEvent(11700090, slot=1, args=(11700100, 1, 1701102, 11705090), arg_types='iBii')
    RunEvent(11700090, slot=2, args=(11700102, 0, 1701131, 11705091), arg_types='iBii')
    RunEvent(11700090, slot=3, args=(11700102, 1, 1701132, 11705091), arg_types='iBii')
    RunEvent(11705150, slot=0, args=(11700205, 1701200, 1701210))
    RunEvent(11700200, slot=0, args=(11700205, 1701200, 1701201, 1703200, 1703201, 1703010, 1703011, 11705151))
    RunEvent(11700200, slot=1, args=(11700205, 1701210, 1701211, 1703210, 1703211, 1703012, 1703013, 11705152))
    RunEvent(11700150, slot=0, args=(1703100, 1702780))
    RunEvent(11700150, slot=1, args=(1703101, 1702781))

    # Normal prison doors. All opened with the same key as the giant cell.
    RunEvent(11700300, slot=0, args=(11700300, 10010865, 1701500))
    RunEvent(11700300, slot=1, args=(11700311, 10010865, 1701501))
    RunEvent(11700300, slot=2, args=(11700302, 10010865, 1701502))
    RunEvent(11700300, slot=3, args=(11700313, 10010865, 1701503))
    RunEvent(11700300, slot=4, args=(11700304, 10010865, 1701504))
    RunEvent(11700300, slot=5, args=(11700305, 10010865, 1701505))
    RunEvent(11700300, slot=6, args=(11700320, 10010865, OBJECT.GiantCellDoor))

    # Prison exit door is already open.
    EndOfAnimation(1701300, 0)

    # Old Seath stuff.
    DisableMapSound(1703800)
    DisableObject(1701800)  # Primordial Crystal.
    DisableObject(1701990)  # Cave fog.
    DeleteFX(1701991, erase_root_only=False)

    RunEvent(11700810, slot=12, args=(1700150, 0, 0))  # Make her drop Fire Keeper Soul.

    # Old chest events deleted. (11700600)

    # Pisaca control.
    RunEvent(11705110, slot=0, args=(1700110,))
    RunEvent(11705110, slot=1, args=(1700111,))
    RunEvent(11705110, slot=2, args=(1700112,))
    RunEvent(11705110, slot=3, args=(1700113,))
    RunEvent(11705110, slot=4, args=(1700114,))
    RunEvent(11705110, slot=5, args=(1700115,))
    RunEvent(11705110, slot=6, args=(1700116,))
    RunEvent(11705110, slot=7, args=(1700117,))
    RunEvent(11705110, slot=8, args=(1700118,))
    RunEvent(11705110, slot=9, args=(1700119,))
    RunEvent(11705110, slot=10, args=(1700120,))
    RunEvent(11705110, slot=11, args=(1700121,))
    RunEvent(11705110, slot=12, args=(1700122,))
    RunEvent(11705110, slot=13, args=(1700123,))
    RunEvent(11705110, slot=14, args=(1700124,))
    RunEvent(11705110, slot=15, args=(1700125,))
    RunEvent(11705110, slot=16, args=(1700126,))
    RunEvent(11705110, slot=17, args=(1700127,))
    RunEvent(11705110, slot=18, args=(1700908,))
    RunEvent(11705110, slot=19, args=(1700909,))

    ReturnToFirelink()
    GetMimicRing()
    ApplyMimicRingStealth()

    SetMimicTrap(0, OBJECT.Chest1, CHR.HungryMimic1, CHR.LoganMimic1, CHR.Looter1, FLAG.Mimic1Fed, REGION.Mimic1)
    SetMimicTrap(1, OBJECT.Chest2, CHR.HungryMimic2, CHR.LoganMimic2, CHR.Looter2, FLAG.Mimic2Fed, REGION.Mimic2)
    SetMimicTrap(2, OBJECT.Chest3, CHR.HungryMimic3, CHR.LoganMimic3, CHR.Looter3, FLAG.Mimic3Fed, REGION.Mimic3)
    SetMimicTrap(3, OBJECT.Chest4, CHR.HungryMimic4, CHR.LoganMimic4, CHR.Looter4, FLAG.Mimic4Fed, REGION.Mimic4)
    SetMimicTrap(4, OBJECT.Chest5, CHR.HungryMimic5, CHR.LoganMimic5, CHR.Looter5, FLAG.Mimic5Fed, REGION.Mimic5)
    SetMimicTrap(5, OBJECT.Chest6, CHR.HungryMimic6, CHR.LoganMimic6, CHR.Looter6, FLAG.Mimic6Fed, REGION.Mimic6)


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    RecruitLogan()
    ReturnHavelGear()
    RecruitHavel()
    PisacaBattle()


@NeverRestart
def Event11700080(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700080: Event 11700080 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfFlagOn(3, 11700080)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11700080)
    SkipLinesIfFinishedConditionTrue(5, 3)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WarpToEntity(10000, destination=ARG_8_11, destination_type=Category.region, model_point=-1, short_warp=True)
    SkipLines(1)
    WarpToEntity(10000, destination=ARG_12_15, destination_type=Category.region, model_point=-1, short_warp=True)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=False, skip_transition=False)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)


@NeverRestart
def Event11700083(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700083: Event 11700083 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WarpToEntity(10000, destination=ARG_8_11, destination_type=Category.region, model_point=-1, short_warp=True)
    SkipLines(1)
    WarpToEntity(10000, destination=ARG_12_15, destination_type=Category.region, model_point=-1, short_warp=True)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=False, skip_transition=False)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)


@RestartOnRest
def Event11705080():
    """ 11705080: Event 11705080 """
    EndIfThisEventOn()
    DisableCharacter(1700900)
    DisableCharacter(1700901)
    DisableCharacter(1700902)
    DisableCharacter(1700903)
    DisableCharacter(1700904)
    DisableCharacter(1700905)
    DisableCharacter(1700906)
    DisableCharacter(1700907)
    DisableCharacter(1700908)
    DisableCharacter(1700909)
    IfFlagOn(0, 11700050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1700900)
    EnableCharacter(1700901)
    EnableCharacter(1700902)
    EnableCharacter(1700903)
    EnableCharacter(1700904)
    EnableCharacter(1700905)
    EnableCharacter(1700906)
    EnableCharacter(1700907)
    EnableCharacter(1700908)
    EnableCharacter(1700909)


@RestartOnRest
def Event11705081():
    """ 11705081: Event 11705081 """
    IfFlagOn(-1, 11705085)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11700050)
    DisableFlag(11705085)
    EnableFlag(5001)
    Kill(1700900, award_souls=False)
    Kill(1700901, award_souls=False)
    Kill(1700902, award_souls=False)
    Kill(1700903, award_souls=False)
    Kill(1700904, award_souls=False)
    Kill(1700905, award_souls=False)
    Kill(1700906, award_souls=False)
    Kill(1700907, award_souls=False)
    Kill(1700908, award_souls=False)
    Kill(1700909, award_souls=False)


@RestartOnRest
def Event11705082():
    """ 11705082: Event 11705082 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type_enum=2, value=50)
    IfInsideMap(1, DUKES_ARCHIVES)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11700050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type_enum=2, value=50)
    IfInsideMap(2, DUKES_ARCHIVES)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11700050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type_enum=2, value=50)
    IfInsideMap(3, DUKES_ARCHIVES)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11700050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type_enum=2, value=50)
    IfInsideMap(4, DUKES_ARCHIVES)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11700050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type_enum=2, value=50)
    IfInsideMap(5, DUKES_ARCHIVES)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11700050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type_enum=2, value=50)
    IfInsideMap(6, DUKES_ARCHIVES)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11700050)
    RestartIfConditionFalse(-6)
    EnableFlag(11700050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type_enum=5, value=50)
    IfInsideMap(7, DUKES_ARCHIVES)
    RestartIfConditionFalse(7)
    DisableFlag(11700050)
    EnableFlag(11705085)


@NeverRestart
def Event11700085():
    """ 11700085: Event 11700085 """
    SkipLinesIfFlagOff(4, 11800100)
    EnableFlag(11700086)
    DisableObject(1701710)
    DeleteFX(1701711, erase_root_only=False)
    End()
    SkipLinesIfFlagOff(3, 11700086)
    DisableObject(1701710)
    DeleteFX(1701711, erase_root_only=False)
    End()
    EndIfClient()
    IfDialogPromptActivated(0, prompt_text=10010410, anchor_entity=1702610, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=1701710)
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


@RestartOnRest
def Event11700000():
    """ 11700000: Event 11700000 """
    EndIfThisEventOn()
    DisableObject(1701990)
    DeleteFX(1701991, erase_root_only=False)
    DisableCharacter(1700800)
    EnableObjectInvulnerability(1701800)
    IfThisEventOff(1)
    IfHost(1)
    IfPlayerInsideRegion(1, 1702999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)
    EnableFlag(11705390)
    EnableFlag(11705391)
    EnableFlag(11705393)
    IfCharacterType(2, PLAYER, CharacterType.black_phantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(cutscene_id=170000, skippable=True, fade_out=False, player_id=10000, warp_to_region=1702801, warp_to_map=DUKES_ARCHIVES)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(cutscene_id=170000, skippable=False, fade_out=False, player_id=10000, warp_to_region=1702801, warp_to_map=DUKES_ARCHIVES)
    SkipLines(1)
    PlayCutscene(cutscene_id=170000, skippable=False, fade_out=False, player_id=10000)
    WaitFrames(1)
    DisableObjectInvulnerability(1701800)
    EnableObject(1701990)
    CreateFX(1701991)
    WarpToEntity(1700800, destination=1702800, destination_type=Category.region, model_point=-1, short_warp=True)
    EnableCharacter(1700800)


@NeverRestart
def Event11705380():
    """ 11705380: Event 11705380 """
    IfFlagOff(1, 11700000)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1702898, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1701890, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(10000, 1702897)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=False, skip_transition=False)
    Restart()


@NeverRestart
def Event11705381():
    """ 11705381: Event 11705381 """
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfCharacterType(1, PLAYER, CharacterType.white_phantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1702898, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1701890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(10000, 1702897)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=False, skip_transition=False)
    Restart()


@NeverRestart
def Event11705386():
    """ 11705386: Event 11705386 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11700000)
    IfPlayerInsideRegion(1, 1702896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700700)


@NeverRestart
def Event11705382():
    """ 11705382: Event 11705382 """
    DisableNetworkSync()
    IfFlagOff(1, 11700000)
    IfDialogPromptActivated(1, prompt_text=10010404, anchor_entity=1702895, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1701890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(10000, 1702894)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=True, skip_transition=False)
    DisableBossHealthBar(1700700, name_id=5290, slot=0)
    Restart()


@RestartOnRest
def Event11705383():
    """ 11705383: Event 11705383 """
    DisableAI(1700700)
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfPlayerInsideRegion(1, 1702890)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1700700)
    EnableBossHealthBar(1700700, name_id=5290, slot=0)
    IfAllPlayersOutsideRegion(0, 1702890)
    Restart()


@NeverRestart
def Event11705384():
    """ 11705384: Event 11705384 """
    DisableNetworkSync()
    DisableMapSound(1703801)
    IfFlagOff(1, 11700000)
    IfFlagOn(1, 11705386)
    IfPlayerInsideRegion(1, 1702890)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1703801)
    IfFlagOn(-1, 11700000)
    IfPlayerOutsideRegion(-1, 1702890)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest
def Event11705385():
    """ 11705385: Event 11705385 """
    EnableImmortality(1700700)
    AddSpecialEffect(1700700, 5441)
    AddSpecialEffect(1700700, 5442)
    AddSpecialEffect(1700700, 5443)
    IfFlagOn(0, 11700000)
    DisableCharacter(1700700)
    DisableObject(1701050)
    DisableObject(1701890)
    DeleteFX(1701891, erase_root_only=True)


@NeverRestart
def Event11705390():
    """ 11705390: Event 11705390 """
    IfFlagOff(1, 14)
    IfFlagOn(1, 11700000)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1702998, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1701990, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(10000, 1702997)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=True, skip_transition=False)
    ActivateMultiplayerBuffs(1700800)
    Restart()


@NeverRestart
def Event11705391():
    """ 11705391: Event 11705391 """
    IfFlagOff(1, 14)
    IfFlagOn(1, 11705393)
    IfCharacterType(1, PLAYER, CharacterType.white_phantom)
    IfAlive(1, 1700800)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1702998, anchor_type=Category.region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1701990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(10000, 1702997)
    ForceAnimation(10000, 7410, loop=False, wait_for_completion=False, skip_transition=False)
    Restart()


@NeverRestart
def Event11705393():
    """ 11705393: Event 11705393 """
    SkipLinesIfThisEventOn(8)
    IfFlagOn(1, 11700000)
    IfFlagOff(1, 14)
    IfPlayerInsideRegion(1, 1702996)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)


@RestartOnRest
def Event11705392():
    """ 11705392: Event 11705392 """
    SkipLinesIfFlagOff(5, 14)
    DisableCharacter(1700800)
    Kill(1700800, award_souls=False)
    DisableCharacter(1700801)
    Kill(1700801, award_souls=False)
    End()
    DisableAI(1700800)
    IfFlagOn(1, 11705393)
    IfPlayerInsideRegion(1, 1702990)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1700800)
    EnableBossHealthBar(1700800, name_id=5290, slot=0)


@NeverRestart
def Event11700001():
    """ 11700001: Event 11700001 """
    DisableObject(1701950)
    IfDead(0, 1700800)
    EnableFlag(14)
    KillBoss(1700800)
    SkipLinesIfClient(1)
    AwardAchievement(38)
    DisableObject(1701990)
    DeleteFX(1701991, erase_root_only=True)
    CreateTemporaryFX(90014, anchor_entity=1701950, anchor_type=Category.object, model_point=-1)
    Wait(2.0)
    EnableObject(1701950)
    RegisterBonfire(11700920, obj=1701950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


@NeverRestart
def Event11705394():
    """ 11705394: Event 11705394 """
    DisableNetworkSync()
    IfFlagOff(1, 14)
    IfFlagOn(1, 11705392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11705391)
    IfPlayerInsideRegion(1, 1702990)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1703800)


@NeverRestart
def Event11705395():
    """ 11705395: Event 11705395 """
    DisableNetworkSync()
    IfFlagOn(1, 14)
    IfFlagOn(1, 11705394)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1703800)


@RestartOnRest
def Event11705396():
    """ 11705396: Event 11705396 """
    AddSpecialEffect(1700800, 5440)
    AddSpecialEffect(1700800, 5441)
    AddSpecialEffect(1700800, 5442)
    AddSpecialEffect(1700800, 5443)
    EnableImmortality(1700800)
    CreateObjectFX(170004, obj=1701800, model_point=100)
    IfObjectDestroyed(0, 1701800)
    DeleteObjectFX(1703100, erase_root=True)
    ForceAnimation(1700800, 7000, loop=False, wait_for_completion=False, skip_transition=False)
    IfHasTAEEvent(0, 1700800, tae_event_id=500)
    CancelSpecialEffect(1700800, 5440)
    CancelSpecialEffect(1700800, 5441)
    CancelSpecialEffect(1700800, 5442)
    CancelSpecialEffect(1700800, 5443)
    DisableImmortality(1700800)


@RestartOnRest
def Event11705397():
    """ 11705397: Event 11705397 """
    DisableCharacter(1700801)
    EndIfFlagOn(14)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(1700800, bit_index=1, switch_type=0)
    SetHitboxMask(1700800, bit_index=1, switch_type=1)
    AICommand(1700800, command_id=20, slot=0)
    End()
    IfBackreadEnabled(0, 1700800)
    CreateNPCPart(1700800, part_npc_type=5290, part_index=1, part_health=330, damage_correction=1.0, body_damage_correction=1.0, is_invincible=0, start_in_stop_state=0)
    IfHealthGreaterThan(1, 1700800, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, 1700800, npc_part_type=5290, value=0)
    IfHealthLessThanOrEqual(2, 1700800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(1700800, 8000, loop=False, wait_for_completion=False, skip_transition=False)
    IfHasTAEEvent(0, 1700800, tae_event_id=400)
    WarpToEntity(1700801, destination=1700800, destination_type=Category.character, model_point=150, copy_draw_hitbox=1700800)
    EnableCharacter(1700801)
    SetDisplayMask(1700800, bit_index=1, switch_type=0)
    SetHitboxMask(1700800, bit_index=1, switch_type=1)
    ForceAnimation(1700801, 8100, loop=False, wait_for_completion=False, skip_transition=False)
    AICommand(1700800, command_id=20, slot=0)
    ReplanAI(1700800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52910000, host_only=True)


@NeverRestart
def Event11700160(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 11700160: Event 11700160 """
    IfFlagOff(1, ARG_16_19)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=ARG_4_7, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfObjectActivated(2, objact_id=ARG_8_11)
    IfObjectActivated(3, objact_id=ARG_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_16_19)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(8, ARG_0_3)
    SkipLinesIfFinishedConditionFalse(4, 1)
    WarpToEntity(10000, destination=ARG_4_7, destination_type=Category.object, model_point=191, short_warp=True)
    ForceAnimation(10000, 8000, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(ARG_4_7, 0, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(105)
    EnableFlag(ARG_20_23)
    IfFlagOff(0, ARG_16_19)
    Restart()
    SkipLinesIfFinishedConditionFalse(4, 1)
    WarpToEntity(10000, destination=ARG_4_7, destination_type=Category.object, model_point=191, short_warp=True)
    ForceAnimation(10000, 8000, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(ARG_4_7, 2, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(105)
    EnableFlag(ARG_24_27)
    IfFlagOff(0, ARG_16_19)
    Restart()


@NeverRestart
def Event11700105(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 11700105: Event 11700105 """
    SkipLinesIfFlagOff(4, ARG_0_3)
    EndOfAnimation(ARG_4_7, 11)
    EnableObjectActivation(ARG_8_11, objact_param_id=-1)
    DisableObjectActivation(ARG_12_15, objact_param_id=-1)
    SkipLines(2)
    DisableObjectActivation(ARG_8_11, objact_param_id=-1)
    EnableObjectActivation(ARG_12_15, objact_param_id=-1)
    IfHost(1)
    IfFlagOn(1, ARG_20_23)
    IfHost(2)
    IfFlagOn(2, ARG_24_27)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(ARG_20_23)
    DisableFlag(ARG_24_27)
    DisableObjectActivation(ARG_8_11, objact_param_id=-1)
    DisableObjectActivation(ARG_12_15, objact_param_id=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(ARG_0_3)
    ForceAnimation(ARG_4_7, 1, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(300)
    DisableFlag(ARG_16_19)
    Restart()
    DisableFlag(ARG_0_3)
    ForceAnimation(ARG_4_7, 3, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(344)
    DisableFlag(ARG_16_19)
    Restart()


@NeverRestart
def Event11700090(ARG_0_3: int, ARG_4_4: uchar, ARG_8_11: int, ARG_12_15: int):
    """ 11700090: Event 11700090 """
    DisableNetworkSync()
    IfFlagState(1, ARG_0_3, state=ARG_4_4)
    IfFlagOff(1, ARG_12_15)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=ARG_8_11, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=195, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010170, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.ok_cancel, number_buttons=NumberButtons.no_button)
    Restart()


@NeverRestart
def Event11705150(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11705150: Event 11705150 """
    IfDialogPromptActivated(1, prompt_text=10010503, anchor_entity=ARG_4_7, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfDialogPromptActivated(2, prompt_text=10010503, anchor_entity=ARG_8_11, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(7, 1)
    WarpToEntity(10000, destination=ARG_4_7, destination_type=Category.object, model_point=191, short_warp=True)
    SkipLinesIfFlagOn(2, ARG_0_3)
    ForceAnimation(ARG_4_7, 0, loop=False, wait_for_completion=False, skip_transition=False)
    SkipLines(1)
    ForceAnimation(ARG_4_7, 2, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(10000, 8010, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(105)
    SkipLinesIfFinishedConditionFalse(7, 2)
    WarpToEntity(10000, destination=ARG_8_11, destination_type=Category.object, model_point=191, short_warp=True)
    SkipLinesIfFlagOn(2, ARG_0_3)
    ForceAnimation(ARG_8_11, 0, loop=False, wait_for_completion=False, skip_transition=False)
    SkipLines(1)
    ForceAnimation(ARG_8_11, 2, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(10000, 8010, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    IfFlagOff(3, 11705151)
    IfFlagOff(3, 11705152)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart
def Event11700200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 11700200: Event 11700200 """
    DisableObject(ARG_8_11)
    SkipLinesIfFlagOn(5, ARG_0_3)
    EndOfAnimation(ARG_4_7, 3)
    DisableHitbox(ARG_16_19)
    DisableNavimeshType(ARG_20_23, NavimeshType.solid)
    EnableNavimeshType(ARG_24_27, NavimeshType.solid)
    SkipLines(4)
    EndOfAnimation(ARG_4_7, 1)
    DisableHitbox(ARG_12_15)
    EnableNavimeshType(ARG_20_23, NavimeshType.solid)
    DisableNavimeshType(ARG_24_27, NavimeshType.solid)
    IfFlagOn(0, ARG_28_31)
    SkipLinesIfFlagOn(11, ARG_0_3)
    ForceAnimation(ARG_4_7, 1, loop=False, wait_for_completion=False, skip_transition=False)
    DisableHitbox(ARG_12_15)
    EnableObject(ARG_8_11)
    EnableNavimeshType(ARG_20_23, NavimeshType.solid)
    ForceAnimation(ARG_8_11, 1, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(180)
    DisableObject(ARG_8_11)
    EnableHitbox(ARG_16_19)
    EnableFlag(ARG_0_3)
    DisableFlag(ARG_28_31)
    Restart()
    ForceAnimation(ARG_4_7, 3, loop=False, wait_for_completion=False, skip_transition=False)
    DisableHitbox(ARG_16_19)
    EnableObject(ARG_8_11)
    EnableNavimeshType(ARG_24_27, NavimeshType.solid)
    ForceAnimation(ARG_8_11, 3, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(180)
    DisableObject(ARG_8_11)
    EnableHitbox(ARG_12_15)
    DisableFlag(ARG_0_3)
    DisableFlag(ARG_28_31)
    Restart()


@NeverRestart
def Event11700110():
    """ 11700110: Event 11700110 """
    SkipLinesIfThisEventOff(5)
    DisableObjectActivation(1701111, objact_param_id=-1)
    EndOfAnimation(1701110, 0)
    DisableObject(1701109)
    DisableHitbox(1703220)
    End()
    DisableObject(1701109)
    DisableHitbox(1703221)
    IfObjectActivated(0, objact_id=11700110)
    DisableHitbox(1703220)
    EnableObject(1701109)
    ForceAnimation(1701110, 0, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(1701109, 0, loop=False, wait_for_completion=True, skip_transition=False)
    DisableObject(1701109)
    EnableHitbox(1703221)


@NeverRestart
def Event11700120(obj_act_flag: int, bookcase: int, lever: int, open_animation: int, ARG_16_19: int):
    """ 11700120: Event 11700120 """
    SkipLinesIfThisEventSlotOff(4)
    SkipLinesIfEqual(1, left_value=ARG_16_19, right_value=1)
    DisableObjectActivation(lever, objact_param_id=-1)
    EndOfAnimation(bookcase, open_animation)
    End()
    SkipLinesIfEqual(1, left_value=ARG_16_19, right_value=0)
    IfFlagOn(-1, 11700140)
    IfObjectActivated(-1, objact_id=obj_act_flag)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(obj_act_flag)
    ForceAnimation(bookcase, open_animation, loop=False, wait_for_completion=False, skip_transition=False)


@NeverRestart
def Event11700150(ARG_0_3: int, ARG_4_7: int):
    """ 11700150: Event 11700150 """
    IfAllPlayersOutsideRegion(0, ARG_4_7)
    EnableHitbox(ARG_0_3)
    IfPlayerInsideRegion(0, ARG_4_7)
    DisableHitbox(ARG_0_3)
    Restart()


@NeverRestart
def Event11705100():
    """ 11705100: Event 11705100 """
    DisableNetworkSync()
    IfPlayerInsideRegion(1, 1702890)
    IfHost(1)
    IfDead(1, 10000)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(1702900)
    SaveRequest()


@NeverRestart
def Event11705101():
    """ 11705101: Event 11705101 """
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, 51700990)
    IfFlagOff(1, 11705101)
    IfFlagOff(1, 11700133)
    IfPlayerInsideRegion(1, 1702100)
    IfHost(2)
    IfFlagOn(2, 11705106)
    IfHost(3)
    IfFlagOn(3, 11705107)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFlagOn(9, 11700002)
    SkipLinesIfFinishedConditionFalse(8, 1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(cutscene_id=170010, skippable=True, fade_out=False, player_id=10000)
    SkipLines(1)
    PlayCutscene(cutscene_id=170010, skippable=False, fade_out=False, player_id=10000)
    WaitFrames(1)
    ForceAnimation(1701410, 0, loop=False, wait_for_completion=False, skip_transition=False)
    EnableFlag(11700002)
    EnableFlag(61700105)
    SkipLinesIfFinishedConditionTrue(1, 1)
    SkipLinesIfFinishedConditionTrue(9, 3)
    SkipLinesIfFlagOn(2, 61700105)
    RunEvent(11705108)
    Restart()
    EnableMapSound(1703500)
    ForceAnimation(1701400, 0, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(150)
    ForceAnimation(1701400, 1, loop=False, wait_for_completion=False, skip_transition=False)
    RunEvent(11705108)
    Restart()
    SkipLinesIfFlagOff(2, 61700105)
    RunEvent(11705108)
    Restart()
    DisableMapSound(1703500)
    EnableFlag(11700133)
    ForceAnimation(1701400, 2, loop=False, wait_for_completion=False, skip_transition=False)
    WaitFrames(50)
    RunEvent(11705108)
    Restart()


@NeverRestart
def Event11705102():
    """ 11705102: Event 11705102 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(1, 61700105)
    DisableMapSound(1703500)


@NeverRestart
def Event11705103():
    """ 11705103: Event 11705103 """
    IfFlagOn(1, 61700105)
    IfObjectActivated(1, objact_id=11705105)
    IfFlagOff(2, 61700105)
    IfObjectActivated(2, objact_id=11705105)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11705106)
    Restart()
    EnableFlag(11705107)
    Restart()


@NeverRestart
def Event11705108():
    """ 11705108: Event 11705108 """
    DisableNetworkSync()
    IfFramesElapsed(1, 10)
    IfInsideMap(1, DUKES_ARCHIVES)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1701401, objact_param_id=-1)


@RestartOnRest
def Event11705110(ARG_0_3: int):
    """ 11705110: Event 11705110 """
    IfFlagOn(1, 61700105)
    IfPlayerInsideRegion(-7, 1702100)
    IfPlayerInsideRegion(-7, 1702101)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(2, 61700105)
    IfAllPlayersOutsideRegion(2, 1702100)
    IfAllPlayersOutsideRegion(2, 1702101)
    IfFlagOff(3, 61700105)
    IfFlagOn(3, 11700002)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, 1)
    AICommand(ARG_0_3, command_id=1, slot=0)
    ReplanAI(ARG_0_3)
    IfAllPlayersOutsideRegion(7, 1702100)
    IfAllPlayersOutsideRegion(7, 1702101)
    IfConditionTrue(-2, input_condition=7)
    IfFlagOff(-2, 61700105)
    IfConditionTrue(0, input_condition=-2)
    Restart()
    SkipLinesIfFinishedConditionFalse(7, 2)
    AICommand(ARG_0_3, command_id=2, slot=0)
    ReplanAI(ARG_0_3)
    IfPlayerInsideRegion(-3, 1702100)
    IfPlayerInsideRegion(-3, 1702101)
    IfFlagOff(-3, 61700105)
    IfConditionTrue(0, input_condition=-3)
    Restart()
    AICommand(ARG_0_3, command_id=3, slot=0)
    ReplanAI(ARG_0_3)
    IfFlagOn(0, 61700105)
    Restart()


@RestartOnRest
def Event11700130():
    """ 11700130: Event 11700130 """
    EndIfClient()
    SkipLinesIfFlagOff(3, 51700990)
    DisableCharacter(1700100)
    Kill(1700100, award_souls=False)
    End()
    DisableCollision(1700100)
    DisableGravity(1700100)


@RestartOnRest
def Event11705140(ARG_0_3: int, ARG_4_7: int):
    """ 11705140: Event 11705140 """
    EndIfThisEventSlotOn()
    IfFlagOn(0, 11705101)
    SetNest(ARG_0_3, ARG_4_7)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    IfThisEventSlotOn(-1)
    IfEntityInsideRegion(-1, ARG_0_3, ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    ClearTargetList(ARG_0_3)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@NeverRestart
def Event11700140():
    """ 11700140: Event 11700140 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1701300, 0)
    End()
    IfPlayerOwnsGood(1, 2005, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1701300, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfFlagOn(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(405)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WarpToEntity(10000, destination=1701300, destination_type=Category.object, model_point=120, short_warp=True)
    ForceAnimation(10000, 7120, loop=False, wait_for_completion=False, skip_transition=False)
    ForceAnimation(1701300, 0, loop=False, wait_for_completion=False, skip_transition=False)
    EndIfClient()
    DisplayDialog(10010864, anchor_entity=1701300, display_distance=3.0, button_type=ButtonType.yes_no, number_buttons=NumberButtons.no_button)
    End()


@NeverRestart
def Event11700141():
    """ 11700141: Event 11700141 """
    DisableNetworkSync()
    IfFlagOff(1, 11700140)
    IfPlayerDoesNotOwnGood(1, 2005, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1701300, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=False)
    IfFlagOff(2, 11700140)
    IfDialogPromptActivated(2, prompt_text=10010400, anchor_entity=1701300, anchor_type=Category.object, facing_angle=60.0, max_distance=1.5, model_point=101, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010163, anchor_entity=1701300, display_distance=3.0, button_type=ButtonType.ok_cancel, number_buttons=NumberButtons.no_button)
    Restart()


@RestartOnRest
def Event11705170():
    """ 11705170: Event 11705170 """
    DisableNetworkSync()
    EndIfClient()
    DisableFlag(11705170)
    IfPlayerInsideRegion(0, 1702402)
    EnableFlag(11705170)
    IfPlayerOutsideRegion(0, 1702402)
    Restart()


@RestartOnRest
def Event11705160(ARG_0_3: int, ARG_4_7: float):
    """ 11705160: Event 11705160 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    IfEntityWithinDistance(0, ARG_0_3, 10000, ARG_4_7)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=13000)


@RestartOnRest
def Event11705250(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11705250: Event 11705250 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_4_7)
    IfPlayerInsideRegion(-1, ARG_0_3)
    IfAttacked(-1, ARG_4_7, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_4_7, ARG_8_11, loop=False, wait_for_completion=True, skip_transition=False)
    EnableAI(ARG_4_7)


@RestartOnRest
def Event11705270(ARG_0_3: int, ARG_4_7: float):
    """ 11705270: Event 11705270 """
    EndIfThisEventSlotOn()
    SetStandbyAnimationSettings(ARG_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, ARG_0_3, 10000, ARG_4_7)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=9060)


def OpenCellDoor(obj_act_flag: int, message: int, door: int):
    """ 11700300: Open Havel's giant cell and display message. Now displays message on every load. """
    IfObjectActivated(0, objact_id=obj_act_flag)
    DisplayDialog(message, anchor_entity=door, display_distance=3.0, button_type=ButtonType.yes_no, number_buttons=NumberButtons.no_button)
    DisableObjectActivation(door, objact_param_id=-1, relative_idx=0)
    DisableObjectActivation(door, objact_param_id=-1, relative_idx=1)
    DisableObjectActivation(door, objact_param_id=-1, relative_idx=2)
    DisableObjectActivation(door, objact_param_id=-1, relative_idx=3)


@RestartOnRest
def Event11705200():
    """ 11705200: Event 11705200 """
    RunEvent(11705240, slot=0, args=(1700900,))
    RunEvent(11705240, slot=1, args=(1700901,))
    RunEvent(11705240, slot=2, args=(1700902,))
    RunEvent(11705240, slot=3, args=(1700903,))
    RunEvent(11705201, slot=0, args=(11705200, 1700300, 1702301, 11705202))
    RunEvent(11705201, slot=1, args=(11705201, 1700300, 1702306, 11705202))
    RunEvent(11705201, slot=2, args=(11705202, 1700300, 1702305, 11705202))
    EnableFlag(11705210)
    RunEvent(11705201, slot=10, args=(11705210, 1700301, 1702311, 11705213))
    RunEvent(11705201, slot=11, args=(11705211, 1700301, 1702312, 11705213))
    RunEvent(11705201, slot=12, args=(11705212, 1700301, 1702313, 11705213))
    RunEvent(11705201, slot=13, args=(11705213, 1700301, 1702314, 11705213))
    EnableFlag(11705220)
    RunEvent(11705201, slot=20, args=(11705220, 1700302, 1702321, 11705221))
    RunEvent(11705201, slot=21, args=(11705221, 1700302, 1702322, 11705221))


@RestartOnRest
def Event11705240(ARG_0_3: int):
    """ 11705240: Event 11705240 """
    DisableNetworkSync()
    IfBackreadEnabled(0, ARG_0_3)
    AICommand(ARG_0_3, command_id=1, slot=0)


@UnknownRestart
def Event11705201(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11705201: Event 11705201 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, ARG_0_3)
    IfHasTAEEvent(1, ARG_4_7, tae_event_id=1000)
    IfConditionTrue(0, input_condition=1)
    WarpToEntity(ARG_4_7, destination=ARG_8_11, destination_type=Category.region, model_point=-1, short_warp=True)
    SetNest(ARG_4_7, ARG_8_11)
    ForceAnimation(ARG_4_7, 7000, loop=False, wait_for_completion=True, skip_transition=False)
    SkipLinesIfFlagOff(1, ARG_12_15)
    AICommand(ARG_4_7, command_id=1, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event11700810(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11700810: Event 11700810 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfDead(0, ARG_0_3)
    SkipLinesIfEqual(4, left_value=ARG_4_7, right_value=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(ARG_8_11, host_only=True)
    End()


@RestartOnRest
def Event11705280(ARG_0_3: int):
    """ 11705280: Event 11705280 """
    IfAlive(0, ARG_0_3)
    IfDead(0, ARG_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(32300100, host_only=True)


@NeverRestart
def Event11700600(ARG_0_3: int, ARG_4_7: int):
    """ 11700600: Event 11700600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, objact_param_id=-1)
    EnableTreasure(ARG_0_3)
    End()
    DisableTreasure(ARG_0_3)
    IfObjectActivated(0, objact_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@RestartOnRest
def Event11705010(ARG_0_3: int):
    """ 11705010: Event 11705010 """
    IfAlive(1, ARG_0_3)
    IfBackreadEnabled(1, ARG_0_3)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5421)
    IfCharacterType(2, PLAYER, CharacterType.black_phantom)
    IfConditionFalse(1, input_condition=2)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=ARG_0_3, anchor_type=Category.character, facing_angle=45.0, max_distance=1.2000000476837158, model_point=7, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    WarpToEntity(10000, destination=ARG_0_3, destination_type=Category.character, model_point=100, copy_draw_hitbox=ARG_0_3)
    ForceAnimation(10000, 7521, loop=False, wait_for_completion=False, skip_transition=False)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event11705020(ARG_0_3: int):
    """ 11705020: Event 11705020 """
    IfCharacterDoesNotHaveSpecialEffect(1, ARG_0_3, 5420)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    IfBackreadDisabled(7, ARG_0_3)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(ARG_0_3, 3001, loop=False, wait_for_completion=True, skip_transition=False)
    IfCharacterHasSpecialEffect(3, ARG_0_3, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(ARG_0_3, 3001, loop=False, wait_for_completion=True, skip_transition=False)
    IfCharacterHasSpecialEffect(4, ARG_0_3, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(ARG_0_3, 3001, loop=False, wait_for_completion=True, skip_transition=False)
    IfCharacterHasSpecialEffect(5, ARG_0_3, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(ARG_0_3, 3006, loop=False, wait_for_completion=True, skip_transition=False)
    ReplanAI(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    Restart()


@RestartOnRest
def Event11705030(ARG_0_3: int):
    """ 11705030: Event 11705030 """
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5421)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 3150)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(ARG_0_3, command_id=200, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(ARG_0_3, command_id=210, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11705040(ARG_0_3: int):
    """ 11705040: Event 11705040 """
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, ARG_0_3, 3150)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, ARG_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(ARG_0_3, command_id=201, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(ARG_0_3, command_id=211, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11705050(ARG_0_3: int, ARG_4_7: int):
    """ 11705050: Event 11705050 """
    IfSinglePlayer(1)
    IfEntityInsideRegion(1, ARG_0_3, ARG_4_7)
    IfBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(ARG_0_3, 5421)
    ClearTargetList(ARG_0_3)
    ReplanAI(ARG_0_3)
    WarpToEntity(ARG_0_3, destination=ARG_4_7, destination_type=Category.region, model_point=-1, short_warp=True)
    IfBackreadEnabled(0, ARG_0_3)
    Restart()


@RestartOnRest
def Event11700900(ARG_0_3: int):
    """ 11700900: Event 11700900 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(ARG_0_3)
    End()
    IfDead(0, ARG_0_3)
    End()


@RestartOnRest
def Event11705060(ARG_0_3: int):
    """ 11705060: Event 11705060 """
    EndIfHost()
    IfBackreadDisabled(1, ARG_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(ARG_0_3, disable_interpolation=True)
    ForceAnimation(ARG_0_3, 0, loop=False, wait_for_completion=False, skip_transition=False)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event11700700():
    """ 11700700: Event 11700700 """
    IfAlive(0, 1700510)
    EndIfFlagOn(11700700)
    IfDLCOwned(1)
    IfDead(1, 1700510)
    IfFlagOn(1, 11200530)
    IfFlagOff(1, 1121)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(27100200, host_only=True)


@NeverRestart
def Event11700510(ARG_0_3: int, ARG_4_7: int):
    """ 11700510: Event 11700510 """
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfFlagOn(2, ARG_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, ARG_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(ARG_0_3)
    IfFlagOn(0, 703)
    EnableFlag(ARG_4_7)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.hostile_ally)
    SaveRequest()


@NeverRestart
def Event11700520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700520: Event 11700520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11700530(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700530: Event 11700530 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1092)
    IfPlayerInsideRegion(1, 1702410)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    EnableFlag(11020694)
    EnableCharacter(ARG_0_3)
    DisableFlag(61700320)
    EndOfAnimation(1701506, 1)
    EnableObjectActivation(1701506, objact_param_id=27401, relative_idx=0)
    EnableObjectActivation(1701506, objact_param_id=27401, relative_idx=1)
    DisableObjectActivation(1701506, objact_param_id=27401, relative_idx=2)
    DisableObjectActivation(1701506, objact_param_id=27401, relative_idx=3)


@NeverRestart
def Event11700531(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700531: Event 11700531 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1093)
    IfFlagOn(1, 61700320)
    IfAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    EnableFlag(11700594)


@NeverRestart
def Event11700532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700532: Event 11700532 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1094)
    IfHost(1)
    IfPlayerOutsideRegion(1, 1702410)
    IfFlagOff(2, 1096)
    IfFlagOn(2, 1093)
    IfFlagOn(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    EnableFlag(11700594)
    EnableCharacter(ARG_0_3)
    WarpToEntity(ARG_0_3, destination=1702501, destination_type=Category.region, model_point=-1, set_draw_hitbox=1703300)
    IfBackreadEnabled(0, ARG_0_3)
    SetNest(ARG_0_3, 1702501)


@NeverRestart
def Event11700533(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11700533: Event 11700533 """
    SkipLinesIfFlagOn(2, 11700595)
    DisableObject(1701664)
    DisableObjectActivation(1701664, objact_param_id=-1)
    IfFlagOff(1, 1096)
    IfThisEventOff(1)
    IfFlagOn(1, 1095)
    IfFlagOn(1, 14)
    IfFlagOn(1, 728)
    IfFlagOn(1, 11700592)
    IfFlagOff(2, 1096)
    IfFlagOn(2, 1095)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)
    EnableCharacter(ARG_16_19)
    EnableFlag(11700595)


@NeverRestart
def Event11700538(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700538: Event 11700538 """
    DisableCharacter(1700500)
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1540)
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1513)
    IfFlagRangeAnyOn(1, 1501, 1511)
    IfAlive(1, ARG_0_3)
    IfFlagOn(2, 1541)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    EnableCharacter(1700500)
    SetDisplayMask(1700500, bit_index=1, switch_type=1)


@NeverRestart
def Event11700539(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700539: Event 11700539 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1541)
    IfDead(1, 1700500)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    WarpToEntity(ARG_0_3, destination=1700500, destination_type=Category.character, model_point=101, copy_draw_hitbox=1700500)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11700540(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700540: Event 11700540 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1542)
    IfFlagOn(1, 11700593)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1542)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11700545(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11700545: Event 11700545 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 724)
    IfFlagOn(2, 1181)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange(ARG_4_7, ARG_8_11)
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@RestartOnRest
def SetMimicTrap(chest: Object, hungry_mimic: Character, logan_mimic: Character, looter: Character, fed_flag: Flag,
                 mimic_region: Region):
    """ 11702010: Full Mimic event and looter death. Controls Logan's Mimics too. """
    AddSpecialEffect(hungry_mimic, 5421)
    ClearTargetList(hungry_mimic)
    ReplanAI(hungry_mimic)
    DisableCharacter(hungry_mimic)
    SetTeamType(logan_mimic, TeamType.white_phantom)

    if FlagEnabled(fed_flag):
        DisableObject(chest)
        DisableCharacter(looter)
        Kill(looter, False)
        return

    DisableCharacter(logan_mimic)
    EndOfAnimation(chest, 0)  # Open chest.

    await (HasSpecialEffect(PLAYER, SPEFFECT.MimicRing)
           and DialogPromptActivated(TEXT.SummonMimic, anchor_entity=chest, model_point=-1, anchor_type=Category.object,
                                     facing_angle=180.0, max_distance=2.0))

    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    Wait(1.0)
    ForceAnimation(PLAYER, 7897)

    DisableObject(chest)
    # AddSpecialEffect(hungry_mimic, 5421)
    # ClearTargetList(hungry_mimic)
    # ReplanAI(hungry_mimic)
    # WarpToEntity(hungry_mimic, mimic_region, destination_type=Category.region, short_warp=True)
    EnableCharacter(hungry_mimic)
    SetTeamType(hungry_mimic, TeamType.white_phantom)
    EnableInvincibility(hungry_mimic)
    DisableHealthBar(hungry_mimic)

    PlayerSpotted = Condition(IsTargeting(looter, PLAYER))

    await (PlayerSpotted
           or (HasSpecialEffect(hungry_mimic, 5421) and not IsTargeting(looter, PLAYER)
               and EntityWithinDistance(looter, hungry_mimic, 2.0)))

    if PlayerSpotted:
        # Disable Mimic and restart event.
        DisplayStatus(TEXT.Caught)
        EnableObject(chest)
        DisableCharacter(hungry_mimic)
        return RESTART

    WarpToEntity(looter, destination=hungry_mimic, destination_type=Category.character, model_point=100,
                 copy_draw_hitbox=hungry_mimic)
    ForceAnimation(looter, 7521, loop=False, wait_for_completion=False, skip_transition=False)
    AICommand(hungry_mimic, command_id=10, slot=0)
    ReplanAI(hungry_mimic)
    Wait(0.1)
    AICommand(hungry_mimic, command_id=-1, slot=0)

    await IsDead(looter)

    EnableFlag(fed_flag)
    Wait(1.0)
    DisplayStatus(TEXT.MimicSatiated)
    Wait(0.5)
    DisableCharacter(hungry_mimic)
    EnableCharacter(logan_mimic)
    EnableObject(chest)


@RestartOnRest
def ReturnToFirelink():
    """ 11702000: Crow takes you from the balcony back to Firelink. """
    EnableInvincibility(CHR.Crow)
    DisableHealthBar(CHR.Crow)
    await DialogPromptActivated(TEXT.ReturnToFirelink, anchor_entity=CHR.Crow, facing_angle=180.0, max_distance=3.0,
                                model_point=-1)
    WarpToMap(FIRELINK_SHRINE)
    Wait(3.0)
    return RESTART


@RestartOnRest
def RecruitLogan():
    """ 11702001: Recruit Logan after feeding all six Mimics. """
    if FLAG.LoganRecruited:
        DisableCharacter(CHR.Logan)
        return

    DisableGravity(CHR.Logan)
    EnableInvincibility(CHR.Logan)
    DisableHealthBar(CHR.Logan)
    SetTeamType(CHR.Logan, TeamType.white_phantom)
    SetStandbyAnimationSettings(CHR.Logan, 7830)

    await (FLAG.MimicRingGiven and FLAG.Mimic1Fed and FLAG.Mimic2Fed and FLAG.Mimic3Fed
           and FLAG.Mimic4Fed and FLAG.Mimic5Fed and FLAG.Mimic6Fed)

    await PlayerWithinDistance(CHR.LoganTalk, 5.0)

    Wait(1.0)
    EnableGravity(CHR.Logan)
    Wait(2.0)
    EnableFlag(FLAG.LoganRecruited)
    AddSpecialEffect(PLAYER, SPEFFECT.LoganReward)
    DisplayBanner(TextBannerType.magic_revival)
    Wait(5.0)
    WarpToMap(FIRELINK_SHRINE)


def ReturnHavelGear():
    """ 11702004: Give all of Havel's six equipment pieces back. """
    if FLAG.HavelGearReturned:
        return

    await DialogPromptActivated(TEXT.ReturnHavelGear, CHR.NakedHavel,
                                model_point=-1, facing_angle=180.0, max_distance=2.0)

    if (HasArmor(ARMOR.HavelsHelm) and HasArmor(ARMOR.HavelsArmor) and HasArmor(ARMOR.HavelsGauntlets)
            and HasArmor(ARMOR.HavelsLeggings)
            and HasWeapon(WEAPON.DragonTooth) and HasWeapon(WEAPON.HavelsGreatshield)):
        RemoveArmorFromPlayer(ARMOR.HavelsHelm)
        RemoveArmorFromPlayer(ARMOR.HavelsArmor)
        RemoveArmorFromPlayer(ARMOR.HavelsGauntlets)
        RemoveArmorFromPlayer(ARMOR.HavelsLeggings)
        RemoveWeaponFromPlayer(WEAPON.DragonTooth)
        RemoveWeaponFromPlayer(WEAPON.HavelsGreatshield)
        EnableFlag(FLAG.HavelGearReturned)
    else:
        DisplayDialog(TEXT.MissingHavelGear, CHR.Havel)
        Wait(3.0)
        return RESTART


@RestartOnRest
def RecruitHavel():
    """ 11702002: Recruit Havel after freeing him and giving him all his gear. """
    SetTeamType(CHR.Havel, TeamType.white_phantom)
    SetTeamType(CHR.NakedHavel, TeamType.white_phantom)

    if FLAG.HavelRecruited:
        DisableCharacter(CHR.Havel)
        DisableCharacter(CHR.NakedHavel)
        return

    DisableCharacter(CHR.Havel)

    await FLAG.HavelGearReturned

    DisableCharacter(CHR.NakedHavel)
    EnableCharacter(CHR.Havel)

    await FLAG.PisacasAllDead

    EnableFlag(FLAG.HavelRecruited)
    AddSpecialEffect(PLAYER, SPEFFECT.HavelReward)
    DisplayBanner(TextBannerType.magic_revival)
    Wait(4.0)
    DisableCharacter(CHR.Havel)
    # No warp back to Firelink.


@RestartOnRest
def PisacaBattle():
    """ 11702005: Control Pisacas and cell door activation for Havel rescue. """

    DisableMapSound(1703500)
    DisableAI(CHR.Havel)
    if THIS_FLAG:
        DisableCharacter(1700110)
        DisableCharacter(1700111)
        DisableCharacter(1700112)
        DisableCharacter(1700120)
        DisableCharacter(1700116)
        DisableCharacter(1700117)
        DisableCharacter(1700118)
        DisableCharacter(1700113)
        DisableCharacter(1700114)
        DisableCharacter(1700115)
        EnableFlag(FLAG.GiantCellIsOpen)
        EndOfAnimation(OBJECT.GiantCellDoor, 0)  # Open the door.
        DisableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=0)
        DisableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=1)
        DisableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=2)
        DisableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=3)
        return

    DisableFlag(FLAG.GiantCellIsOpen)
    EndOfAnimation(OBJECT.GiantCellDoor, 1)  # Close the door.
    EnableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=0)
    EnableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=1)
    EnableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=2)
    EnableObjectActivation(OBJECT.GiantCellDoor, objact_param_id=27401, relative_idx=3)

    SetTeamType(1700110, TeamType.white_phantom)
    SetTeamType(1700111, TeamType.white_phantom)
    SetTeamType(1700112, TeamType.white_phantom)
    SetTeamType(1700120, TeamType.white_phantom)
    SetTeamType(1700116, TeamType.white_phantom)
    SetTeamType(1700117, TeamType.white_phantom)
    SetTeamType(1700118, TeamType.white_phantom)
    SetTeamType(1700113, TeamType.white_phantom)
    SetTeamType(1700114, TeamType.white_phantom)
    SetTeamType(1700115, TeamType.white_phantom)
    DisableAI(1700110)
    DisableAI(1700111)
    DisableAI(1700112)
    DisableAI(1700120)
    DisableAI(1700116)
    DisableAI(1700117)
    DisableAI(1700118)
    DisableAI(1700113)
    DisableAI(1700114)
    DisableAI(1700115)

    await (FLAG.GiantCellIsOpen and FLAG.HavelGearReturned)

    EnableMapSound(1703500)
    EnableAI(CHR.Havel)
    AddSpecialEffect(CHR.Havel, SPEFFECT.HavelHealth)

    SetTeamType(1700110, TeamType.enemy)
    SetTeamType(1700111, TeamType.enemy)
    SetTeamType(1700112, TeamType.enemy)
    SetTeamType(1700120, TeamType.enemy)
    SetTeamType(1700116, TeamType.enemy)
    SetTeamType(1700117, TeamType.enemy)
    SetTeamType(1700118, TeamType.enemy)
    SetTeamType(1700113, TeamType.enemy)
    SetTeamType(1700114, TeamType.enemy)
    SetTeamType(1700115, TeamType.enemy)
    EnableAI(1700110)
    EnableAI(1700111)
    EnableAI(1700112)
    EnableAI(1700120)
    EnableAI(1700116)
    EnableAI(1700117)
    EnableAI(1700118)
    EnableAI(1700113)
    EnableAI(1700114)
    EnableAI(1700115)

    await (IsDead(1700110) and IsDead(1700111) and IsDead(1700112) and IsDead(1700120) and IsDead(1700116)
           and IsDead(1700117) and IsDead(1700118) and IsDead(1700113) and IsDead(1700114) and IsDead(1700115))

    DisableMapSound(1703500)

    await IsAlive(CHR.Havel)
    return


def GetMimicRing():
    """ 11702003: Get Mimic Ring from Logan. """
    if THIS_FLAG:
        return

    await DialogPromptActivated(TEXT.Talk, CHR.LoganTalk, facing_angle=180.0, max_distance=3.0, model_point=-1)

    DisplayStatus(TEXT.LoganInstructions)
    Wait(1.0)
    AwardItemLot(ITEMLOT.MimicRing)


def ApplyMimicRingStealth():
    """ 11702006: Get stealth. """
    await (HasSpecialEffect(PLAYER, SPEFFECT.MimicRing) and InsideMap(DUKES_ARCHIVES))
    AddSpecialEffect(PLAYER, SPEFFECT.MimicRingStealth)
    await (not HasSpecialEffect(PLAYER, SPEFFECT.MimicRing) or OutsideMap(DUKES_ARCHIVES))
    CancelSpecialEffect(PLAYER, SPEFFECT.MimicRingStealth)
    return RESTART
