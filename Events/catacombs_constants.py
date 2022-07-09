import soulstruct.emevd.ds_types as dt


# Bone of Power: One Punch Man mode. Invincible and instant kill.
#   Found in the pit, but can only be picked up when the other four bones are found.
# Bone of Terror: Both you and all enemies (Bonewheels) move at double speed.
#   Dropped by "Black Knight" Bonewheel.
# Bone of Pain: Your HP is halved.
#   Found in the crypt behind the Titanite Demon.
# Bone of Death: Healing is disabled.
#   Found in the crypt behind the Giant Skeleton.
# Bone of Fervor: Pyromancy only. You receive the Pyromancy Flame, some pyromancies, and +5 attunement slots.
#   Found in the old secret bonfire room.


class CHR(dt.Character):
    Patches = 6320
    VamosBonewheel = 6200

    BlackKnightBonewheel = 1300400

    PitBonewheel1 = 1300600
    PitBonewheel2 = 1300601
    PitBonewheel3 = 1300602
    PitBonewheel4 = 1300603
    PitBonewheel5 = 1300604
    PitBonewheel6 = 1300605
    PitBonewheel7 = 1300606
    PitBonewheel8 = 1300607
    PitBonewheel9 = 1300608
    PitBonewheel10 = 1300609


class FLAG(dt.Flag):
    PatchesRecruited = 1902

    PatchesQuestReceived = 11302001
    OnePunchBoneTaken = 51300260
    OnePunchBoneTestComplete = 11302002


class GOOD(dt.Good):
    BoneOfFire = 301
    BoneOfDecay = 302
    BoneOfHaste = 303
    BoneOfWeakness = 304
    BoneOfTheOnePunchMan = 305


class ITEMLOT(dt.ItemLot):
    BoneOfHaste = 4520


class OBJECT(dt.Object):
    BoneOfTheOnePunchManCorpse = 1301675
    PitFog1 = 1301890
    PitFog2 = 1301892


class FX(dt.IntEnum):
    PitFog1 = 1301891
    PitFog2 = 1301893


class REGION(dt.Region):
    ReturnToFirelink = 1302675


class SPEFFECT(dt.IntEnum):
    BoneOfFire = 4720  # Pyromancy only.
    BoneOfDecay = 4721  # No healing.
    BoneOfHaste = 4722  # 150% speed.
    BoneOfWeakness = 4723  # Half health.
    BoneOfTheOnePunchMan = 4724  # Invincible and super powerful.
    BoneOfHasteEnemySpeed = 4725

    PatchesSoulReward = 4802  # 12000 souls


class TEXT(dt.Text):
    ReturnToFirelink = 10010140
    GiveBones = 10010154
    ProveYourWorth = 10010155
    ReceivePatchesQuest = 10010156
    LobosEZ = 10010157
    TakeRemains = 10010158
    YouAreNotWorthy = 10010159
    Talk = 10010200
    FinalBoneAppeared = 10010390
