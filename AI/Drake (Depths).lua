--@package: m10_00_00_00.luabnd, 352003_battle.lua
--@battle_goal: 352003, wyvern_on_earth352003Battle

-- "Sumade" reference to Valley of Drakes region removed.

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 2.3
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 2.5
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 4.3
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 8
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 8
local localScriptConfigVar10 = 0.5
local localScriptConfigVar11 = 7.3
local localScriptConfigVar12 = 4.5
local localScriptConfigVar13 = 13
wyvern_on_earth352003Battle_Activate = function(ai, goal)
   local func1_var2 = ai:GetRandam_Int(1, 100)
   local func1_var3 = ai:GetRandam_Int(1, 100)
   local func1_var4 = ai:GetRandam_Int(1, 100)
   local func1_var5 = ai:GetRandam_Int(1, 100)
   local func1_var6 = ai:GetRandam_Int(1, 100)
   local func1_var7 = 0
   local func1_var8 = ai:GetDist(TARGET_ENE_0)
   local func1_var9 = 0
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_F, 17.5) then
      func1_var9 = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_F, 12.8) then
      func1_var10 = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_F, 12.5) then
      func1_var11 = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_B, 11.6) then
      func1_var12 = 1
   end
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = 0
   local func1_var16 = 0
   local func1_var17 = 0
   local func1_var18 = 0
   local func1_var19 = 0
   local func1_var20 = 0
   local func1_var21 = 0
   local func1_var22 = 0
   local func1_var23 = 0
   local func1_var24 = 0
   local func1_var25 = 0
   local func1_var26 = 0
   if func1_var8 >= 8.5 and func1_var8 <= 14.5 and func1_var9 == 1 then
      func1_var24 = 150
   end
   if func1_var8 >= 4 and func1_var8 <= 8.2 and func1_var10 == 1 then
      func1_var20 = 150
   end
   if func1_var8 >= 0 and func1_var8 <= 6 and func1_var11 == 1 then
      func1_var23 = 150
   end
   if func1_var8 >= 0 and func1_var8 <= 1.5 and func1_var12 == 1 then
      func1_var19 = 150
   end
   if func1_var8 >= 6 then
      func1_var16 = 50
      func1_var17 = 50
      func1_var13 = 0
   elseif func1_var8 >= 2.5 then
      if ai:IsFinishTimer(0) == true then
         func1_var26 = 10
         func1_var16 = 20
         func1_var17 = 40
         func1_var13 = 40
      end
   elseif ai:IsFinishTimer(0) == true then
      func1_var26 = 40
      func1_var16 = 10
      func1_var17 = 15
      func1_var13 = 45
   end

   local func1_var27 = ai:GetRandam_Int(1, func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 + func1_var22 + func1_var23 + func1_var24 + func1_var25 + func1_var26)
   if func1_var27 <= func1_var13 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 100
   elseif func1_var27 <= func1_var13 + func1_var14 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 100
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar9, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3007, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 + func1_var22 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 + func1_var22 + func1_var23 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 + func1_var22 + func1_var23 + func1_var24 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3011, TARGET_ENE_0, DIST_Middle, 0)
      func1_var7 = 0
   elseif func1_var27 <= func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18 + func1_var19 + func1_var20 + func1_var21 + func1_var22 + func1_var23 + func1_var24 + func1_var25 then
      if func1_var4 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 0, 701, TARGET_NONE, -1, AI_DIR_TYPE_B, 4.2)
      elseif func1_var4 <= 75 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 0, 702, TARGET_NONE, -1, AI_DIR_TYPE_L, 4.2)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 0, 703, TARGET_NONE, -1, AI_DIR_TYPE_R, 4.2)
      end
      ai:SetTimer(0, 5)
   end
   local func1_var28 = ai:GetRandam_Int(1, 100)
   if func1_var28 <= func1_var7 then
      wyvern_on_earth352003_ActAfter_AdjustSpace(ai, goal)
   end
end

wyvern_on_earth352003_ActAfter_AdjustSpace = function(ai, goal)
end

OnIf_352003 = function(ai, goal, func4_param2)
   local func4_var3 = ai:GetRandam_Int(1, 100)
   local func4_var4 = ai:GetRandam_Int(1, 100)
   local func4_var5 = ai:GetRandam_Int(1, 100)
   local func4_var6 = ai:GetDist(TARGET_ENE_0)
   if func4_param2 == 0 then
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_SELF)
      goal:AddSubGoal(GOAL_COMMON_Turn, 2, TARGET_ENE_0, 0, 0, 0)
      GetWellSpace_Odds = 0
   end
end

wyvern_on_earth352003Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

wyvern_on_earth352003Battle_Terminate = function(ai, goal)
end

wyvern_on_earth352003Battle_Interupt = function(ai, goal)
   return false
end


