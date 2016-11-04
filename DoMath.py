class DoMath(object):
    
    def _compute_team(self, summonerList, summoners):
    
        # A couple of initializations for later use
        total_mastery0 = total_mastery1 = total_mastery2 = total_mastery3 = total_mastery4 = 0
        specific_mastery0 = specific_mastery1 = specific_mastery2 = specific_mastery3 = specific_mastery4 = 0
        current_team_power = 0
        best_team_power = -1
        final_champ_zero = final_champ_one = final_champ_two = final_champ_three = final_champ_four = ''
        final_role_zero = final_role_one = final_role_two = final_role_three = final_role_four = ''
        valid_roles = ['MID', 'TOP', 'JUNGLE', 'DUO_CARRY', 'DUO_SUPPORT']
        champ_id_array = [0, 0, 0, 0, 0]
        
        # Find total mastery points per summoner (take the total points for each champion, and sum them)    
        for x0, mastered_champs0 in summonerList[0].items():
            for x0, champ_info0 in mastered_champs0.items():
                for role_info0 in champ_info0[1:]:
                    total_mastery0 += int(list(role_info0.values())[0])
    
        for x1, mastered_champs1 in summonerList[1].items():
            for x1, champ_info1 in mastered_champs1.items():
                for role_info1 in champ_info1[1:]:
                    total_mastery1 += int(list(role_info1.values())[0])
       
        for x2, mastered_champs2 in summonerList[2].items():
            for x2, champ_info2 in mastered_champs2.items():
                for role_info2 in champ_info2[1:]:
                    total_mastery2 += int(list(role_info2.values())[0])
       
        for x3, mastered_champs3 in summonerList[3].items():
            for x3, champ_info3 in mastered_champs3.items():
                for role_info3 in champ_info3[1:]:
                    total_mastery3 += int(list(role_info3.values())[0])
        
        for x4, mastered_champs4 in summonerList[4].items():
            for x4, champ_info4 in mastered_champs4.items():
                for role_info4 in champ_info4[1:]:
                    total_mastery4 += int(list(role_info4.values())[0])
                    
        # First we make sure we don't divide by zero at any point down the road
        if total_mastery0 == 0:
            total_mastery0 = 1
        if total_mastery1 == 0:
            total_mastery1 = 1
        if total_mastery2 == 0:
            total_mastery2 = 1
        if total_mastery3 == 0:
            total_mastery3 = 1
        if total_mastery4 == 0:
            total_mastery4 = 1

        # Iterate through team combinations and find the "valid" ones (ones with each of the 5 positions)
        # summonerList is a dictionary that maps a summoner ID to a list of champions.  x0 is the summoner ID, mastered_champs is a list of {champion id: [champsion name], {role, points}}
        for x0, mastered_champs0 in summonerList[0].items():
            #print (mastered_champs0)
            for x0, champ_info0 in mastered_champs0.items():
                    #print (champ_info0[1:]) -- {role: points}
                    #print (champ_info0[:1]) -- champ name
                    #print(x0) -- champ id
                    for role_info0 in champ_info0[1:]:
                        #print (role_info0) -- {role:points}
                        for role0 in role_info0:
                            #print ('summoner 0', x0, role0) -- summoner, champ id, role
                            # Empty any existing list of 'taken' roles and champions
                            roleList = []
                            champList = []
                            summoner_zero_role = role0
                            summoner_zero_champ = x0
                            summoner_zero_champ_name = champ_info0[:1]
                            # Skip if the role isn't a real role
                            if (summoner_zero_role not in valid_roles):
                                continue
                            # Otherwise, add it to a list of taken roles, and champs, and continue for the next summoner
                            roleList.append(summoner_zero_role)
                            champList.append(summoner_zero_champ)
                            for x1, mastered_champs1 in summonerList[1].items():
                                for x1, champ_info1 in mastered_champs1.items():
                                    #champList = champList[:1]
                                    for role_info1 in champ_info1[1:]:
                                        for role1 in role_info1:
                                            roleList = roleList[:1]
                                            champList = champList[:1]
                                            summoner_one_role = role1
                                            summoner_one_champ = x1
                                            summoner_one_champ_name = champ_info1[:1]
                                            if (summoner_one_role not in valid_roles 
                                                or summoner_one_role in roleList 
                                                or len(roleList) == 0 
                                                or summoner_one_champ in champList):
                                                continue
                                            roleList.append(summoner_one_role)
                                            champList.append(summoner_one_champ)
                                            for x2, mastered_champs2 in summonerList[2].items():
                                                for x2, champ_info2 in mastered_champs2.items():
                                                    for role_info2 in champ_info2[1:]:
                                                        for role2 in role_info2:
                                                            roleList = roleList[:2]
                                                            champList = champList[:2]
                                                            summoner_two_role = role2
                                                            summoner_two_champ = x2
                                                            summoner_two_champ_name = champ_info2[:1]
                                                            if (summoner_two_role not in valid_roles 
                                                                or summoner_two_role in roleList 
                                                                or len(roleList) <= 1 
                                                                or summoner_two_champ in champList):
                                                                continue
                                                            roleList.append(summoner_two_role)
                                                            champList.append(summoner_two_champ)
                                                            for x3, mastered_champs3 in summonerList[3].items():
                                                                for x3, champ_info3 in mastered_champs3.items():
                                                                    for role_info3 in champ_info3[1:]:
                                                                        for role3 in role_info3:
                                                                            roleList = roleList[:3]
                                                                            champList = champList[:3]
                                                                            summoner_three_role = role3
                                                                            summoner_three_champ = x3
                                                                            summoner_three_champ_name = champ_info3[:1]
                                                                            if (summoner_three_role not in valid_roles 
                                                                                or summoner_three_role in roleList 
                                                                                or len(roleList) <= 2 
                                                                                or summoner_three_champ in champList):
                                                                                continue
                                                                            champList.append(summoner_three_champ)
                                                                            roleList.append(summoner_three_role)
                                                                            for x4, mastered_champs4 in summonerList[4].items():
                                                                                for x4, champ_info4 in mastered_champs4.items():
                                                                                    for role_info4 in champ_info4[1:]:
                                                                                        for role4 in role_info4:
                                                                                            roleList = roleList[:4]
                                                                                            champList = champList[:4]
                                                                                            summoner_four_role = role4
                                                                                            summoner_four_champ = x4
                                                                                            summoner_four_champ_name = champ_info4[:1]
                                                                                            if (summoner_four_role not in valid_roles 
                                                                                                or summoner_four_role in roleList 
                                                                                                or len(roleList) <= 3 
                                                                                                or summoner_four_champ in champList):
                                                                                                continue
                                                                                            else:
                                                                                                # We found a team of 5 champions that fills each of the meta roles!!
                                                                                                champList.append(summoner_four_champ)
                                                                                                roleList.append(summoner_four_role)
                                                                                                # Do math to see if the team should be played
                                                                                                # Each champion gets its final point value determined by the following
                                                                                                # (Total points earned on that champion) * (Percentage of games played in that role) / (Total mastery points earned for the top X champions that we are testing)
                                                                                                specific_mastery0 = int(list(role_info0.values())[0]) / total_mastery0
                                                                                                specific_mastery1 = int(list(role_info1.values())[0]) / total_mastery1
                                                                                                specific_mastery2 = int(list(role_info2.values())[0]) / total_mastery2
                                                                                                specific_mastery3 = int(list(role_info3.values())[0]) / total_mastery3
                                                                                                specific_mastery4 = int(list(role_info4.values())[0]) / total_mastery4
                                                                                                current_team_power = specific_mastery0 + specific_mastery1 + specific_mastery2 + specific_mastery3 + specific_mastery4
                                                                                                # This team generation accomplishes a few things.  One, makes sure that you are playing the champion in the role you normally play in
                                                                                                # Two, it accounts for a player's relative skill on that champ compared to others.  One trick ponies are welcome here too
                                                                                                # Three, it maximizes the overall team composition without bias.  It works on numbers alone, so it can be used to fairly recommend a 
                                                                                                # composition even if everyone wants to play mid (because if you aren't saying 'mid or feed', are you really playing League?)
                                                                                                if current_team_power > best_team_power:
                                                                                                    best_team_power = current_team_power
                                                                                                    final_champ_zero = str(summoner_zero_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_one = str(summoner_one_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_two = str(summoner_two_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_three = str(summoner_three_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                                                                                                    final_champ_four = str(summoner_four_champ_name).replace('[', '').replace(']', '').replace("'", "").replace('"', '"')
                                                                                                    final_role_zero = str(summoner_zero_role)
                                                                                                    final_role_one = str(summoner_one_role)
                                                                                                    final_role_two = str(summoner_two_role)
                                                                                                    final_role_three = str(summoner_three_role)
                                                                                                    final_role_four = str(summoner_four_role)
                                                                                                    # For use with recalc.py
                                                                                                    champ_id_array[0] = summoner_zero_champ
                                                                                                    champ_id_array[1] = summoner_one_champ
                                                                                                    champ_id_array[2] = summoner_two_champ
                                                                                                    champ_id_array[3] = summoner_three_champ
                                                                                                    champ_id_array[4] = summoner_four_champ

        if best_team_power > 0:
            return (summoners[0] + ',' + final_champ_zero + ',' + final_role_zero + ',' + summoners[1] + ',' + final_champ_one + ',' + final_role_one + ',' + summoners[2] + ',' + final_champ_two + ','
                                + final_role_two + ',' + summoners[3] + ',' + final_champ_three + ',' + final_role_three + ',' + summoners[4] + ',' + final_champ_four + ',' + final_role_four + ',' 
                                + str(champ_id_array[0]) + ',' + str(champ_id_array[1]) + ',' + str(champ_id_array[2]) + ',' + str(champ_id_array[3]) + ',' + str(champ_id_array[4]))
        else:
            return ('An ideal team could not be found')                                                                                   