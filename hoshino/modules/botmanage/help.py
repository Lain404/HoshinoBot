from hoshino import Service, Privilege as Priv

sv = Service('_help_', manage_priv=Priv.SUPERUSER, visible=False)

MANUAL = '''

你还在@UE？ Out了！
UE、CXK均可使用
cxk给爷来一井
[@bot来发十连] 十连转蛋模拟
[@bot来发单抽] 单抽转蛋模拟
[@bot来一井] 4w5钻！买定离手！
[@bot妈] 每日签到
[查看卡池] 查看群中现在的卡池及出率
[b拆 妹弓] 后以空格隔开接角色名，查询竞技场解法
[pcr速查] 常用网址/速查表
[bcr速查] B服萌新攻略
[rank表] 查看rank推荐表
[黄骑充电表] 查询黄骑1动充电规律
[@bot官漫132] 官方四格阅览
[挖矿 +名次 如：挖矿 15001] 查询矿场中还剩多少钻
[切噜一下] 后以空格隔开接想要转换为切噜语的话
[切噜～♪切啰巴切拉切蹦切蹦] 切噜语翻译
[!帮助] 查看会战管理功能的说明
[启用 bangumi] 开启番剧更新推送
[@bot来点新番] 查看最近的更新(↑需先开启番剧更新推送↑)
[@bot精致睡眠] 8小时精致睡眠(bot需具有群管理权限)
[给我来一份精致昏睡下午茶套餐] 叫一杯先辈特调红茶(bot需具有群管理权限)
[@bot来杯咖啡] 联系我，空格后接反馈内容
[翻译 もう一度、キミとつながる物語] 机器翻译
[lssv] 查看功能模块的开关状态
'''.strip()

@sv.on_command('help', aliases=('manual', '帮助', '说明', '使用说明', '幫助', '說明', '使用說明', '菜单', '菜單'), only_to_me=True)
async def send_help(session):
    await session.send(MANUAL)
