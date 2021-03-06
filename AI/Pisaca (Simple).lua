--@package: m17_00_00_00.luabnd, 333000_battle.lua
--@battle_goal: 333000, Pisaca333000Battle

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 4
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 4.5
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 5
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 7
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 10
Pisaca333000Battle_Activate = function(ai, goal)
   local func1_var2 = ai:GetTeamOrder(ORDER_TYPE_Role)
   local func1_var3 = ai:GetDist(TARGET_ENE_0)
   local func1_var4 = ai:GetRandam_Int(1, 100)
   local func1_var5 = ai:GetRandam_Int(1, 100)
   local func1_var6 = ai:GetRandam_Int(1, 100)
   local func1_var8 = ai:GetExcelParam(AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer)
   local func1_var9 = ai:GetTeamOrder(ORDER_TYPE_Role)
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = 0
   local func1_var16 = 0
   local func1_var17 = 0
   local func1_var18 = 0
   if func1_var8 == 1 and func1_var9 == ROLE_TYPE_Torimaki then
      Torimaki_Act(ai, goal, func1_var10)
   elseif func1_var8 == 1 and func1_var9 == ROLE_TYPE_Kankyaku then
      Kankyaku_Act(ai, goal, func1_var10)
   elseif func1_var3 >= 10 then
      func1_var12 = 30
      func1_var13 = 0
      func1_var14 = 70
      func1_var15 = 0
   elseif func1_var3 >= 6 then
      func1_var12 = 20
      func1_var13 = 20
      func1_var14 = 60
      func1_var15 = 0
   elseif func1_var3 >= 3 then
      func1_var12 = 0
      func1_var13 = 30
      func1_var14 = 35
      func1_var15 = 35
   else
      func1_var12 = 0
      func1_var13 = 10
      func1_var14 = 35
      func1_var15 = 55
   end
   local func1_var19 = ai:GetRandam_Int(1, func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 + func1_var18)
   if func1_var19 <= func1_var12 then
      if localScriptConfigVar8 <= func1_var3 and func1_var4 <= 40 then
         local func1_var20 = localScriptConfigVar9
         local func1_var21 = localScriptConfigVar9 + 2
         local func1_var22 = 0
         local func1_var23 = 3005
         local func1_var24 = DIST_Middle
         Approach_and_Attack_Act(ai, goal, func1_var20, func1_var21, func1_var22, func1_var23, func1_var24)
      else
         local func1_var20 = localScriptConfigVar7
         local func1_var21 = localScriptConfigVar7 + 2
         local func1_var22 = 0
         local func1_var23 = 3004
         local func1_var24 = DIST_Middle
         Approach_and_Attack_Act(ai, goal, func1_var20, func1_var21, func1_var22, func1_var23, func1_var24)
      end
      func1_var11 = 100
   elseif func1_var19 <= func1_var12 + func1_var13 then
      local func1_var20 = localScriptConfigVar3
      local func1_var21 = localScriptConfigVar3 + 100
      local func1_var22 = 0
      local func1_var23 = 3002
      local func1_var24 = DIST_Middle
      Approach_and_Attack_Act(ai, goal, func1_var20, func1_var21, func1_var22, func1_var23, func1_var24)
      func1_var11 = 100
   elseif func1_var19 <= func1_var12 + func1_var13 + func1_var14 then
      local func1_var20 = localScriptConfigVar5
      local func1_var21 = localScriptConfigVar5 + 2
      local func1_var22 = 0
      local func1_var23 = 3003
      local func1_var24 = DIST_Middle
      Approach_and_Attack_Act(ai, goal, func1_var20, func1_var21, func1_var22, func1_var23, func1_var24)
      func1_var11 = 100
   elseif func1_var19 <= func1_var12 + func1_var13 + func1_var14 + func1_var15 then
      local func1_var20 = localScriptConfigVar1
      local func1_var21 = localScriptConfigVar1 + 1
      local func1_var22 = 0
      Approach_Act(ai, goal, func1_var20, func1_var21, func1_var22)
      if func1_var4 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      end
      func1_var11 = 100
   elseif func1_var19 <= func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 then
      -- Nothing.
   elseif func1_var19 <= func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 then
      -- Nothing
   else
      goal:AddSubGoal(GOAL_COMMON_Wait, 5, TARGET_NONE, 0, 0, 0)
      func1_var11 = 0
   end
   local func1_var20 = ai:GetRandam_Int(1, 100)
   if func1_var20 <= func1_var11 then
      local func1_var21 = 0
      local func1_var22 = 30
      local func1_var23 = 0
      local func1_var24 = 20
      local func1_var25 = 50
      local func1_var26 = 0
      GetWellSpace_Act(ai, goal, func1_var21, func1_var22, func1_var23, func1_var24, func1_var25, func1_var26)
   end
end

Pisaca333000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Pisaca333000Battle_Terminate = function(ai, goal)
end

Pisaca333000Battle_Interupt = function(ai, goal)
   local func4_var2 = ai:GetRandam_Int(1, 100)
   local func4_var3 = ai:GetRandam_Int(1, 100)
   local func4_var4 = ai:GetRandam_Int(1, 100)
   local func4_var5 = ai:GetDist(TARGET_ENE_0)
   local func4_var6 = ai:GetEventRequest(0)
   local func4_var7 = 30
   local func4_var8 = 30
   local func4_var9 = 35
   local func4_var10 = 35
   local func4_var11 = 3.5
   if RebByOpGuard_Step(ai, goal, func4_var7, func4_var8, func4_var9, func4_var10, func4_var11) then
      return true
   end
   if func4_var6 == 3 and ai:IsInterupt(INTERUPT_Damaged) then
      if func4_var5 >= 10 then
         local func4_var12 = localScriptConfigVar7
         local func4_var13 = localScriptConfigVar7 + 0
         local func4_var14 = 0
         local func4_var15 = 3004
         local func4_var16 = DIST_Middle
         Approach_and_Attack_Act(ai, goal, func4_var12, func4_var13, func4_var14, func4_var15, func4_var16)
         return true
      elseif func4_var5 >= 5 then
         local func4_var12 = localScriptConfigVar3
         local func4_var13 = localScriptConfigVar3 + 0
         local func4_var14 = 0
         local func4_var15 = 3002
         local func4_var16 = DIST_Middle
         Approach_and_Attack_Act(ai, goal, func4_var12, func4_var13, func4_var14, func4_var15, func4_var16)
         return true
      end
   end
   return false
end


