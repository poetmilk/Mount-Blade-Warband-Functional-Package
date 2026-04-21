
# 新加点系统初始化参数
("init_new_game_character_system",
[
    (assign, "$g_pm_auto_point_base_slot", 1600),  # 设置基础槽的值
    (assign, "$g_pm_auto_point_base_slot_part", 1800),  # 设置部分trp的基础槽的值

    (store_add, ":slot_trp_auto_1931", "$g_pm_auto_point_base_slot_part", 131), # 铁 骨 1931
    (store_add, ":slot_trp_auto_1932", "$g_pm_auto_point_base_slot_part", 132), # 强 击 1932
    (store_add, ":slot_trp_auto_1933", "$g_pm_auto_point_base_slot_part", 133), # 强 掷 1933
    (store_add, ":slot_trp_auto_1934", "$g_pm_auto_point_base_slot_part", 134), # 强 弓 1934
    (store_add, ":slot_trp_auto_1935", "$g_pm_auto_point_base_slot_part", 135), # 武 器 掌 握 1935
    (store_add, ":slot_trp_auto_1936", "$g_pm_auto_point_base_slot_part", 136), # 盾 防 1936
    (store_add, ":slot_trp_auto_1937", "$g_pm_auto_point_base_slot_part", 137), # 跑 动 1937
    (store_add, ":slot_trp_auto_1938", "$g_pm_auto_point_base_slot_part", 138), # 骑 术 1938
    (store_add, ":slot_trp_auto_1939", "$g_pm_auto_point_base_slot_part", 139), # 骑 射 1939
    (store_add, ":slot_trp_auto_1940", "$g_pm_auto_point_base_slot_part", 140), # 掠 夺 1940
    (store_add, ":slot_trp_auto_1941", "$g_pm_auto_point_base_slot_part", 141), # 教 练 1941
    (store_add, ":slot_trp_auto_1942", "$g_pm_auto_point_base_slot_part", 142), # 追 踪 1942
    (store_add, ":slot_trp_auto_1943", "$g_pm_auto_point_base_slot_part", 143), # 战 术 1943
    (store_add, ":slot_trp_auto_1944", "$g_pm_auto_point_base_slot_part", 144), # 向 导 1944
    (store_add, ":slot_trp_auto_1945", "$g_pm_auto_point_base_slot_part", 145), # 侦 察 1945
    (store_add, ":slot_trp_auto_1946", "$g_pm_auto_point_base_slot_part", 146), # 辎 重 管 理 1946
    (store_add, ":slot_trp_auto_1947", "$g_pm_auto_point_base_slot_part", 147), # 疗 伤 1947
    (store_add, ":slot_trp_auto_1948", "$g_pm_auto_point_base_slot_part", 148), # 手 术 1948
    (store_add, ":slot_trp_auto_1949", "$g_pm_auto_point_base_slot_part", 149), # 急 救 1949
    (store_add, ":slot_trp_auto_1950", "$g_pm_auto_point_base_slot_part", 150), # 工 程 学 1950
    (store_add, ":slot_trp_auto_1951", "$g_pm_auto_point_base_slot_part", 151), # 说 服 力 1951
    (store_add, ":slot_trp_auto_1952", "$g_pm_auto_point_base_slot_part", 152), # 俘 虏 管 理 1952
    (store_add, ":slot_trp_auto_1953", "$g_pm_auto_point_base_slot_part", 153), # 统 御 1953
    (store_add, ":slot_trp_auto_1954", "$g_pm_auto_point_base_slot_part", 154), # 交 易 1954
    # ========== 设置技能点的上限值 ==========  
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1931", 10), # 铁 骨 1931 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1932", 10), # 强 击 1932 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1933", 10), # 强 掷 1933 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1934", 10), # 强 弓 1934 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1935", 10), # 武 器 掌 握 1935 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1936", 10), # 盾 防 1936 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1937", 10), # 跑 动 1937 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1938", 10), # 骑 术 1938 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1939", 10), # 骑 射 1939 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1940", 10), # 掠 夺 1940 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1941", 10), # 教 练 1941 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1942", 10), # 追 踪 1942 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1943", 10), # 战 术 1943 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1944", 10), # 向 导 1944 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1945", 10), # 侦 察 1945 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1946", 10), # 辎 重 管 理 1946 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1947", 10), # 疗 伤 1947 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1948", 10), # 手 术 1948 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1949", 10), # 急 救 1949 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1950", 10), # 工 程 学 1950 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1951", 10), # 说 服 力 1951 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1952", 10), # 俘 虏 管 理 1952 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1953", 10), # 统 御 1953 
    (troop_set_slot, "trp_auto_temp_list_3", ":slot_trp_auto_1954", 10), # 交 易 1954 

    # 定义属性可加点的最大值-包含这个值-
    # 战团默认的最大值是63，超过这个值会有bug
    # 如果想超过这个默认值，需要使用wse，并修改wse的配置文件，WSE2里的rgl_config文件，搜索iAttributeLimit
    (assign, "$g_pm_auto_property_max", 63),  
    (assign, "$g_pm_reset_price_per_attr_point", 1000),  # 洗点时1属性点价格
    (assign, "$g_pm_reset_price_per_skill_point", 500),  # 洗点时1技能点价格


    (try_for_range, ":troop", 0, "trp_burning_object"),
        (troop_is_hero, ":troop"),
        (this_or_next|eq, ":troop", "trp_player"),
        (this_or_next|eq, ":troop", "trp_kingdom_1_pretender"),
        (this_or_next|is_between, ":troop", "trp_npc_01", "trp_hero_red_sir_actus"),  # 子mod提拔的npc
        (is_between, ":troop", "trp_npc_adonja", "trp_kingdom_1_lord"),  # 这些NPC才能进行加点操作

        # 这里对NPC更换装备的所需要的玩家等级进行限制，如果玩家没达到该等级，则无法进行换装
        (store_add, ":auto_all_slot_1629", "$g_pm_auto_point_base_slot", 29), # 1629
        (try_begin),
            (this_or_next|eq, ":troop", "trp_npc_lethaldiran"),
            (eq, ":troop", "trp_kingdom_1_pretender"),
            (troop_set_slot, ":troop", ":auto_all_slot_1629", 30), 
        (else_try),
            (this_or_next|eq, ":troop", "trp_npc_alistair"),
            (this_or_next|eq, ":troop", "trp_npc_rayne"),
            (this_or_next|eq, ":troop", "trp_npc_roland"),
            (this_or_next|eq, ":troop", "trp_npc_frederick"), 
            (eq, ":troop", "trp_npc_boadice"),
            (troop_set_slot, ":troop", ":auto_all_slot_1629", 25), 
        (else_try),
            (troop_set_slot, ":troop", ":auto_all_slot_1629", 0),  # 默认就是只要0级就可以
        (try_end),

        # ========== 获取初始属性、技能、武器熟练度 ==========   
        # 设置该槽值为1，代表可以进行加点操作的troop
        (store_add, ":auto_all_slot_1630", "$g_pm_auto_point_base_slot", 30), # 1630
        (troop_set_slot, ":troop", ":auto_all_slot_1630", 1), 

        # 获取初始等级
        (store_character_level, ":var_begin_character_level", ":troop"), # 获取角色等级
        # 存储初始等级到槽里
        (store_add, ":auto_all_slot_1621", "$g_pm_auto_point_base_slot", 21), # 1621
        (troop_set_slot, ":troop", ":auto_all_slot_1621", ":var_begin_character_level"), 
        # 存储之前等级到槽里
        (store_add, ":auto_all_slot_1601", "$g_pm_auto_point_base_slot", 1), # 1601
        (troop_set_slot, ":troop", ":auto_all_slot_1601", ":var_begin_character_level"), 

        # 获取玩家的这些属性
        (store_attribute_level, ":var_begin_ca_strength", ":troop", ca_strength), # 获取初始力量属性
        (store_attribute_level, ":var_begin_ca_agility", ":troop", ca_agility), # 获取初始敏捷属性
        (store_attribute_level, ":var_begin_ca_intelligence", ":troop", ca_intelligence), # 获取初始智力属性
        (store_attribute_level, ":var_begin_ca_charisma", ":troop", ca_charisma), # 获取初始魅力属性

        # 存储智力到槽里
        (store_add, ":auto_all_slot_1610", "$g_pm_auto_point_base_slot", 10), # 1610
        (troop_set_slot, ":troop", ":auto_all_slot_1610", ":var_begin_ca_intelligence"), 

        # 存储初始属性到槽里
        (store_add, ":auto_all_slot_1622", "$g_pm_auto_point_base_slot", 22), # 1622
        (troop_set_slot, ":troop", ":auto_all_slot_1622", ":var_begin_ca_strength"), 
        (store_add, ":auto_all_slot_1623", "$g_pm_auto_point_base_slot", 23), # 1623
        (troop_set_slot, ":troop", ":auto_all_slot_1623", ":var_begin_ca_agility"), 
        (store_add, ":auto_all_slot_1624", "$g_pm_auto_point_base_slot", 24), # 1624
        (troop_set_slot, ":troop", ":auto_all_slot_1624", ":var_begin_ca_intelligence"), 
        (store_add, ":auto_all_slot_1625", "$g_pm_auto_point_base_slot", 25), # 1625
        (troop_set_slot, ":troop", ":auto_all_slot_1625", ":var_begin_ca_charisma"), 
        # 存储之前的属性到槽里
        (store_add, ":auto_all_slot_1602", "$g_pm_auto_point_base_slot", 2), # 1602
        (troop_set_slot, ":troop", ":auto_all_slot_1602", ":var_begin_ca_agility"), 
        (store_add, ":auto_all_slot_1603", "$g_pm_auto_point_base_slot", 3), # 1603
        (troop_set_slot, ":troop", ":auto_all_slot_1603", ":var_begin_ca_intelligence"), 
        (store_add, ":auto_all_slot_1605", "$g_pm_auto_point_base_slot", 5), # 1605
        (troop_set_slot, ":troop", ":auto_all_slot_1605", ":var_begin_ca_charisma"), 
        (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
        (troop_set_slot, ":troop", ":auto_all_slot_1613", 0),  # 设置待加属性点为0
        (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
        (troop_set_slot, ":troop", ":auto_all_slot_1614", 0),  # 设置待加技能点为0
        (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
        (troop_set_slot, ":troop", ":auto_all_slot_1615", 0),  # 设置待加武器点为0

        # 保存同伴初始技能等级，后续用于洗点
        (store_add, ":auto_all_slot_1654", "$g_pm_auto_point_base_slot", 54), # 1654
        (assign, ":operate_index", ":auto_all_slot_1654"),
        (try_for_range, ":sub_idx", 0, 37),
            (this_or_next|eq, ":sub_idx", "skl_ironflesh"),
            (this_or_next|eq, ":sub_idx", "skl_power_strike"),
            (this_or_next|eq, ":sub_idx", "skl_power_throw"),
            (this_or_next|eq, ":sub_idx", "skl_power_draw"),
            (this_or_next|eq, ":sub_idx", "skl_weapon_master"),
            (this_or_next|eq, ":sub_idx", "skl_shield"),
            (this_or_next|eq, ":sub_idx", "skl_athletics"),
            (this_or_next|eq, ":sub_idx", "skl_riding"),
            (this_or_next|eq, ":sub_idx", "skl_horse_archery"),
            (this_or_next|eq, ":sub_idx", "skl_looting"),
            (this_or_next|eq, ":sub_idx", "skl_trainer"),
            (this_or_next|eq, ":sub_idx", "skl_tracking"),
            (this_or_next|eq, ":sub_idx", "skl_tactics"),
            (this_or_next|eq, ":sub_idx", "skl_pathfinding"),
            (this_or_next|eq, ":sub_idx", "skl_spotting"),
            (this_or_next|eq, ":sub_idx", "skl_inventory_management"),
            (this_or_next|eq, ":sub_idx", "skl_wound_treatment"),
            (this_or_next|eq, ":sub_idx", "skl_surgery"),
            (this_or_next|eq, ":sub_idx", "skl_first_aid"),
            (this_or_next|eq, ":sub_idx", "skl_engineer"),
            (this_or_next|eq, ":sub_idx", "skl_persuasion"),
            (this_or_next|eq, ":sub_idx", "skl_prisoner_management"),
            (this_or_next|eq, ":sub_idx", "skl_leadership"),
            (eq, ":sub_idx", "skl_trade"),
            (store_skill_level, reg10, ":sub_idx", ":troop"),  # 获取当前技能的数值
            (troop_set_slot, ":troop", ":operate_index", reg10),  # 赋值给存储初始技能数值的对应槽
            (val_sub, ":operate_index", 1),
        (try_end),

       
    (try_end),

    # ==============================================
    # 初始化10个预设自动加点方案的槽值-trp_auto_point
    # ==============================================
    # 方案
    #(assign, ":tmp_offset", 2001),
    (store_add, ":tmp_offset", "$g_pm_auto_point_base_slot_part", 201), # 2001
    (try_for_range, ":stack_index", 0, 71),
        (try_for_range, ":programme_index", 0, 10),
            # 计算索引值
            (store_mul, ":tmp_mul", ":programme_index", 100),
            (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
            (val_add, ":tmp_trp_index", ":tmp_mul"), 

            # ==============================================
            # 初始化默认的方案的值
            # ==============================================
            (try_begin),
                (eq, ":stack_index", 0), # 方案名称
                (try_begin),  # 这个区间用单数
                    (is_between, ":programme_index", 0, 5), 
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", ":programme_index"),
                    (str_store_string, s7, "str_auto_point_input_default_none"),
                    (troop_set_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),  # 这个区间用复数
                    (is_between, ":programme_index", 5, 10),
                    (store_sub, ":programme_index_sub_5", ":programme_index", 5),
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", ":programme_index_sub_5"),
                    (str_store_string, s7, "str_auto_point_input_default_none"),
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (try_end),
            (else_try),
                (is_between, ":stack_index", 1, 24),  # 10个方案的下拉框对象值全部设置为-未选择
                (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 0),  # 0就是最后一项-未选择，24是铁骨
            (else_try),
                (is_between, ":stack_index", 24, 47),
                (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 0),  # 技能的目标值为0
            (else_try),
                (is_between, ":stack_index", 47, 70),
                (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 0),  # 是否强行加智力来增加值-否
            (try_end),

            (try_begin),
                # ==============================================
                # 步兵自动加点方案 
                # ==============================================
                (eq, ":programme_index", 9), # 步兵方案
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    #(troop_set_slot, "trp_auto_point", ":tmp_trp_index", "str_auto_point_input_default_infantry"), # 设置方案名称
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", 4), 
                    (str_store_string, s7, "str_auto_point_input_default_infantry"), 
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),
                    (is_between, ":stack_index", 1, 24),  
                    (try_begin),
                        (eq, ":stack_index", 1), # 第1个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 2), # 第2个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 3), # 第3个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 4), # 第4个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 5), # 第5个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷
                    (else_try),
                        (eq, ":stack_index", 6), # 第6个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 18),  # 下拉框升级的技能-跑动

                    (else_try),
                        (eq, ":stack_index", 7), # 第7个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 8), # 第8个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 9), # 第9个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 10), # 第10个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 11), # 第11个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷
                    (else_try),
                        (eq, ":stack_index", 12), # 第12个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 18),  # 下拉框升级的技能-跑动

                    (else_try),
                        (eq, ":stack_index", 13), # 第13个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 14), # 第14个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 15), # 第15个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 16), # 第16个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 17), # 第17个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷
                    (else_try),
                        (eq, ":stack_index", 18), # 第18个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 18),  # 下拉框升级的技能-跑动
                    (try_end),
                (else_try),
                    (is_between, ":stack_index", 24, 47),
                    (try_begin),
                        (eq, ":stack_index", 24), # 第1个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强击-升到3
                    (else_try),
                        (eq, ":stack_index", 25), # 第2个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-武器掌握-升到3
                    (else_try),
                        (eq, ":stack_index", 26), # 第3个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-铁骨-升到3
                    (else_try),
                        (eq, ":stack_index", 27), # 第4个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-盾防-升到3
                    (else_try),
                        (eq, ":stack_index", 28), # 第5个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强掷-升到3
                    (else_try),
                        (eq, ":stack_index", 29), # 第6个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-跑动-升到3

                    (else_try),
                        (eq, ":stack_index", 30), # 第7个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强击-升到6
                    (else_try),
                        (eq, ":stack_index", 31), # 第8个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-武器掌握-升到6
                    (else_try),
                        (eq, ":stack_index", 32), # 第9个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-铁骨-升到6
                    (else_try),
                        (eq, ":stack_index", 33), # 第10个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-盾防-升到6
                    (else_try),
                        (eq, ":stack_index", 34), # 第11个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强掷-升到6
                    (else_try),
                        (eq, ":stack_index", 35), # 第12个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-跑动-升到6

                    (else_try),
                        (eq, ":stack_index", 36), # 第13个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强击-升到10
                    (else_try),
                        (eq, ":stack_index", 37), # 第14个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-武器掌握-升到10
                    (else_try),
                        (eq, ":stack_index", 38), # 第15个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到10
                    (else_try),
                        (eq, ":stack_index", 39), # 第16个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-盾防-升到10
                    (else_try),
                        (eq, ":stack_index", 40), # 第17个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强掷-升到10
                    (else_try),
                        (eq, ":stack_index", 41), # 第18个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-跑动-升到10
                    (try_end),
                # (else_try),
                #     (is_between, ":stack_index", 47, 70),
                #     (try_begin),
                #         (eq, ":stack_index", 47), # 第一个升级的技能-是否通过点智力强行升级
                #         (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 0),  # 是否强行加智力来增加值-否
                #     (else_try),
                #         (eq, ":stack_index", 48), # 第二个升级的技能-值
                #         (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 0),  # 铁骨升级到10
                #     (try_end),
                (try_end),
            (else_try),
                # ==============================================
                # 骑兵自动加点方案 
                # ==============================================
                (eq, ":programme_index", 8), # 骑兵方案
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    #(troop_set_slot, "trp_auto_point", ":tmp_trp_index", "str_auto_point_input_default_cavalry"), # 设置方案名称
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", 3),
                    (str_store_string, s7, "str_auto_point_input_default_cavalry"),
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),
                    (is_between, ":stack_index", 1, 24),  
                    (try_begin),
                        (eq, ":stack_index", 1), # 第1个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 2), # 第2个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 3), # 第3个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 4), # 第4个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 5), # 第5个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 6), # 第6个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷

                    (else_try),
                        (eq, ":stack_index", 7), # 第7个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 8), # 第8个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 9), # 第9个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 10), # 第10个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 11), # 第11个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 12), # 第12个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷

                    (else_try),
                        (eq, ":stack_index", 13), # 第13个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击 依次类推 交易是1
                    (else_try),
                        (eq, ":stack_index", 14), # 第14个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 15), # 第15个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 16), # 第16个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 17), # 第17个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (else_try),
                        (eq, ":stack_index", 18), # 第18个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 22),  # 下拉框升级的技能-强掷
                    (try_end),
                (else_try),
                    (is_between, ":stack_index", 24, 47),
                    (try_begin),
                        (eq, ":stack_index", 24), # 第1个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强击-升到3
                    (else_try),
                        (eq, ":stack_index", 25), # 第2个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-武器掌握-升到3
                    (else_try),
                        (eq, ":stack_index", 26), # 第3个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-骑术-升到3
                    (else_try),
                        (eq, ":stack_index", 27), # 第4个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-铁骨-升到3
                    (else_try),
                        (eq, ":stack_index", 28), # 第5个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-盾防-升到3
                    (else_try),
                        (eq, ":stack_index", 29), # 第6个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强掷-升到3

                    (else_try),
                        (eq, ":stack_index", 30), # 第7个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强击-升到6
                    (else_try),
                        (eq, ":stack_index", 31), # 第8个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-武器掌握-升到6
                    (else_try),
                        (eq, ":stack_index", 32), # 第9个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-骑术-升到6
                    (else_try),
                        (eq, ":stack_index", 33), # 第10个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-铁骨-升到6
                    (else_try),
                        (eq, ":stack_index", 34), # 第11个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-盾防-升到6
                    (else_try),
                        (eq, ":stack_index", 35), # 第12个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强掷-升到6

                    (else_try),
                        (eq, ":stack_index", 36), # 第13个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强击-升到10
                    (else_try),
                        (eq, ":stack_index", 37), # 第14个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-武器掌握-升到10
                    (else_try),
                        (eq, ":stack_index", 38), # 第15个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-骑术-升到10
                    (else_try),
                        (eq, ":stack_index", 39), # 第16个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到10
                    (else_try),
                        (eq, ":stack_index", 40), # 第17个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-盾防-升到10
                    (else_try),
                        (eq, ":stack_index", 41), # 第18个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强掷-升到10
                    (try_end),



                (try_end),

            (else_try),
                # ==============================================
                # 弓兵自动加点方案 
                # ==============================================
                (eq, ":programme_index", 7), # 弓兵方案 
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    #(troop_set_slot, "trp_auto_point", ":tmp_trp_index", "str_auto_point_input_default_archers"), # 设置方案名称
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", 2),
                    (str_store_string, s7, "str_auto_point_input_default_archers"),
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),
                    (is_between, ":stack_index", 1, 24),  
                    (try_begin),
                        (eq, ":stack_index", 1), # 第1个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 2), # 第2个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 3), # 第3个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 4), # 第4个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨

                    (else_try),
                        (eq, ":stack_index", 5), # 第5个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 6), # 第6个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 7), # 第7个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 8), # 第8个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨

                    (else_try),
                        (eq, ":stack_index", 9), # 第9个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 10), # 第10个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 11), # 第11个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 12), # 第12个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (try_end),
                (else_try),
                    (is_between, ":stack_index", 24, 47),
                    (try_begin),
                        (eq, ":stack_index", 24), # 第1个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强弓-升到3
                    (else_try),
                        (eq, ":stack_index", 25), # 第2个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-武器掌握-升到3
                    (else_try),
                        (eq, ":stack_index", 26), # 第3个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强击-升到3
                    (else_try),
                        (eq, ":stack_index", 27), # 第4个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-铁骨-升到3

                    (else_try),
                        (eq, ":stack_index", 28), # 第5个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强弓-升到6
                    (else_try),
                        (eq, ":stack_index", 29), # 第6个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-武器掌握-升到6
                    (else_try),
                        (eq, ":stack_index", 30), # 第7个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强击-升到6
                    (else_try),
                        (eq, ":stack_index", 31), # 第8个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-铁骨-升到6

                    (else_try),
                        (eq, ":stack_index", 32), # 第9个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强弓-升到10
                    (else_try),
                        (eq, ":stack_index", 33), # 第10个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-武器掌握-升到10
                    (else_try),
                        (eq, ":stack_index", 34), # 第11个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强击-升到10
                    (else_try),
                        (eq, ":stack_index", 35), # 第12个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到10
                    (try_end),



                (try_end),

            (else_try),
                # ==============================================
                # 弓骑兵自动加点方案 
                # ==============================================
                (eq, ":programme_index", 6), # 弓骑兵方案 
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    #(troop_set_slot, "trp_auto_point", ":tmp_trp_index", "str_auto_point_input_default_horse_archers"), # 设置方案名称
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", 1),
                    (str_store_string, s7, "str_auto_point_input_default_horse_archers"),
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),
                    (is_between, ":stack_index", 1, 24),  
                    (try_begin),
                        (eq, ":stack_index", 1), # 第1个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 2), # 第2个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 3), # 第3个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 4), # 第4个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 16),  # 下拉框升级的技能-骑射
                    (else_try),
                        (eq, ":stack_index", 5), # 第5个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 6), # 第6个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 7), # 第7个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防

                    (else_try),
                        (eq, ":stack_index", 8), # 第8个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 9), # 第9个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 10), # 第10个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 11), # 第11个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 16),  # 下拉框升级的技能-骑射
                    (else_try),
                        (eq, ":stack_index", 12), # 第12个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 13), # 第13个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 14), # 第14个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防

                    (else_try),
                        (eq, ":stack_index", 15), # 第15个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 21),  # 下拉框升级的技能-强弓
                    (else_try),
                        (eq, ":stack_index", 16), # 第16个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 17), # 第17个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 17),  # 下拉框升级的技能-骑术
                    (else_try),
                        (eq, ":stack_index", 18), # 第18个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 16),  # 下拉框升级的技能-骑射
                    (else_try),
                        (eq, ":stack_index", 19), # 第19个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 20), # 第20个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 21), # 第21个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (try_end),
                (else_try),
                    (is_between, ":stack_index", 24, 47),
                    (try_begin),
                        (eq, ":stack_index", 24), # 第1个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强弓-升到3
                    (else_try),
                        (eq, ":stack_index", 25), # 第2个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-武器掌握-升到3
                    (else_try),
                        (eq, ":stack_index", 26), # 第3个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-骑术-升到3
                    (else_try),
                        (eq, ":stack_index", 27), # 第4个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-骑射-升到3
                    (else_try),
                        (eq, ":stack_index", 28), # 第5个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强击-升到3
                    (else_try),
                        (eq, ":stack_index", 29), # 第6个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-铁骨-升到3
                    (else_try),
                        (eq, ":stack_index", 30), # 第7个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-盾防-升到3

                    (else_try),
                        (eq, ":stack_index", 31), # 第8个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强弓-升到6
                    (else_try),
                        (eq, ":stack_index", 32), # 第9个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-武器掌握-升到6
                    (else_try),
                        (eq, ":stack_index", 33), # 第10个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-骑术-升到6
                    (else_try),
                        (eq, ":stack_index", 34), # 第11个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-骑射-升到6
                    (else_try),
                        (eq, ":stack_index", 35), # 第12个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强击-升到6
                    (else_try),
                        (eq, ":stack_index", 36), # 第13个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到6
                    (else_try),
                        (eq, ":stack_index", 37), # 第14个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-盾防-升到6

                    (else_try),
                        (eq, ":stack_index", 38), # 第15个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强弓-升到10
                    (else_try),
                        (eq, ":stack_index", 39), # 第16个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-武器掌握-升到10
                    (else_try),
                        (eq, ":stack_index", 40), # 第17个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-骑术-升到10
                    (else_try),
                        (eq, ":stack_index", 41), # 第18个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-骑射-升到10
                    (else_try),
                        (eq, ":stack_index", 42), # 第16个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强击-升到10
                    (else_try),
                        (eq, ":stack_index", 43), # 第17个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到10
                    (else_try),
                        (eq, ":stack_index", 44), # 第18个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-盾防-升到10
                    (try_end),


                (try_end),



            (else_try),
                # ==============================================
                # 弩或火枪兵自动加点方案 
                # ==============================================
                (eq, ":programme_index", 5), # 弩或火枪兵方案 
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    #(troop_set_slot, "trp_auto_point", ":tmp_trp_index", "str_auto_point_input_default_horse_archers"), # 设置方案名称
                    (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", 0),
                    (str_store_string, s7, "str_auto_point_input_default_crossbow"),
                    (troop_set_plural_name, ":trp_store_scheme_name", 7),
                    (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
                (else_try),
                    (is_between, ":stack_index", 1, 24),  
                    (try_begin),
                        (eq, ":stack_index", 1), # 第1个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 2), # 第2个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 3), # 第3个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 4), # 第4个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防

                    (else_try),
                        (eq, ":stack_index", 5), # 第5个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 6), # 第6个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 7), # 第7个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 8), # 第8个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防

                    (else_try),
                        (eq, ":stack_index", 9), # 第9个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 20),  # 下拉框升级的技能-武器掌握
                    (else_try),
                        (eq, ":stack_index", 10), # 第10个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 23),  # 下拉框升级的技能-强击
                    (else_try),
                        (eq, ":stack_index", 11), # 第11个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 24),  # 下拉框升级的技能-铁骨
                    (else_try),
                        (eq, ":stack_index", 12), # 第12个升级的技能
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 19),  # 下拉框升级的技能-盾防
                    (try_end),
                (else_try),
                    (is_between, ":stack_index", 24, 47),
                    (try_begin),
                        (eq, ":stack_index", 24), # 第1个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-武器掌握-升到3
                    (else_try),
                        (eq, ":stack_index", 25), # 第2个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-强击-升到3
                    (else_try),
                        (eq, ":stack_index", 26), # 第3个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-铁骨-升到3
                    (else_try),
                        (eq, ":stack_index", 27), # 第4个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 3),  # 下拉框升级的技能-盾防-升到3

                    (else_try),
                        (eq, ":stack_index", 28), # 第5个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-武器掌握-升到6
                    (else_try),
                        (eq, ":stack_index", 29), # 第6个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-强击-升到6
                    (else_try),
                        (eq, ":stack_index", 30), # 第7个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-铁骨-升到6
                    (else_try),
                        (eq, ":stack_index", 31), # 第8个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 6),  # 下拉框升级的技能-盾防-升到6

                    (else_try),
                        (eq, ":stack_index", 32), # 第9个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-武器掌握-升到10
                    (else_try),
                        (eq, ":stack_index", 33), # 第10个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-强击-升到10
                    (else_try),
                        (eq, ":stack_index", 34), # 第11个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-铁骨-升到10
                    (else_try),
                        (eq, ":stack_index", 35), # 第12个升级的技能的值
                        (troop_set_slot, "trp_auto_point", ":tmp_trp_index", 10),  # 下拉框升级的技能-盾防-升到10
                    (try_end),
                (try_end),



            (try_end),
        (try_end),
    (try_end),


]), 


# ==============================================
# 脚本：获取部队智力属性等级
# 功能：传入部队ID，将智力值存入reg0寄存器返回
# ==============================================
  # 用法：
  # (call_script, "script_store_intelligence_attribute_level", ":troop"),
  # (assign, ":current_intelligence_value", reg0),
("store_intelligence_attribute_level", [
  (store_script_param, ":target_troop_id", 1),  # 获取脚本参数1：目标部队ID
  (store_add, ":auto_all_slot_1610", "$g_pm_auto_point_base_slot", 10), # 1610
  (troop_get_slot, reg0, ":target_troop_id", ":auto_all_slot_1610"),  # 从槽位1610读取部队智力值到reg0

  # 用法：
  # (call_script, "script_store_intelligence_attribute_level", ":troop"),
  # (assign, ":current_intelligence_value", reg0),
]),

# ==============================================
# 脚本：提升部队智力属性等级
# 功能：传入部队ID + 提升点数，增加对应部队智力
# ==============================================
  # 用法：
  # (call_script, "script_raise_intelligence_attribute_level", ":troop", 1),
("raise_intelligence_attribute_level", [
  # 参数获取
  (store_script_param, ":target_troop_id", 1),  # 获取脚本参数1：目标部队ID
  (store_script_param, ":intelligence_add_value", 2),  # 获取脚本参数2：智力提升点数

  # 读取与计算
  (store_add, ":auto_all_slot_1610", "$g_pm_auto_point_base_slot", 10), # 1610
  (troop_get_slot, reg0, ":target_troop_id", ":auto_all_slot_1610"),  # 读取当前智力值存入reg0
  (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
  (troop_get_slot, reg1, ":target_troop_id", ":auto_all_slot_1614"),  # 读取当前剩余技能点
  (store_add, ":current_intelligence_value", reg0, ":intelligence_add_value"),  # 当前智力 + 提升点数 = 新智力值
  (store_add, ":curr_alloc_skill", reg1, ":intelligence_add_value"),
  # 保存结果
  
  (troop_set_slot, ":target_troop_id", ":auto_all_slot_1610", ":current_intelligence_value"),  # 将新智力值写回槽位1610
  (troop_set_slot, ":target_troop_id", ":auto_all_slot_1614", ":curr_alloc_skill"), # 设置新的待加技能槽
]),


# ==========================================
# 脚本：用于升级后计算获得的属性、技能点、武器点。
# 参数1：目标英雄
# 返回：
#   reg0 = 当前troop属性可用点数
#   reg1 = 当前troop技能可用点数
#   reg2 = 当前troop武器熟练度可用点数
# ==========================================
("calculate_available_points",
[
    (store_script_param, ":troop", 1),
    # ========== 第一步：计算由于等级差不同导致的待加点变化 ==========
    # 获取等级差数据
    (store_add, ":auto_all_slot_1601", "$g_pm_auto_point_base_slot", 1), # 1601
    (troop_get_slot, ":last_level", ":troop", ":auto_all_slot_1601"), # 获取之前的等级
    (store_character_level, ":curr_level", ":troop"), # 获取角色当前等级
    (store_sub, ":level_diff", ":curr_level", ":last_level"), # 等级差
    
    # 获取原本的待加点
    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
    (troop_get_slot, ":curr_alloc_attr", ":troop", ":auto_all_slot_1613"), # 获取待加属性点
    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
    (troop_get_slot, ":curr_alloc_skill", ":troop", ":auto_all_slot_1614"), # 获取待加技能点
    (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
    (troop_get_slot, ":curr_alloc_weapon", ":troop", ":auto_all_slot_1615"), # 获取待加武器点
    # 每升一级，获得一点属性点，一点技能点
    (val_add, ":curr_alloc_attr", ":level_diff"),
    (val_add, ":curr_alloc_skill", ":level_diff"),
    # 每升一级，获得10点武器点
    (store_mul, ":level_diff_mul_10", ":level_diff", 10),  
    (val_add, ":curr_alloc_weapon", ":level_diff_mul_10"),  

    (troop_set_slot, ":troop", ":auto_all_slot_1613", ":curr_alloc_attr"),  # 设置待加属性点为计算等级差后的属性点
    (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点为计算等级差后的技能点
    (troop_set_slot, ":troop", ":auto_all_slot_1615", ":curr_alloc_weapon"),  # 设置待加武器点为计算等级差后的武器点

    (troop_set_slot, ":troop", ":auto_all_slot_1601", ":curr_level"),  # 设置等级
]), 


# ==========================================
# 脚本：新加点系统增加属性实际数值
# 作用：消耗待加属性点升级属性，不能超过63
# 参数1：目标英雄
# 参数2：需要提升的属性ca_strength, ca_agility, ca_intelligence, ca_charisma
# 参数3：要提升的属性值
# ==========================================
("new_char_sys_add_attr_point",
[
    # 读取三个参数
    (store_script_param, ":troop", 1),
    (store_script_param, ":attr_id", 2),
    (store_script_param, ":add_level", 3),


    (assign, ":curr_attr", 0), 
    (try_begin),
        (eq, ":attr_id", ca_intelligence),  # 智力单独计算
        (call_script, "script_store_intelligence_attribute_level", ":troop"),
        (assign, ":curr_attr", reg0),
    (else_try),
        (store_attribute_level, ":curr_attr", ":troop", ":attr_id"), # 获取当前属性值
    (try_end),
    (store_add, ":dst_attr", ":curr_attr", ":add_level"),  # 计算预计升到多少属性
    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
    (troop_get_slot, ":curr_alloc_attr", ":troop", ":auto_all_slot_1613"), # 获取待加属性点

    (try_begin),
        (le, ":dst_attr", "$g_pm_auto_property_max"),  # 必须小于该值才能成功加点
        (ge, ":curr_alloc_attr", ":add_level"),  # 必须有足够待加属性点才能成功加点
        (try_begin),
            (eq, ":attr_id", ca_intelligence),  # 智力单独计算
            (call_script, "script_raise_intelligence_attribute_level", ":troop", ":add_level"),
        (else_try),
            (troop_raise_attribute, ":troop", ":attr_id", ":add_level"),  # 实际提升属性函数
        (try_end),
        (val_sub, ":curr_alloc_attr", ":add_level"),  # 减去消耗的属性点
        (troop_set_slot, ":troop", ":auto_all_slot_1613", ":curr_alloc_attr"),  # 设置待加属性点
        #(call_script, "script_calculate_available_points", ":troop"), # 自动计算由于属性点变化导致的剩余技能点变化
    (try_end),
]), 

# ==============================================
# 脚本功能：获取部队/英雄某项技能是否可加点
# 入参1：目标部队/英雄ID
# 入参2：需要查询的技能ID
# 入参3：需要加点的等级
# 出参：返回值存入 reg0，为该技能是否可加点
# ==============================================
("get_troop_skill_is_can_added",
[
   # 读取三个参数
    (store_script_param, ":troop", 1),
    (store_script_param, ":skill_id", 2),
    (store_script_param, ":add_level", 3),

    (store_attribute_level, ":var_ca_strength", ":troop", ca_strength), # 获取当前力量属性 
    (store_attribute_level, ":var_ca_agility", ":troop", ca_agility), # 获取当前敏捷属性 
    #(store_attribute_level, ":var_ca_intelligence", ":troop", ca_intelligence), # 获取当前智力属性 
    (call_script, "script_store_intelligence_attribute_level", ":troop"),
    (assign, ":var_ca_intelligence", reg0),
    (store_attribute_level, ":var_ca_charisma", ":troop", ca_charisma), # 获取当前魅力属性 

    (store_div, ":ca_strength_div_3", ":var_ca_strength", 3),  # 取当前力量属性的三分之一作为上限 
    (store_div, ":ca_agility_div_3", ":var_ca_agility", 3),  # 取当前敏捷属性的三分之一作为上限 
    (store_div, ":ca_intelligence_div_3", ":var_ca_intelligence", 3),  # 取当前智力属性的三分之一作为上限 
    (store_div, ":ca_charisma_div_3", ":var_ca_charisma", 3),  # 取当前魅力属性的三分之一作为上限 

    (store_skill_level, ":curr_skill", ":skill_id", ":troop"), # 获取技能等级 
    (call_script, "script_game_get_skill_modifier_for_troop", ":troop", ":skill_id"),  # 调用获取额外技能点的脚本 
    (assign, ":skill_modifier_value", reg0),  # 获取额外技能点的值 
    (store_add, ":dst_skill_add_1", ":curr_skill", ":add_level"),  # 计算预计升到多少级 
    #(val_sub, ":dst_skill_add_1", ":skill_modifier_value"),  # 需要减去额外加的技能点 
    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
    (troop_get_slot, ":curr_alloc_skill", ":troop", ":auto_all_slot_1614"), # 获取待加技能点
    (assign, ":can_add_point", 0), # 默认不可加点

    (store_add, ":slot_trp_auto_1931", "$g_pm_auto_point_base_slot_part", 131), # 铁 骨 1931
    (store_add, ":slot_trp_auto_1932", "$g_pm_auto_point_base_slot_part", 132), # 强 击 1932
    (store_add, ":slot_trp_auto_1933", "$g_pm_auto_point_base_slot_part", 133), # 强 掷 1933
    (store_add, ":slot_trp_auto_1934", "$g_pm_auto_point_base_slot_part", 134), # 强 弓 1934
    (store_add, ":slot_trp_auto_1935", "$g_pm_auto_point_base_slot_part", 135), # 武 器 掌 握 1935
    (store_add, ":slot_trp_auto_1936", "$g_pm_auto_point_base_slot_part", 136), # 盾 防 1936
    (store_add, ":slot_trp_auto_1937", "$g_pm_auto_point_base_slot_part", 137), # 跑 动 1937
    (store_add, ":slot_trp_auto_1938", "$g_pm_auto_point_base_slot_part", 138), # 骑 术 1938
    (store_add, ":slot_trp_auto_1939", "$g_pm_auto_point_base_slot_part", 139), # 骑 射 1939
    (store_add, ":slot_trp_auto_1940", "$g_pm_auto_point_base_slot_part", 140), # 掠 夺 1940
    (store_add, ":slot_trp_auto_1941", "$g_pm_auto_point_base_slot_part", 141), # 教 练 1941
    (store_add, ":slot_trp_auto_1942", "$g_pm_auto_point_base_slot_part", 142), # 追 踪 1942
    (store_add, ":slot_trp_auto_1943", "$g_pm_auto_point_base_slot_part", 143), # 战 术 1943
    (store_add, ":slot_trp_auto_1944", "$g_pm_auto_point_base_slot_part", 144), # 向 导 1944
    (store_add, ":slot_trp_auto_1945", "$g_pm_auto_point_base_slot_part", 145), # 侦 察 1945
    (store_add, ":slot_trp_auto_1946", "$g_pm_auto_point_base_slot_part", 146), # 辎 重 管 理 1946
    (store_add, ":slot_trp_auto_1947", "$g_pm_auto_point_base_slot_part", 147), # 疗 伤 1947
    (store_add, ":slot_trp_auto_1948", "$g_pm_auto_point_base_slot_part", 148), # 手 术 1948
    (store_add, ":slot_trp_auto_1949", "$g_pm_auto_point_base_slot_part", 149), # 急 救 1949
    (store_add, ":slot_trp_auto_1950", "$g_pm_auto_point_base_slot_part", 150), # 工 程 学 1950
    (store_add, ":slot_trp_auto_1951", "$g_pm_auto_point_base_slot_part", 151), # 说 服 力 1951
    (store_add, ":slot_trp_auto_1952", "$g_pm_auto_point_base_slot_part", 152), # 俘 虏 管 理 1952
    (store_add, ":slot_trp_auto_1953", "$g_pm_auto_point_base_slot_part", 153), # 统 御 1953
    (store_add, ":slot_trp_auto_1954", "$g_pm_auto_point_base_slot_part", 154), # 交 易 1954 
    
    (try_begin), # 铁骨-力量 
        (eq, ":skill_id", "skl_ironflesh"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1931"), # 获取铁骨上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 强击-力量 
        (eq, ":skill_id", "skl_power_strike"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1932"), # 获取强击上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 强制-力量 
        (eq, ":skill_id", "skl_power_throw"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1933"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 强弓-力量 
        (eq, ":skill_id", "skl_power_draw"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1934"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 武器掌握-敏捷 
        (eq, ":skill_id", "skl_weapon_master"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1935"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 盾防-敏捷 
        (eq, ":skill_id", "skl_shield"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1936"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 跑动-敏捷 
        (eq, ":skill_id", "skl_athletics"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1937"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 骑术-敏捷 
        (eq, ":skill_id", "skl_riding"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1938"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 骑射-敏捷 
        (eq, ":skill_id", "skl_horse_archery"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1939"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 掠夺-敏捷 
        (eq, ":skill_id", "skl_looting"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1940"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 教练-智力 
        (eq, ":skill_id", "skl_trainer"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1941"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 追踪和狩猎-智力 
        (eq, ":skill_id", "skl_tracking"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1942"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 战术-智力 
        (eq, ":skill_id", "skl_tactics"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1943"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 向导-智力 
        (eq, ":skill_id", "skl_pathfinding"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1944"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 侦察-智力 
        (eq, ":skill_id", "skl_spotting"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1945"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 辎重管理-智力 
        (eq, ":skill_id", "skl_inventory_management"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1946"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 疗伤-智力 
        (eq, ":skill_id", "skl_wound_treatment"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1947"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 手术-智力 
        (eq, ":skill_id", "skl_surgery"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1948"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 急救-智力 
        (eq, ":skill_id", "skl_first_aid"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1949"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 工程学-智力 
        (eq, ":skill_id", "skl_engineer"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1950"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 说服力-魅力
        (eq, ":skill_id", "skl_persuasion"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1951"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 俘虏管理-魅力
        (eq, ":skill_id", "skl_prisoner_management"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1952"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 统御-魅力
        (eq, ":skill_id", "skl_leadership"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1953"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (assign, ":can_add_point", 1), # 可加点
    (else_try), # 交易-魅力
        (eq, ":skill_id", "skl_trade"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1954"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点 
        (assign, ":can_add_point", 1), # 可加点
    (try_end),

    (assign, reg0, ":can_add_point"),
]),

# ==========================================
# 脚本：英雄技能升级
# 作用：消耗技能点升级技能，受上限限制，并且不能超过对应属性的三分之一，注意要考虑书籍等额外的绿色技能加成
# 参数1：目标英雄
# 参数2：技能ID
# 参数3：要提升的等级数
# ==========================================
("new_char_sys_add_skill_point",
[
    # 读取三个参数
    (store_script_param, ":troop", 1),
    (store_script_param, ":skill_id", 2),
    (store_script_param, ":add_level", 3),

    (store_attribute_level, ":var_ca_strength", ":troop", ca_strength), # 获取当前力量属性 
    (store_attribute_level, ":var_ca_agility", ":troop", ca_agility), # 获取当前敏捷属性 
    (call_script, "script_store_intelligence_attribute_level", ":troop"),  # 获取当前智力属性 
    (assign, ":var_ca_intelligence", reg0),
    (store_attribute_level, ":var_ca_charisma", ":troop", ca_charisma), # 获取当前魅力属性 

    (store_div, ":ca_strength_div_3", ":var_ca_strength", 3),  # 取当前力量属性的三分之一作为上限 
    (store_div, ":ca_agility_div_3", ":var_ca_agility", 3),  # 取当前敏捷属性的三分之一作为上限 
    (store_div, ":ca_intelligence_div_3", ":var_ca_intelligence", 3),  # 取当前智力属性的三分之一作为上限 
    (store_div, ":ca_charisma_div_3", ":var_ca_charisma", 3),  # 取当前魅力属性的三分之一作为上限 

    (store_skill_level, ":curr_skill", ":skill_id", ":troop"), # 获取技能等级 
    (call_script, "script_game_get_skill_modifier_for_troop", ":troop", ":skill_id"),  # 调用获取额外技能点的脚本 
    (assign, ":skill_modifier_value", reg0),  # 获取额外技能点的值 
    (store_add, ":dst_skill_add_1", ":curr_skill", ":add_level"),  # 计算预计升到多少级 
    #(val_sub, ":dst_skill_add_1", ":skill_modifier_value"),  # 需要减去额外加的技能点 
    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
    (troop_get_slot, ":curr_alloc_skill", ":troop", ":auto_all_slot_1614"), # 获取待加技能点

    (store_add, ":slot_trp_auto_1931", "$g_pm_auto_point_base_slot_part", 131), # 铁 骨 1931
    (store_add, ":slot_trp_auto_1932", "$g_pm_auto_point_base_slot_part", 132), # 强 击 1932
    (store_add, ":slot_trp_auto_1933", "$g_pm_auto_point_base_slot_part", 133), # 强 掷 1933
    (store_add, ":slot_trp_auto_1934", "$g_pm_auto_point_base_slot_part", 134), # 强 弓 1934
    (store_add, ":slot_trp_auto_1935", "$g_pm_auto_point_base_slot_part", 135), # 武 器 掌 握 1935
    (store_add, ":slot_trp_auto_1936", "$g_pm_auto_point_base_slot_part", 136), # 盾 防 1936
    (store_add, ":slot_trp_auto_1937", "$g_pm_auto_point_base_slot_part", 137), # 跑 动 1937
    (store_add, ":slot_trp_auto_1938", "$g_pm_auto_point_base_slot_part", 138), # 骑 术 1938
    (store_add, ":slot_trp_auto_1939", "$g_pm_auto_point_base_slot_part", 139), # 骑 射 1939
    (store_add, ":slot_trp_auto_1940", "$g_pm_auto_point_base_slot_part", 140), # 掠 夺 1940
    (store_add, ":slot_trp_auto_1941", "$g_pm_auto_point_base_slot_part", 141), # 教 练 1941
    (store_add, ":slot_trp_auto_1942", "$g_pm_auto_point_base_slot_part", 142), # 追 踪 1942
    (store_add, ":slot_trp_auto_1943", "$g_pm_auto_point_base_slot_part", 143), # 战 术 1943
    (store_add, ":slot_trp_auto_1944", "$g_pm_auto_point_base_slot_part", 144), # 向 导 1944
    (store_add, ":slot_trp_auto_1945", "$g_pm_auto_point_base_slot_part", 145), # 侦 察 1945
    (store_add, ":slot_trp_auto_1946", "$g_pm_auto_point_base_slot_part", 146), # 辎 重 管 理 1946
    (store_add, ":slot_trp_auto_1947", "$g_pm_auto_point_base_slot_part", 147), # 疗 伤 1947
    (store_add, ":slot_trp_auto_1948", "$g_pm_auto_point_base_slot_part", 148), # 手 术 1948
    (store_add, ":slot_trp_auto_1949", "$g_pm_auto_point_base_slot_part", 149), # 急 救 1949
    (store_add, ":slot_trp_auto_1950", "$g_pm_auto_point_base_slot_part", 150), # 工 程 学 1950
    (store_add, ":slot_trp_auto_1951", "$g_pm_auto_point_base_slot_part", 151), # 说 服 力 1951
    (store_add, ":slot_trp_auto_1952", "$g_pm_auto_point_base_slot_part", 152), # 俘 虏 管 理 1952
    (store_add, ":slot_trp_auto_1953", "$g_pm_auto_point_base_slot_part", 153), # 统 御 1953
    (store_add, ":slot_trp_auto_1954", "$g_pm_auto_point_base_slot_part", 154), # 交 易 1954 

    
    
    (try_begin), # 铁骨-力量 
        (eq, ":skill_id", "skl_ironflesh"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1931"), # 获取铁骨上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 强击-力量 
        (eq, ":skill_id", "skl_power_strike"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1932"), # 获取强击上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 强制-力量 
        (eq, ":skill_id", "skl_power_throw"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1933"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 强弓-力量 
        (eq, ":skill_id", "skl_power_draw"), 
        (le, ":dst_skill_add_1", ":ca_strength_div_3"),  # 不能超过力量属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1934"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 武器掌握-敏捷 
        (eq, ":skill_id", "skl_weapon_master"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1935"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 盾防-敏捷 
        (eq, ":skill_id", "skl_shield"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1936"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 跑动-敏捷 
        (eq, ":skill_id", "skl_athletics"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1937"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 骑术-敏捷 
        (eq, ":skill_id", "skl_riding"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1938"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 骑射-敏捷 
        (eq, ":skill_id", "skl_horse_archery"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1939"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 掠夺-敏捷 
        (eq, ":skill_id", "skl_looting"), 
        (le, ":dst_skill_add_1", ":ca_agility_div_3"),  # 不能超过敏捷属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1940"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 教练-智力 
        (eq, ":skill_id", "skl_trainer"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1941"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 追踪和狩猎-智力 
        (eq, ":skill_id", "skl_tracking"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1942"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 战术-智力 
        (eq, ":skill_id", "skl_tactics"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1943"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 向导-智力 
        (eq, ":skill_id", "skl_pathfinding"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1944"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 侦察-智力 
        (eq, ":skill_id", "skl_spotting"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1945"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 辎重管理-智力 
        (eq, ":skill_id", "skl_inventory_management"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1946"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 疗伤-智力 
        (eq, ":skill_id", "skl_wound_treatment"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1947"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 手术-智力 
        (eq, ":skill_id", "skl_surgery"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1948"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 急救-智力 
        (eq, ":skill_id", "skl_first_aid"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1949"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 工程学-智力 
        (eq, ":skill_id", "skl_engineer"), 
        (le, ":dst_skill_add_1", ":ca_intelligence_div_3"),  # 不能超过智力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1950"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 说服力-魅力
        (eq, ":skill_id", "skl_persuasion"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1951"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 俘虏管理-魅力
        (eq, ":skill_id", "skl_prisoner_management"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1952"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点
    (else_try), # 统御-魅力
        (eq, ":skill_id", "skl_leadership"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1953"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点 
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点 
    (else_try), # 交易-魅力
        (eq, ":skill_id", "skl_trade"), 
        (le, ":dst_skill_add_1", ":ca_charisma_div_3"),  # 不能超过魅力属性的三分之一 
        (troop_get_slot, ":skill_limit", "trp_auto_temp_list_3", ":slot_trp_auto_1954"), # 获取上限值 
        (le, ":dst_skill_add_1", ":skill_limit"),  # 不能超过属性的上限值 
        (ge, ":curr_alloc_skill", ":add_level"),  # 必须有足够待加技能点才能成功加点 
        (troop_raise_skill, ":troop", ":skill_id", ":add_level"),  # 实际提升技能函数 
        (val_sub, ":curr_alloc_skill", ":add_level"),  # 减去消耗的技能点 
        (troop_set_slot, ":troop", ":auto_all_slot_1614", ":curr_alloc_skill"),  # 设置待加技能点 
    (try_end),
]), 

# 是否可以进行武器加点
("new_char_sys_is_can_add_weapon_point",
[
    # 读取三个参数
    (store_script_param, ":troop", 1),
    (store_script_param, ":wpt_id", 2),
    (store_script_param, ":add_val", 3),

    # 获取当前熟练度 & 可用武器点
    (store_proficiency_level, ":curr_prof", ":troop", ":wpt_id"),
    (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
    (troop_get_slot, ":curr_alloc_wpt", ":troop", ":auto_all_slot_1615"),

    # 临时变量：总共需要消耗多少点
    (assign, ":total_cost", 0),
    (assign, ":temp_prof", ":curr_prof"),
    (assign, reg0, 0),

    # 循环计算：每加1点熟练度，算1次消耗
    (try_for_range, ":i", 0, ":add_val"),
        # 当前档位: 每100一级
        (store_div, ":tier", ":temp_prof", 100),
        (val_add, ":tier", 1),          # 0~99→1, 100~199→2, 200~299→3...

        (val_add, ":total_cost", ":tier"),
        (val_add, ":temp_prof", 1),     # 模拟加1点后进入下一档位判断
    (try_end),

    # 最终判断：上限999 & 点数足够
    (try_begin),
        (le, ":temp_prof", 999),
        (ge, ":curr_alloc_wpt", ":total_cost"),
        (assign, reg0, 1),  # 可以进行加点
        # 真正加熟练度
        #(troop_raise_proficiency_linear, ":troop", ":wpt_id", ":add_val"),

        # 扣除总消耗
        #(val_sub, ":curr_alloc_wpt", ":total_cost"),
        #(troop_set_slot, ":troop", 1615, ":curr_alloc_wpt"),
    (try_end),
]),


# ==========================================
# 脚本：新加点系统增加武器实际数值
# 注意：需要判断
# 参数1：目标英雄
# 返回：
#   reg0 = 当前troop属性可用点数
#   reg1 = 当前troop技能可用点数
#   reg2 = 当前troop武器熟练度可用点数
# ==========================================
("new_char_sys_add_weapon_point",
[
    # 读取三个参数
    (store_script_param, ":troop", 1),
    (store_script_param, ":wpt_id", 2),
    (store_script_param, ":add_val", 3),

    # 获取当前熟练度 & 可用武器点
    (store_proficiency_level, ":curr_prof", ":troop", ":wpt_id"),
    (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
    (troop_get_slot, ":curr_alloc_wpt", ":troop", ":auto_all_slot_1615"),

    # 临时变量：总共需要消耗多少点
    (assign, ":total_cost", 0),
    (assign, ":temp_prof", ":curr_prof"),

    # 循环计算：每加1点熟练度，算1次消耗
    (try_for_range, ":i", 0, ":add_val"),
        # 当前档位: 每100一级
        (store_div, ":tier", ":temp_prof", 100),
        (val_add, ":tier", 1),          # 0~99→1, 100~199→2, 200~299→3...

        (val_add, ":total_cost", ":tier"),
        (val_add, ":temp_prof", 1),     # 模拟加1点后进入下一档位判断
    (try_end),

    # 最终判断：上限999 & 点数足够
    (try_begin),
        (lt, ":temp_prof", 999),
        (ge, ":curr_alloc_wpt", ":total_cost"),

        # 真正加熟练度
        (troop_raise_proficiency_linear, ":troop", ":wpt_id", ":add_val"),

        # 扣除总消耗
        (val_sub, ":curr_alloc_wpt", ":total_cost"),
        (troop_set_slot, ":troop", ":auto_all_slot_1615", ":curr_alloc_wpt"),
    (try_end),
]),

# ==============================================
# 脚本：paint_line
# 功能：创建一个矩形网格覆盖层【用于UI绘制/矩形填充】
# 参数【你已定义】：
#   1: 起点X坐标
#   2: 起点Y坐标
#   3: 宽度
#   4: 高度
#   5: 颜色值
# 返回：
#   reg0 = 创建的覆盖层ID
# ==============================================
("paint_line",
[
    # ==============================================
    # 读取脚本传入参数【严格按你定义的含义】
    # ==============================================
    (store_script_param, ":start_x", 1),      # 参数1：起点X坐标
    (store_script_param, ":start_y", 2),      # 参数2：起点Y坐标
    (store_script_param, ":width", 3),        # 参数3：宽度
    (store_script_param, ":height", 4),       # 参数4：高度
    (store_script_param, ":color", 5),        # 参数5：颜色

    # ==============================================
    # 条件判断：X坐标大于0时才创建覆盖层
    # ==============================================
    (try_begin),
        (gt, ":start_x", 0),                  # 判断：起点X > 0 才执行绘制

        # 创建基础白色平面覆盖层
        (create_mesh_overlay, reg1, "mesh_white_plane"),

        # 坐标缩放：游戏UI坐标系放大50倍
        (val_mul, ":start_x", 50),           # 起点X坐标 ×50 适配坐标系
        (val_mul, ":start_y", 50),           # 起点Y坐标 ×50 适配坐标系

        # ==============================================
        # 设置覆盖层尺寸【宽度、高度】
        # ==============================================
        (position_set_x, pos0, ":start_x"),  # 将缩放后的X存入位置寄存器
        (position_set_y, pos0, ":start_y"),  # 将缩放后的Y存入位置寄存器
        (overlay_set_size, reg1, pos0),      # 应用尺寸到覆盖层

        # ==============================================
        # 设置覆盖层屏幕显示位置
        # ==============================================
        (position_set_x, pos0, ":width"),    # 设置X轴显示位置
        (position_set_y, pos0, ":height"),   # 设置Y轴显示位置
        (overlay_set_position, reg1, pos0),  # 应用位置到覆盖层

        # ==============================================
        # 设置覆盖层颜色
        # ==============================================
        (overlay_set_color, reg1, ":color"), # 给覆盖层设置指定颜色
    (try_end),

    # ==============================================
    # 返回创建的覆盖层ID
    # ==============================================
    (assign, reg0, reg1),                    # 将覆盖层ID存入reg0返回
]),


# 脚本功能：在界面指定位置创建一个简单的文字显示控件
# 参数说明：
#  param1: 字符串ID【-1表示使用已存入s1的字符串】
#  param2: 显示位置 X 坐标
#  param3: 显示位置 Y 坐标
#  param4: 文字宽度范围【文本框宽度】
#  param5: 文字显示样式标记【如居中、换行等】
#  param6: 文字颜色值【0表示不设置，使用默认】
("create_a_simple_string_at_position",
[
    # --------------------------
    # 步骤1：读取传入的6个脚本参数
    # 并赋值给语义化局部变量
    # --------------------------
    (store_script_param, ":text_id", 1),          # 要显示的文字ID
    (store_script_param, ":pos_x", 2),            # 文字在界面上的 X 坐标
    (store_script_param, ":pos_y", 3),            # 文字在界面上的 Y 坐标
    (store_script_param, ":text_width", 4),       # 文字显示的宽度范围
    (store_script_param, ":text_style", 5),       # 文字显示样式标记
    (store_script_param, ":text_color", 6),       # 文字颜色值

    # --------------------------
    # 步骤2：根据参数创建文字控件
    # 如果 param1 = -1，直接使用已缓存的字符串 s1
    # 否则使用传入的文字ID
    # --------------------------
    (try_begin),
        (eq, ":text_id", -1),                     # 判断是否使用预设字符串 s1
        (create_text_overlay, reg1, 1, ":text_style"),  # 创建文字控件【使用s1】
    (else_try),
        (create_text_overlay, reg1, ":text_id", ":text_style"),  # 使用指定文字ID创建
    (try_end),

    # --------------------------
    # 步骤3：设置文字控件的显示尺寸
    # 宽度 = text_width，高度自动适配
    # --------------------------
    (position_set_x, pos1, ":text_width"),        # 设置控件宽度
    (position_set_y, pos1, ":text_width"),        # 设置控件高度【与宽度一致】
    (overlay_set_size, reg1, pos1),               # 应用尺寸到文字控件

    # --------------------------
    # 步骤4：设置文字控件在界面上的坐标
    # --------------------------
    (position_set_x, pos1, ":pos_x"),             # 设置 X 坐标
    (position_set_y, pos1, ":pos_y"),             # 设置 Y 坐标
    (overlay_set_position, reg1, pos1),           # 应用坐标到文字控件

    # --------------------------
    # 步骤5：如果传入了颜色值，设置文字颜色
    # --------------------------
    (try_begin),
        (gt, ":text_color", 0),                   # 判断颜色值是否有效【>0】
        (overlay_set_color, reg1, ":text_color"),  # 设置文字颜色
    (try_end),

    # --------------------------
    # 步骤6：将创建好的控件ID存入 reg0 返回
    # 外部脚本可通过 reg0 获取这个文字控件
    # --------------------------
    (assign, reg0, reg1),
]),


# 脚本功能：创建一个【下拉标签/组合标签控件】【Combo Label】，用于界面选择菜单
# 参数说明：
#  param1: 控件显示位置 X 坐标
#  param2: 控件显示位置 Y 坐标
#  param3: 控件宽度
#  param4: 控件高度
("create_a_combo_label_overlay",
[
    # ==================================================
    # 第一步：接收并解析外部传入的 4 个参数
    # ==================================================
    (store_script_param, ":pos_x", 1),  # 读取参数1：控件 X 坐标
    (store_script_param, ":pos_y", 2),  # 读取参数2：控件 Y 坐标
    (store_script_param, ":width", 3),  # 读取参数3：控件宽度
    (store_script_param, ":height", 4),  # 读取参数4：控件高度

    # ==================================================
    # 第二步：创建 Combo Label 控件【下拉选择框】
    # ==================================================
    (create_combo_label_overlay, reg0),        # 创建组合标签控件，控件ID存入 reg0

    # ==================================================
    # 第三步：设置控件的尺寸【宽 × 高】
    # ==================================================
    (position_set_x, pos1, ":width"),          # 设置 pos1 的 X 值 = 控件宽度
    (position_set_y, pos1, ":height"),         # 设置 pos1 的 Y 值 = 控件高度
    (overlay_set_size, reg0, pos1),            # 把尺寸应用到创建好的控件

    # ==================================================
    # 第四步：设置控件在界面上的显示位置
    # ==================================================
    (position_set_x, pos1, ":pos_x"),          # 设置 pos1 的 X 值 = 目标 X 坐标
    (position_set_y, pos1, ":pos_y"),          # 设置 pos1 的 Y 值 = 目标 Y 坐标
    (overlay_set_position, reg0, pos1),        # 把位置应用到控件
]),


# 脚本功能：创建一个网格/图片界面控件【Mesh Overlay】
# 支持设置尺寸、位置、颜色、透明度
# 参数说明：
#  param1: 网格资源ID  mesh ID
#  param2: 控件宽度 【宽度<=0则不设置】
#  param3: 控件高度 【高度<=0则不设置】
#  param4: 控件 X 坐标
#  param5: 控件 Y 坐标
#  param6: 颜色值 [-1表示不设置]
#  param7: 透明度值 [-1表示不设置]
# 返回值：创建的控件ID存入 reg0
("create_a_mesh_overlay",
[
    # ==================================================
    # 第一步：读取并解析所有传入参数
    # ==================================================
    (store_script_param, ":mesh_id", 1),   # 读取参数1：要显示的网格/图片ID
    (store_script_param, ":width", 2),   # 读取参数2：控件宽度
    (store_script_param, ":height", 3),   # 读取参数3：控件高度
    (store_script_param, ":pos_x", 4),   # 读取参数4：控件在界面上的X坐标
    (store_script_param, ":pos_y", 5),   # 读取参数5：控件在界面上的Y坐标
    (store_script_param, ":color", 6),   # 读取参数6：控件颜色
    (store_script_param, ":alpha", 7),   # 读取参数7：控件透明度

    # ==================================================
    # 第二步：创建Mesh控件
    # ==================================================
    (create_mesh_overlay, reg1, ":mesh_id"),      # 根据指定的mesh ID创建控件，ID存入reg1

    # ==================================================
    # 第三步：如果宽高>0，则设置控件大小
    # ==================================================
    (try_begin),
        (gt, ":width", 0),                        # 判断宽度是否大于0【有效】
        (position_set_x, pos0, ":width"),         # 设置pos0的X为控件宽度
        (position_set_y, pos0, ":height"),         # 设置pos0的Y为控件高度
        (overlay_set_size, reg1, pos0),            # 将宽高应用到控件
    (try_end),

    # ==================================================
    # 第四步：设置控件在界面上的显示位置
    # ==================================================
    (position_set_x, pos0, ":pos_x"),             # 设置pos0的X为目标坐标
    (position_set_y, pos0, ":pos_y"),             # 设置pos0的Y为目标坐标
    (overlay_set_position, reg1, pos0),           # 将坐标应用到控件

    # ==================================================
    # 第五步：如果颜色≠-1，则设置控件颜色
    # ==================================================
    (try_begin),
        (neg|eq, ":color", -1),                   # 判断颜色值是否有效【不是-1】
        (overlay_set_color, reg1, ":color"),      # 给控件设置颜色
    (try_end),

    # ==================================================
    # 第六步：如果透明度≠-1，则设置控件透明度
    # ==================================================
    (try_begin),
        (neg|eq, ":alpha", -1),                   # 判断透明度值是否有效【不是-1】
        (overlay_set_alpha, reg1, ":alpha"),      # 给控件设置透明度
    (try_end),

    # ==================================================
    # 第七步：将创建好的控件ID返回给调用方
    # ==================================================
    (assign, reg0, reg1),                         # 把控件ID存入reg0返回
]),

# 脚本功能：创建一个图片按钮控件【Image Button Overlay】
# 支持设置正常/按下状态贴图、尺寸、位置、颜色、透明度
# 参数说明：
#  param1: 正常状态显示的 Mesh/图片 ID
#  param2: 按下状态显示的 Mesh/图片 ID
#  param3: 控件宽度
#  param4: 控件高度
#  param5: 控件在界面上的 X 坐标
#  param6: 控件在界面上的 Y 坐标
#  param7: 控件颜色【-1 表示不设置】
#  param8: 控件透明度【-1 表示不设置】
# 返回值：创建好的控件 ID 存入 reg0
("create_a_image_overlay",
[
    # ==================================================
    # 第一步：读取并解析外部传入的 8 个参数
    # ==================================================
    (store_script_param, ":mesh_normal", 1),   # 参数1：按钮正常状态的贴图ID
    (store_script_param, ":mesh_pressed", 2),   # 参数2：按钮按下状态的贴图ID
    (store_script_param, ":width", 3),   # 参数3：按钮宽度
    (store_script_param, ":height", 4),   # 参数4：按钮高度
    (store_script_param, ":pos_x", 5),   # 参数5：按钮 X 坐标
    (store_script_param, ":pos_y", 6),   # 参数6：按钮 Y 坐标
    (store_script_param, ":color", 7),   # 参数7：按钮颜色
    (store_script_param, ":alpha", 8),   # 参数8：按钮透明度

    # ==================================================
    # 第二步：创建图片按钮控件
    # ==================================================
    # 创建按钮，使用正常/按下两种状态贴图，控件ID存入 reg1
    (create_image_button_overlay, reg1, ":mesh_normal", ":mesh_pressed"),

    # ==================================================
    # 第三步：设置按钮控件的尺寸【宽 × 高】
    # ==================================================
    (position_set_x, pos0, ":width"),          # 设置位置变量的 X = 按钮宽度
    (position_set_y, pos0, ":height"),         # 设置位置变量的 Y = 按钮高度
    (overlay_set_size, reg1, pos0),            # 将宽高应用到按钮控件

    # ==================================================
    # 第四步：设置按钮在界面上的显示坐标
    # ==================================================
    (position_set_x, pos0, ":pos_x"),          # 设置位置变量的 X = 目标 X 坐标
    (position_set_y, pos0, ":pos_y"),          # 设置位置变量的 Y = 目标 Y 坐标
    (overlay_set_position, reg1, pos0),        # 将坐标应用到按钮控件

    # ==================================================
    # 第五步：如果颜色有效，则设置按钮颜色
    # ==================================================
    (try_begin),
        (neg|eq, ":color", -1),                # 判断颜色值不是 -1【需要设置】
        (overlay_set_color, reg1, ":color"),   # 给按钮设置指定颜色
    (try_end),

    # ==================================================
    # 第六步：如果透明度有效，则设置按钮透明度
    # ==================================================
    (try_begin),
        (neg|eq, ":alpha", -1),               # 判断透明度值不是 -1【需要设置】
        (overlay_set_alpha, reg1, ":alpha"),    # 给按钮设置指定透明度
    (try_end),

    # ==================================================
    # 第七步：将创建好的控件ID返回给调用脚本
    # ==================================================
    (assign, reg0, reg1),                     # 把控件ID存入 reg0 用于返回
]),

# ==============================================
# 脚本：paint_rectangle
# 功能：调用 paint_line 绘制四条线，组成空心矩形
# 依赖：script_paint_line
# 参数【你已定义】：
#   1: 线条宽度
#   2: 矩形宽度
#   3: 矩形高度
#   4: 起点X坐标
#   5: 起点Y坐标
#   6: 颜色
# ==============================================
("paint_rectangle",
[
    # ==============================================
    # 读取参数【严格按你写的注释】
    # ==============================================
    (store_script_param, ":line_width",      1),    # 线条宽度
    (store_script_param, ":rect_width",      2),    # 矩形宽度
    (store_script_param, ":rect_height",     3),    # 矩形高度
    (store_script_param, ":start_x",         4),    # 起点X坐标
    (store_script_param, ":start_y",         5),    # 起点Y坐标
    (store_script_param, ":color",           6),    # 颜色

    # ==============================================
    # 绘制矩形：顶边
    # ==============================================
    (call_script, "script_paint_line", ":rect_width", ":line_width", ":start_x", ":start_y", ":color"),

    # ==============================================
    # 绘制矩形：左边
    # ==============================================
    (call_script, "script_paint_line", ":line_width", ":rect_height", ":start_x", ":start_y", ":color"),

    # ==============================================
    # 计算底边 Y 坐标
    # ==============================================
    (store_add, ":bottom_line_y", ":start_y", ":rect_height"),

    # ==============================================
    # 绘制矩形：底边
    # ==============================================
    (call_script, "script_paint_line", ":rect_width", ":line_width", ":start_x", ":bottom_line_y", ":color"),

    # ==============================================
    # 计算右边 X 坐标
    # ==============================================
    (store_add, ":right_line_x", ":start_x", ":rect_width"),
    (val_sub, ":right_line_x", ":line_width"),

    # ==============================================
    # 绘制矩形：右边
    # ==============================================
    (call_script, "script_paint_line", ":line_width", ":rect_height", ":right_line_x", ":start_y", ":color"),
]),

# 脚本功能：根据类型创建按钮控件【普通按钮 / 游戏按钮】
# 支持自动设置文字、尺寸、坐标、颜色、透明度
# 参数说明：
# 1: 字符串ID【按钮文字，-1代表使用s1缓存字符串】
# 2: 按钮宽度
# 3: 按钮高度
# 4: 按钮 X 坐标
# 5: 按钮 Y 坐标
# 6: 按钮类型【1=游戏按钮，其他=普通按钮】
# 7: 颜色【-1=不设置】
# 8: 透明度【-1=不设置】
# 返回值：创建的按钮ID存入 reg0
("create_a_button_overlay_by_type",
[
    # ==============================================
    # 读取所有 8 个传入参数
    # ==============================================
    (store_script_param, ":text_id", 1),          # 读取参数1：按钮文字字符串ID
    (store_script_param, ":btn_width", 2),        # 读取参数2：按钮宽度
    (store_script_param, ":btn_height", 3),       # 读取参数3：按钮高度
    (store_script_param, ":pos_x", 4),            # 读取参数4：按钮界面X坐标
    (store_script_param, ":pos_y", 5),            # 读取参数5：按钮界面Y坐标
    (store_script_param, ":btn_type", 6),         # 读取参数6：按钮类型【1=游戏按钮】
    (store_script_param, ":color", 7),            # 读取参数7：按钮颜色
    (store_script_param, ":alpha", 8),            # 读取参数8：按钮透明度

    # ==============================================
    # 设置按钮显示文字
    # ==============================================
    (try_begin),
    (this_or_next|eq, ":text_id", -1),            # 判断：文字ID=-1 或 =20
    (eq, ":text_id", 20),                         # 满足则不修改s1
    (else_try),
    (str_store_string, s1, ":text_id"),           # 不满足则将文字ID存入s1
    (try_end),

    # ==============================================
    # 根据类型创建按钮【游戏按钮 / 普通按钮】
    # ==============================================
    (try_begin),
    (eq, ":btn_type", 1),                         # 判断是否为游戏按钮类型
    (create_game_button_overlay, reg1, 1),         # 创建游戏按钮，ID存入reg1
    (else_try),
    (create_button_overlay, reg1, 1),             # 创建普通按钮，ID存入reg1
    (try_end),

    # ==============================================
    # 如果宽度>0，则设置按钮尺寸
    # ==============================================
    (try_begin),
    (gt, ":btn_width", 0),                        # 判断宽度有效
    (position_set_x, pos1, ":btn_width"),         # 设置宽度到pos1
    (position_set_y, pos1, ":btn_height"),        # 设置高度到pos1
    (overlay_set_size, reg1, pos1),               # 应用尺寸到按钮
    (try_end),

    # ==============================================
    # 设置按钮在界面上的显示位置
    # ==============================================
    (position_set_x, pos1, ":pos_x"),              # 设置X坐标
    (position_set_y, pos1, ":pos_y"),              # 设置Y坐标
    (overlay_set_position, reg1, pos1),           # 应用坐标到按钮

    # ==============================================
    # 如果颜色≠-1，则设置按钮颜色
    # ==============================================
    (try_begin),
    (neg|eq, ":color", -1),                       # 判断颜色有效
    (overlay_set_color, reg1, ":color"),          # 设置按钮颜色
    (try_end),

    # ==============================================
    # 如果透明度≠-1，则设置按钮透明度
    # ==============================================
    (try_begin),
    (neg|eq, ":alpha", -1),                       # 判断透明度有效
    (overlay_set_alpha, reg1, ":alpha"),          # 设置按钮透明度
    (try_end),

    # ==============================================
    # 返回创建好的按钮ID
    # ==============================================
    (assign, reg0, reg1),                         # 将按钮ID存入reg0返回
]),

# 脚本功能：创建一个【带下拉列表的组合按钮】【下拉选择框控件】
# 支持自定义宽高和界面坐标
# 参数说明：
# 1: 控件宽度
# 2: 控件高度
# 3: 控件在界面上的 X 坐标
# 4: 控件在界面上的 Y 坐标
# 返回值：创建好的控件ID存入 reg0
("creat_a_combo_button_with_pull_down_list",
[
    # ==============================================
    # 读取传入的 4 个参数
    # ==============================================
    (store_script_param, ":width", 1),          # 读取参数1：控件宽度
    (store_script_param, ":height", 2),         # 读取参数2：控件高度
    (store_script_param, ":pos_x", 3),          # 读取参数3：控件显示 X 坐标
    (store_script_param, ":pos_y", 4),          # 读取参数4：控件显示 Y 坐标

    # ==============================================
    # 创建核心控件：下拉组合按钮
    # ==============================================
    (create_combo_button_overlay, reg1),        # 创建下拉按钮控件，ID存入 reg1

    # ==============================================
    # 如果宽度 > 0，则设置控件尺寸
    # ==============================================
    (try_begin),
    (gt, ":width", 0),                          # 判断宽度是否有效【大于0】
    (position_set_x, pos1, ":width"),           # 设置控件宽度到位置变量 pos1
    (position_set_y, pos1, ":height"),          # 设置控件高度到位置变量 pos1
    (overlay_set_size, reg1, pos1),             # 将宽高应用到控件
    (try_end),

    # ==============================================
    # 设置控件在界面上的显示坐标
    # ==============================================
    (position_set_x, pos1, ":pos_x"),           # 设置 X 坐标到位置变量
    (position_set_y, pos1, ":pos_y"),           # 设置 Y 坐标到位置变量
    (overlay_set_position, reg1, pos1),         # 将坐标应用到控件

    # ==============================================
    # 返回创建好的控件ID
    # ==============================================
    (assign, reg0, reg1),                       # 把控件ID存入 reg0 供外部调用
]),

# 脚本功能：创建带双空格/双倍行间距的文本显示控件
# 支持自定义显示区域、尺寸、坐标、颜色
# 参数说明：
# 1: 字符串ID【-1表示直接使用已缓存的s1】
# 2: 文本显示 X 坐标
# 3: 文本显示 Y 坐标
# 4: 文本显示区域宽度
# 5: 文本显示区域高度
# 6: 控件尺寸【宽高一致】
# 7: 文字颜色【0表示不设置】
# 返回值：创建的文本控件ID存入 reg0
("create_a_string_with_double_space",
[
    # ==============================================
    # 读取所有 7 个传入参数
    # ==============================================
    (store_script_param, ":text_id", 1),            # 读取参数1：文字字符串ID
    (store_script_param, ":pos_x", 2),              # 读取参数2：控件显示 X 坐标
    (store_script_param, ":pos_y", 3),              # 读取参数3：控件显示 Y 坐标
    (store_script_param, ":area_width", 4),         # 读取参数4：文本区域宽度
    (store_script_param, ":area_height", 5),       # 读取参数5：文本区域高度
    (store_script_param, ":control_size", 6),       # 读取参数6：控件整体尺寸
    (store_script_param, ":text_color", 7),         # 读取参数7：文字颜色值

    # ==============================================
    # 设置要显示的文字内容
    # ==============================================
    (try_begin),
    (eq, ":text_id", -1),                           # 判断字符串ID是否为-1
    (else_try),
    (str_store_string, s1, ":text_id"),             # 非-1则将字符串ID存入s1缓存
    (try_end),

    # ==============================================
    # 创建带双空格格式的文本控件
    # ==============================================
    (create_text_overlay, reg1, 1, 10240),         # 创建文本控件，启用双空格/换行样式

    # ==============================================
    # 设置文本显示区域大小【文字排版范围】
    # ==============================================
    (position_set_x, pos1, ":area_width"),         # 设置区域宽度
    (position_set_y, pos1, ":area_height"),        # 设置区域高度
    (overlay_set_area_size, reg1, pos1),           # 应用区域大小到控件

    # ==============================================
    # 设置控件整体显示尺寸
    # ==============================================
    (position_set_x, pos1, ":control_size"),       # 设置控件宽度
    (position_set_y, pos1, ":control_size"),       # 设置控件高度
    (overlay_set_size, reg1, pos1),                # 应用尺寸到控件

    # ==============================================
    # 设置控件在界面上的显示坐标
    # ==============================================
    (position_set_x, pos1, ":pos_x"),               # 设置目标 X 坐标
    (position_set_y, pos1, ":pos_y"),               # 设置目标 Y 坐标
    (overlay_set_position, reg1, pos1),            # 应用坐标到控件

    # ==============================================
    # 如果颜色值有效，则设置文字颜色
    # ==============================================
    (try_begin),
    (gt, ":text_color", 0),                        # 判断颜色值大于0 有效 
    (overlay_set_color, reg1, ":text_color"),      # 设置文字颜色
    (try_end),

    # ==============================================
    # 返回创建完成的控件ID
    # ==============================================
    (assign, reg0, reg1),                          # 将控件ID存入reg0返回调用方
]),

# ==============================================
# 界面预加载逻辑：pre_1
# 功能：满足条件时，在界面上创建两条白色装饰线条 横线 + 竖线
# ==============================================
("pre_1",
[
    # ==============================================
    # 条件判断：仅当全局开关 $new_test 开启时，才执行界面绘制
    # ==============================================
    (try_begin),
        # 判断：开启新测试界面开关 $new_test = 1 时执行
        (eq, "$g_pm_new_test", 1),
        
        # ==============================================
        # 步骤1：创建空白文本覆盖层 占位/辅助定位 
        # ==============================================
        # 创建文本覆盖层，绑定对象 g_presentation_obj_39，显示空白文本，样式参数4112
        (create_text_overlay, "$g_pm_presentation_obj_39", "str_auto_point_force_add", 4112),
        
        # ==============================================
        # 步骤2：创建【竖直线条】白色平面网格
        # ==============================================
        # 创建网格覆盖层，绑定对象 g_presentation_obj_38，使用白色平面素材 mesh_white_plane
        (create_mesh_overlay, "$g_pm_presentation_obj_38", "mesh_white_plane"),
        # 设置位置寄存器 pos9 的 X 坐标：线条宽度 50
        (position_set_x, pos9, 50),
        # 设置位置寄存器 pos9 的 Y 坐标：线条高度 37500 长竖线 
        (position_set_y, pos9, 37500),
        # 将 pos9 定义的尺寸应用到竖直线条覆盖层
        (overlay_set_size, "$g_pm_presentation_obj_38", pos9),
        
        # ==============================================
        # 步骤3：创建【水平线条】白色平面网格
        # ==============================================
        # 创建网格覆盖层，绑定对象 g_presentation_obj_37，使用白色平面素材 mesh_white_plane
        (create_mesh_overlay, "$g_pm_presentation_obj_37", "mesh_white_plane"),
        # 设置位置寄存器 pos9 的 X 坐标：线条长度 50000 长横线 
        (position_set_x, pos9, 50000),
        # 设置位置寄存器 pos9 的 Y 坐标：线条高度 50
        (position_set_y, pos9, 50),
        # 将 pos9 定义的尺寸应用到水平线条覆盖层
        (overlay_set_size, "$g_pm_presentation_obj_37", pos9),
    (try_end),
]),

# 脚本功能：将 0~1000 范围内的数值，转换为游戏界面使用的固定点坐标值
("convert_val_of_1000_to_cur_fixe_point",
[
    # ==============================================
    # 步骤1：获取传入的参数【需要转换的原始数值】
    # ==============================================
    (store_script_param, ":input_value", 1),       # 读取脚本参数1，存入 :input_value【待转换的输入值，范围0~1000】

    # ==============================================
    # 步骤2：初始化固定点系数
    # ==============================================
    (assign, ":fixed_point_coeff", 1),              # 将系数初始化为 1
    (convert_to_fixed_point, ":fixed_point_coeff"), # 转换为游戏引擎的固定点格式【UI坐标计算标准格式】

    # ==============================================
    # 步骤3：执行坐标换算核心计算
    # ==============================================
    (store_mul, ":result_temp", ":input_value", ":fixed_point_coeff"), # 输入值 × 固定点系数，得到临时结果
    (val_div, ":result_temp", 1000),                # 临时结果 ÷ 1000，完成比例缩放

    # ==============================================
    # 步骤4：输出最终结果到 reg0
    # ==============================================
    (assign, reg0, ":result_temp"),                 # 将计算完成的坐标值存入 reg0 返回
]),

("pre_2",  # 每帧执行的鼠标跟随UI更新脚本
[
    # ==============================================
    # 主条件：仅当开启测试模式 $new_test = 1 时执行
    # ==============================================
    (try_begin),                                    # 开始主判断
        (eq, "$g_pm_new_test", 1),                       # 判断：是否开启鼠标跟随测试模式

        # ==============================================
        # 步骤1：获取当前鼠标屏幕坐标
        # ==============================================
        (mouse_get_position, pos9),                  # 获取鼠标坐标，存入位置寄存器 pos9
        (position_get_x, reg50, pos9),               # 提取鼠标 X 坐标 → reg50
        (position_get_y, reg51, pos9),               # 提取鼠标 Y 坐标 → reg51

        # ==============================================
        # 步骤2：更新 横向线条UI【仅跟随X轴】
        # ==============================================
        (position_set_x, pos9, reg50),               # 设置 pos9 的 X = 鼠标X
        (position_set_y, pos9, 0),                  # 设置 pos9 的 Y = 0【固定顶部】
        (overlay_set_position, "$g_pm_presentation_obj_38", pos9),  # 更新横向线条位置

        # ==============================================
        # 步骤3：更新 纵向线条UI【仅跟随Y轴】
        # ==============================================
        (position_set_x, pos9, 0),                  # 设置 pos9 的 X = 0【固定左侧】
        (position_set_y, pos9, reg51),               # 设置 pos9 的 Y = 鼠标Y
        (overlay_set_position, "$g_pm_presentation_obj_37", pos9),  # 更新纵向线条位置

        # ==============================================
        # 步骤4：计算 X 轴偏移量【鼠标左右偏置】
        # 功能：鼠标X < 500 则向右偏移，否则向左偏移
        # ==============================================
        (try_begin),                                # 开始X轴偏移判断
            (neg|gt, reg50, 500),                   # 判断：鼠标X ≤ 500
            (call_script, "script_convert_val_of_1000_to_cur_fixe_point", 70),  # 调用脚本换算固定点 +70
            (assign, ":offset_x", reg0),            # 偏移量X = +70【文本向右偏移】
        (else_try),                                 # 否则：鼠标X > 500
            (call_script, "script_convert_val_of_1000_to_cur_fixe_point", -70), # 调用脚本换算固定点 -70
            (assign, ":offset_x", reg0),            # 偏移量X = -70【文本向左偏移】
        (try_end),                                  # 结束X轴偏移判断

        # ==============================================
        # 步骤5：计算 Y 轴偏移量【鼠标上下偏置】
        # 功能：鼠标Y 低于上限则向下偏移，否则向上偏移
        # ==============================================
        (try_begin),                                # 开始Y轴偏移判断
            (call_script, "script_convert_val_of_1000_to_cur_fixe_point", 375), # 获取Y轴上限 375
            (neg|gt, reg51, reg0),                  # 判断：鼠标Y ≤ 上限值
            (call_script, "script_convert_val_of_1000_to_cur_fixe_point", 20),  # 偏移 +20
            (assign, ":offset_y", reg0),            # 偏移量Y = +20【文本向下偏移】
        (else_try),                                 # 否则：鼠标Y > 上限值
            (call_script, "script_convert_val_of_1000_to_cur_fixe_point", -20),  # 偏移 -20
            (assign, ":offset_y", reg0),            # 偏移量Y = -20【文本向上偏移】
        (try_end),                                  # 结束Y轴偏移判断

        # ==============================================
        # 步骤6：计算坐标文本最终显示位置
        # ==============================================
        (store_add, ":final_x", reg50, ":offset_x"), # 最终X = 鼠标X + X偏移
        (store_add, ":final_y", reg51, ":offset_y"), # 最终Y = 鼠标Y + Y偏移
        (position_set_x, pos9, ":final_x"),          # 设置 pos9 X 坐标
        (position_set_y, pos9, ":final_y"),          # 设置 pos9 Y 坐标

        # ==============================================
        # 步骤7：更新坐标文本UI位置 + 显示内容
        # ==============================================
        (overlay_set_position, "$g_pm_presentation_obj_39", pos9),  # 设置文本位置
        (overlay_set_text, "$g_pm_presentation_obj_39", "str_auto_reg50_reg51"),  # 设置文本：显示 【X,Y】
    (try_end),                                          # 结束主判断
]),




# ==============================================
# 脚本：new_char_sys_troop_can_use_item
# 功能：判断一支部队能否使用某件装备
# 参数：
#   1: 部队ID
#   2: 物品ID
#   3: 物品修饰符/强化等级
# 返回：
#   reg0：能否使用【1=能，0=不能】
#   reg1：需求数值
#   reg2：需求属性名称文本ID
# ==============================================
("new_char_sys_troop_can_use_item",
[
    # ==============================================
    # 步骤1：读取传入的三个参数
    # ==============================================
    (store_script_param, ":troop_id", 1),              # 参数1 → 要检测的部队ID
    (store_script_param, ":item_id", 2),              # 参数2 → 物品ID
    (store_script_param, ":item_modifier", 3),        # 参数3 → 物品修饰符/强化等级

    # ==============================================
    # 步骤2：获取物品类型
    # ==============================================
    (item_get_type, ":item_type", ":item_id"),         # 获取物品类型【马匹、武器、书籍等】

    # ==============================================
    # 步骤3：获取物品基础需求值
    # ==============================================
    (try_begin),
        (eq, ":item_type", 20),                        # 如果是书籍类
        (item_get_slot, ":require_value", ":item_id", slot_item_intelligence_requirement),  # 获取智力需求
    (else_try),
        (item_get_difficulty, ":require_value", ":item_id"),          # 否则用原生指令获取装备需求值
    (try_end),

    # ==============================================
    # 步骤4：根据物品修饰符调整需求数值
    # ==============================================
    (try_begin),
        (eq, ":item_type", 1),                         # 如果是马匹
        (try_begin),
            (eq, ":item_modifier", 32),                # 豪华 +1 需求
            (val_add, ":require_value", 1),
        (else_try),
            (eq, ":item_modifier", 33),                # 胆小 -1 需求
            (val_add, ":require_value", -1),
        (else_try),
            (eq, ":item_modifier", 36),                # 修饰符 +2 需求
            (val_add, ":require_value", 2),
        (try_end),
    (else_try),
        (eq, ":require_value", 0),                     # 若基础需求为0，不执行修饰符逻辑
    (else_try),
        (eq, ":item_modifier", 32),                    # 豪华 +1
        (val_add, ":require_value", 1),
    (else_try),
        (eq, ":item_modifier", 33),                    # 胆小 -1
        (val_sub, ":require_value", 1),
    (else_try),
        (eq, ":item_modifier", 18),                    # 重 +1【非马匹】
        (neg|eq, ":item_type", 1),
        (val_add, ":require_value", 1),
    (else_try),
        (eq, ":item_modifier", 19),                    # 坚硬的 +2
        (val_add, ":require_value", 2),
    (else_try),
        (eq, ":item_modifier", 17),                    # 极品 +4
        (val_add, ":require_value", 4),
    (try_end),

    # ==============================================
    # 步骤5：获取部队对应属性/技能等级
    # ==============================================
    (try_begin),
        (eq, ":item_type", 1),                         # 马匹 → 骑术
        (store_skill_level, ":troop_value", skl_riding, ":troop_id"),
        (assign, ":require_text", "str_ui_hero_strengthen_string_18"),
    (else_try),
        (eq, ":item_type", 7),                         # 盾防 
        (store_skill_level, ":troop_value", skl_shield, ":troop_id"),
        (assign, ":require_text", "str_ui_hero_strengthen_string_16"),
    (else_try),
        (this_or_next|eq, ":item_type", 9),            # 武器/盔甲类 → 力量
        (this_or_next|eq, ":item_type", 2),
        (this_or_next|eq, ":item_type", 3),
        (this_or_next|eq, ":item_type", 4),
        (this_or_next|eq, ":item_type", 12),
        (this_or_next|eq, ":item_type", 13),
        (this_or_next|eq, ":item_type", 14),
        (this_or_next|eq, ":item_type", 16),
        (this_or_next|eq, ":item_type", 17),
        (this_or_next|eq, ":item_type", 18),
        (eq, ":item_type", 15),
        (store_attribute_level, ":troop_value", ":troop_id", ca_strength),
        (assign, ":require_text", "str_ui_hero_strengthen_string_1"),
    (else_try),
        (eq, ":item_type", 8),                         # 弓 → 强弓
        (store_skill_level, ":troop_value", skl_power_draw, ":troop_id"),
        (assign, ":require_text", "str_ui_hero_strengthen_string_14"),
    (else_try),
        (eq, ":item_type", 10),                        # 投掷 → 强掷
        (store_skill_level, ":troop_value", skl_power_throw, ":troop_id"),
        (assign, ":require_text", "str_ui_hero_strengthen_string_13"),
    (else_try),
        (eq, ":item_type", 20),                        # 书籍 → 智力
        (call_script, "script_store_intelligence_attribute_level", ":troop_id"),
        (assign, ":troop_value", reg0),
        (assign, ":require_text", "str_ui_hero_strengthen_string_3"),  # 需要智力
    (else_try),
        (assign, ":troop_value", 0),                  # 默认值-1
    (try_end),

    # ==============================================
    # 步骤6：最终判断能否使用
    # ==============================================
    (try_begin),
        # 属性不足不能使用
        (neg|ge, ":troop_value", ":require_value"),
        (assign, reg0, 0),                             # 返回0：不能使用
    (else_try),
        (assign, reg0, 1),                             # 返回1：可以使用
    (try_end),

    # ==============================================
    # 步骤7：设置返回值
    # ==============================================
    (assign, reg1, ":require_value"),                  # 返回需求数值
    (assign, reg2, ":require_text"),                  # 返回需求属性文本ID
]),


  # ==============================================
  # 脚本名称：script_save_troop_points_for_reset
  # 功能：保存当前英雄的所有属性、技能、熟练度、可用点数到 trp_auto_point
  # 用途：用于【加点重设】功能，不切换角色/不退出界面可回滚
  # 存储目标：trp_auto_point
  # 存储起始槽：1800
  # ==============================================
  ("save_troop_points_for_reset", [
      # 传入参数：$g_script_param_1 = 要保存的英雄 troop
      (store_script_param, ":troop", 1),

      # ==========================================
      # 1. 保存 4 大属性 【槽 1800 ~ 1803】
      # ==========================================
      (store_attribute_level, reg0, ":troop", ca_strength),      # 力量
      (store_add, ":operate_slot_1800", "$g_pm_auto_point_base_slot_part", 0), # 1800
      (troop_set_slot, "trp_auto_point", ":operate_slot_1800", reg0),
      
      (store_attribute_level, reg0, ":troop", ca_agility),      # 敏捷
      (store_add, ":operate_slot_1801", "$g_pm_auto_point_base_slot_part", 1), # 1801
      (troop_set_slot, "trp_auto_point", ":operate_slot_1801", reg0),
      
      (call_script, "script_store_intelligence_attribute_level", ":troop"),     # 智力
      (store_add, ":operate_slot_1802", "$g_pm_auto_point_base_slot_part", 2), # 1802
      (troop_set_slot, "trp_auto_point", ":operate_slot_1802", reg0),
      
      (store_attribute_level, reg0, ":troop", ca_charisma),      # 魅力
      (store_add, ":operate_slot_1803", "$g_pm_auto_point_base_slot_part", 3), # 1803
      (troop_set_slot, "trp_auto_point", ":operate_slot_1803", reg0),

      # ==========================================
      # 2. 保存 25 个技能 【槽 1804 ~ 1828】
      # ==========================================
      (store_skill_level, reg0, "skl_ironflesh", ":troop"),          # 铁骨
      (store_add, ":operate_slot_1804", "$g_pm_auto_point_base_slot_part", 4), # 1804
      (troop_set_slot, "trp_auto_point", ":operate_slot_1804", reg0),
      
      (store_skill_level, reg0, "skl_power_strike", ":troop"),       # 强击
      (store_add, ":operate_slot_1805", "$g_pm_auto_point_base_slot_part", 5), # 1805
      (troop_set_slot, "trp_auto_point", ":operate_slot_1805", reg0),
      
      (store_skill_level, reg0, "skl_power_throw", ":troop"),         # 强掷
      (store_add, ":operate_slot_1806", "$g_pm_auto_point_base_slot_part", 6), # 1806
      (troop_set_slot, "trp_auto_point", ":operate_slot_1806", reg0),
      
      (store_skill_level, reg0, "skl_power_draw", ":troop"),         # 强弓
      (store_add, ":operate_slot_1807", "$g_pm_auto_point_base_slot_part", 7), # 1807
      (troop_set_slot, "trp_auto_point", ":operate_slot_1807", reg0),
      
      (store_skill_level, reg0, "skl_weapon_master", ":troop"),       # 武器掌握
      (store_add, ":operate_slot_1808", "$g_pm_auto_point_base_slot_part", 8), # 1808
      (troop_set_slot, "trp_auto_point", ":operate_slot_1808", reg0),
      
      (store_skill_level, reg0, "skl_shield", ":troop"),              # 盾防
      (store_add, ":operate_slot_1809", "$g_pm_auto_point_base_slot_part", 9), # 1809
      (troop_set_slot, "trp_auto_point", ":operate_slot_1809", reg0),
      
      (store_skill_level, reg0, "skl_athletics", ":troop"),           # 跑动
      (store_add, ":operate_slot_1810", "$g_pm_auto_point_base_slot_part", 10), # 1810
      (troop_set_slot, "trp_auto_point", ":operate_slot_1810", reg0),
      
      (store_skill_level, reg0, "skl_riding", ":troop"),              # 骑术
      (store_add, ":operate_slot_1811", "$g_pm_auto_point_base_slot_part", 11), # 1811
      (troop_set_slot, "trp_auto_point", ":operate_slot_1811", reg0),
      
      (store_skill_level, reg0, "skl_horse_archery", ":troop"),       # 骑射
      (store_add, ":operate_slot_1812", "$g_pm_auto_point_base_slot_part", 12), # 1812
      (troop_set_slot, "trp_auto_point", ":operate_slot_1812", reg0),
      
      (store_skill_level, reg0, "skl_looting", ":troop"),             # 掠夺
      (store_add, ":operate_slot_1813", "$g_pm_auto_point_base_slot_part", 13), # 1813
      (troop_set_slot, "trp_auto_point", ":operate_slot_1813", reg0),
      
      (store_skill_level, reg0, "skl_trainer", ":troop"),            # 教练
      (store_add, ":operate_slot_1814", "$g_pm_auto_point_base_slot_part", 14), # 1814
      (troop_set_slot, "trp_auto_point", ":operate_slot_1814", reg0),
      
      (store_skill_level, reg0, "skl_tracking", ":troop"),           # 追踪
      (store_add, ":operate_slot_1815", "$g_pm_auto_point_base_slot_part", 15), # 1815
      (troop_set_slot, "trp_auto_point", ":operate_slot_1815", reg0),
      
      (store_skill_level, reg0, "skl_tactics", ":troop"),            # 战术
      (store_add, ":operate_slot_1816", "$g_pm_auto_point_base_slot_part", 16), # 1816
      (troop_set_slot, "trp_auto_point", ":operate_slot_1816", reg0),
      
      (store_skill_level, reg0, "skl_pathfinding", ":troop"),        # 向导
      (store_add, ":operate_slot_1817", "$g_pm_auto_point_base_slot_part", 17), # 1817
      (troop_set_slot, "trp_auto_point", ":operate_slot_1817", reg0),
      
      (store_skill_level, reg0, "skl_spotting", ":troop"),           # 侦察
      (store_add, ":operate_slot_1818", "$g_pm_auto_point_base_slot_part", 18), # 1818
      (troop_set_slot, "trp_auto_point", ":operate_slot_1818", reg0),
      
      (store_skill_level, reg0, "skl_inventory_management", ":troop"),# 辎重
      (store_add, ":operate_slot_1819", "$g_pm_auto_point_base_slot_part", 19), # 1819
      (troop_set_slot, "trp_auto_point", ":operate_slot_1819", reg0),
      
      (store_skill_level, reg0, "skl_wound_treatment", ":troop"),    # 疗伤
      (store_add, ":operate_slot_1820", "$g_pm_auto_point_base_slot_part", 20), # 1820
      (troop_set_slot, "trp_auto_point", ":operate_slot_1820", reg0),
      
      (store_skill_level, reg0, "skl_surgery", ":troop"),            # 手术
      (store_add, ":operate_slot_1821", "$g_pm_auto_point_base_slot_part", 21), # 1821
      (troop_set_slot, "trp_auto_point", ":operate_slot_1821", reg0),
      
      (store_skill_level, reg0, "skl_first_aid", ":troop"),         # 急救
      (store_add, ":operate_slot_1822", "$g_pm_auto_point_base_slot_part", 22), # 1822
      (troop_set_slot, "trp_auto_point", ":operate_slot_1822", reg0),
      
      (store_skill_level, reg0, "skl_engineer", ":troop"),           # 工程
      (store_add, ":operate_slot_1823", "$g_pm_auto_point_base_slot_part", 23), # 1823
      (troop_set_slot, "trp_auto_point", ":operate_slot_1823", reg0),
      
      (store_skill_level, reg0, "skl_persuasion", ":troop"),         # 说服
      (store_add, ":operate_slot_1824", "$g_pm_auto_point_base_slot_part", 24), # 1824
      (troop_set_slot, "trp_auto_point", ":operate_slot_1824", reg0),
      
      (store_skill_level, reg0, "skl_prisoner_management", ":troop"),# 俘虏
      (store_add, ":operate_slot_1825", "$g_pm_auto_point_base_slot_part", 25), # 1825
      (troop_set_slot, "trp_auto_point", ":operate_slot_1825", reg0),
      
      (store_skill_level, reg0, "skl_leadership", ":troop"),         # 统御
      (store_add, ":operate_slot_1826", "$g_pm_auto_point_base_slot_part", 26), # 1826
      (troop_set_slot, "trp_auto_point", ":operate_slot_1826", reg0),
      
      (store_skill_level, reg0, "skl_trade", ":troop"),              # 交易
      (store_add, ":operate_slot_1827", "$g_pm_auto_point_base_slot_part", 27), # 1827
      (troop_set_slot, "trp_auto_point", ":operate_slot_1827", reg0),

      # ==========================================
      # 3. 保存 7 个武器熟练度 【槽 1828 ~ 1834】
      # ==========================================
      (store_proficiency_level, reg0, ":troop", wpt_one_handed_weapon),      # 单手
      (store_add, ":operate_slot_1828", "$g_pm_auto_point_base_slot_part", 28), # 1828
      (troop_set_slot, "trp_auto_point", ":operate_slot_1828", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_two_handed_weapon),      # 双手
      (store_add, ":operate_slot_1829", "$g_pm_auto_point_base_slot_part", 29), # 1829
      (troop_set_slot, "trp_auto_point", ":operate_slot_1829", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_polearm),          # 长杆
      (store_add, ":operate_slot_1830", "$g_pm_auto_point_base_slot_part", 30), # 1830
      (troop_set_slot, "trp_auto_point", ":operate_slot_1830", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_archery),         # 弓
      (store_add, ":operate_slot_1831", "$g_pm_auto_point_base_slot_part", 31), # 1831
      (troop_set_slot, "trp_auto_point", ":operate_slot_1831", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_crossbow),        # 弩
      (store_add, ":operate_slot_1832", "$g_pm_auto_point_base_slot_part", 32), # 1832
      (troop_set_slot, "trp_auto_point", ":operate_slot_1832", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_throwing),        # 投掷
      (store_add, ":operate_slot_1833", "$g_pm_auto_point_base_slot_part", 33), # 1833
      (troop_set_slot, "trp_auto_point", ":operate_slot_1833", reg0),
      
      (store_proficiency_level, reg0, ":troop", wpt_firearm),            # 火器
      (store_add, ":operate_slot_1834", "$g_pm_auto_point_base_slot_part", 34), # 1834
      (troop_set_slot, "trp_auto_point", ":operate_slot_1834", reg0),

      # ==========================================
      # 4. 保存 3 个可用点数 【槽 1835 ~ 1837】
      # ==========================================
      (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
      (troop_get_slot, reg0, ":troop", ":auto_all_slot_1613"),    # 可用属性点
      (store_add, ":operate_slot_1835", "$g_pm_auto_point_base_slot_part", 35), # 1835
      (troop_set_slot, "trp_auto_point", ":operate_slot_1835", reg0),
      
      (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
      (troop_get_slot, reg0, ":troop", ":auto_all_slot_1614"),    # 可用技能点
      (store_add, ":operate_slot_1836", "$g_pm_auto_point_base_slot_part", 36), # 1836
      (troop_set_slot, "trp_auto_point", ":operate_slot_1836", reg0),
      
      (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
      (troop_get_slot, reg0, ":troop", ":auto_all_slot_1615"),    # 可用熟练度点
      (store_add, ":operate_slot_1837", "$g_pm_auto_point_base_slot_part", 37), # 1837
      (troop_set_slot, "trp_auto_point", ":operate_slot_1837", reg0),
  ]),

# ==============================================
# 脚本名称：script_restore_troop_points_from_reset
# 功能：从 trp_auto_point 恢复所有属性、技能、熟练度、可用点数
# 机制：纯原生 raise 方式，无 set，100% 兼容骑砍
# ==============================================
("restore_troop_points_from_reset", [
    (store_script_param, ":troop", 1),

    # ========== 恢复 4 大属性 ==========
    # 力量
    (store_add, ":operate_slot_1800", "$g_pm_auto_point_base_slot_part", 0), # 1800
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1800"),
    (store_attribute_level, ":current", ":troop", ca_strength),
    (val_sub, ":target", ":current"),
    (troop_raise_attribute, ":troop", ca_strength, ":target"),

    # 敏捷
    (store_add, ":operate_slot_1801", "$g_pm_auto_point_base_slot_part", 1), # 1801
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1801"),
    (store_attribute_level, ":current", ":troop", ca_agility),
    (val_sub, ":target", ":current"),
    (troop_raise_attribute, ":troop", ca_agility, ":target"),

    # 智力
    (store_add, ":operate_slot_1802", "$g_pm_auto_point_base_slot_part", 2), # 1802
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1802"),

    (store_add, ":auto_all_slot_1604", "$g_pm_auto_point_base_slot", 4), # 1604
    (troop_set_slot, ":troop", ":auto_all_slot_1604", ":target"),  # 设置智力之前的值为目标值，不然智力会参与二次计算
    (call_script, "script_store_intelligence_attribute_level", ":troop"),
    (assign, ":current", reg0),
    (val_sub, ":target", ":current"),
    (call_script, "script_raise_intelligence_attribute_level", ":troop", ":target"),



    # 魅力
    (store_add, ":operate_slot_1803", "$g_pm_auto_point_base_slot_part", 3), # 1803
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1803"),
    (store_attribute_level, ":current", ":troop", ca_charisma),
    (val_sub, ":target", ":current"),
    (troop_raise_attribute, ":troop", ca_charisma, ":target"),

    # ========== 恢复 25 个技能 ==========
    # 铁骨
    (store_add, ":operate_slot_1804", "$g_pm_auto_point_base_slot_part", 4), # 1804
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1804"),
    (store_skill_level, ":current", skl_ironflesh, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_ironflesh, ":target"),

    # 强击
    (store_add, ":operate_slot_1805", "$g_pm_auto_point_base_slot_part", 5), # 1805
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1805"),
    (store_skill_level, ":current", skl_power_strike, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_power_strike, ":target"),

    # 强掷
    (store_add, ":operate_slot_1806", "$g_pm_auto_point_base_slot_part", 6), # 1806
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1806"),
    (store_skill_level, ":current", skl_power_throw, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_power_throw, ":target"),

    # 强弓
    (store_add, ":operate_slot_1807", "$g_pm_auto_point_base_slot_part", 7), # 1807
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1807"),
    (store_skill_level, ":current", skl_power_draw, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_power_draw, ":target"),

    # 武器掌握
    (store_add, ":operate_slot_1808", "$g_pm_auto_point_base_slot_part", 8), # 1808
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1808"),
    (store_skill_level, ":current", skl_weapon_master, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_weapon_master, ":target"),

    # 盾防
    (store_add, ":operate_slot_1809", "$g_pm_auto_point_base_slot_part", 9), # 1809
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1809"),
    (store_skill_level, ":current", skl_shield, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_shield, ":target"),

    # 跑动
    (store_add, ":operate_slot_1810", "$g_pm_auto_point_base_slot_part", 10), # 1810
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1810"),
    (store_skill_level, ":current", skl_athletics, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_athletics, ":target"),

    # 骑术
    (store_add, ":operate_slot_1811", "$g_pm_auto_point_base_slot_part", 11), # 1811
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1811"),
    (store_skill_level, ":current", skl_riding, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_riding, ":target"),

    # 骑射
    (store_add, ":operate_slot_1812", "$g_pm_auto_point_base_slot_part", 12), # 1812
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1812"),
    (store_skill_level, ":current", skl_horse_archery, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_horse_archery, ":target"),

    # 掠夺
    (store_add, ":operate_slot_1813", "$g_pm_auto_point_base_slot_part", 13), # 1813  
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1813"),
    (store_skill_level, ":current", skl_looting, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_looting, ":target"),

    # 教练
    (store_add, ":operate_slot_1814", "$g_pm_auto_point_base_slot_part", 14), # 1814
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1814"),
    (store_skill_level, ":current", skl_trainer, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_trainer, ":target"),

    # 追踪
    (store_add, ":operate_slot_1815", "$g_pm_auto_point_base_slot_part", 15), # 1815
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1815"),
    (store_skill_level, ":current", skl_tracking, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_tracking, ":target"),

    # 战术
    (store_add, ":operate_slot_1816", "$g_pm_auto_point_base_slot_part", 16), # 1816
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1816"),
    (store_skill_level, ":current", skl_tactics, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_tactics, ":target"),

    # 向导
    (store_add, ":operate_slot_1817", "$g_pm_auto_point_base_slot_part", 17), # 1817
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1817"),
    (store_skill_level, ":current", skl_pathfinding, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_pathfinding, ":target"),

    # 侦察
    (store_add, ":operate_slot_1818", "$g_pm_auto_point_base_slot_part", 18), # 1818
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1818"),
    (store_skill_level, ":current", skl_spotting, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_spotting, ":target"),

    # 辎重管理
    (store_add, ":operate_slot_1819", "$g_pm_auto_point_base_slot_part", 19), # 1819
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1819"),
    (store_skill_level, ":current", skl_inventory_management, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_inventory_management, ":target"),

    # 疗伤
    (store_add, ":operate_slot_1820", "$g_pm_auto_point_base_slot_part", 20), # 1820
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1820"),
    (store_skill_level, ":current", skl_wound_treatment, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_wound_treatment, ":target"),

    # 手术
    (store_add, ":operate_slot_1821", "$g_pm_auto_point_base_slot_part", 21), # 1821
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1821"),
    (store_skill_level, ":current", skl_surgery, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_surgery, ":target"),

    # 急救
    (store_add, ":operate_slot_1822", "$g_pm_auto_point_base_slot_part", 22), # 1822
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1822"),
    (store_skill_level, ":current", skl_first_aid, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_first_aid, ":target"),

    # 工程
    (store_add, ":operate_slot_1823", "$g_pm_auto_point_base_slot_part", 23), # 1823
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1823"),
    (store_skill_level, ":current", skl_engineer, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_engineer, ":target"),

    # 说服
    (store_add, ":operate_slot_1824", "$g_pm_auto_point_base_slot_part", 24), # 1824
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1824"),
    (store_skill_level, ":current", skl_persuasion, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_persuasion, ":target"),

    # 俘虏管理
    (store_add, ":operate_slot_1825", "$g_pm_auto_point_base_slot_part", 25), # 1825
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1825"),
    (store_skill_level, ":current", skl_prisoner_management, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_prisoner_management, ":target"),

    # 统御
    (store_add, ":operate_slot_1826", "$g_pm_auto_point_base_slot_part", 26), # 1826
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1826"),
    (store_skill_level, ":current", skl_leadership, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_leadership, ":target"),

    # 交易
    (store_add, ":operate_slot_1827", "$g_pm_auto_point_base_slot_part", 27), # 1827
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1827"),
    (store_skill_level, ":current", skl_trade, ":troop"),
    (val_sub, ":target", ":current"),
    (troop_raise_skill, ":troop", skl_trade, ":target"),

    # ========== 恢复 7 个武器熟练度 ==========
    # 单手
    (store_add, ":operate_slot_1828", "$g_pm_auto_point_base_slot_part", 28), # 1828
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1828"),
    (store_proficiency_level, ":current", ":troop", wpt_one_handed_weapon),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_one_handed_weapon, ":target"),

    # 双手
    (store_add, ":operate_slot_1829", "$g_pm_auto_point_base_slot_part", 29), # 1829
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1829"),
    (store_proficiency_level, ":current", ":troop", wpt_two_handed_weapon),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_two_handed_weapon, ":target"),

    # 长杆
    (store_add, ":operate_slot_1830", "$g_pm_auto_point_base_slot_part", 30), # 1830
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1830"),
    (store_proficiency_level, ":current", ":troop", wpt_polearm),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_polearm, ":target"),

    # 弓
    (store_add, ":operate_slot_1831", "$g_pm_auto_point_base_slot_part", 31), # 1831
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1831"),
    (store_proficiency_level, ":current", ":troop", wpt_archery),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_archery, ":target"),

    # 弩
    (store_add, ":operate_slot_1832", "$g_pm_auto_point_base_slot_part", 32), # 1832
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1832"),
    (store_proficiency_level, ":current", ":troop", wpt_crossbow),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_crossbow, ":target"),

    # 投掷
    (store_add, ":operate_slot_1833", "$g_pm_auto_point_base_slot_part", 33), # 1833
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1833"),
    (store_proficiency_level, ":current", ":troop", wpt_throwing),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_throwing, ":target"),

    # 火器
    (store_add, ":operate_slot_1834", "$g_pm_auto_point_base_slot_part", 34), # 1834
    (troop_get_slot, ":target", "trp_auto_point", ":operate_slot_1834"),
    (store_proficiency_level, ":current", ":troop", wpt_firearm),
    (val_sub, ":target", ":current"),
    (troop_raise_proficiency_linear, ":troop", wpt_firearm, ":target"),

    # ========== 恢复 3 个可用点数【直接 set 即可】 ==========
    (store_add, ":operate_slot_1835", "$g_pm_auto_point_base_slot_part", 35), # 1835
    (troop_get_slot, reg0, "trp_auto_point", ":operate_slot_1835"),
    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
    (troop_set_slot, ":troop", ":auto_all_slot_1613", reg0),
    
    (store_add, ":operate_slot_1836", "$g_pm_auto_point_base_slot_part", 36), # 1836
    (troop_get_slot, reg0, "trp_auto_point", ":operate_slot_1836"),
    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
    (troop_set_slot, ":troop", ":auto_all_slot_1614", reg0),
    
    (store_add, ":operate_slot_1837", "$g_pm_auto_point_base_slot_part", 37), # 1837
    (troop_get_slot, reg0, "trp_auto_point", ":operate_slot_1837"),
    (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
    (troop_set_slot, ":troop", ":auto_all_slot_1615", reg0),
  ]),


# ==============================================
# 脚本名称：new_char_sys_respec_troop_full
# 功能：完整洗点 —— 恢复初始属性/技能，保留加成，计算返还点数
# 传入：troop
# 输出：
#   ":reset_attr_points"  洗出的总属性点
#   ":reset_skill_points" 洗出的总技能点
# ==============================================
("new_char_sys_respec_troop_full", [
    (store_script_param, ":troop", 1),
    # 清零统计值
    (assign, ":reset_attr_points", 0),
    (assign, ":reset_skill_points", 0),

    # ==========================================
    # 1. 先获取【当前智力】和【初始智力】
    # ==========================================
    (call_script, "script_store_intelligence_attribute_level", ":troop"),
    (assign, ":old_int", reg0),
    (store_add, ":auto_all_slot_1624", "$g_pm_auto_point_base_slot", 24), # 1624
    (troop_get_slot, ":base_int", ":troop", ":auto_all_slot_1624"),

    # ==========================================
    # 2. 恢复所有属性 → 同时统计返还的属性点
    # ==========================================
    # 力量
    (store_attribute_level, ":old_str", ":troop", ca_strength),
    (store_add, ":auto_all_slot_1622", "$g_pm_auto_point_base_slot", 22), # 1622
    (troop_get_slot, ":base_str", ":troop", ":auto_all_slot_1622"),
    (store_sub, ":diff", ":old_str", ":base_str"),
    (val_add, ":reset_attr_points", ":diff"),
    (store_sub, ":neg_diff", 0, ":diff"),
    (troop_raise_attribute, ":troop", ca_strength, ":neg_diff"),

    # 敏捷
    (store_attribute_level, ":old_agi", ":troop", ca_agility),
    (store_add, ":auto_all_slot_1623", "$g_pm_auto_point_base_slot", 23), # 1623
    (troop_get_slot, ":base_agi", ":troop", ":auto_all_slot_1623"),
    (store_sub, ":diff", ":old_agi", ":base_agi"),
    (val_add, ":reset_attr_points", ":diff"),
    (store_sub, ":neg_diff", 0, ":diff"),
    (troop_raise_attribute, ":troop", ca_agility, ":neg_diff"),

    # 智力
    (store_sub, ":diff_int", ":old_int", ":base_int"),
    (val_add, ":reset_attr_points", ":diff_int"),
    (store_sub, ":neg_diff_int", 0, ":diff_int"),
    (call_script, "script_raise_intelligence_attribute_level", ":troop", ":neg_diff_int"),

    # (call_script, "script_store_intelligence_attribute_level", ":troop"),
    # (assign, ":curr_v", reg0),
    # (troop_set_slot, ":troop", 1604, ":curr_v"),  # 设置智力之前的值为目标值，不然智力会参与二次计算

    # 魅力
    (store_attribute_level, ":old_cha", ":troop", ca_charisma),
    (store_add, ":auto_all_slot_1625", "$g_pm_auto_point_base_slot", 25), # 1625
    (troop_get_slot, ":base_cha", ":troop", ":auto_all_slot_1625"),
    (store_sub, ":diff", ":old_cha", ":base_cha"),
    (val_add, ":reset_attr_points", ":diff"),
    (store_sub, ":neg_diff", 0, ":diff"),
    (troop_raise_attribute, ":troop", ca_charisma, ":neg_diff"),

    # ==========================================
    # 3. 智力变化 → 技能点返还
    # ==========================================
    # (store_mul, ":skill_change", ":diff_int", 1),
    # (val_sub, ":reset_skill_points", ":skill_change"),

    # ==========================================
    # 4. 恢复所有技能【保留装备/加成】
    # ==========================================
    (store_add, ":auto_all_slot_1654", "$g_pm_auto_point_base_slot", 54), # 1654
    (assign, ":skl_offset", ":auto_all_slot_1654"),

    (try_for_range, ":skl", 0, 37),
        (this_or_next|eq, ":skl", "skl_ironflesh"),
        (this_or_next|eq, ":skl", "skl_power_strike"),
        (this_or_next|eq, ":skl", "skl_power_throw"),
        (this_or_next|eq, ":skl", "skl_power_draw"),
        (this_or_next|eq, ":skl", "skl_weapon_master"),
        (this_or_next|eq, ":skl", "skl_shield"),
        (this_or_next|eq, ":skl", "skl_athletics"),
        (this_or_next|eq, ":skl", "skl_riding"),
        (this_or_next|eq, ":skl", "skl_horse_archery"),
        (this_or_next|eq, ":skl", "skl_looting"),
        (this_or_next|eq, ":skl", "skl_trainer"),
        (this_or_next|eq, ":skl", "skl_tracking"),
        (this_or_next|eq, ":skl", "skl_tactics"),
        (this_or_next|eq, ":skl", "skl_pathfinding"),
        (this_or_next|eq, ":skl", "skl_spotting"),
        (this_or_next|eq, ":skl", "skl_inventory_management"),
        (this_or_next|eq, ":skl", "skl_wound_treatment"),
        (this_or_next|eq, ":skl", "skl_surgery"),
        (this_or_next|eq, ":skl", "skl_first_aid"),
        (this_or_next|eq, ":skl", "skl_engineer"),
        (this_or_next|eq, ":skl", "skl_persuasion"),
        (this_or_next|eq, ":skl", "skl_prisoner_management"),
        (this_or_next|eq, ":skl", "skl_leadership"),
        (eq, ":skl", "skl_trade"),
        # 当前总技能等级【含加成】
        (store_skill_level, ":old_total", ":skl", ":troop"),
        # 获取加成
        (call_script, "script_game_get_skill_modifier_for_troop", ":troop", ":skl"),
        (assign, ":modifier", reg0),
        # 玩家手动加的技能点
        (store_sub, ":old_spent", ":old_total", ":modifier"),
        # 初始技能等级
        (troop_get_slot, ":base_skill", ":troop", ":skl_offset"),
        # 计算需要重置的点数
        (store_sub, ":diff_skill", ":old_spent", ":base_skill"),
        (val_add, ":reset_skill_points", ":diff_skill"),
        # 恢复技能
        (store_sub, ":neg_diff_skill", 0, ":diff_skill"),
        (troop_raise_skill, ":troop", ":skl", ":neg_diff_skill"),
        (val_sub, ":skl_offset", 1),
    (try_end),

    # ==========================================
    # 5. 把洗出来的点数还给玩家
    # ==========================================
    # 属性点
    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
    (troop_get_slot, ":attr_points", ":troop", ":auto_all_slot_1613"),
    (val_add, ":attr_points", ":reset_attr_points"),
    (troop_set_slot, ":troop", ":auto_all_slot_1613", ":attr_points"),


    # 技能点
    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
    (troop_get_slot, ":skill_points", ":troop", ":auto_all_slot_1614"),
    (val_add, ":skill_points", ":reset_skill_points"),
    (troop_set_slot, ":troop", ":auto_all_slot_1614", ":skill_points"),


    # 执行完之后，将重置的对象也更改
    (call_script, "script_save_troop_points_for_reset", ":troop"),

  ]),


# 开始洗点【实际调用的op】
("use_it_new_char_sys_respec_troop_full", [
    (store_script_param, ":troop", 1),
    # 清零统计值
    (assign, ":reset_attr_points", 0),
    (assign, ":reset_skill_points", 0),

    (try_begin),
        (eq, "$g_pm_auto_point_is_can_move_item", 0), 
        (display_message, "str_auto_point_not_move_item", 0xFF0000), # 提示无法在该场景进行洗点
    (try_end),
    (eq, "$g_pm_auto_point_is_can_move_item", 1), 

    # ==========================================
    # 1. 先获取【当前智力】和【初始智力】
    # ==========================================
    #(store_attribute_level, ":old_int", ":troop", ca_intelligence),
    (call_script, "script_store_intelligence_attribute_level", ":troop"),
    (assign, ":old_int", reg0),
    (store_add, ":auto_all_slot_1624", "$g_pm_auto_point_base_slot", 24), # 1624
    (troop_get_slot, ":base_int", ":troop", ":auto_all_slot_1624"),


    # 力量
    (store_attribute_level, ":old_str", ":troop", ca_strength),
    (store_add, ":auto_all_slot_1622", "$g_pm_auto_point_base_slot", 22), # 1622
    (troop_get_slot, ":base_str", ":troop", ":auto_all_slot_1622"),
    (store_sub, ":diff", ":old_str", ":base_str"),
    (val_add, ":reset_attr_points", ":diff"),

    # 敏捷
    (store_attribute_level, ":old_agi", ":troop", ca_agility),
    (store_add, ":auto_all_slot_1623", "$g_pm_auto_point_base_slot", 23), # 1623
    (troop_get_slot, ":base_agi", ":troop", ":auto_all_slot_1623"),
    (store_sub, ":diff", ":old_agi", ":base_agi"),
    (val_add, ":reset_attr_points", ":diff"),

    # 智力
    (store_sub, ":diff_int", ":old_int", ":base_int"),
    (val_add, ":reset_attr_points", ":diff_int"),

    # 魅力
    (store_attribute_level, ":old_cha", ":troop", ca_charisma),
    (store_add, ":auto_all_slot_1625", "$g_pm_auto_point_base_slot", 25), # 1625
    (troop_get_slot, ":base_cha", ":troop", ":auto_all_slot_1625"),
    (store_sub, ":diff", ":old_cha", ":base_cha"),
    (val_add, ":reset_attr_points", ":diff"),

    # ==========================================
    # 3. 智力变化 → 技能点返还
    # ==========================================
    (store_mul, ":skill_change", ":diff_int", 1),
    #(val_sub, ":reset_skill_points", ":skill_change"),

    # ==========================================
    # 4. 恢复所有技能【保留装备/加成】
    # ==========================================
    (store_add, ":auto_all_slot_1654", "$g_pm_auto_point_base_slot", 54), # 1654
    (assign, ":skl_offset", ":auto_all_slot_1654"),

    (try_for_range, ":skl", 0, 37),
        (this_or_next|eq, ":skl", "skl_ironflesh"),
        (this_or_next|eq, ":skl", "skl_power_strike"),
        (this_or_next|eq, ":skl", "skl_power_throw"),
        (this_or_next|eq, ":skl", "skl_power_draw"),
        (this_or_next|eq, ":skl", "skl_weapon_master"),
        (this_or_next|eq, ":skl", "skl_shield"),
        (this_or_next|eq, ":skl", "skl_athletics"),
        (this_or_next|eq, ":skl", "skl_riding"),
        (this_or_next|eq, ":skl", "skl_horse_archery"),
        (this_or_next|eq, ":skl", "skl_looting"),
        (this_or_next|eq, ":skl", "skl_trainer"),
        (this_or_next|eq, ":skl", "skl_tracking"),
        (this_or_next|eq, ":skl", "skl_tactics"),
        (this_or_next|eq, ":skl", "skl_pathfinding"),
        (this_or_next|eq, ":skl", "skl_spotting"),
        (this_or_next|eq, ":skl", "skl_inventory_management"),
        (this_or_next|eq, ":skl", "skl_wound_treatment"),
        (this_or_next|eq, ":skl", "skl_surgery"),
        (this_or_next|eq, ":skl", "skl_first_aid"),
        (this_or_next|eq, ":skl", "skl_engineer"),
        (this_or_next|eq, ":skl", "skl_persuasion"),
        (this_or_next|eq, ":skl", "skl_prisoner_management"),
        (this_or_next|eq, ":skl", "skl_leadership"),
        (eq, ":skl", "skl_trade"),
        # 当前总技能等级【含加成】
        (store_skill_level, ":old_total", ":skl", ":troop"),
        # 获取加成
        (call_script, "script_game_get_skill_modifier_for_troop", ":troop", ":skl"),
        (assign, ":modifier", reg0),
        # 玩家手动加的技能点
        (store_sub, ":old_spent", ":old_total", ":modifier"),
        # 初始技能等级
        (troop_get_slot, ":base_skill", ":troop", ":skl_offset"),
        # 计算需要重置的点数
        (store_sub, ":diff_skill", ":old_spent", ":base_skill"),
        (val_add, ":reset_skill_points", ":diff_skill"),
        (val_sub, ":skl_offset", 1),
    (try_end),

    # ==========================================
    # 计算洗点花的第纳尔【由于智力对技能点的影响，所以计算洗下的技能点【计算钱的】和实际洗点算法是有出入的】
    # ==========================================
    # 例子：1属性点=第纳尔，1技能点=第纳尔
    (store_mul, ":cost1", ":reset_attr_points", "$g_pm_reset_price_per_attr_point"),
    (store_mul, ":cost2", ":reset_skill_points", "$g_pm_reset_price_per_skill_point"),
    (store_add, ":total_cost", ":cost1", ":cost2"),

    (store_troop_gold, ":curr_gold", "trp_player"),
    (try_begin),
        (neg|ge, ":curr_gold", ":total_cost"),
        (display_message, "str_auto_point_not_money", 0xFF0000), # 提示没有钱
    (try_end),
    (ge, ":curr_gold", ":total_cost"), # 检查背包是否有这么多钱



    # ==========================================
    # 装备拆到玩家的物品栏
    # ==========================================
    
    # 有特殊情况不会拆装备，就是玩家等级没到指定等级不让扒装备的npc
    (assign, ":is_special_case", 0),
    (try_begin),
        (store_character_level, ":curr_character_level", "trp_player"), # 获取玩家等级
        (store_add, ":auto_all_slot_1629", "$g_pm_auto_point_base_slot", 29), # 1629
        (troop_get_slot, ":curr_can_equip_slot_value", ":troop", ":auto_all_slot_1629"), # 获取某个槽的值，如果玩家没达到该等级，则无法进行换装
        (neg|ge, ":curr_character_level", ":curr_can_equip_slot_value"), # 当前玩家等级大于等于该值
        (assign, ":is_special_case", 1),
    (try_end),


    (assign, ":has_equip_nums", 0),  # 计算troop装备数量
    (try_for_range, ":equip_slot", 0, 9),
        (troop_get_inventory_slot, ":item", ":troop", ":equip_slot"),
        (try_begin),
           (neg|eq, ":item", -1), # 槽位不为空，进行计数
           (val_add, ":has_equip_nums", 1),
        (try_end),
    (try_end),
    (assign, reg10, ":has_equip_nums"),
    #(display_message, "@{reg10}", 0xFFFF00), 
    # 计算玩家是否有足够空间放这些装备
    (assign, ":has_free_cap", 0),
    (assign, ":free_cap", 0),
    (try_begin),
        # 如果洗点的对象不是玩家
        (neg|eq, ":troop", "trp_player"),
        (store_free_inventory_capacity, ":free_cap"),
    (else_try),
        # 如果洗点的对象是玩家，则需要考虑到玩家洗点后的物品栏变化【只有30个格子】
        (eq, ":troop", "trp_player"),
        (try_for_range, ":inv_slot", 10, 40),
            (troop_get_inventory_slot, ":item_id", "trp_player", ":inv_slot"),
            (eq, ":item_id", -1), # 槽位为空，进行计数
            (val_add, ":free_cap", 1),
        (try_end),
        (assign, reg10, ":free_cap"),
        #(display_message, "@{reg10}", 0xFF0000), 
    (try_end),
    # 判断是否卸装备或者需要提示
    (try_begin),
        (neg|ge, ":free_cap", ":has_equip_nums"),  # 如果没有空间则提示
        (eq, ":is_special_case", 0), # 不是特殊情况
        (display_message, "str_auto_point_not_free_cap", 0xFF0000), # 提示没有物品栏
    (else_try),
        (ge, ":free_cap", ":has_equip_nums"), # 必须有空间
        (assign, ":has_free_cap", 1), # 可以进行卸装备
    (try_end),


    # 特殊情况和有空间的情况，往下进行
    (this_or_next|eq, ":has_free_cap", 1),
    (eq, ":is_special_case", 1),

    # 遍历玩家的空的物品栏，将装备卸下
    (try_begin),
        (eq, ":is_special_case", 0), # 不为特殊情况才进行卸装备
        (troop_get_inventory_capacity, ":player_inv_capacity", "trp_player"),  # 获取玩家背包总容量
        (try_for_range, ":inv_slot", 10, ":player_inv_capacity"),
            # 获取背包物品
            (troop_get_inventory_slot, ":item_id", "trp_player", ":inv_slot"),
            (eq, ":item_id", -1), # 槽位为空，进行卸装备操作
            (assign, ":is_change", 0),
            (try_for_range_backwards, ":equip_slot", 0, 9),
                (eq, ":is_change", 0),
                (troop_get_inventory_slot, ":item", ":troop", ":equip_slot"),
                (try_begin),
                    (neg|eq, ":item", -1), # 槽位不为空，进行操作
                    (troop_get_inventory_slot, ":hero_item", ":troop", ":equip_slot"),
                    (troop_get_inventory_slot_modifier, ":hero_mod", ":troop", ":equip_slot"),
                    # 设置物品栏为选取的装备
                    (troop_set_inventory_slot, "trp_player", ":inv_slot", ":hero_item"),
                    (troop_set_inventory_slot_modifier, "trp_player", ":inv_slot", ":hero_mod"),
                    # 设置装备栏为空
                    (troop_set_inventory_slot, ":troop", ":equip_slot", -1),
                    (assign, ":is_change", 1), # 用于跳出循环
                (try_end),
            (try_end),
        (try_end),
    (try_end),
    

    (troop_remove_gold, "trp_player", ":total_cost"),  # 进行扣钱

    (call_script, "script_new_char_sys_respec_troop_full", ":troop"), # 执行实际的洗点操作
    (call_script, "script_new_char_sys_respec_troop_full", ":troop"), # 执行实际的洗点操作【必须洗2次，不然有额外加成时满级技能洗不完】
    (try_begin),
        (eq, ":troop", "trp_player"), # 如果是玩家，洗完点后将物品栏设置为第一页
        (assign, "$g_pm_temp_4", 0),
    (try_end),


  ]),


# 计算洗点所需的第纳尔
("how_pay_respec_troop_full", [
    (store_script_param, ":troop", 1),
    # 清零统计值
    (assign, ":reset_attr_points", 0),
    (assign, ":reset_skill_points", 0),


    # ==========================================
    # 1. 先获取【当前智力】和【初始智力】
    # ==========================================
    (call_script, "script_store_intelligence_attribute_level", ":troop"),
    (assign, ":old_int", reg0),
    (store_add, ":auto_all_slot_1624", "$g_pm_auto_point_base_slot", 24), # 1624
    (troop_get_slot, ":base_int", ":troop", ":auto_all_slot_1624"),


    # 力量
    (store_attribute_level, ":old_str", ":troop", ca_strength),
    (store_add, ":auto_all_slot_1622", "$g_pm_auto_point_base_slot", 22), # 1622
    (troop_get_slot, ":base_str", ":troop", ":auto_all_slot_1622"),
    (store_sub, ":diff", ":old_str", ":base_str"),
    (val_add, ":reset_attr_points", ":diff"),

    # 敏捷
    (store_attribute_level, ":old_agi", ":troop", ca_agility),
    (store_add, ":auto_all_slot_1623", "$g_pm_auto_point_base_slot", 23), # 1623
    (troop_get_slot, ":base_agi", ":troop", ":auto_all_slot_1623"),
    (store_sub, ":diff", ":old_agi", ":base_agi"),
    (val_add, ":reset_attr_points", ":diff"),

    # 智力
    (store_sub, ":diff_int", ":old_int", ":base_int"),
    (val_add, ":reset_attr_points", ":diff_int"),

    # 魅力
    (store_attribute_level, ":old_cha", ":troop", ca_charisma),
    (store_add, ":auto_all_slot_1625", "$g_pm_auto_point_base_slot", 25), # 1625
    (troop_get_slot, ":base_cha", ":troop", ":auto_all_slot_1625"),
    (store_sub, ":diff", ":old_cha", ":base_cha"),
    (val_add, ":reset_attr_points", ":diff"),

    # ==========================================
    # 3. 智力变化 → 技能点返还
    # ==========================================
    (store_mul, ":skill_change", ":diff_int", 1),
    #(val_sub, ":reset_skill_points", ":skill_change"),

    # ==========================================
    # 4. 恢复所有技能【保留装备/加成】
    # ==========================================
    (store_add, ":auto_all_slot_1654", "$g_pm_auto_point_base_slot", 54), # 1654
    (assign, ":skl_offset", ":auto_all_slot_1654"),

    (try_for_range, ":skl", 0, 37),
        (this_or_next|eq, ":skl", "skl_ironflesh"),
        (this_or_next|eq, ":skl", "skl_power_strike"),
        (this_or_next|eq, ":skl", "skl_power_throw"),
        (this_or_next|eq, ":skl", "skl_power_draw"),
        (this_or_next|eq, ":skl", "skl_weapon_master"),
        (this_or_next|eq, ":skl", "skl_shield"),
        (this_or_next|eq, ":skl", "skl_athletics"),
        (this_or_next|eq, ":skl", "skl_riding"),
        (this_or_next|eq, ":skl", "skl_horse_archery"),
        (this_or_next|eq, ":skl", "skl_looting"),
        (this_or_next|eq, ":skl", "skl_trainer"),
        (this_or_next|eq, ":skl", "skl_tracking"),
        (this_or_next|eq, ":skl", "skl_tactics"),
        (this_or_next|eq, ":skl", "skl_pathfinding"),
        (this_or_next|eq, ":skl", "skl_spotting"),
        (this_or_next|eq, ":skl", "skl_inventory_management"),
        (this_or_next|eq, ":skl", "skl_wound_treatment"),
        (this_or_next|eq, ":skl", "skl_surgery"),
        (this_or_next|eq, ":skl", "skl_first_aid"),
        (this_or_next|eq, ":skl", "skl_engineer"),
        (this_or_next|eq, ":skl", "skl_persuasion"),
        (this_or_next|eq, ":skl", "skl_prisoner_management"),
        (this_or_next|eq, ":skl", "skl_leadership"),
        (eq, ":skl", "skl_trade"),
        # 当前总技能等级【含加成】
        (store_skill_level, ":old_total", ":skl", ":troop"),
        # 获取加成
        (call_script, "script_game_get_skill_modifier_for_troop", ":troop", ":skl"),
        (assign, ":modifier", reg0),
        # 玩家手动加的技能点
        (store_sub, ":old_spent", ":old_total", ":modifier"),
        # 初始技能等级
        (troop_get_slot, ":base_skill", ":troop", ":skl_offset"),
        # 计算需要重置的点数
        (store_sub, ":diff_skill", ":old_spent", ":base_skill"),
        (val_add, ":reset_skill_points", ":diff_skill"),
        (val_sub, ":skl_offset", 1),
    (try_end),

    # ==========================================
    # 计算洗点花的第纳尔【由于智力对技能点的影响，所以计算洗下的技能点【计算钱的】和实际洗点算法是有出入的】
    # ==========================================
    # 例子：1属性点=第纳尔，1技能点=第纳尔
    (store_mul, ":cost1", ":reset_attr_points", "$g_pm_reset_price_per_attr_point"),
    (store_mul, ":cost2", ":reset_skill_points", "$g_pm_reset_price_per_skill_point"),
    (store_add, ":total_cost", ":cost1", ":cost2"),

    (assign, reg0, ":total_cost"),
    (assign, reg1, ":reset_attr_points"),
    (assign, reg2, ":reset_skill_points"),
    (str_store_troop_name, s1, ":troop"),



  ]),


# 通过传入的下拉框的值 auto_point_skill和目标值 auto_point_skill_dst，
# 获取实际的属性【reg0】需要加点的属性值reg1和值reg2
("calc_auto_point_dst_attri", [
    (store_script_param, ":auto_point_skill", 1),
    (store_script_param, ":auto_point_skill_dst", 2),

    (assign, reg0, -1),
    (assign, reg1, -1),

    # 获取实际的属性值auto_point_skill=1时为交易
    (try_begin), #24 = 铁骨
        (eq, ":auto_point_skill", 24),
        (assign, reg0, "skl_ironflesh"),
        (assign, reg1, ca_strength),
    (else_try), # 23 = 强击
        (eq, ":auto_point_skill", 23),
        (assign, reg0, "skl_power_strike"),
        (assign, reg1, ca_strength),
    (else_try),  # 22 = 强掷
        (eq, ":auto_point_skill", 22),
        (assign, reg0, "skl_power_throw"),
        (assign, reg1, ca_strength),
    (else_try),  # 21 = 强弓
        (eq, ":auto_point_skill", 21),
        (assign, reg0, "skl_power_draw"),
        (assign, reg1, ca_strength),
    (else_try),   # 20 = 武器掌握
        (eq, ":auto_point_skill", 20),
        (assign, reg0, "skl_weapon_master"),
        (assign, reg1, ca_agility),
    (else_try),   # 19 = 盾防
        (eq, ":auto_point_skill", 19),
        (assign, reg0, "skl_shield"),
        (assign, reg1, ca_agility),
    (else_try),  # 18 = 跑动
        (eq, ":auto_point_skill", 18),
        (assign, reg0, "skl_athletics"),
        (assign, reg1, ca_agility),
    (else_try),  # 17 = 骑术
        (eq, ":auto_point_skill", 17),
        (assign, reg0, "skl_riding"),
        (assign, reg1, ca_agility),
    (else_try),  # 16 = 骑射
        (eq, ":auto_point_skill", 16),
        (assign, reg0, "skl_horse_archery"),
        (assign, reg1, ca_agility),
    (else_try),  # 15 = 掠夺
        (eq, ":auto_point_skill", 15),
        (assign, reg0, "skl_looting"),
        (assign, reg1, ca_agility),
    (else_try),  # 14 = 教练
        (eq, ":auto_point_skill", 14),
        (assign, reg0, "skl_trainer"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 13 = 追踪
        (eq, ":auto_point_skill", 13),
        (assign, reg0, "skl_tracking"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 12 = 战术
        (eq, ":auto_point_skill", 12),
        (assign, reg0, "skl_tactics"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 11 = 向导
        (eq, ":auto_point_skill", 11),
        (assign, reg0, "skl_pathfinding"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 10 = 侦察
        (eq, ":auto_point_skill", 10),
        (assign, reg0, "skl_spotting"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 9 = 辎重管理
        (eq, ":auto_point_skill", 9),
        (assign, reg0, "skl_inventory_management"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 8 = 疗伤
        (eq, ":auto_point_skill", 8),
        (assign, reg0, "skl_wound_treatment"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 7 = 手术
        (eq, ":auto_point_skill", 7),
        (assign, reg0, "skl_surgery"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 6 = 急救
        (eq, ":auto_point_skill", 6),
        (assign, reg0, "skl_first_aid"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 5 = 工程学
        (eq, ":auto_point_skill", 5),
        (assign, reg0, "skl_engineer"),
        (assign, reg1, ca_intelligence),
    (else_try),  # 4 = 说服
        (eq, ":auto_point_skill", 4),
        (assign, reg0, "skl_persuasion"),
        (assign, reg1, ca_charisma),
    (else_try),  # 3 = 俘虏管理
        (eq, ":auto_point_skill", 3),
        (assign, reg0, "skl_prisoner_management"),
        (assign, reg1, ca_charisma),
    (else_try),  # 2 = 统御
        (eq, ":auto_point_skill", 2),
        (assign, reg0, "skl_leadership"),
        (assign, reg1, ca_charisma),
    (else_try),  # 1 = 交易
        (eq, ":auto_point_skill", 1),
        (assign, reg0, "skl_trade"),
        (assign, reg1, ca_charisma),
    (try_end),
    # 对应的属性值乘3
    (store_mul, reg2, ":auto_point_skill_dst", 3),
]),



# 通过当前troop装备的武器类型，判断自动加武器点的项
("auto_point_add_weapon", [
 # 获取玩家队伍同伴数量
    (party_get_num_companion_stacks, ":companion_count", "p_main_party"),
    # 遍历所有同伴
    (try_for_range, ":stack_index", 0, ":companion_count"),
        # 获取当前部队的英雄ID
        (party_stack_get_troop_id, ":troop", "p_main_party", ":stack_index"),
        # 筛选条件：玩家/特殊英雄/英雄单位/排除指定NPC
        (troop_is_hero, ":troop"),
        (store_add, ":auto_all_slot_1630", "$g_pm_auto_point_base_slot", 30), # 1630
        (store_add, ":auto_all_slot_1724", "$g_pm_auto_point_base_slot", 124), # 1724
        (troop_slot_eq, ":troop", ":auto_all_slot_1630", 1), # 判断该槽值为1，代表可以进行加点操作的troop
        (troop_slot_eq, ":troop", ":auto_all_slot_1724", 1), # 判断该槽值为1，代表开启加点功能的troop
        (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
        (troop_get_slot, ":curr_weapon_point", ":troop", ":auto_all_slot_1615"), # 获取剩余未加的武器点
        (gt, ":curr_weapon_point", 0), # 武器点大于0
        # 定义四个槽的类型 
        (store_add, ":item_type_base_slot", "$g_pm_auto_point_base_slot_part", 571), # 2371 存储4个武器槽的基础值
        (try_for_range, ":weapon_index", 0, 4),
            (store_add, ":item_type_slot",":item_type_base_slot", ":weapon_index"),
            (troop_set_slot, "trp_auto_point", ":item_type_slot", -1), # 设置默认值为-1
            # 获取当前槽的武器类型
            (troop_get_inventory_slot, ":troop_item", ":troop", ":weapon_index"),
            (gt, ":troop_item", 0), # 存在武器
            (item_get_type, ":item_type", ":troop_item"),
            (try_begin),
                (eq, ":item_type", itp_type_one_handed_wpn), # 单手武器
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_one_handed_weapon),
            (else_try),
                (eq, ":item_type", itp_type_two_handed_wpn), # 双手武器
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_two_handed_weapon),
            (else_try),
                (eq, ":item_type", itp_type_polearm), # 长杆武器
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_polearm),
            (else_try),
                (eq, ":item_type", itp_type_bow), # 弓
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_archery),
            (else_try),
                (eq, ":item_type", itp_type_crossbow), # 弩
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_crossbow),
            (else_try),
                (eq, ":item_type", itp_type_thrown), # 投掷
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_throwing),
            (else_try),
                (this_or_next|eq, ":item_type", itp_type_pistol), # 火器
                (eq, ":item_type", itp_type_musket), # 火枪
                (troop_set_slot, "trp_auto_point", ":item_type_slot", wpt_firearm),
            (else_try),
                (troop_set_slot, "trp_auto_point", ":item_type_slot", -1),
            (try_end),
        (try_end),
        # 进行武器加点
        (try_for_range, ":weapon_add_index", 0, ":curr_weapon_point"),
            # 定义一个比较大的值，比如10000，这个值用来获取玩家当前最小的武器值
            (assign, ":weapon_type_min_value", 10000),
            (assign, ":weapon_type_min", -1),
            (try_for_range, ":weapon_index", 0, 4),  # 获取当前4个槽当中值最小的那个，进行一次加点
                (store_add, ":item_type_slot",":item_type_base_slot", ":weapon_index"),
                (troop_get_slot, ":curr_weapon_type", "trp_auto_point", ":item_type_slot"), # 获取当前槽的武器类型
                (neg|eq, ":curr_weapon_type", -1), # 且不等于-1时
                (store_proficiency_level, ":curr_weapon_value", ":troop", ":curr_weapon_type"), # 获取槽里保存的类型的值
                (assign, reg0, ":curr_weapon_value"),
                #(display_message, "@{reg0}", 0xFF0000),
                (try_begin),
                    (le, ":curr_weapon_value", ":weapon_type_min_value"), # 当比上一个值要小时
                    (assign, ":weapon_type_min_value", ":curr_weapon_value"),
                    (assign, ":weapon_type_min", ":curr_weapon_type"),  # 则定义为新的武器类型的槽值
                (try_end),
            (try_end),
            # 获取到最小的值后，进行武器的加点
            #(display_message, "@-------------", 0xFF0000),
            (neg|eq, ":weapon_type_min", -1),
            (call_script, "script_new_char_sys_add_weapon_point", ":troop", ":weapon_type_min", 1),
        (try_end),
    (try_end),
]),

  
# 开始自动加点【实际调用的op】
("start_auto_point", [
    (store_add, ":auto_all_slot_1724", "$g_pm_auto_point_base_slot", 124), # 1724
    (assign, ":is_open_auto_point_slot", ":auto_all_slot_1724"), # 自动加点-是否开启自动加点 1开启，0未开启 
    (store_add, ":auto_all_slot_1655", "$g_pm_auto_point_base_slot", 55), # 1655
    (assign, ":auto_point_skill_base_slot", ":auto_all_slot_1655"), # 自动加点-下拉框1-23的加点项，数量23 0为未开启，1为交易，24是铁骨 
    (store_add, ":auto_all_slot_1678", "$g_pm_auto_point_base_slot", 78), # 1678
    (assign, ":auto_point_skill_dst_base_slot", ":auto_all_slot_1678"), # 自动加点-自动加点目标值，数量23
    (store_add, ":auto_all_slot_1701", "$g_pm_auto_point_base_slot", 101), # 1701
    (assign, ":is_force_base_slot", ":auto_all_slot_1701"), # 自动加点-技能点不够是否点智力强行加点，数量23

    (store_add, ":auto_all_slot_1630", "$g_pm_auto_point_base_slot", 30), # 1630

    # 获取玩家队伍同伴数量
    (party_get_num_companion_stacks, ":companion_count", "p_main_party"),
    # 遍历所有同伴
    (try_for_range, ":stack_index", 0, ":companion_count"),
        # 获取当前部队的英雄ID
        (party_stack_get_troop_id, ":troop", "p_main_party", ":stack_index"),
        # 筛选条件：玩家/特殊英雄/英雄单位/排除指定NPC
        (troop_is_hero, ":troop"),
        (troop_slot_eq, ":troop", ":auto_all_slot_1630", 1), # 判断该槽值为1，代表可以进行加点操作的troop
        (troop_slot_eq, ":troop", ":auto_all_slot_1724", 1), # 判断该槽值为1，代表开启加点功能的troop
        # 自动加点前，进行可利用点的计算
        (call_script, "script_calculate_available_points", ":troop"),
        (assign, ":max_btn", 23),
        (try_for_range, ":btn_idx", 0, ":max_btn"),
            (store_add, ":auto_point_skill_slot",":auto_point_skill_base_slot", ":btn_idx"),
            # 获取下拉框的值 auto_point_skill
            (troop_get_slot, ":auto_point_skill", ":troop", ":auto_point_skill_slot"),  
            (try_begin),
                (gt, ":auto_point_skill", 0), # 下拉框选择的值不为”未选择“
                # 获取目标值 auto_point_skill_dst
                (store_add, ":auto_point_skill_dst_slot",":auto_point_skill_dst_base_slot", ":btn_idx"),
                (troop_get_slot, ":auto_point_skill_dst", ":troop", ":auto_point_skill_dst_slot"),  # 获取目标值
                (try_begin),
                    (gt, ":auto_point_skill_dst", 0), # 目标值大于0
                    (call_script, "script_calc_auto_point_dst_attri", ":auto_point_skill", ":auto_point_skill_dst"),
                    (assign, ":curr_skill_flag", reg0), # 技能flag
                    (assign, ":curr_attri_flag", reg1), # 属性flag
                    (assign, ":curr_attri_dst_value", reg2), # 属性值预计升到的值
                    # ==============================================
                    # 加属性
                    # ==============================================
                    # 获取当前属性等级  
                    (try_begin),
                        (store_attribute_level, ":curr_attri_value", ":troop", ":curr_attri_flag"), 
                        (gt, ":curr_attri_dst_value", ":curr_attri_value"),  # 属性值预计升到的值 大于 当前属性值 则加属性到预计值
                        (store_sub, ":diff_attri", ":curr_attri_dst_value", ":curr_attri_value"),  # 计算差值
                        (try_for_range, ":add_range", 0, ":diff_attri"), # 循环进行加属性点
                            (call_script, "script_new_char_sys_add_attr_point", ":troop", ":curr_attri_flag", 1),
                        (try_end),
                    (try_end),
                    # 加属性后，进行技能点的重新计算
                    (call_script, "script_calculate_available_points", ":troop"),
                    # ==============================================
                    # 加技能【不强行加的】
                    # ==============================================
                    # 获取当前技能等级
                    (try_begin),
                        (store_skill_level, ":curr_skill_value", ":curr_skill_flag", ":troop"), # 获取技能值
                        (gt, ":auto_point_skill_dst", ":curr_skill_value"),  # 技能值预计升到的值 大于 当前技能值 则加技能到预计值
                        (store_sub, ":diff_skill", ":auto_point_skill_dst", ":curr_skill_value"),  # 计算差值
                        (try_for_range, ":add_range", 0, ":diff_skill"), # 循环进行加技能点
                            (call_script, "script_new_char_sys_add_skill_point", ":troop", ":curr_skill_flag", 1),
                        (try_end),
                    (try_end),
                    # ==============================================
                    # 加技能【勾选了强行加】
                    # 如果加了目标技能点，但是还没达到目标值，则会触发，加一点智力来增加一点技能点
                    # ==============================================
                    # 获取目标值 auto_point_is_force
                    (try_begin),
                        (store_add, ":is_force_dst_slot",":is_force_base_slot", ":btn_idx"),
                        (troop_get_slot, ":auto_point_is_force", ":troop", ":is_force_dst_slot"),  # 获取目标值
                        (eq, ":auto_point_is_force", 1),  # 开启了强行加点
                        # 计算目前还差多少，就是需要加多少智力的点
                        (store_skill_level, ":curr_skill_value", ":curr_skill_flag", ":troop"), # 获取技能值
                        (gt, ":auto_point_skill_dst", ":curr_skill_value"),  # 技能值预计升到的值 大于 当前技能值 则加技能到预计值
                        (store_sub, ":diff_skill", ":auto_point_skill_dst", ":curr_skill_value"),  # 计算差值
                        (try_for_range, ":add_range", 0, ":diff_skill"), # 循环进行加智力
                            (call_script, "script_new_char_sys_add_attr_point", ":troop", ca_intelligence, 1),
                        (try_end),
                    (try_end),
                    # 加属性后，进行技能点的重新计算
                    (call_script, "script_calculate_available_points", ":troop"),
                    # 再次加技能
                    (try_begin),
                        (store_skill_level, ":curr_skill_value", ":curr_skill_flag", ":troop"), # 获取技能值
                        (gt, ":auto_point_skill_dst", ":curr_skill_value"),  # 技能值预计升到的值 大于 当前技能值 则加技能到预计值
                        (store_sub, ":diff_skill", ":auto_point_skill_dst", ":curr_skill_value"),  # 计算差值
                        (try_for_range, ":add_range", 0, ":diff_skill"), # 循环进行加技能点
                            (call_script, "script_new_char_sys_add_skill_point", ":troop", ":curr_skill_flag", 1),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
    (try_end),

    (call_script, "script_auto_point_add_weapon"),  # 进行武器点的加点

]),



# 自动加点-选择方案，可以选择预设方案覆盖当前加点方式
("auto_point_choose_scheme", [
  (store_script_param, ":selected_troop", 1),  # 获取当前操作的troop

  #(assign, reg0, "$g_pm_prsn_auto_point_comb_index"),
  #(display_message, "@{reg0}", 0xFF0000),

  # 获取当前方案下拉框选择的 g_prsn_auto_point_comb_index
  (store_add, ":tmp_offset", "$g_pm_auto_point_base_slot_part", 201),  # 2001
  (store_add, ":combo_button_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (store_add, ":number_box_button_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (store_add, ":checkbox_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (try_for_range_backwards, ":stack_index", 0, 71),
      (try_for_range, ":programme_index", 0, 10),
          # 计算索引值
          (eq, "$g_pm_prsn_auto_point_comb_index", ":programme_index"), # 仅处理当前选中的方案
          (store_mul, ":tmp_mul", ":programme_index", 100),
          (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
          (val_add, ":tmp_trp_index", ":tmp_mul"), 
          (try_begin),
              (is_between, ":stack_index", 1, 24),  # 技能下拉框 curr_skill_index
              (troop_get_slot, ":curr_skill_index", "trp_auto_point", ":tmp_trp_index"),
              # 设置troop的值
              (store_add, ":combo_button_slot_num_curr", ":combo_button_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_set_slot, ":selected_troop", ":combo_button_slot_num_curr", ":curr_skill_index"), # 设置某个槽的值
          (else_try),
              (is_between, ":stack_index", 24, 47),  # 目标技能值 curr_skill_value
              (troop_get_slot, ":curr_skill_value", "trp_auto_point", ":tmp_trp_index"),
              # 设置troop的值
              (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_set_slot, ":selected_troop", ":number_box_button_slot_num_curr", ":curr_skill_value"), # 设置某个槽的值
          (else_try),
              (is_between, ":stack_index", 47, 70),  # 是否强行加智力来增加值-否 curr_skill_is_force
              (troop_get_slot, ":curr_skill_is_force", "trp_auto_point", ":tmp_trp_index"),
              # 设置troop的值
              (store_add, ":checkbox_slot_num_curr", ":checkbox_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_set_slot, ":selected_troop", ":checkbox_slot_num_curr", ":curr_skill_is_force"), # 设置某个槽的值
          (try_end),
      (try_end),
  (try_end),


]),


# 自动加点-添加方案，可以将当前加点方式保存到预设方案
("auto_point_add_scheme", [
  (store_script_param, ":selected_troop", 1),  # 获取当前操作的troop

  # 获取当前方案下拉框选择的 g_prsn_auto_point_comb_index
  (store_add, ":tmp_offset", "$g_pm_auto_point_base_slot_part", 201),  # 2001
  (store_add, ":combo_button_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (store_add, ":number_box_button_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (store_add, ":checkbox_base_num_curr", "$g_pm_auto_point_base_slot", 54), # 1654
  (try_for_range_backwards, ":stack_index", 0, 71),
      (try_for_range, ":programme_index", 0, 10),
          # 计算索引值
          (eq, "$g_pm_prsn_auto_point_comb_index", ":programme_index"), # 仅处理当前选中的方案
          (store_mul, ":tmp_mul", ":programme_index", 100),
          (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
          (val_add, ":tmp_trp_index", ":tmp_mul"), 
          (try_begin),
              (is_between, ":stack_index", 1, 24),  # 技能下拉框 curr_skill_index
              (store_add, ":combo_button_slot_num_curr", ":combo_button_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_get_slot, ":curr_skill_index", ":selected_troop", ":combo_button_slot_num_curr"), # 设置某个槽的值
              # 设置troop的值
              (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":curr_skill_index"),
          (else_try),
              (is_between, ":stack_index", 24, 47),  # 目标技能值 curr_skill_value
              (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_get_slot, ":curr_skill_value", ":selected_troop", ":number_box_button_slot_num_curr"), # 设置某个槽的值
              # 设置troop的值
              (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":curr_skill_value"),
          (else_try),
              (is_between, ":stack_index", 47, 70),  # 是否强行加智力来增加值-否 curr_skill_is_force
              (store_add, ":checkbox_slot_num_curr", ":checkbox_base_num_curr", ":stack_index"), # 获取实际的槽
              (troop_get_slot, ":curr_skill_is_force", ":selected_troop", ":checkbox_slot_num_curr"), # 设置某个槽的值
              # 设置troop的值
              (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":curr_skill_is_force"),
          (try_end),

          # 设置方案名称
          (eq, ":stack_index", 0), # 方案名称
          (try_begin),  # 这个区间用单数
              (is_between, "$g_pm_prsn_auto_point_comb_index", 0, 5), 
              (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", "$g_pm_prsn_auto_point_comb_index"),
              (troop_set_name, ":trp_store_scheme_name", 24),
              (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
          (else_try),  # 这个区间用复数
              (is_between, "$g_pm_prsn_auto_point_comb_index", 5, 10),
              (store_sub, ":programme_index_sub_5", "$g_pm_prsn_auto_point_comb_index", 5),
              (store_add, ":trp_store_scheme_name", "trp_auto_point_store_scheme_name_1", ":programme_index_sub_5"),
              (troop_set_plural_name, ":trp_store_scheme_name", 24),
              (troop_set_slot, "trp_auto_point", ":tmp_trp_index", ":trp_store_scheme_name"), 
          (try_end),
      (try_end),
  (try_end),


]),

# 获取当前技能的最大值
("get_troop_skill_max_level", [
  (store_script_param, ":skill_id", 1),  # 获取当前操作的技能id
  (store_add, ":operate_index", "$g_pm_auto_point_base_slot_part", 154), # 交 易 1954
  (try_for_range, ":sub_idx", 0, 37),
      (this_or_next|eq, ":sub_idx", "skl_ironflesh"),
      (this_or_next|eq, ":sub_idx", "skl_power_strike"),
      (this_or_next|eq, ":sub_idx", "skl_power_throw"),
      (this_or_next|eq, ":sub_idx", "skl_power_draw"),
      (this_or_next|eq, ":sub_idx", "skl_weapon_master"),
      (this_or_next|eq, ":sub_idx", "skl_shield"),
      (this_or_next|eq, ":sub_idx", "skl_athletics"),
      (this_or_next|eq, ":sub_idx", "skl_riding"),
      (this_or_next|eq, ":sub_idx", "skl_horse_archery"),
      (this_or_next|eq, ":sub_idx", "skl_looting"),
      (this_or_next|eq, ":sub_idx", "skl_trainer"),
      (this_or_next|eq, ":sub_idx", "skl_tracking"),
      (this_or_next|eq, ":sub_idx", "skl_tactics"),
      (this_or_next|eq, ":sub_idx", "skl_pathfinding"),
      (this_or_next|eq, ":sub_idx", "skl_spotting"),
      (this_or_next|eq, ":sub_idx", "skl_inventory_management"),
      (this_or_next|eq, ":sub_idx", "skl_wound_treatment"),
      (this_or_next|eq, ":sub_idx", "skl_surgery"),
      (this_or_next|eq, ":sub_idx", "skl_first_aid"),
      (this_or_next|eq, ":sub_idx", "skl_engineer"),
      (this_or_next|eq, ":sub_idx", "skl_persuasion"),
      (this_or_next|eq, ":sub_idx", "skl_prisoner_management"),
      (this_or_next|eq, ":sub_idx", "skl_leadership"),
      (eq, ":sub_idx", "skl_trade"),
      (try_begin),
          (eq, ":sub_idx", ":skill_id"),  # 获取当前的技能最大值
          (troop_get_slot, reg0, "trp_auto_temp_list_3", ":operate_index"),
      (try_end),
      (val_sub, ":operate_index", 1),
  (try_end),

]),

# 记录同伴的初始属性和技能值，还有可分配的属性点和技能点【洗点用】
("auto_record_initial_attr_skill",
[
    (store_script_param, ":troop", 1),  # 记录初始状态的同伴
    (store_script_param, ":model", 2),  # 0为正常获取智力模式；1为获取新系统智力模式

    # 获取玩家的这些属性
    (store_attribute_level, ":var_begin_ca_strength", ":troop", ca_strength), # 获取初始力量属性
    (store_attribute_level, ":var_begin_ca_agility", ":troop", ca_agility), # 获取初始敏捷属性
    (store_attribute_level, ":var_begin_ca_intelligence", ":troop", ca_intelligence), # 获取初始智力属性
    (try_begin),
        (eq, ":model", 1),  # 智力单独计算
        #(troop_slot_eq, ":hero", 1630, 1),  # 新加点系统可以操作的troop
        (call_script, "script_store_intelligence_attribute_level", ":troop"),
        (assign, ":var_begin_ca_intelligence", reg0),
    (try_end),
    (store_attribute_level, ":var_begin_ca_charisma", ":troop", ca_charisma), # 获取初始魅力属性

    # 存储初始属性到槽里
    (store_add, ":auto_all_slot_1622", "$g_pm_auto_point_base_slot", 22), # 1622
    (troop_set_slot, ":troop", ":auto_all_slot_1622", ":var_begin_ca_strength"),
    (store_add, ":auto_all_slot_1623", "$g_pm_auto_point_base_slot", 23), # 1623
    (troop_set_slot, ":troop", ":auto_all_slot_1623", ":var_begin_ca_agility"), 
    (store_add, ":auto_all_slot_1624", "$g_pm_auto_point_base_slot", 24), # 1624
    (troop_set_slot, ":troop", ":auto_all_slot_1624", ":var_begin_ca_intelligence"), 
    (store_add, ":auto_all_slot_1625", "$g_pm_auto_point_base_slot", 25), # 1625
    (troop_set_slot, ":troop", ":auto_all_slot_1625", ":var_begin_ca_charisma"), 

    # 存储初始可用属性和技能到槽里
    # (assign, ":curr_can_use_attr", 0),
    # (assign, ":curr_can_use_skill", 0),

    # (troop_get_slot, ":curr_can_use_attr", ":troop", 1613), # 获取某个槽的值
    # (troop_get_slot, ":curr_can_use_skill", ":troop", 1614), # 获取某个槽的值

    # (troop_set_slot, ":troop", 1608, ":curr_can_use_attr"),  # 存储初始可用属性到槽里
    # (troop_set_slot, ":troop", 1609, ":curr_can_use_skill"),  # 存储初始可用技能到槽里

    # 保存同伴初始技能等级，后续用于洗点
    (store_add, ":operate_index", "$g_pm_auto_point_base_slot", 54), # 1654
    (try_for_range, ":sub_idx", 0, 37),
        (this_or_next|eq, ":sub_idx", "skl_ironflesh"),
        (this_or_next|eq, ":sub_idx", "skl_power_strike"),
        (this_or_next|eq, ":sub_idx", "skl_power_throw"),
        (this_or_next|eq, ":sub_idx", "skl_power_draw"),
        (this_or_next|eq, ":sub_idx", "skl_weapon_master"),
        (this_or_next|eq, ":sub_idx", "skl_shield"),
        (this_or_next|eq, ":sub_idx", "skl_athletics"),
        (this_or_next|eq, ":sub_idx", "skl_riding"),
        (this_or_next|eq, ":sub_idx", "skl_horse_archery"),
        (this_or_next|eq, ":sub_idx", "skl_looting"),
        (this_or_next|eq, ":sub_idx", "skl_trainer"),
        (this_or_next|eq, ":sub_idx", "skl_tracking"),
        (this_or_next|eq, ":sub_idx", "skl_tactics"),
        (this_or_next|eq, ":sub_idx", "skl_pathfinding"),
        (this_or_next|eq, ":sub_idx", "skl_spotting"),
        (this_or_next|eq, ":sub_idx", "skl_inventory_management"),
        (this_or_next|eq, ":sub_idx", "skl_wound_treatment"),
        (this_or_next|eq, ":sub_idx", "skl_surgery"),
        (this_or_next|eq, ":sub_idx", "skl_first_aid"),
        (this_or_next|eq, ":sub_idx", "skl_engineer"),
        (this_or_next|eq, ":sub_idx", "skl_persuasion"),
        (this_or_next|eq, ":sub_idx", "skl_prisoner_management"),
        (this_or_next|eq, ":sub_idx", "skl_leadership"),
        (eq, ":sub_idx", "skl_trade"),
        (store_skill_level, reg10, ":sub_idx", ":troop"),  # 获取当前技能的数值
        (troop_set_slot, ":troop", ":operate_index", reg10),  # 赋值给存储初始技能数值的对应槽
        (val_sub, ":operate_index", 1),
    (try_end),
]),


# 开始新的场景
("auto_point_before_mission_start", [
  (assign, "$g_pm_auto_point_is_can_move_item", 0),  # 进入场景后，封锁更换装备和洗点功能

  ]),

# 结束新的场景
("auto_point_end_mission", [
  (assign, "$g_pm_auto_point_is_can_move_item", 1), # 退出场景时，解锁更换装备和洗点功能
  (call_script, "script_start_auto_point"),  # 退出场景时，运行一次自动加点
  ]),