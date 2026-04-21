# ==============================================
# 界面名称：特殊部队装备交换界面
# 功能：玩家可给特殊英雄NPC更换装备、升级属性/技能/熟练度、查看角色详情
# ==============================================
("exchange_special_troop_equippment", 0, mesh_bg_auto_main_win, [   # mesh_load_bg_auto_main_win = 1047
    # ==============================================
    # 触发事件1：界面加载时执行 初始化核心逻辑
    # ==============================================
    (ti_on_presentation_load, [
        # 设置浮点数运算倍率 骑砍固定格式 
        (set_fixed_point_multiplier, 1000),
        # 设置界面无限时长 不自动关闭 
        (presentation_set_duration, 999999),

        # ==============================================
        # 首次进入界面初始化：重置临时变量
        # ==============================================
        (try_begin),
            # 判断是否首次进入界面
            (eq, "$g_pm_first_enter_pren", 0),
            # 重置分页变量
            (assign, "$g_pm_temp_4", 0),
            (assign, "$g_pm_temp_3", 0),
            #(assign, "$g_pm_new_test", 1),
            (call_script, "script_calculate_available_points", "trp_player"),
            (call_script, "script_save_troop_points_for_reset", "trp_player"),  # 首次进入肯定是选中玩家的，存储玩家的点数，便于重设
            (assign, "$g_pm_prsn_auto_point_comb_index", 0),
            (str_store_string, s24, "str_auto_point_input_default"), # 首次进入重置输入框中的内容
            # 关闭首次进入标记
            (assign, "$g_pm_first_enter_pren", 1),
            

            #(start_presentation, "prsnt_exchange_special_troop_equippment"),
        (try_end),

        # ==============================================
        # 全局设置：玩家托管部队任务天数=3
        # ==============================================
        (assign, "$g_pm_is_show_extra_prerequisite", 1),   # 设置显示额外条件
        # # 计算英雄ID上限：妻子ID+1
        # (store_add, ":hero_max_id", "trp_auto_knight_1_1_wife", 1),

        # ==============================================
        # 核心循环：遍历所有特殊英雄，自动升级属性点数
        # 逻辑：角色升级后，自动分配未使用的属性/技能点
        # ==============================================
        # (try_for_range, ":current_hero", "trp_auto_special_hero_1", ":hero_max_id"),
        #     # 特殊处理：妻子ID替换为玩家ID
        #     (try_begin),
        #         (eq, ":current_hero", "trp_auto_knight_1_1_wife"),
        #         (assign, ":current_hero", "trp_player"),
        #     (try_end),

        #     # 获取当前英雄等级
        #     (store_character_level, ":hero_level", ":current_hero"),
        #     # 判断：角色等级 > 已记录等级 需要分配点数
        #     (neg|troop_slot_ge, ":current_hero", 204, ":hero_level"),
        #     # 获取上次记录的等级
        #     (troop_get_slot, ":last_record_level", ":current_hero", 204),
        #     # 计算升级差值 可分配点数
        #     (store_sub, ":level_up_points", ":hero_level", ":last_record_level"),
        #     # 更新当前等级记录
        #     (troop_set_slot, ":current_hero", 204, ":hero_level"),
            
        #     # 给 属性点 增加升级差值
        #     (troop_get_slot, ":attr_points", ":current_hero", 201),
        #     (val_add, ":attr_points", ":level_up_points"),
        #     (troop_set_slot, ":current_hero", 201, ":attr_points"),
            
        #     # 给 技能点 增加升级差值
        #     (troop_get_slot, ":skill_points", ":current_hero", 202),
        #     (val_add, ":skill_points", ":level_up_points"),
        #     (troop_set_slot, ":current_hero", 202, ":skill_points"),
        # (try_end),

        # ==============================================
        # 初始化临时部队数据
        # ==============================================
        #(call_script, "script_initialize_temp_troop"),

        # 重置所有界面控件ID
        (assign, "$g_pm_presentation_obj_2", -1),
        (assign, "$g_pm_presentation_obj_3", -1),
        (assign, "$g_pm_presentation_obj_4", -1),
        (assign, "$g_pm_presentation_obj_5", -1),
        (assign, "$g_pm_presentation_obj_6", -1),
        (assign, "$g_pm_presentation_obj_designer_1", -1),
        (assign, "$g_pm_presentation_obj_10", -1),
        (assign, "$g_pm_presentation_obj_11", -1),
        (assign, "$g_pm_presentation_obj_12", -1),
        (create_text_overlay, reg0, "str_auto_point_force_add"), # 为了防止出现ui索引的bug创建的一个空的

        # ==============================================
        # 绘制界面背景矩形 UI底框 
        # ==============================================
        # (call_script, "script_paint_rectangle", 3, 153, 655, 655, 63, 1118481),
        # (call_script, "script_paint_rectangle", 3, 180, 302, 805, 63, 1118481),
        # (call_script, "script_paint_rectangle", 3, 180, 502, 805, 63, 1118481),
        # (call_script, "script_paint_rectangle", 3, 180, 655, 805, 63, 1118481),
        # (call_script, "script_paint_rectangle", 3, 422, 470, 236, 248, 1118481),


        # ==============================================
        # 非任务状态下：创建 返回地图 按钮
        # ==============================================
        (try_begin),
            (call_script, "script_create_a_button_overlay_by_type", "str_auto_point_return_to_map", 80, 30, 945, 20, 1, -1, -1),
            (assign, "$g_pm_prsn_auto_point_btn_back", reg0),
        (try_end),

        # ==============================================
        # 创建重设按钮
        # ==============================================
        (call_script, "script_create_a_button_overlay_by_type", "str_auto_point_reset", 80, 30, 865, 20, 1, -1, -1),
        (assign, "$g_pm_prsn_auto_point_btn_reset", reg0),

        # ==============================================
        # 创建洗点按钮
        # ==============================================
        (call_script, "script_create_a_button_overlay_by_type", "str_auto_point_reset_stats", 80, 30, 785, 20, 1, -1, -1),
        (assign, "$g_pm_prsn_auto_btn_reset_stats", reg0),


        # ==============================================
        # 创建界面固定文字 技 能/属 性/武 器 熟 练  
        # ==============================================
        (call_script, "script_create_a_simple_string_at_position", "str_ui_hero_strengthen_string_42", 730, 650, 900, 16, 1131537),
        (overlay_set_color, reg0, 0xfff1a2),
        (call_script, "script_create_a_simple_string_at_position", "str_ui_hero_strengthen_string_43", 900, 524, 900, 16, 1131537),
        (overlay_set_color, reg0, 0xfff1a2),
        (call_script, "script_create_a_simple_string_at_position", "str_ui_hero_strengthen_string_44", 900, 326, 900, 16, 1131537),
        (overlay_set_color, reg0, 0xfff1a2),


        # ==============================================
        # 先计算所有英雄的可用点数！
        # ==============================================
        (party_get_num_companion_stacks, ":companion_count", "p_main_party"),
        (try_for_range, ":stack_index", 0, ":companion_count"),
            (party_stack_get_troop_id, ":troop_id", "p_main_party", ":stack_index"),
            (troop_is_hero, ":troop_id"),
            (store_add, ":auto_all_slot_1630", "$g_pm_auto_point_base_slot", 30), # 1630
            (troop_slot_eq, ":troop_id", ":auto_all_slot_1630", 1),
            # 先执行计算脚本，更新1613/1614/1615的数值
            (call_script, "script_calculate_available_points", ":troop_id"),
        (try_end),

        

        # ==============================================
        # 创建下拉选择框 选择要操作的英雄 
        # ==============================================
        (call_script, "script_creat_a_combo_button_with_pull_down_list", 800, 800, 500, 680),
        (assign, "$g_pm_presentation_obj_designer_1", reg0),
        # 初始化下拉框序号
        (assign, ":combo_index", 0),

        # ==============================================
        # 填充下拉框：添加玩家队伍中的英雄NPC
        # ==============================================
        (try_begin),
            #(neg|troop_slot_eq, "trp_auto_player_event_keeper", slot_troop_current_mission, 1),
            # 获取玩家队伍同伴数量
            (party_get_num_companion_stacks, ":companion_count", "p_main_party"),
            # 遍历所有同伴
            (try_for_range, ":stack_index", 0, ":companion_count"),
                # 获取当前部队的英雄ID
                (party_stack_get_troop_id, ":troop_id", "p_main_party", ":stack_index"),
                # 筛选条件：玩家/特殊英雄/英雄单位/排除指定NPC
                #(this_or_next|eq, ":troop_id", "trp_player"),
                #(is_between, ":troop_id", "trp_auto_special_hero_1", "trp_auto_knight_1_1_wife"),
                (troop_is_hero, ":troop_id"),
                #(neg|eq, ":troop_id", "trp_auto_knight_7_1"),
                (store_add, ":auto_all_slot_1630", "$g_pm_auto_point_base_slot", 30), # 1630
                (troop_slot_eq, ":troop_id", ":auto_all_slot_1630", 1), # 判断该槽值为1，代表可以进行加点操作的troop
                # 存储英雄名称到字符串
                (str_store_troop_name, s1, ":troop_id"),
                # 有可分配点数的英雄：名称后添加+标记
                (try_begin),
                    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
                    (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
                    (this_or_next|troop_slot_ge, ":troop_id", ":auto_all_slot_1613", 1),
                    (troop_slot_ge, ":troop_id", ":auto_all_slot_1614", 1),
                    (str_store_string, s1, "str_auto_s1_plus"),
                (try_end),
                (try_begin),  # 如果开启了自动加点，则在前面加*
                    (store_add, ":auto_all_slot_1724", "$g_pm_auto_point_base_slot", 124), # 1724
                    (troop_slot_eq, ":troop_id", ":auto_all_slot_1724", 1),
                    (str_store_string, s1, "str_auto_star_s1"),
                (try_end),
                # 添加到下拉框
                (overlay_add_item, "$g_pm_presentation_obj_designer_1", 1),
                # 记录英雄ID到临时列表
                (troop_set_slot, "trp_auto_temp_list_3", ":combo_index", ":troop_id"),
                (val_add, ":combo_index", 1),
            (try_end),
        (try_end),

        # ==============================================
        # 特殊条件：添加指定英雄到下拉框
        # ==============================================
        # (try_begin),
        #     #(neg|troop_slot_eq, "trp_auto_player_event_keeper", slot_troop_current_mission, 1),
        #     (this_or_next|troop_slot_eq, "trp_auto_player_event_keeper", slot_troop_spouse, -2),
        #     (troop_slot_ge, "trp_auto_player_event_keeper", slot_troop_spouse, 10),
        #     (main_party_has_troop, "trp_auto_knight_7_1"),
        #     (str_store_troop_name, s1, "trp_auto_knight_7_1"),
        #     (overlay_add_item, "$g_pm_presentation_obj_designer_1", 1),
        #     (troop_set_slot, "trp_auto_temp_list_3", ":combo_index", "trp_auto_knight_7_1"),
        #     (val_add, ":combo_index", 1),
        # (try_end),

        # ==============================================
        # 任务状态：仅显示任务指定英雄
        # ==============================================
        # (try_begin),
        #     (troop_slot_eq, "trp_auto_player_event_keeper", slot_troop_current_mission, 1),
        #     # 获取任务英雄ID
        #     (troop_get_slot, ":mission_troop", "trp_player", slot_troop_signup_response_2),
        #     (troop_set_slot, "trp_auto_temp_list_3", ":combo_index", ":mission_troop"),
        #     (str_store_troop_name, s1, ":mission_troop"),
        #     (overlay_add_item, "$g_pm_presentation_obj_designer_1", 1),
        #     (val_add, ":combo_index", 1),
        # (try_end),

        # ==============================================
        # 设置下拉框默认选中项
        # ==============================================
        (overlay_set_val, "$g_pm_presentation_obj_designer_1", "$g_pm_temp_3"),
        # 获取当前选中的英雄
        (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),

        # ==============================================
        # 创建^^  属 性 、 技 能 与 熟 练 度 介 绍  
        # ==============================================
        (call_script, "script_create_a_string_with_double_space", "str_ui_hero_strengthen_string_41", 810, 550, 172, 155, 700, -1),
        (overlay_set_color, reg0, 0xfff1a2),
        (troop_set_slot, "trp_auto_temp_list_1", 1001, reg0),

        # ==============================================
        # 特殊NPC：如果玩家没达到该等级，则无法进行换装
        # ==============================================
        (try_begin),
            (store_character_level, ":curr_character_level", "trp_player"), # 获取玩家等级
            (store_add, ":auto_all_slot_1629", "$g_pm_auto_point_base_slot", 29), # 1629
            (troop_get_slot, ":curr_can_equip_slot_value", ":selected_troop", ":auto_all_slot_1629"), # 获取某个槽的值，如果玩家没达到该等级，则无法进行换装
            (try_begin),
                (this_or_next|neg|ge, ":curr_character_level", ":curr_can_equip_slot_value"), # 当前玩家等级不到该等级
                (eq, "$g_pm_auto_point_is_can_move_item", 0),   # 战斗状态无法换装
                # 遍历装备栏
                (try_for_range, ":equip_slot", 0, 9),
                    # 标记该位置为锁定
                    (troop_set_slot, "trp_auto_temp_list_3_1", ":equip_slot", 1),
                (try_end),
            (else_try), 
                (try_for_range, ":equip_slot", 0, 9),
                    # 标记该位置为为锁定
                    (troop_set_slot, "trp_auto_temp_list_3_1", ":equip_slot", 0),
                (try_end),
        (try_end),

        # ==============================================
        # 创建英雄3D模型展示界面
        # ==============================================
        (try_begin),
            #(eq, "$g_pm_new_test", 0),
            # 计算模型偏移量
            (store_mul, ":model_offset", ":selected_troop", 2),
            # 创建模型展示控件
            (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":model_offset"),
            # 设置模型大小
            (position_set_x, pos1, 646),
            (position_set_y, pos1, 840),
            (overlay_set_size, reg0, pos1),
            # 设置模型位置
            (position_set_x, pos1, 404),
            (position_set_y, pos1, 20),
            (overlay_set_position, reg0, pos1),
            (set_fixed_point_multiplier, 1000),
        (try_end),

        # ==============================================
        # 定义装备栏坐标 9个装备位置
        # ==============================================
        (assign, ":base_x", 270),
        (assign, ":base_y", 40),
        (store_add, ":x_1", ":base_x", 50),
        (store_add, ":x_2", ":base_x", 100),
        (store_add, ":y_1", ":base_y", 50),
        (store_add, ":y_2", ":base_y", 100),
        (store_add, ":y_3", ":base_y", 150),

        # ==============================================
        # 绘制英雄装备栏 9个位置
        # ==============================================
        (try_for_range, ":slot_id", 0, 9),
            # 获取当前装备栏的物品
            (troop_get_inventory_slot, ":item_id", ":selected_troop", ":slot_id"),
            # 分配每个装备栏的坐标
            (try_begin),
                (eq, ":slot_id", 0), 
                (assign, ":cur_x", ":x_2"), 
                (assign, ":cur_y", ":y_3"),
            (else_try), 
                (eq, ":slot_id", 1), 
                (assign, ":cur_x", ":x_2"), 
                (assign, ":cur_y", ":y_2"),
            (else_try), 
                (eq, ":slot_id", 2), 
                (assign, ":cur_x", ":x_2"), 
                (assign, ":cur_y", ":y_1"),
            (else_try), 
                (eq, ":slot_id", 3), 
                (assign, ":cur_x", ":x_2"), 
                (assign, ":cur_y", ":base_y"),
            (else_try), 
                (eq, ":slot_id", 4), 
                (assign, ":cur_x", ":x_1"), 
                (assign, ":cur_y", ":y_3"),
            (else_try), 
                (eq, ":slot_id", 5), 
                (assign, ":cur_x", ":x_1"), 
                (assign, ":cur_y", ":y_2"),
            (else_try), 
                (eq, ":slot_id", 6), 
                (assign, ":cur_x", ":x_1"), 
                (assign, ":cur_y", ":y_1"),
            (else_try), 
                (eq, ":slot_id", 7), 
                (assign, ":cur_x", ":base_x"), 
                (assign, ":cur_y", ":y_2"),
            (else_try), 
                (eq, ":slot_id", 8), 
                (assign, ":cur_x", ":base_x"), 
                (assign, ":cur_y", ":base_y"),
            (try_end),

            # 创建装备栏背景
            (call_script, "script_create_a_mesh_overlay", "mesh_mp_inventory_choose", 400, 400, ":cur_x", ":cur_y", -1, -1),
            # 锁定装备：显示白色遮罩
            (try_begin),
                (troop_slot_eq, "trp_auto_temp_list_3_1", ":slot_id", 1),
                (call_script, "script_create_a_image_overlay", "mesh_white_plane", "mesh_white_plane", 2500, 2400, ":cur_x", ":cur_y", 14483456, -1),
                (assign, ":slot_overlay", reg0),
            # 普通装备栏：显示空槽背景
            (else_try),
                (call_script, "script_create_a_image_overlay", "mesh_mp_inventory_slot_empty", "mesh_mp_inventory_slot_empty", 400, 400, ":cur_x", ":cur_y", -1, -1),
                (assign, ":slot_overlay", reg0),
            (try_end),
            # 记录控件ID
            (troop_set_slot, "trp_auto_temp_list_1", ":slot_id", ":slot_overlay"),

            # 有装备：显示物品图标
            (try_begin),
                (ge, ":item_id", 1),
                (create_mesh_overlay_with_item_id, reg1, ":item_id"),
                # 设置物品大小
                (position_set_x, pos1, 500),
                (position_set_y, pos1, 500),
                (overlay_set_size, reg1, pos1),
                # 居中显示物品
                (val_add, ":cur_x", 25),
                (val_add, ":cur_y", 25),
                (position_set_x, pos1, ":cur_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg1, pos1),
                # 记录物品控件
                (troop_set_slot, "trp_auto_temp_list_4", ":slot_id", reg1),
            (else_try),
                (troop_set_slot, "trp_auto_temp_list_4", ":slot_id", -1),
            (try_end),
        (try_end),

        # ==============================================
        # 玩家背包栏初始化
        # ==============================================
        (call_script, "script_create_a_simple_string_at_position", "str_cb_note_365", 120, 680, 800, 16, -1),
        # 获取玩家背包总容量
        (troop_get_inventory_capacity, ":player_inv_capacity", "trp_player"),
        # 计算每页显示数量
        (store_div, ":page_size", ":player_inv_capacity", 4),
        (assign, ":item_spacing", 50),
        (assign, ":start_y", 610),
        (assign, ":row_item_max", 4),
        (assign, ":start_x", 20),
        # 计算分页总数
        (store_div, ":total_pages", ":player_inv_capacity", 44),

        # ==============================================
        # 创建背包分页选择框
        # ==============================================
        (try_begin),
            (ge, ":total_pages", 1),
            (call_script, "script_create_a_combo_label_overlay", 120, 620, 700, 700),
            (assign, "$g_pm_presentation_obj_12", reg0),
            (val_add, ":total_pages", 1),
            # 生成分页选项
            (try_for_range, ":page_idx", 0, ":total_pages"),
                (assign, reg1, ":page_idx"),
                (val_add, reg1, 1),
                (str_store_string, s1, "str_auto_reg1"),
                (overlay_add_item, "$g_pm_presentation_obj_12", 1),
            (try_end),
            # 设置默认分页
            (overlay_set_val, "$g_pm_presentation_obj_12", "$g_pm_temp_4"),
        (try_end),

        # ==============================================
        # 计算当前分页显示范围
        # ==============================================
        (store_mul, ":page_start_offset", "$g_pm_temp_4", 44),
        (assign, ":page_item_start", 10),
        (assign, ":page_item_end", 54),
        (val_add, ":page_item_start", ":page_start_offset"),
        (val_add, ":page_item_end", ":page_start_offset"),

        # ==============================================
        # 绘制玩家背包物品栏
        # ==============================================
        (assign, ":cur_row_count", 1),
        (assign, ":cur_item_x", 20),
        (assign, ":cur_item_y", 540),
        (try_for_range, ":inv_slot", 10, ":player_inv_capacity"),
            # 获取背包物品
            (troop_get_inventory_slot, ":item_id", "trp_player", ":inv_slot"),
            # 非当前页：隐藏控件
            (try_begin),
                (neg|is_between, ":inv_slot", ":page_item_start", ":page_item_end"),
                (assign, ":draw_x", -200),
                (assign, ":draw_y", 50),
            # 当前页：正常显示
            (else_try),
                (assign, ":draw_x", ":cur_item_x"),
                (assign, ":draw_y", ":cur_item_y"),
            (try_end),

            # 创建背包栏背景
            (call_script, "script_create_a_mesh_overlay", "mesh_mp_inventory_choose", 400, 400, ":draw_x", ":draw_y", -1, -1),
            (troop_set_slot, "trp_auto_temp_list_5", ":inv_slot", reg0),
            (call_script, "script_create_a_image_overlay", "mesh_mp_inventory_slot_empty", "mesh_mp_inventory_slot_empty", 400, 400, ":draw_x", ":draw_y", -1, -1),
            (troop_set_slot, "trp_auto_temp_list_1", ":inv_slot", reg0),

            # 显示物品图标
            (try_begin),
                (ge, ":item_id", 1),
                (create_mesh_overlay_with_item_id, reg1, ":item_id"),
                (position_set_x, pos1, 500),
                (position_set_y, pos1, 500),
                (overlay_set_size, reg1, pos1),
                (store_add, ":icon_x", ":cur_item_x", 25),
                (store_add, ":icon_y", ":cur_item_y", 25),
                # 隐藏非当前页物品
                (try_begin),
                    (neg|is_between, ":inv_slot", ":page_item_start", ":page_item_end"),
                    (assign, ":icon_x", -200),
                    (assign, ":icon_y", 50),
                (try_end),
                (position_set_x, pos1, ":icon_x"),
                (position_set_y, pos1, ":icon_y"),
                (overlay_set_position, reg1, pos1),
                (troop_set_slot, "trp_auto_temp_list_4", ":inv_slot", reg1),
            (else_try),
                (troop_set_slot, "trp_auto_temp_list_4", ":inv_slot", -1),
            (try_end),

            # 自动换行排版
            (try_begin),
                (is_between, ":inv_slot", ":page_item_start", ":page_item_end"),
                (val_add, ":cur_row_count", 1),
                (val_add, ":cur_item_x", ":item_spacing"),
                # 满4个物品换行
                (try_begin),
                    (gt, ":cur_row_count", ":row_item_max"),
                    (assign, ":cur_row_count", 1),
                    (assign, ":cur_item_x", 20),
                    (val_sub, ":cur_item_y", ":item_spacing"),
                (try_end),
            (try_end),
        (try_end),




        # ==============================================
        # 显示英雄属性点数 颜色区分可分配/已用完
        # ==============================================
        (assign, ":attr_available", 0),
        (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
        (troop_get_slot, ":attr_available", ":selected_troop", ":auto_all_slot_1613"),
        (try_begin),
            (ge, ":attr_available", 1),
            (assign, ":text_color", 0xfff1a2), # 黄色：可分配
        (else_try),
            (assign, ":text_color", 0xfff1a2),   # 灰色：已用完
        (try_end),
        (assign, reg10, ":attr_available"),
        (str_store_string, s1, "str_ui_hero_strengthen_string_35"), # 剩 余 属 性 点
        (call_script, "script_create_a_simple_string_at_position", -1, 840, 384, 800, 32772, ":text_color"),

        # ==============================================
        # 显示英雄技能点数
        # ==============================================
        (assign, ":skill_available", 0),
        (store_add, ":auto_all_slot_1614", "$g_pm_auto_point_base_slot", 14), # 1614
        (troop_get_slot, ":skill_available", ":selected_troop", ":auto_all_slot_1614"),
        (try_begin),
            (ge, ":skill_available", 1),
            (assign, ":text_color", 0xfff1a2),
        (else_try),
            (assign, ":text_color", 0xfff1a2),
        (try_end),
        (assign, reg10, ":skill_available"),
        (str_store_string, s1, "str_ui_hero_strengthen_string_36"), # 剩 余 技 能 点
        (call_script, "script_create_a_simple_string_at_position", -1, 670, 80, 800, 32772, ":text_color"),

        # ==============================================
        # 显示英雄熟练度点数
        # ==============================================
        (assign, ":prof_available", 0),
        (store_add, ":auto_all_slot_1615", "$g_pm_auto_point_base_slot", 15), # 1615
        (troop_get_slot, ":prof_available", ":selected_troop", ":auto_all_slot_1615"),
        (try_begin),
            (ge, ":prof_available", 1),
            (assign, ":text_color", 0xfff1a2),
        (else_try),
            (assign, ":text_color", 0xfff1a2),
        (try_end),
        (assign, reg10, ":prof_available"),
        (str_store_string, s1, "str_ui_hero_strengthen_string_37"),  # 剩 余 熟 练 点
        (call_script, "script_create_a_simple_string_at_position", -1, 840, 81, 800, 32772, ":text_color"),

        # ==============================================
        # 显示英雄等级
        # ==============================================
        (store_character_level, reg10, ":selected_troop"),
        (str_store_string, s1, "str_ui_hero_strengthen_string_83"), # 等 级
        (call_script, "script_create_a_simple_string_at_position", -1, 633, 208, 800, 32776, 102),
        (assign, "$g_pm_prsn_auto_point_str_exp", reg0),

        # ==============================================
        # 显示英雄生命值 颜色区分健康/受伤 
        # ==============================================
        (store_troop_health, ":hero_health", ":selected_troop", 0),
        (try_begin),
            (gt, ":hero_health", 50),
            (assign, ":text_color", 8704),  # 绿色：健康
        (else_try),
            (assign, ":text_color", 16711680),# 红色：受伤
        (try_end),
        (assign, reg10, ":hero_health"),
        (str_store_string, s1, "str_ui_hero_strengthen_string_84"), # 血 量
        (call_script, "script_create_a_simple_string_at_position", -1, 633, 178, 800, 32776, ":text_color"),
        (assign, "$g_pm_prsn_auto_point_str_hp", reg0),

        # ==============================================
        # 显示英雄护甲值
        # ==============================================
        # (call_script, "script_get_troop_armor_points", ":selected_troop"),
        # (assign, ":armor_value", reg0),
        # (try_begin),
        #     (gt, ":armor_value", 0),
        #     (assign, reg10, ":armor_value"),
        #     (str_store_string, s1, "@{reg10}"),
        #     (str_store_string, s2, "str_cb_note_166"),
        #     (str_store_string, s1, "@{s2}{s1}"),
        #     (call_script, "script_create_a_simple_string_at_position", -1, 600, 590, 800, 32776, 102),
        # (try_end),



        
        # ==============================================
        # 遍历创建所有属性/技能/熟练度按钮 48个
        # ==============================================
        (assign, ":button_index", 0),
        (try_for_range, ":attr_skill_idx", 0, 48),
            # 定义变量
            (assign, ":btn_text", "str_ui_hero_strengthen_string_1"),
            (assign, ":btn_x", 0),
            (assign, ":btn_y", 0),
            (assign, ":y_spacing", 0),
            (assign, ":text_offset", 0),
            (assign, ":text_width", 0),
            # 分三类设置坐标/文字：属性 0-3 、熟练度 4-9 、技能 10+ 
            (try_begin),
                (is_between, ":attr_skill_idx", 0, 4),
                (assign, ":sub_idx", ":button_index"), # 用来计算y的实际差值
                (assign, ":btn_text", "str_ui_hero_strengthen_string_1"),
                (assign, ":btn_x", 840),
                (assign, ":btn_y", 504),
                (store_mul, ":tmp_y_spacing", ":sub_idx", 30),
                (val_sub, ":btn_y", ":tmp_y_spacing"),
                (assign, ":text_offset", 80),
                (assign, ":text_width", 750),
            (else_try),
                (is_between, ":attr_skill_idx", 4, 11),
                (store_sub, ":sub_idx", ":button_index", 4),
                (assign, ":btn_text", "str_ui_hero_strengthen_string_5"),
                (assign, ":btn_x", 840),
                (assign, ":btn_y", 296),
                (store_mul, ":tmp_y_spacing", ":sub_idx", 30),
                (val_sub, ":btn_y", ":tmp_y_spacing"),
                (assign, ":text_offset", 80),
                (assign, ":text_width", 750),
            (else_try),
                (is_between, ":attr_skill_idx", 11, 48),
                (store_sub, ":sub_idx", ":button_index", 11),
                (assign, ":btn_text", "str_ui_hero_strengthen_string_34"),
                (assign, ":btn_x", 670),
                (assign, ":btn_y", 170),
                (store_mul, ":tmp_y_spacing", ":sub_idx", -20),
                (val_sub, ":btn_y", ":tmp_y_spacing"),
                (assign, ":text_offset", 105),
                (assign, ":text_width", 550),
            (try_end),

            # 默认按钮可点击
            (assign, ":btn_enable", 1),
            (assign, ":can_add_point", -1),

            # ==============================================
            #  属性类 读取数值+判断可加点
            # ==============================================
            (try_begin),
                (is_between, ":attr_skill_idx", 0, 4),
                (assign, ":sub_idx", ":attr_skill_idx"),
                (try_begin),
                    (eq, ":sub_idx", ca_intelligence),  # 智力单独计算
                    (call_script, "script_store_intelligence_attribute_level", ":selected_troop"),
                (else_try),
                    (store_attribute_level, reg0, ":selected_troop", ":sub_idx"), # 获取当前属性值
                (try_end),
                (assign, ":cur_value", reg0),
                # 有属性点可分配
                (try_begin),
                    (store_add, ":auto_all_slot_1613", "$g_pm_auto_point_base_slot", 13), # 1613
                    (troop_slot_ge, ":selected_troop", ":auto_all_slot_1613", 1),
                    (lt, ":cur_value", "$g_pm_auto_property_max"),
                    (assign, ":can_add_point", 1),
                (try_end),
                (store_add, ":final_text", ":sub_idx", ":btn_text"),
            # ==============================================
            #  熟练度类 读取数值+判断可加点
            # ==============================================
            (else_try),
                (is_between, ":attr_skill_idx", 4, 11),
                (store_sub, ":sub_idx", ":attr_skill_idx", 4),
                (store_proficiency_level, ":cur_value", ":selected_troop", ":sub_idx"),
                (call_script, "script_new_char_sys_is_can_add_weapon_point", ":selected_troop", ":sub_idx", 1),
                (assign, ":can_add_point", reg0),    
                (store_add, ":final_text", ":sub_idx", ":btn_text"),
            # ==============================================
            #  技能类 读取数值+判断可加点
            # ==============================================
            (else_try),
                (is_between, ":attr_skill_idx", 11, 48),
                (store_sub, ":sub_idx", ":attr_skill_idx", 11),
                (assign, ":btn_enable", -1),
                # 筛选战斗/非战斗技能
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
                (assign, ":btn_enable", 1),
                (store_sub, ":btn_idx", ":button_index", 11),
                (store_sub, ":final_text", ":btn_text", ":btn_idx"),
          
                # 获取技能真实等级
                (store_skill_level, reg0, ":sub_idx", ":selected_troop"),
                (assign, ":cur_value", reg0),
                # 判断是否可加点
                (call_script, "script_get_troop_skill_is_can_added", ":selected_troop", ":sub_idx", 1),
                (assign, ":can_add_point", reg0),                     
            (try_end),

            # ==============================================
            # 创建属性/技能/熟练度按钮
            # ==============================================
            (eq, ":btn_enable", 1),
            (create_button_overlay, reg1, ":final_text"),
            # 设置按钮大小
            (position_set_x, pos1, ":text_width"),
            (position_set_y, pos1, ":text_width"),
            (overlay_set_size, reg1, pos1),
            # 设置按钮位置
            (position_set_x, pos1, ":btn_x"),
            (position_set_y, pos1, ":btn_y"),
            (overlay_set_position, reg1, pos1),
            (overlay_set_color, reg1, 0xfff1a2),
            # 记录按钮数据
            (troop_set_slot, "trp_auto_temp_list_1_1", ":button_index", reg1),
            (troop_set_slot, "trp_auto_temp_list_2_2", ":button_index", ":final_text"),
            (troop_set_slot, "trp_auto_temp_list_3_2", ":button_index", ":sub_idx"),

            # ==============================================
            # 显示数值 技能带加成/属性直接显示 
            # ==============================================
            (try_begin),
                (is_between, ":attr_skill_idx", 11, 48),
                # 获取技能基础/真实/加成等级
                (store_sub, ":sub_idx", ":attr_skill_idx", 11),
                #(store_skill_level, ":base_skill", ":sub_idx", ":selected_troop"),
                #(call_script, "script_hero_get_skill_real_lv", ":selected_troop", ":sub_idx"),
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

                (store_skill_level, reg0, ":sub_idx", ":selected_troop"),
                (assign, ":real_skill", reg0),
                (call_script, "script_game_get_skill_modifier_for_troop", ":selected_troop", ":sub_idx"),
                (assign, ":skill_bonus", reg0),
                (store_sub, ":base_skill", ":real_skill", ":skill_bonus"),
                # 颜色区分：有加成 橙 普通 黑
                (try_begin),
                    (ge, ":skill_bonus", 1),
                    (assign, ":text_color", 0x53e94b),
                    #(assign, ":text_color", 0xfff1a2),
                    (assign, reg10, ":base_skill"),
                    (assign, reg11, ":real_skill"),
                    (assign, reg12, ":skill_bonus"),
                    (str_store_string, s1, "str_auto_reg11_reg10_reg12"),
                (else_try),
                    (assign, ":text_color", 0xfff1a2),
                    (assign, reg10, ":base_skill"),
                    (str_store_string, s1, "str_auto_reg10_simple"),
                (try_end),
                (create_text_overlay, reg1, 1, 32776),
            (else_try),
                # 属性直接显示数值
                (assign, reg10, ":cur_value"),
                (create_text_overlay, reg1, "str_auto_reg10_simple", 32772),
                (assign, ":text_color", 0xfff1a2),
            (try_end),

            # 设置数值文字位置
            (position_set_x, pos1, ":text_width"),
            (position_set_y, pos1, ":text_width"),
            (overlay_set_size, reg1, pos1),
            (store_add, ":text_x", ":btn_x", ":text_offset"),
            (position_set_x, pos1, ":text_x"),
            (position_set_y, pos1, ":btn_y"),
            (overlay_set_position, reg1, pos1),
            (overlay_set_color, reg1, ":text_color"),

            # ==============================================
            # 可加点：显示 + 按钮
            # ==============================================
            (try_begin),
                (eq, ":can_add_point", 1),
                # 创建加号按钮
                (create_image_button_overlay, reg1, "mesh_faya_little_diamond_button_up", "mesh_faya_little_diamond_button_down"),
                #(create_image_button_overlay, reg1, "mesh_button1_up", "mesh_button1_down"),
                (position_set_x, pos1, 200),
                (position_set_y, pos1, 200),
                (overlay_set_size, reg1, pos1),
                # 调整位置
                (store_add, ":btn_x", ":text_x", 30),
                (try_begin),
                    (is_between, ":attr_skill_idx", 11, 48),
                    (val_sub, ":btn_x", 25),
                (try_end),
                (position_set_x, pos1, ":btn_x"),
                (position_set_y, pos1, ":btn_y"),
                (overlay_set_position, reg1, pos1),
                # 记录加号按钮
                (troop_set_slot, "trp_auto_temp_list_1_2", ":button_index", reg1),
                # 显示+文字
                (create_text_overlay, reg1, "str_auto_plus", 16),
                (val_add, ":btn_x", 6),
                (position_set_x, pos1, ":btn_x"),
                (store_sub, ":btn_y", ":btn_y", 2),
                (position_set_y, pos1, ":btn_y"),
                (overlay_set_position, reg1, pos1),
                (position_set_x, pos1, 800),
                (position_set_y, pos1, 800),
                (overlay_set_size, reg1, pos1),
            (else_try),
                (troop_set_slot, "trp_auto_temp_list_1_2", ":button_index", -1),
            (try_end),

            # 序号+垂直间距
            (val_add, ":button_index", 1),
            (val_sub, ":btn_y", ":y_spacing"),
        (try_end),

        # ==============================================
        # 显示英雄天赋特性
        # ==============================================
        # (call_script, "script_create_a_simple_string_at_position", "str_ui_player_get_skill_record_2", 405, 650, 800, 4, 1131537),
        # (assign, ":peculiarity_x", 405),
        # (assign, ":peculiarity_y", 620),
        # # 遍历所有天赋
        # (try_for_range, ":peculiarity_str", "str_ui_hero_skill_iron_heart", "str_ui_hero_skill_end"),
        #     (assign, "$g_pm_show_real_peculiarity", 1),
        #     # 判断英雄是否拥有该天赋
        #     (call_script, "script_cf_hero_has_peculiarity_no", ":selected_troop", ":peculiarity_str"),
        #     # 创建天赋按钮
        #     (call_script, "script_create_a_button_overlay_by_type", ":peculiarity_str", 800, 800, ":peculiarity_x", ":peculiarity_y", 0, 136, -1),
        #     (troop_set_slot, "trp_auto_temp_list_1_1", ":button_index", reg0),
        #     (troop_set_slot, "trp_auto_temp_list_2_2", ":button_index", ":peculiarity_str"),
        #     (val_add, ":button_index", 1),
        #     (val_sub, ":peculiarity_y", 30),
        # (try_end),
        #(assign, "$g_pm_show_real_peculiarity", -1),

        # ==============================================
        # 自动加点相关
        # ==============================================
        # 创建是否启用自动加点复选框
        (create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
        (position_set_x, pos1, 253),
        (position_set_y, pos1, 650),
        (overlay_set_position, reg1, pos1),
        (assign, "$g_pm_prsn_auto_point_is_open", reg1), 
        (store_add, ":auto_all_slot_1724", "$g_pm_auto_point_base_slot", 124), # 1724
        (troop_get_slot, ":curr_is_open_auto_value", ":selected_troop", ":auto_all_slot_1724"), # 获取某个槽的值
        (overlay_set_val, reg1, ":curr_is_open_auto_value"),
        # 创建自动加点文字
        (call_script, "script_create_a_simple_string_at_position", "str_is_open_auto_add_point", 332, 650, 800, 16, -1),
        # 创建方案下拉框
        (call_script, "script_creat_a_combo_button_with_pull_down_list", 700, 700, 342, 620),
        (assign, "$g_pm_prsn_auto_point_comb", reg0), 
        # 添加默认的方案
        #(assign, ":tmp_offset", 2001),
        (store_add, ":tmp_offset", "$g_pm_auto_point_base_slot_part", 201), # 2001
        (try_for_range_backwards, ":stack_index", 0, 71),
            (try_for_range, ":programme_index", 0, 10),
                # 计算索引值
                (store_mul, ":tmp_mul", ":programme_index", 100),
                (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
                (val_add, ":tmp_trp_index", ":tmp_mul"), 
                (try_begin),
                    (eq, ":stack_index", 0), # 方案名称
                    (try_begin),  # 这个区间用单数
                        (is_between, ":programme_index", 0, 5), 
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name, s8, ":trp_store_scheme_name"),
                    (else_try),  # 这个区间用复数
                        (is_between, ":programme_index", 5, 10),
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name_plural, s8, ":trp_store_scheme_name"),
                    (try_end),
                    (overlay_add_item, "$g_pm_prsn_auto_point_comb", 8),
                (try_end),
            (try_end),
        (try_end),
        (overlay_set_val, "$g_pm_prsn_auto_point_comb", "$g_pm_prsn_auto_point_comb_index"),


        # 创建一个编辑框
        (create_simple_text_box_overlay, reg2),             # 创建文本输入框，ID存入 reg2
        (assign, "$g_pm_prsn_auto_point_simple_text_box", reg2), 
        #(position_set_x, pos0, 150),                        # 宽度 300
        #(position_set_y, pos0, 20),                         # 高度 20
        #(overlay_set_size, reg1, pos0),                     # 应用尺寸
        (position_set_x, pos0, 253),                        # X坐标 200
        (position_set_y, pos0, 590),                        # Y坐标 200
        (overlay_set_position, reg2, pos0),                 # 应用位置
        (overlay_set_text, reg2, 24),
        (assign, "$g_pm_prsn_auto_point_input_name", reg2), 
        
        # 创建选择方案按钮
        (call_script, "script_create_a_button_overlay_by_type", "str_auto_point_select_scheme", 80, 20, 290, 563, 1, -1, -1),
        (assign, "$g_pm_prsn_auto_point_btn_choose", reg0),

        # 创建添加方案按钮
        (call_script, "script_create_a_button_overlay_by_type", "str_auto_point_add_scheme", 80, 20, 390, 563, 1, -1, -1),
        (assign, "$g_pm_prsn_auto_point_btn_add", reg0),

        # 添加删除方案按钮
        #(call_script, "script_create_a_button_overlay_by_type", "str_auto_point_delete_scheme", 50, 20, 410, 563, 1, -1, -1),

        # ==============================================
        # 自动加点加点组-左侧
        # ==============================================
        (try_for_range, ":auto_point_idx", 0, 23),
            (store_add, ":combo_button_base_num", "$g_pm_auto_point_base_slot_part", 271),  # 2071
            (store_add, ":number_box_button_base_num", "$g_pm_auto_point_base_slot_part", 371),  # 2171
            (store_add, ":checkbox_base_num", "$g_pm_auto_point_base_slot_part", 471),  # 2271
            (store_add, ":combo_button_base_num_curr", "$g_pm_auto_point_base_slot", 55), # 1655 自动加点-下拉框1-23的加点项，数量23
            (store_add, ":number_box_button_base_num_curr", "$g_pm_auto_point_base_slot", 78), # 1678 自动加点-自动加点目标值，数量23
            (store_add, ":checkbox_base_num_curr", "$g_pm_auto_point_base_slot", 101), # 1701 自动加点-技能点不够是否点智力强行加点，数量23

            (try_begin),
                (is_between, ":auto_point_idx", 0, 10),
                (assign, ":tmp_auto_y_spacing", 30),
                (val_mul, ":tmp_auto_y_spacing", ":auto_point_idx"),
                (assign, ":tmp_auto_y", 530),
                (val_sub, ":tmp_auto_y", ":tmp_auto_y_spacing"),
                (store_add, ":auto_point_no", ":auto_point_idx", 1),
                (assign, reg10, ":auto_point_no"),
                (call_script, "script_create_a_simple_string_at_position", "str_auto_point_no", 264, ":tmp_auto_y", 800, 16, -1),
                (call_script, "script_creat_a_combo_button_with_pull_down_list", 300, 600, 312, ":tmp_auto_y"),
                (store_add, ":combo_button_slot_num", ":combo_button_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":combo_button_slot_num", reg0), # 设置下拉框对象
                (str_store_string, s1, "str_auto_point_combox_default"),
                (overlay_add_item, reg0, 1),
                (try_for_range_backwards, ":auto_point_comb_idx", 0, 24),
                    (assign, ":btn_text", "str_ui_hero_strengthen_string_11"),
                    (store_add, ":final_text", ":auto_point_comb_idx", ":btn_text"),
                    (str_store_string, s1, ":final_text"),
                    (overlay_add_item, reg0, 1),
                (try_end),
                # 设置当前的技能下拉框的默认值
                (store_add, ":combo_button_slot_num_curr", ":combo_button_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_combo_button_value", ":selected_troop", ":combo_button_slot_num_curr"), # 获取某个槽的值
                (overlay_set_val, reg0, ":curr_combo_button_value"),
                # 创建一个数字框
                # 创建数字框之前要对前面的下拉框的技能进行判断，然后设置上限
                (assign, ":max_skill_value", 0),
                (try_begin), # curr_combo_button_value == 1为交易，24是铁骨
                    (eq, ":curr_combo_button_value", 0), # 等于0，则最大值则为0
                    (assign, ":max_skill_value", 0),
                (else_try),
                    (store_add, ":tmp_max_skill_slot_base", "$g_pm_auto_point_base_slot_part", 155), # 1955
                    (store_sub, ":slot_max_skill_value", ":tmp_max_skill_slot_base", ":curr_combo_button_value"),
                    (troop_get_slot, ":max_skill_value", "trp_auto_temp_list_3", ":slot_max_skill_value"), # 获取当前选中的槽的最大值的等级
                (try_end),
                (val_add, ":max_skill_value", 1),  # 最终值要加1
                (create_number_box_overlay, reg1, 0, ":max_skill_value"), # 创建ID=reg1，范围0-100
                (position_set_x, pos1, 70),
                (position_set_y, pos1, 20), 
                (overlay_set_size, reg1, pos1),
                (position_set_x, pos0, 355),
                (position_set_y, pos0, ":tmp_auto_y"),
                (overlay_set_position, reg1, pos0),
                (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_number_box_button_value", ":selected_troop", ":number_box_button_slot_num_curr"), # 获取某个槽的值
                (overlay_set_val, reg1, ":curr_number_box_button_value"),
                (store_add, ":number_box_slot_num", ":number_box_button_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":number_box_slot_num", reg1), # 设置下拉框对象

                # 创建一个勾选框
                (create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
                (position_set_x, pos1, 425),
                (position_set_y, pos1, ":tmp_auto_y"),
                (overlay_set_position, reg1, pos1),
                (store_add, ":checkbox_base_slot_curr", ":checkbox_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_checkbox_value", ":selected_troop", ":checkbox_base_slot_curr"), # 获取某个槽的值
                (overlay_set_val, reg1, ":curr_checkbox_value"),
                (store_add, ":checkbox_slot_num", ":checkbox_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":checkbox_slot_num", reg1), # 设置下拉框对象
                (call_script, "script_create_a_simple_string_at_position", "str_auto_point_force_add", 422, ":tmp_auto_y", 800, 16, -1),


            # ==============================================
            # 自动加点加点组-右侧
            # ==============================================
            (else_try),
                (is_between, ":auto_point_idx", 10, 23),
                (store_sub, ":auto_point_idx_2", ":auto_point_idx", 10),
                (assign, ":tmp_auto_y_spacing", 30),
                (val_mul, ":tmp_auto_y_spacing", ":auto_point_idx_2"),
                (assign, ":tmp_auto_y", 620),
                (val_sub, ":tmp_auto_y", ":tmp_auto_y_spacing"),
                (store_add, ":auto_point_no", ":auto_point_idx_2", 11),
                (assign, reg10, ":auto_point_no"),
                (call_script, "script_create_a_simple_string_at_position", "str_auto_point_no", 460, ":tmp_auto_y", 800, 16, -1),
                (call_script, "script_creat_a_combo_button_with_pull_down_list", 300, 600, 508, ":tmp_auto_y"),
                (store_add, ":combo_button_slot_num", ":combo_button_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":combo_button_slot_num", reg0), # 设置下拉框对象
                (str_store_string, s1, "str_auto_point_combox_default"),
                (overlay_add_item, reg0, 1),
                (try_for_range_backwards, ":auto_point_comb_idx", 0, 24),
                    (assign, ":btn_text", "str_ui_hero_strengthen_string_11"),
                    (store_add, ":final_text", ":auto_point_comb_idx", ":btn_text"),
                    (str_store_string, s1, ":final_text"),
                    (overlay_add_item, reg0, 1),
                (try_end),

                # 设置当前的技能下拉框的默认值
                (store_add, ":combo_button_slot_num_curr", ":combo_button_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_combo_button_value", ":selected_troop", ":combo_button_slot_num_curr"), # 获取某个槽的值
                (overlay_set_val, reg0, ":curr_combo_button_value"),
                # 创建一个数字框
                (create_number_box_overlay, reg1, 0, 11), # 创建ID=reg1，范围0-100
                (position_set_x, pos1, 70),
                (position_set_y, pos1, 20), 
                (overlay_set_size, reg1, pos1),
                (position_set_x, pos0, 551),
                (position_set_y, pos0, ":tmp_auto_y"),
                (overlay_set_position, reg1, pos0),
                (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_number_box_button_value", ":selected_troop", ":number_box_button_slot_num_curr"), # 获取某个槽的值
                (overlay_set_val, reg1, ":curr_number_box_button_value"),
                (store_add, ":number_box_slot_num", ":number_box_button_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":number_box_slot_num", reg1), # 设置下拉框对象
                # 创建一个勾选框
                (create_check_box_overlay, reg1, "mesh_checkbox_off", "mesh_checkbox_on"),
                (position_set_x, pos1, 621),
                (position_set_y, pos1, ":tmp_auto_y"),
                (overlay_set_position, reg1, pos1),
                (store_add, ":checkbox_base_slot_curr", ":checkbox_base_num_curr", ":auto_point_idx"), # 获取实际的槽
                (troop_get_slot, ":curr_checkbox_value", ":selected_troop", ":checkbox_base_slot_curr"), # 获取某个槽的值
                (overlay_set_val, reg1, ":curr_checkbox_value"),
                (store_add, ":checkbox_slot_num", ":checkbox_base_num", ":auto_point_idx"), # 获取实际的槽
                (troop_set_slot, "trp_auto_point", ":checkbox_slot_num", reg1), # 设置下拉框对象
                (call_script, "script_create_a_simple_string_at_position", "str_auto_point_force_add", 622, ":tmp_auto_y", 800, 16, -1),

            (try_end),
        (try_end),



        # 界面前置初始化脚本
        (call_script, "script_pre_1"),
    ]),
    # (ti_on_presentation_run, [
    #         ###### mouse fix pos system #######
    #     (call_script, "script_mouse_fix_pos_run"),#辅助线
    #         ###### mouse fix pos system #######
    # ]),


    # ==============================================
    # 触发事件3：控件状态改变 点击/选择 
    # ==============================================
    (ti_on_presentation_event_state_change, [
        # 获取触发控件ID/状态
        (store_trigger_param_1, ":trigger_overlay"),
        (store_trigger_param_2, ":trigger_state"),
        (set_fixed_point_multiplier, 1000),
        # 获取托管部队ID/当前选中英雄
        (troop_get_slot, ":keeper_troop", "trp_auto_player_set_keeper", 43),
        (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),

        # ==============================================
        # 背包分页切换
        # ==============================================
        (try_begin),
            (eq, "$g_pm_presentation_obj_12", ":trigger_overlay"),
            (assign, "$g_pm_temp_4", ":trigger_state"),
            # 重新计算分页显示范围
            (troop_get_inventory_capacity, ":player_inv_capacity", "trp_player"),
            (store_mul, ":page_offset", "$g_pm_temp_4", 44),
            (assign, ":page_start", 10),
            (assign, ":page_end", 54),
            (val_add, ":page_start", ":page_offset"),
            (val_add, ":page_end", ":page_offset"),
            # 重置排版
            (assign, ":row_count", 1),
            (assign, ":item_x", 20),
            (assign, ":item_y", 540),
            (assign, ":item_space", 50),
            (assign, ":max_row", 4),
            # 遍历刷新背包控件位置
            (try_for_range, ":inv_slot", 10, ":player_inv_capacity"),
                (troop_get_slot, ":bg_overlay", "trp_auto_temp_list_5", ":inv_slot"),
                (troop_get_slot, ":slot_overlay", "trp_auto_temp_list_1", ":inv_slot"),
                (troop_get_slot, ":item_overlay", "trp_auto_temp_list_4", ":inv_slot"), # 物品对象控件
                # 非当前页：隐藏
                (position_set_x, pos1, -200),
                (position_set_y, pos1, 50),
                (try_begin),
                    (neg|is_between, ":inv_slot", ":page_start", ":page_end"),
                    (overlay_set_position, ":bg_overlay", pos1),
                    (overlay_set_position, ":slot_overlay", pos1),
                    (try_begin),
                        (ge, ":item_overlay", 0),
                        (overlay_set_position, ":item_overlay", pos1),
                    (try_end),
                # 当前页：显示
                (else_try),
                    (position_set_x, pos2, ":item_x"),
                    (position_set_y, pos2, ":item_y"),
                    (overlay_set_position, ":bg_overlay", pos2),
                    (overlay_set_position, ":slot_overlay", pos2),
                    # 物品居中
                    (store_add, ":icon_x", ":item_x", 25),
                    (store_add, ":icon_y", ":item_y", 25),
                    (position_set_x, pos2, ":icon_x"),
                    (position_set_y, pos2, ":icon_y"),
                    (try_begin),
                        (ge, ":item_overlay", 0),
                        (overlay_set_position, ":item_overlay", pos2),
                    (try_end),
                    # 自动换行
                    (val_add, ":row_count", 1),
                    (val_add, ":item_x", ":item_space"),
                    (try_begin),
                        (is_between, ":inv_slot", ":page_start", ":page_end"),
                        (gt, ":row_count", ":max_row"),
                        (assign, ":row_count", 1),
                        (assign, ":item_x", 20),
                        (val_sub, ":item_y", ":item_space"),
                    (try_end),
                (try_end),
            (try_end),
        # ==============================================
        # 点击英雄装备栏：交换/装备物品
        # ==============================================
        (else_try),
            (assign, ":click_slot", -1),
            # 匹配点击的装备栏
            (try_for_range, ":slot_idx", 0, 9),
                (troop_slot_eq, "trp_auto_temp_list_1", ":slot_idx", ":trigger_overlay"),
                (assign, ":click_slot", ":slot_idx"),
            (try_end),
            (ge, ":click_slot", 0),
            # 获取点击物品控件
            (troop_get_slot, ":click_item_overlay", "trp_auto_temp_list_4", ":click_slot"),
            # 取消拖动
            (try_begin),
                (eq, "$g_pm_presentation_obj_10", ":click_item_overlay"),
                (assign, ":refresh_ui", 1),
            # 装备栏之间交换物品
            (else_try),
                (ge, "$g_pm_presentation_obj_10", 0),
                (try_begin),
                    (is_between, "$g_pm_presentation_obj_11", 0, 9),
                    (assign, ":is_valid_swap", 0),
                    # 同类装备栏可交换
                    (try_begin),
                        (is_between, "$g_pm_presentation_obj_11", 0, 4),
                        (is_between, ":click_slot", 0, 4),
                        (assign, ":is_valid_swap", 1),
                    (else_try),
                        (eq, "$g_pm_presentation_obj_11", ":click_slot"),
                        (assign, ":is_valid_swap", 1),
                    (try_end),
                    # 执行交换
                    (try_begin),
                        (eq, ":is_valid_swap", 1),
                        (troop_get_inventory_slot, ":item_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                        (troop_get_inventory_slot_modifier, ":mod_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                        (troop_inventory_slot_get_item_amount, ":item_amount_a", ":selected_troop", "$g_pm_presentation_obj_11"), # 获取a物品数量
                        (troop_get_inventory_slot, ":item_b", ":selected_troop", ":click_slot"),
                        (troop_get_inventory_slot_modifier, ":mod_b", ":selected_troop", ":click_slot"),
                        (troop_inventory_slot_get_item_amount, ":item_amount_b", ":selected_troop", ":click_slot"), # 获取b物品数量
                        (troop_set_inventory_slot, ":selected_troop", "$g_pm_presentation_obj_11", ":item_b"),
                        (troop_set_inventory_slot_modifier, ":selected_troop", "$g_pm_presentation_obj_11", ":mod_b"),
                        (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                            (gt, ":item_b", 0),
                            (item_get_type, ":item_type", ":item_b"),  # 获取物品类型
                            (item_has_property, ":item_b", itp_consumable),  # 消耗品
                            (troop_inventory_slot_set_item_amount, ":selected_troop", "$g_pm_presentation_obj_11", ":item_amount_b"), # 设置b物品数量
                        (try_end),
                        (troop_set_inventory_slot, ":selected_troop", ":click_slot", ":item_a"),
                        (troop_set_inventory_slot_modifier, ":selected_troop", ":click_slot", ":mod_a"),
                        (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                            (gt, ":item_a", 0),
                            (item_get_type, ":item_type", ":item_a"),  # 获取物品类型
                            (item_has_property, ":item_a", itp_consumable),  # 消耗品
                            (troop_inventory_slot_set_item_amount, ":selected_troop", ":click_slot", ":item_amount_a"), # 设置a物品数量
                        (try_end),
                        
                        (assign, ":refresh_ui", 1),
                    (try_end),
                # 背包→英雄装备
                (else_try),
                    (ge, "$g_pm_presentation_obj_11", 10),
                    (troop_get_inventory_slot, ":player_item", "trp_player", "$g_pm_presentation_obj_11"),
                    (troop_get_inventory_slot_modifier, ":player_mod", "trp_player", "$g_pm_presentation_obj_11"),
                    (troop_inventory_slot_get_item_amount, ":item_amount_player", "trp_player", "$g_pm_presentation_obj_11"), # 获取背包物品数量
                    # 判断英雄能否使用该物品
                    (call_script, "script_new_char_sys_troop_can_use_item", ":selected_troop", ":player_item", ":player_mod"),
                    (try_begin),
                        (eq, reg0, 1),
                        # 非锁定装备栏
                        (neg|troop_slot_eq, "trp_auto_temp_list_3_1", ":click_slot", 1),
                        # 判断物品类型匹配装备栏
                        (item_get_type, ":item_type", ":player_item"),
                        (assign, ":is_match_slot", 0),
                        (try_begin),
                            (is_between, ":click_slot", 0, 4),
                            (this_or_next|eq, ":item_type", 2),
                            (this_or_next|eq, ":item_type", 3),
                            (this_or_next|eq, ":item_type", 4),
                            (this_or_next|eq, ":item_type", 8),
                            (this_or_next|eq, ":item_type", 9),
                            (this_or_next|eq, ":item_type", 10),
                            (this_or_next|eq, ":item_type", 5),
                            (this_or_next|eq, ":item_type", 6),
                            (this_or_next|eq, ":item_type", 16),
                            (this_or_next|eq, ":item_type", 17),
                            (this_or_next|eq, ":item_type", 18),
                            (eq, ":item_type", 7),
                            (assign, ":is_match_slot", 1),
                        (else_try),
                            (eq, ":click_slot", 4), 
                            (eq, ":item_type", 12), 
                            (assign, ":is_match_slot", 1),
                        (else_try),
                            (eq, ":click_slot", 5), 
                            (eq, ":item_type", 13), 
                            (assign, ":is_match_slot", 1),
                        (else_try),
                            (eq, ":click_slot", 6), 
                            (eq, ":item_type", 14), 
                            (assign, ":is_match_slot", 1),
                        (else_try),
                            (eq, ":click_slot", 7), 
                            (eq, ":item_type", 15), 
                            (assign, ":is_match_slot", 1),
                        (else_try),
                            (eq, ":click_slot", 8), 
                            (eq, ":item_type", 1),  
                            (assign, ":is_match_slot", 1),
                        (try_end),
                        # 执行装备
                        (try_begin),
                            (eq, ":is_match_slot", 1),
                            (troop_get_inventory_slot, ":hero_item", ":selected_troop", ":click_slot"),
                            (troop_get_inventory_slot_modifier, ":hero_mod", ":selected_troop", ":click_slot"),
                            (troop_inventory_slot_get_item_amount, ":item_amount_hero", ":selected_troop", ":click_slot"), # 获取英雄物品数量
                            (troop_set_inventory_slot, "trp_player", "$g_pm_presentation_obj_11", ":hero_item"),
                            (troop_set_inventory_slot_modifier, "trp_player", "$g_pm_presentation_obj_11", ":hero_mod"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":hero_item", 0),          
                                (item_get_type, ":item_type", ":hero_item"),  # 获取物品类型
                                (item_has_property, ":hero_item", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, "trp_player", "$g_pm_presentation_obj_11", ":item_amount_hero"), # 设置英雄物品数量
                            (try_end),
                            (troop_set_inventory_slot, ":selected_troop", ":click_slot", ":player_item"),
                            (troop_set_inventory_slot_modifier, ":selected_troop", ":click_slot", ":player_mod"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":player_item", 0),
                                (item_get_type, ":item_type", ":player_item"),  # 获取物品类型
                                (item_has_property, ":player_item", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, ":selected_troop", ":click_slot", ":item_amount_player"), # 设置背包物品数量
                            (try_end),
                            
                            (assign, ":refresh_ui", 1),
                        (try_end),
                    (try_end),
                (try_end),
            # 开始拖动物品
            (else_try),
                (ge, ":click_item_overlay", 0),
                (assign, "$g_pm_presentation_obj_10", ":click_item_overlay"),
                (assign, "$g_pm_presentation_obj_11", ":click_slot"),
            (try_end),
            # 刷新界面
            (try_begin),
                (eq, ":refresh_ui", 1),
                (assign, "$g_pm_presentation_obj_10", -1),
                (assign, "$g_pm_presentation_obj_11", -1),
                (start_presentation, "prsnt_exchange_special_troop_equippment"),
            (try_end),
        # ==============================================
        # 点击玩家背包：交换/卸下物品
        # ==============================================
        (else_try),
            (troop_get_inventory_capacity, ":player_inv_cap", "trp_player"),
            (assign, ":click_slot", -1),
            (try_for_range, ":slot_idx", 10, ":player_inv_cap"),
                (troop_slot_eq, "trp_auto_temp_list_1", ":slot_idx", ":trigger_overlay"),
                (assign, ":click_slot", ":slot_idx"),
                (assign, ":player_inv_cap", -1),
            (try_end),
            (ge, ":click_slot", 0),
            (troop_get_slot, ":click_item_overlay", "trp_auto_temp_list_4", ":click_slot"),
            (assign, ":refresh_ui", -1),
            # 拖动状态：执行交换/卸下
            (try_begin),
                (ge, "$g_pm_presentation_obj_10", 0),
                # 背包内部交换
                (try_begin),
                    (ge, "$g_pm_presentation_obj_11", 10),
                    (troop_get_inventory_slot, ":item_a", "trp_player", "$g_pm_presentation_obj_11"),
                    (troop_get_inventory_slot_modifier, ":mod_a", "trp_player", "$g_pm_presentation_obj_11"),
                    (troop_inventory_slot_get_item_amount, ":item_amount_a", "trp_player", "$g_pm_presentation_obj_11"), # 获取a物品数量
                    (troop_get_inventory_slot, ":item_b", "trp_player", ":click_slot"),
                    (troop_get_inventory_slot_modifier, ":mod_b", "trp_player", ":click_slot"),
                    (troop_inventory_slot_get_item_amount, ":item_amount_b", "trp_player", ":click_slot"), # 获取b物品数量
                    (troop_set_inventory_slot, "trp_player", "$g_pm_presentation_obj_11", ":item_b"),
                    (troop_set_inventory_slot_modifier, "trp_player", "$g_pm_presentation_obj_11", ":mod_b"),
                    (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                        (gt, ":item_b", 0),
                        (item_get_type, ":item_type", ":item_b"),  # 获取物品类型
                        (item_has_property, ":item_b", itp_consumable),  # 消耗品
                        (troop_inventory_slot_set_item_amount, "trp_player", "$g_pm_presentation_obj_11", ":item_amount_b"), # 设置b物品数量
                    (try_end),
                    
                    (troop_set_inventory_slot, "trp_player", ":click_slot", ":item_a"),
                    (troop_set_inventory_slot_modifier, "trp_player", ":click_slot", ":mod_a"),
                    (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                        (gt, ":item_a", 0),
                        (item_get_type, ":item_type", ":item_a"),  # 获取物品类型
                        (item_has_property, ":item_a", itp_consumable),  # 消耗品
                        (troop_inventory_slot_set_item_amount, "trp_player", ":click_slot", ":item_amount_a"), # 设置a物品数量
                    (try_end),
                    
                    (assign, ":refresh_ui", 1),
                # 卸下英雄装备→背包
                (else_try),
                    (troop_get_inventory_slot, ":player_item", "trp_player", ":click_slot"),
                    (eq, ":player_item", -1),
                    (try_begin),
                        #(eq, "$g_pm_presentation_obj_11", 5),
                    # 非锁定装备栏可卸下
                    #(else_try),
                        (neg|troop_slot_eq, "trp_auto_temp_list_3_1", "$g_pm_presentation_obj_11", 1),
                        (troop_get_inventory_slot, ":hero_item", ":selected_troop", "$g_pm_presentation_obj_11"),
                        (troop_get_inventory_slot_modifier, ":hero_mod", ":selected_troop", "$g_pm_presentation_obj_11"),
                        (troop_inventory_slot_get_item_amount, ":item_amount_hero", ":selected_troop", "$g_pm_presentation_obj_11"), # 获取英雄物品数量
                        (troop_set_inventory_slot, "trp_player", ":click_slot", ":hero_item"),
                        (troop_set_inventory_slot_modifier, "trp_player", ":click_slot", ":hero_mod"),
                      
                        (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                            (gt, ":hero_item", 0),
                            (item_get_type, ":item_type", ":hero_item"),  # 获取物品类型
                            (item_has_property, ":hero_item", itp_consumable),  # 消耗品
                            (troop_inventory_slot_set_item_amount, "trp_player", ":click_slot", ":item_amount_hero"), # 设置英雄物品数量
                        (try_end),
                        (troop_set_inventory_slot, ":selected_troop", "$g_pm_presentation_obj_11", -1),
                        (assign, ":refresh_ui", 1),
                    (try_end),
                # 装备栏←→背包交换
                (else_try),
                    (troop_get_inventory_slot, ":player_item", "trp_player", ":click_slot"),
                    (ge, ":player_item", 0),
                    (troop_get_inventory_slot_modifier, ":player_mod", "trp_player", ":click_slot"),
                    (troop_inventory_slot_get_item_amount, ":item_amount_player", "trp_player", ":click_slot"), # 获取玩家物品数量
                    (item_get_type, ":player_type", ":player_item"),
                    (troop_get_inventory_slot, ":hero_item", ":selected_troop", "$g_pm_presentation_obj_11"),
                    (item_get_type, ":hero_type", ":hero_item"),
                    # 判断能否装备
                    (call_script, "script_new_char_sys_troop_can_use_item", ":selected_troop", ":player_item", ":player_mod"),
                    (try_begin),
                        (eq, reg0, 1), # 可以使用
                        (neg|troop_slot_eq, "trp_auto_temp_list_3_1", "$g_pm_presentation_obj_11", 1), # 并且玩家等级达到操作的等级
                        # 物品类型匹配
                        (try_begin),
                            (this_or_next|eq, ":hero_type", 12),
                            (this_or_next|eq, ":hero_type", 13),
                            (this_or_next|eq, ":hero_type", 15),
                            (this_or_next|eq, ":hero_type", 14),
                            (eq, ":hero_type", 1),
                            (eq, ":hero_type", ":player_type"),
                            # 执行交换
                            (troop_get_inventory_slot, ":item_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                            (troop_get_inventory_slot_modifier, ":mod_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                            (troop_inventory_slot_get_item_amount, ":item_amount_a", ":selected_troop", "$g_pm_presentation_obj_11"), # 获取a物品数量
                            (troop_get_inventory_slot, ":item_b", "trp_player", ":click_slot"),
                            (troop_get_inventory_slot_modifier, ":mod_b", "trp_player", ":click_slot"),
                            (troop_inventory_slot_get_item_amount, ":item_amount_b", "trp_player", ":click_slot"), # 获取b物品数量
                            (troop_set_inventory_slot, ":selected_troop", "$g_pm_presentation_obj_11", ":item_b"),
                            (troop_set_inventory_slot_modifier, ":selected_troop", "$g_pm_presentation_obj_11", ":mod_b"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":item_b", 0),
                                (item_get_type, ":item_type", ":item_b"),  # 获取物品类型
                                (item_has_property, ":item_b", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, ":selected_troop", "$g_pm_presentation_obj_11", ":item_amount_b"), # 设置b物品数量
                            (try_end),
                            
                            (troop_set_inventory_slot, "trp_player", ":click_slot", ":item_a"),
                            (troop_set_inventory_slot_modifier, "trp_player", ":click_slot", ":mod_a"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":item_a", 0),
                                (item_get_type, ":item_type", ":item_a"),  # 获取物品类型
                                (item_has_property, ":item_a", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, "trp_player", ":click_slot", ":item_amount_a"), # 设置a物品数量
                            (try_end),
                            
                            (assign, ":refresh_ui", 1),
                        (else_try),
                            # 武器/防具通用匹配
                            (this_or_next|eq, ":hero_type", 2),
                            (this_or_next|eq, ":hero_type", 3),
                            (this_or_next|eq, ":hero_type", 4),
                            (this_or_next|eq, ":hero_type", 8),
                            (this_or_next|eq, ":hero_type", 9),
                            (this_or_next|eq, ":hero_type", 10),
                            (this_or_next|eq, ":hero_type", 5),
                            (this_or_next|eq, ":hero_type", 6),
                            (this_or_next|eq, ":hero_type", 16),
                            (this_or_next|eq, ":hero_type", 17),
                            (this_or_next|eq, ":hero_type", 18),
                            (eq, ":hero_type", 7),
                            (this_or_next|eq, ":player_type", 2),
                            (this_or_next|eq, ":player_type", 3),
                            (this_or_next|eq, ":player_type", 4),
                            (this_or_next|eq, ":player_type", 8),
                            (this_or_next|eq, ":player_type", 9),
                            (this_or_next|eq, ":player_type", 10),
                            (this_or_next|eq, ":player_type", 5),
                            (this_or_next|eq, ":player_type", 6),
                            (this_or_next|eq, ":player_type", 16),
                            (this_or_next|eq, ":player_type", 17),
                            (this_or_next|eq, ":player_type", 18),
                            (eq, ":player_type", 7),
                            # 执行交换
                            (troop_get_inventory_slot, ":item_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                            (troop_get_inventory_slot_modifier, ":mod_a", ":selected_troop", "$g_pm_presentation_obj_11"),
                            (troop_inventory_slot_get_item_amount, ":item_amount_a", ":selected_troop", "$g_pm_presentation_obj_11"), # 获取a物品数量
                            (troop_get_inventory_slot, ":item_b", "trp_player", ":click_slot"),
                            (troop_get_inventory_slot_modifier, ":mod_b", "trp_player", ":click_slot"),
                            (troop_inventory_slot_get_item_amount, ":item_amount_b", "trp_player", ":click_slot"), # 获取b物品数量
                            (troop_set_inventory_slot, ":selected_troop", "$g_pm_presentation_obj_11", ":item_b"),
                            (troop_set_inventory_slot_modifier, ":selected_troop", "$g_pm_presentation_obj_11", ":mod_b"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":item_b", 0),
                                (item_get_type, ":item_type", ":item_b"),  # 获取物品类型
                                (item_has_property, ":item_b", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, ":selected_troop", "$g_pm_presentation_obj_11", ":item_amount_b"), # 设置b物品数量
                            (try_end),
                            
                            (troop_set_inventory_slot, "trp_player", ":click_slot", ":item_a"),
                            (troop_set_inventory_slot_modifier, "trp_player", ":click_slot", ":mod_a"),
                            (try_begin),  # 如果是弹药类或者食物类，才进行设置数量
                                (gt, ":item_a", 0),
                                (item_get_type, ":item_type", ":item_a"),  # 获取物品类型
                                (item_has_property, ":item_a", itp_consumable),  # 消耗品
                                (troop_inventory_slot_set_item_amount, "trp_player", ":click_slot", ":item_amount_a"), # 设置a物品数量
                            (try_end),
                            
                            (assign, ":refresh_ui", 1),
                        (try_end),
                    (try_end),
                (try_end),
            # 开始拖动背包物品
            (else_try),
                (ge, ":click_item_overlay", 0),
                (assign, "$g_pm_presentation_obj_10", ":click_item_overlay"),
                (assign, "$g_pm_presentation_obj_11", ":click_slot"),
            (try_end),
            # 刷新界面
            (try_begin),
                (eq, ":refresh_ui", 1),
                (assign, "$g_pm_presentation_obj_10", -1),
                (assign, "$g_pm_presentation_obj_11", -1),
                (start_presentation, "prsnt_exchange_special_troop_equippment"),
            (try_end),
        # ==============================================
        # 点击 + 按钮：分配属性/技能/熟练度点数
        # ==============================================
        (else_try),
            (assign, ":click_btn", -1),
            (assign, ":max_btn", 48),
            (try_for_range, ":btn_idx", 0, ":max_btn"),
                (troop_slot_eq, "trp_auto_temp_list_1_2", ":btn_idx", ":trigger_overlay"),
                (assign, ":click_btn", ":btn_idx"),  # <--- 按钮编号存在这里
                (assign, ":max_btn", -1),
            (try_end),
            (ge, ":click_btn", 0),
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            # 分配属性点
            (try_begin),
                (is_between, ":click_btn", 0, 4),
                (assign, ":attr_idx", ":click_btn"),
                (assign, ":add_points", 1),
                # 增加属性
                (call_script, "script_new_char_sys_add_attr_point", ":selected_troop", ":attr_idx", ":add_points"),
            # 分配熟练度点
            (else_try),
                (is_between, ":click_btn", 4, 11),
                (store_sub, ":prof_idx", ":click_btn", 4),
                (assign, ":add_prof", 1),
                #(troop_raise_proficiency_linear, ":selected_troop", ":prof_idx", ":add_prof"),
                (call_script, "script_new_char_sys_add_weapon_point", ":selected_troop", ":prof_idx", ":add_prof"),
            # 分配技能点
            (else_try),
                (is_between, ":click_btn", 11, 48),
                (assign, ":add_skill", 1),
                (troop_get_slot, ":skill_idx", "trp_auto_temp_list_3_2", ":click_btn"),
                #(call_script, "script_hero_add_skill_points", ":selected_troop", ":skill_idx", ":add_skill"),
                (assign, reg0, ":skill_idx"),
                #(display_message, "@{reg0}", 0xFF0000),
                (call_script, "script_new_char_sys_add_skill_point", ":selected_troop", ":skill_idx", ":add_skill"),
            (try_end),
            # 刷新界面
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        # ==============================================
        # 切换下拉框：选择不同英雄
        # ==============================================
        (else_try),
            (eq, ":trigger_overlay", "$g_pm_presentation_obj_designer_1"),
            (assign, "$g_pm_temp_3", ":trigger_state"),
            (troop_set_slot, "trp_auto_player_set_keeper", 43, "trp_player"),
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (call_script, "script_save_troop_points_for_reset", ":selected_troop"),  # 存储npc的点数，便于重设
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        # ==============================================
        # 点击重设按钮
        # ==============================================
        (else_try),
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_btn_reset"),
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (call_script, "script_restore_troop_points_from_reset", ":selected_troop"),
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        # ==============================================
        # 点击洗点按钮
        # ==============================================
        (else_try),
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_btn_reset_stats"),
            #(troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            #(call_script, "script_how_pay_respec_troop_full", ":selected_troop"),

            # 是否进行洗点确认框
            #(question_box, "str_auto_you_want_to_reset_stats", "@111", "@222"),

            #(presentation_set_duration, 0),
            (assign, "$g_pm_auto_point_question_flag", 0),
            (start_presentation, "prsnt_question_auto_point_reset_stats"),
        # ==============================================
        # 点击 返回 按钮
        # ==============================================
        (else_try),
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_btn_back"),
            (assign, "$g_pm_first_enter_pren", 0),   # 设置为首次进入
            (assign, "$g_pm_is_show_extra_prerequisite", 0),   # 设置显示额外条件
            (call_script, "script_start_auto_point"), # 退出界面开启自动加点
            (presentation_set_duration, 0),
            
            #(jump_to_menu, "mnu_auto_return_to_map"),
        # ==============================================
        # 自动加点相关 点击 
        # ==============================================
        (else_try), # 是否开启自动加点功能
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_is_open"),  
            (store_add, ":auto_all_slot_1724", "$g_pm_auto_point_base_slot", 124), # 1724
            (troop_set_slot, ":selected_troop", ":auto_all_slot_1724", ":trigger_state"), # 设置某个槽的值
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (else_try),  # 选择预设方案下拉框
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_comb"),
            (assign, "$g_pm_prsn_auto_point_comb_index", ":trigger_state"), # 设置当前选择的方案
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (else_try),  # 点击选择方案按钮
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_btn_choose"),
            # 获取trp名字
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (call_script, "script_how_pay_respec_troop_full", ":selected_troop"),
            (str_store_troop_name, s5, ":selected_troop"),
            # 获取当前选中的方案名字
            (assign, ":tmp_offset", 2001),
            (try_for_range_backwards, ":stack_index", 0, 71),
                (try_for_range, ":programme_index", 0, 10),
                    # 计算索引值
                    (eq, "$g_pm_prsn_auto_point_comb_index", ":programme_index"), # 仅处理当前选中的方案
                    (store_mul, ":tmp_mul", ":programme_index", 100),
                    (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
                    (val_add, ":tmp_trp_index", ":tmp_mul"), 
                    # 设置方案名称
                    (eq, ":stack_index", 0), # 方案名称
                    (try_begin),  # 这个区间用单数
                        (is_between, ":programme_index", 0, 5), 
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name, s25, ":trp_store_scheme_name"),
                    (else_try),  # 这个区间用复数
                        (is_between, ":programme_index", 5, 10),
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name_plural, s25, ":trp_store_scheme_name"),
                    (try_end),
                (try_end),
            (try_end),
            (assign, "$g_pm_auto_point_question_flag", 1),
            (start_presentation, "prsnt_question_auto_point_reset_stats"),
        (else_try),  # 点击添加方案按钮
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_btn_add"),
            # 获取trp名字
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (call_script, "script_how_pay_respec_troop_full", ":selected_troop"),
            (str_store_troop_name, s5, ":selected_troop"),
            # 获取当前选中的方案名字
            (assign, ":tmp_offset", 2001),
            (try_for_range_backwards, ":stack_index", 0, 71),
                (try_for_range, ":programme_index", 0, 10),
                    # 计算索引值
                    (eq, "$g_pm_prsn_auto_point_comb_index", ":programme_index"), # 仅处理当前选中的方案
                    (store_mul, ":tmp_mul", ":programme_index", 100),
                    (store_add, ":tmp_trp_index", ":tmp_offset", ":stack_index"), 
                    (val_add, ":tmp_trp_index", ":tmp_mul"), 
                    # 设置方案名称
                    (eq, ":stack_index", 0), # 方案名称
                    (try_begin),  # 这个区间用单数
                        (is_between, ":programme_index", 0, 5), 
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name, s25, ":trp_store_scheme_name"),
                    (else_try),  # 这个区间用复数
                        (is_between, ":programme_index", 5, 10),
                        (troop_get_slot, ":trp_store_scheme_name", "trp_auto_point", ":tmp_trp_index"), 
                        (str_store_troop_name_plural, s25, ":trp_store_scheme_name"),
                    (try_end),
                (try_end),
            (try_end),
            (assign, "$g_pm_auto_point_question_flag", 2),
            (start_presentation, "prsnt_question_auto_point_reset_stats"),
        (else_try),  # 获取输入的名称
            (eq, ":trigger_overlay", "$g_pm_prsn_auto_point_simple_text_box"),
            (str_store_string, s24, 0),
            #(assign, "$g_pm_prsn_auto_point_scheme_name", s24),
            # (display_message, "@{s2}", 0xFF0000),
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (else_try),
            (store_add, ":combo_button_base_num", "$g_pm_auto_point_base_slot_part", 271),  # 2071
            (store_add, ":number_box_button_base_num", "$g_pm_auto_point_base_slot_part", 371),  # 2171
            (store_add, ":checkbox_base_num", "$g_pm_auto_point_base_slot_part", 471),  # 2271

            (store_add, ":combo_button_base_num_curr", "$g_pm_auto_point_base_slot", 55), # 1655 自动加点-下拉框1-23的加点项，数量23
            (store_add, ":number_box_button_base_num_curr", "$g_pm_auto_point_base_slot", 78), # 1678 自动加点-自动加点目标值，数量23
            (store_add, ":checkbox_base_num_curr", "$g_pm_auto_point_base_slot", 101), # 1701 自动加点-技能点不够是否点智力强行加点，数量23

            (assign, ":max_btn", 23),
            (try_for_range, ":btn_idx", 0, ":max_btn"),
                (try_begin),   # 技能选择下拉框
                    (store_add, ":combo_button_slot_num", ":combo_button_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":combo_button_slot_num", ":trigger_overlay"),  # 获取当前触发的按钮
                    (store_add, ":combo_button_slot_num_curr", ":combo_button_base_num_curr", ":btn_idx"), # 获取实际的槽
                    (troop_set_slot, ":selected_troop", ":combo_button_slot_num_curr", ":trigger_state"), # 设置某个槽的值
                    # 设置值为0
                    (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":btn_idx"), # 获取实际的槽
                    (troop_set_slot, ":selected_troop", ":number_box_button_slot_num_curr", 0), # 设置某个槽的值
                    # 设置强行加点为false
                    (store_add, ":checkbox_slot_num_curr", ":checkbox_base_num_curr", ":btn_idx"), # 获取实际的槽
                    (troop_set_slot, ":selected_troop", ":checkbox_slot_num_curr", 0), # 设置某个槽的值
                    (assign, ":max_btn", -1),

                (else_try),   # 技能预计值框
                    (store_add, ":number_box_button_slot_num", ":number_box_button_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":number_box_button_slot_num", ":trigger_overlay"),  # 获取当前触发的按钮
                    (store_add, ":number_box_button_slot_num_curr", ":number_box_button_base_num_curr", ":btn_idx"), # 获取实际的槽
                    (troop_set_slot, ":selected_troop", ":number_box_button_slot_num_curr", ":trigger_state"), # 设置某个槽的值
                    (assign, ":max_btn", -1),

                (else_try),   # 技能强制加点勾选框
                    (store_add, ":checkbox_slot_num", ":checkbox_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":checkbox_slot_num", ":trigger_overlay"),  # 获取当前触发的按钮
                    (store_add, ":checkbox_slot_num_curr", ":checkbox_base_num_curr", ":btn_idx"), # 获取实际的槽
                    (troop_set_slot, ":selected_troop", ":checkbox_slot_num_curr", ":trigger_state"), # 设置某个槽的值
                    (assign, ":max_btn", -1),

            (try_end),
            
            # 刷新界面
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (try_end),
    ]),

    # ==============================================
    # 触发事件：是否洗点弹窗
    # ==============================================
    # (ti_question_answered,[
    #     (store_trigger_param_1, ":var_0"),

    #     (assign, reg8, ":var_0"),
    #     (display_message, "@{reg8}", 0xFF0000),

    #     (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),

    #     # 确认后进行洗点操作
    #     (call_script, "script_use_it_new_char_sys_respec_troop_full", ":selected_troop"),

    #     # 洗点完成刷新界面
    #     (start_presentation, "prsnt_exchange_special_troop_equippment"),
    # ]),
    # ==============================================
    # 触发事件2：界面运行时每帧执行
    # ==============================================
    (ti_on_presentation_run, [
      #(call_script, "script_mouse_fix_pos_run"),#辅助线
        # 界面运行脚本
        (call_script, "script_pre_2"),
        # 拖动装备：跟随鼠标移动
        (try_begin),
            (ge, "$g_pm_presentation_obj_10", 0),
            (mouse_get_position, pos10),
            (overlay_set_position, "$g_pm_presentation_obj_10", pos10),
        (try_end),
        # 右键点击：取消拖动，刷新界面
        (try_begin),
            (key_clicked, key_right_mouse_button),
            (assign, "$g_pm_presentation_obj_10", -1),
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (try_end),
    ]),
# ==============================================
# 触发事件4：鼠标移入/移出控件 显示详情 物品/技能
# 核心逻辑：
# 1. 鼠标移入 → 显示装备详情 或 技能说明文本
# 2. 鼠标移出 → 关闭装备详情 或 清空技能文本
# ==============================================
(ti_on_presentation_mouse_enter_leave, [
    # ====================== 读取鼠标事件基础参数 ======================
    (store_trigger_param_1, ":control_id"),                          # 触发当前事件的控件ID
    (store_trigger_param_2, ":mouse_action"),                        # 0=鼠标移入控件  1=鼠标移出控件

    (str_store_string, s1, "str_ui_hero_strengthen_string_41"),

    # ==========================================================
    # 鼠标【移入】控件 —— 显示详情 装备/技能
    # ==========================================================
    (try_begin),
        (eq, ":mouse_action", 0),                                   # 判断：鼠标移入事件
        (assign, ":inventory_slot_idx", -1),                         # 初始化：物品槽位索引 -1=未找到
        (troop_get_inventory_capacity, ":player_inv_total", "trp_player"), # 获取玩家背包总容量
        (try_for_range, ":loop_idx", 0, ":player_inv_total"),       # 遍历玩家所有物品槽位
            (troop_slot_eq, "trp_auto_temp_list_1", ":loop_idx", ":control_id"), # 匹配：控件对应的物品槽位
            (assign, ":inventory_slot_idx", ":loop_idx"),            # 记录匹配到的槽位编号
        (try_end),
        (ge, ":inventory_slot_idx", 0),                              # 判断：找到有效装备槽位

        (troop_get_slot, ":current_hero", "trp_auto_temp_list_3", "$g_pm_temp_3"), # 获取当前操作的英雄部队ID
        (try_begin),
            (is_between, ":inventory_slot_idx", 0, 9),               # 判断：槽位0-9是英雄身上装备
            (assign, ":item_owner", ":current_hero"),                # 装备归属：当前英雄
        (else_try),
            (assign, ":item_owner", "trp_player"),                  # 其他槽位：归属玩家背包
        (try_end),

        (troop_get_inventory_slot, ":item_id", ":item_owner", ":inventory_slot_idx"), # 获取槽内物品ID
        (troop_get_inventory_slot_modifier, ":item_modifier", ":item_owner", ":inventory_slot_idx"), # 获取物品品质修饰符
        (overlay_get_position, pos0, ":control_id"),                # 获取控件在界面上的坐标
        (neg|eq, ":item_id", -1),                                   # 判断：物品不为空
        (assign, "$g_pm_auto_point_curr_inv_slot", ":inventory_slot_idx"),
        (show_item_details_with_modifier, ":item_id", ":item_modifier", pos0, 100), # 显示物品详情浮窗
        (assign, "$g_pm_current_opened_item_details", ":control_id"),  # 记录：当前打开详情的控件

    # ==========================================================
    # 处理【技能栏】控件移入 
    # ==========================================================
    (else_try),
        (eq, ":mouse_action", 0),                                   # 再次确认：鼠标移入
        (assign, ":skill_slot_idx", -1),                            # 初始化：技能槽位索引 -1=未找到 
        (try_for_range, ":loop_idx", 0, 48),                        # 遍历技能面板48个技能槽
            (troop_slot_ge, "trp_auto_temp_list_1_1", ":loop_idx", 0),   # 过滤：有效技能槽
            (troop_slot_eq, "trp_auto_temp_list_1_1", ":loop_idx", ":control_id"), # 匹配：控件对应的技能槽
            (assign, ":skill_slot_idx", ":loop_idx"),               # 记录匹配到的技能槽位
        (try_end),
        (ge, ":skill_slot_idx", 0),                                 # 判断：找到有效技能槽
        # (assign, reg8, ":skill_slot_idx"),
        # (display_message, "@{reg8}", 0xFF0000),
        (neg|eq, ":skill_slot_idx", 47),   
        (troop_get_slot, ":skill_str_raw", "trp_auto_temp_list_2_2", ":skill_slot_idx"), # 获取技能名称原始字符串ID
        (try_begin),
            (is_between, ":skill_slot_idx", 11, 48),               # 判断：高级/可强化技能槽
            (store_sub, ":skill_str_offset", ":skill_str_raw", "str_ui_hero_strengthen_string_1"), # 计算技能名称偏移量
            (store_add, ":skill_final_str", ":skill_str_offset", "str_ui_hero_strengthen_string_45"), # 拼接最终技能名称
            (troop_get_slot, ":current_hero", "trp_auto_temp_list_3", "$g_pm_temp_3"), # 获取当前操作英雄
            (troop_get_slot, ":skill_id", "trp_auto_temp_list_3_2", ":skill_slot_idx"), # 获取技能ID
            (call_script, "script_get_troop_skill_max_level", ":skill_id"), # 调用脚本：获取技能最大等级
            (assign, reg10, reg0),                                  # 保存技能上限到寄存器10
            (str_store_string, s1, "str_ui_hero_strengthen_string_82"), # 加载技能说明前缀
            (str_store_string, s2, ":skill_final_str"),            # 加载技能名称
            (str_store_string, s1, "str_auto_s1_s2"),                 # 组合最终显示文本
        (else_try),
            # 普通技能：直接显示名称
            (store_sub, ":skill_str_offset", ":skill_str_raw", "str_ui_hero_strengthen_string_1"),
            (store_add, ":skill_final_str", ":skill_str_offset", "str_ui_hero_strengthen_string_45"),
            (str_store_string, s1, ":skill_final_str"),            # 设置技能名称文本
        (try_end),
        (troop_get_slot, ":skill_text_overlay", "trp_auto_temp_list_1", 1001), # 获取技能文本显示控件
        (overlay_set_text, ":skill_text_overlay", s1),               # 设置控件显示技能文本
        (assign, "$g_pm_current_opened_item_details", ":control_id"),    # 记录当前打开详情的控件
    # ==========================================================
    # 处理【自动加点控件】移入 
    # ==========================================================
    (else_try),
        (eq, ":mouse_action", 0),   # 鼠标移入
        (troop_get_slot, ":skill_text_overlay", "trp_auto_temp_list_1", 1001), # 获取技能文本显示控件
        (assign, ":tmp_is_trigger", 0),  # 是否匹配控件
        (try_begin),
            (eq, "$g_pm_presentation_obj_designer_1", ":control_id"),  # 选择同伴
            (overlay_set_text, ":skill_text_overlay", "str_auto_companion_select_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_is_open", ":control_id"),  # 是否开启自动加点
            (overlay_set_text, ":skill_text_overlay", "str_auto_global_switch_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_comb", ":control_id"),  # 选 择 预 设 方 案
            (overlay_set_text, ":skill_text_overlay", "str_auto_scheme_select_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_input_name", ":control_id"),  # 输 入 预 设 方 案 名 称
            (overlay_set_text, ":skill_text_overlay", "str_auto_scheme_name_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_btn_choose", ":control_id"),  # 点 击 按 钮 应 用 下 拉 框 所 选 方 案
            (overlay_set_text, ":skill_text_overlay", "str_auto_scheme_apply_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_btn_add", ":control_id"),  # 点 击 按 钮 添 加 到 预 设 方 案
            (overlay_set_text, ":skill_text_overlay", "str_auto_scheme_save_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_btn_reset_stats", ":control_id"),  # 洗点
            (overlay_set_text, ":skill_text_overlay", "str_auto_respec_cost_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_btn_reset", ":control_id"),  # 重置
            (overlay_set_text, ":skill_text_overlay", "str_auto_rebuild_confirm_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_btn_back", ":control_id"),  # 返回
            (overlay_set_text, ":skill_text_overlay", "str_auto_ui_close_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_str_exp", ":control_id"),  # 经验
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (store_character_level, reg10, ":selected_troop"),
            (store_add, ":level_no", reg10, 1),
            (get_level_boundary, reg0, ":level_no"), # 计算升到level_no所需的经验值
            (overlay_set_text, ":skill_text_overlay", "str_auto_exp_info_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (eq, "$g_pm_prsn_auto_point_str_hp", ":control_id"),  # 血量
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            (store_troop_health, reg0, ":selected_troop", 1),
            (overlay_set_text, ":skill_text_overlay", "str_auto_hp_info_intro"),  # 设置控件显示技能文本
            (assign, ":tmp_is_trigger", 1),
        (else_try),
            (store_add, ":combo_button_base_num", "$g_pm_auto_point_base_slot_part", 271),  # 2071
            (store_add, ":number_box_button_base_num", "$g_pm_auto_point_base_slot_part", 371),  # 2171
            (store_add, ":checkbox_base_num", "$g_pm_auto_point_base_slot_part", 471),  # 2271

            (assign, ":max_btn", 23),
            (try_for_range, ":btn_idx", 0, ":max_btn"),
                (try_begin),   # 技能选择下拉框
                    (store_add, ":combo_button_slot_num", ":combo_button_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":combo_button_slot_num", ":control_id"),  # 获取当前触发的按钮
                    (overlay_set_text, ":skill_text_overlay", "str_auto_skill_select_intro"),  # 设置控件显示技能文本
                    (assign, ":tmp_is_trigger", 1),
                    (assign, ":max_btn", -1),
                (else_try),   # 技能预计值框
                    (store_add, ":number_box_button_slot_num", ":number_box_button_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":number_box_button_slot_num", ":control_id"),  # 获取当前触发的按钮
                    (overlay_set_text, ":skill_text_overlay", "str_auto_skill_target_intro"),  # 设置控件显示技能文本
                    (assign, ":tmp_is_trigger", 1),
                    (assign, ":max_btn", -1),
                (else_try),   # 技能强制加点勾选框
                    (store_add, ":checkbox_slot_num", ":checkbox_base_num", ":btn_idx"),
                    (troop_slot_eq, "trp_auto_point", ":checkbox_slot_num", ":control_id"),  # 获取当前触发的按钮
                    (overlay_set_text, ":skill_text_overlay", "str_auto_skill_force_intro"),  # 设置控件显示技能文本
                    (assign, ":tmp_is_trigger", 1),
                    (assign, ":max_btn", -1),
                (try_end),
            (try_end),

            
        (try_end),
        (eq, ":tmp_is_trigger", 1),

        (assign, "$g_pm_current_opened_item_details", ":control_id"),  # 记录当前打开详情的控件
    # ==========================================================
    # 鼠标【移出】装备控件 —— 关闭装备详情
    # ==========================================================
    (else_try),
        (assign, ":is_equipment_slot", 0),                           # 标记：是否为装备槽控件
        (troop_get_inventory_capacity, ":player_inv_total", "trp_player"), # 获取玩家背包容量
        (try_for_range, ":loop_idx", 0, ":player_inv_total"),       # 遍历装备槽
            (troop_slot_eq, "trp_auto_temp_list_1", ":loop_idx", ":control_id"), # 匹配装备控件
            (assign, ":is_equipment_slot", 1),                      # 标记为装备槽
        (try_end),
        (eq, ":is_equipment_slot", 1),                               # 判断当前是装备槽控件

        (try_begin),
            (eq, "$g_pm_current_opened_item_details", ":control_id"),  # 判断：当前关闭的正是打开的详情
            (close_item_details),                                   # 关闭物品详情浮窗
        (try_end),

    # ==========================================================
    # 鼠标【移出】技能控件 —— 清空技能文本
    # ==========================================================
    (else_try),
        (assign, ":is_skill_slot", 0),                               # 标记：是否为技能槽控件
        (try_for_range, ":loop_idx", 0, 48),                        # 遍历技能槽
            (troop_slot_ge, "trp_auto_temp_list_1_1", ":loop_idx", 0),   # 有效技能槽判断
            (troop_slot_eq, "trp_auto_temp_list_1_1", ":loop_idx", ":control_id"), # 匹配技能控件
            (assign, ":is_skill_slot", 1),                          # 标记为技能槽
        (try_end),
        (eq, ":is_skill_slot", 1),                                  # 判断当前是技能槽控件
        (eq, "$g_pm_current_opened_item_details", ":control_id"),      # 匹配当前打开的详情控件

        (troop_get_slot, ":skill_text_overlay", "trp_auto_temp_list_1", 1001), # 获取技能文本控件
        (overlay_set_text, ":skill_text_overlay", "str_ui_hero_strengthen_string_41"), # 重置为默认文本/空文本
    # ==========================================================
    # 鼠标【移出】自动加点控件 —— 清空技能文本
    # ==========================================================
    (else_try),
            (store_add, ":combo_button_base_num", "$g_pm_auto_point_base_slot_part", 271),  # 2071
            (store_add, ":number_box_button_base_num", "$g_pm_auto_point_base_slot_part", 371),  # 2171
            (store_add, ":checkbox_base_num", "$g_pm_auto_point_base_slot_part", 471),  # 2271
        (assign, ":tmp_is_trigger", 0),

        (assign, ":max_btn", 23),
        (try_for_range, ":btn_idx", 0, ":max_btn"),
            (try_begin),   # 技能选择下拉框
                (store_add, ":combo_button_slot_num", ":combo_button_base_num", ":btn_idx"),
                (troop_slot_eq, "trp_auto_point", ":combo_button_slot_num", ":control_id"),  # 获取当前触发的按钮
                (assign, ":tmp_is_trigger", 1),
                (assign, ":max_btn", -1),
            (else_try),   # 技能预计值框
                (store_add, ":number_box_button_slot_num", ":number_box_button_base_num", ":btn_idx"),
                (troop_slot_eq, "trp_auto_point", ":number_box_button_slot_num", ":control_id"),  # 获取当前触发的按钮
                (assign, ":tmp_is_trigger", 1),
                (assign, ":max_btn", -1),
            (else_try),   # 技能强制加点勾选框
                (store_add, ":checkbox_slot_num", ":checkbox_base_num", ":btn_idx"),
                (troop_slot_eq, "trp_auto_point", ":checkbox_slot_num", ":control_id"),  # 获取当前触发的按钮
                (assign, ":tmp_is_trigger", 1),
                (assign, ":max_btn", -1),
            (try_end),
        (try_end),
        (this_or_next|eq, "$g_pm_presentation_obj_designer_1", ":control_id"),  # 匹配控件
        (this_or_next|eq, "$g_pm_prsn_auto_point_is_open", ":control_id"),  # 是否开启自动加点
        (this_or_next|eq, "$g_pm_prsn_auto_point_comb", ":control_id"),  # 选 择 预 设 方 案
        (this_or_next|eq, "$g_pm_prsn_auto_point_input_name", ":control_id"),  # 输 入 预 设 方 案 名 称
        (this_or_next|eq, "$g_pm_prsn_auto_point_btn_choose", ":control_id"),  # 点 击 按 钮 应 用 下 拉 框 所 选 方 案
        (this_or_next|eq, "$g_pm_prsn_auto_point_btn_add", ":control_id"),  # 点 击 按 钮 添 加 到 预 设 方 案
        (this_or_next|eq, "$g_pm_prsn_auto_btn_reset_stats", ":control_id"),  # 洗点
        (this_or_next|eq, "$g_pm_prsn_auto_point_btn_reset", ":control_id"),  # 重置
        (this_or_next|eq, "$g_pm_prsn_auto_point_btn_back", ":control_id"),  # 返回
        (this_or_next|eq, "$g_pm_prsn_auto_point_str_hp", ":control_id"),  # 血量
        (this_or_next|eq, "$g_pm_prsn_auto_point_str_exp", ":control_id"),  # 经验
        (eq, ":tmp_is_trigger", 1),

        (eq, "$g_pm_current_opened_item_details", ":control_id"),      # 匹配当前打开的详情控件
        (troop_get_slot, ":skill_text_overlay", "trp_auto_temp_list_1", 1001), # 获取技能文本控件
        (overlay_set_text, ":skill_text_overlay", "str_ui_hero_strengthen_string_41"), # 重置为默认文本/空文本
    (try_end),
]),


]),


# ==============================================
# 界面名称：特殊部队装备交换界面
# 功能：玩家可给特殊英雄NPC更换装备、升级属性/技能/熟练度、查看角色详情
# ==============================================
("question_auto_point_reset_stats", 0, mesh_bg_auto_ques_win, [   # mesh_load_bg_auto_ques_win = 1048
    # ==============================================
    # 触发事件1：界面加载时执行 初始化核心逻辑 
    # ==============================================
    (ti_on_presentation_load, [
        # 设置浮点数运算倍率 骑砍固定格式 
        (set_fixed_point_multiplier, 1000),
        # 设置界面无限时长 不自动关闭 
        (presentation_set_duration, 999999),

        # ==============================================
        # 首次进入界面初始化：重置临时变量
        # ==============================================
        (create_text_overlay, reg0, "str_auto_point_force_add"), # 为了防止出现ui索引的bug创建的一个空的
        
        (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
        (call_script, "script_how_pay_respec_troop_full", ":selected_troop"),
        # 创建自动加点文字
        # 判断当前判断框为哪一个
        (try_begin),  # 选择方案
            (eq, "$g_pm_auto_point_question_flag", 1), 
            (call_script, "script_create_a_simple_string_at_position", "str_auto_you_want_to_select_scheme", 501, 337, 800, 16, -1),
        (else_try),  # 添加方案
            (eq, "$g_pm_auto_point_question_flag", 2), 
            (call_script, "script_create_a_simple_string_at_position", "str_auto_you_want_to_add_scheme", 501, 337, 800, 16, -1),
        (else_try),  # 是否洗点 
            (call_script, "script_create_a_simple_string_at_position", "str_auto_you_want_to_reset_stats", 501, 337, 800, 16, -1),
        (try_end),

        # 创建确定按钮
        (call_script, "script_create_a_button_overlay_by_type", "str_yes", 100, 30, 416, 295, 1, -1, -1),
        (assign, "$g_pm_question_reset_stats_yes", reg0),
        # 创建取消按钮
        (call_script, "script_create_a_button_overlay_by_type", "str_no", 100, 30, 573, 295, 1, -1, -1),
        (assign, "$g_pm_question_reset_stats_no", reg0),



    ]),

    # ==============================================
    # 触发事件：洗点确认框，点击确定或取消
    # ==============================================
    (ti_on_presentation_event_state_change, [
        # 获取触发控件ID/状态
        (store_trigger_param_1, ":trigger_overlay"),
        (store_trigger_param_2, ":trigger_state"),
        (set_fixed_point_multiplier, 1000),
        (try_begin),  # 点击是按钮
            (eq, "$g_pm_question_reset_stats_yes", ":trigger_overlay"),  
            (troop_get_slot, ":selected_troop", "trp_auto_temp_list_3", "$g_pm_temp_3"),
            # 确认后进行洗点操作
            (try_begin),  # 选择方案
                (eq, "$g_pm_auto_point_question_flag", 1), 
                (call_script, "script_auto_point_choose_scheme", ":selected_troop"),  # 调用op
            (else_try),  # 添加方案
                (eq, "$g_pm_auto_point_question_flag", 2), 
                (call_script, "script_auto_point_add_scheme", ":selected_troop"),  # 调用op
            (else_try),  # 是否洗点 
                (call_script, "script_use_it_new_char_sys_respec_troop_full", ":selected_troop"),
            (try_end),
            (presentation_set_duration, 0),
            # 洗点完成刷新界面
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (else_try),  # 点击否按钮
            (eq, "$g_pm_question_reset_stats_no", ":trigger_overlay"),
            (presentation_set_duration, 0),
            (start_presentation, "prsnt_exchange_special_troop_equippment"),
        (try_end),
    ]),
    # ==============================================
    # 触发事件2：界面运行时每帧执行
    # ==============================================
    # (ti_on_presentation_run, [
    #   (call_script, "script_mouse_fix_pos_run"),#辅助线
    # ]),


]),