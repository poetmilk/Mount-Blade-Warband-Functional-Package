(0.000000,
[   
    (eq, "$g_pm_auto_point_is_can_move_item", 0),  
    (assign, "$g_pm_auto_point_is_can_move_item", 1),  # 恢复新加点系统大地图上的装备物品和洗点功能
]),

(24.000000,
[   
    (call_script, "script_start_auto_point"),  # 每24小时进行一次自动加点
]),