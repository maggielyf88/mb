with open('index.html', 'r', encoding='utf-8') as f:
    t = f.read()

repls = [
    # ===== home detail =====
    ('<p>品牌 Logo、消息与添加设备入口；宠物切换条（Lucky 金毛贵宾 / Milo 黑色拉布拉多 / Coco 腊肠犬，头像均为与各自状态动图同款形象的卡通正面头像）；状态卡（标题、状态胶囊、Activity / Sleep 小卡、右侧宠物状态图：Lucky / Milo / Coco 均使用本次生成的透明 GIF 动图，分别为睡觉 / 散步 / 玩球，自带呼吸与动作；随当前宠物切换）、AI 洞察条）；Quick Access 四个彩色圆形入口（My Pet·dog、Voice Translation·microphone、Device·device、Genetic Test·dna，SVG 内联以保证离线可用）；Focus on Lucky 提示卡；关联设备列表。</p>',
     '<p>Brand Logo, messages and add-device entry; pet switch bar (Lucky golden retriever / Milo black Labrador / Coco dachshund, avatars are cartoon front-facing images matching each state animation); status card (title, status pill, Activity / Sleep mini cards, right-side pet status image: Lucky / Milo / Coco use the transparent GIF animations generated this time, sleeping / walking / playing ball respectively, with breathing and motion; switches with current pet), AI insight bar); Quick Access four colored round entries (My Pet·dog, Voice Translation·microphone, Device·device, Genetic Test·dna, SVG inlined for offline use); Focus on Lucky tip card; linked device list.</p>'),
    ('<li>点击右上角「+」或设备区底部的「+ Add Device」，弹出同一个添加设备弹框（Smart Dog Harness / Smart Dog House，均 Model 001）。</li>',
     '<li>Tap "+" at top-right or "+ Add Device" at device area bottom to open the same add-device dialog (Smart Dog Harness / Smart Dog House, both Model 001).</li>'),
    ('<li>选择 Smart Dog Harness 并确认，进入参数弹框：参数取自 <code>MQTT_Protocol.pdf</code>（MQTT 3.1.1、Broker、Client ID、Topic、上报字段、事件与可配置上报间隔）；先选 Linked pet 关联宠物（下拉列出系统内已添加的宠物，默认当前选中宠物），再填写 IMEI 与上报间隔，加入后设备即归属该宠物。</li>',
     '<li>Select Smart Dog Harness and confirm to enter parameter dialog: parameters from <code>MQTT_Protocol.pdf</code> (MQTT 3.1.1, Broker, Client ID, Topic, reporting fields, events and configurable reporting interval); first select Linked pet to associate a pet (dropdown lists pets added in system, default current selected), then fill IMEI and reporting interval; after adding, device belongs to that pet.</li>'),
    ('<li>点击 Smart Dog House 会提示「该设备生产中」，暂不提供后续弹框。</li>',
     '<li>Tap Smart Dog House will prompt "Device in production", no further dialog provided for now.</li>'),
    ('<li>切换 Lucky、Milo、Coco 或 All Pets；点击状态卡进入健康详情，点击洞察条进入 AI 管家。</li>',
     '<li>Switch Lucky, Milo, Coco or All Pets; tap status card to enter health details, tap insight bar to enter AI Butler.</li>'),
    ('<li>设备区随当前宠物过滤：Lucky 2 台（Harness + Dog House）、Milo 1 台（Harness）、Coco 无设备（显示 No devices yet），All Pets 汇总 3 台。</li>',
     '<li>Device area filters by current pet: Lucky 2 units (Harness + Dog House), Milo 1 unit (Harness), Coco no devices (shows No devices yet), All Pets totals 3 units.</li>'),
    ('<li>首次使用的新用户可点设备区「Add Device」进入新用户绑定流程：仅支持扫码绑定（智能设备 / 基因检测试剂盒），不提供“选择已有设备”或“稍后绑定”，须绑定产品、创建宠物并关联后才能进入 Home。</li>',
     '<li>New users first time can tap "Add Device" in device area to enter new-user binding flow: supports scan binding only (smart device / genetic test kit), no "choose existing device" or "bind later" options; must bind product, create pet and associate before entering Home.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>新增设备仅写入当前浏览器演示数据；参数为协议文档摘要，不连接真实 Broker。</p><p class="from-phone">【手机框迁出】设备在线 / 离线状态为示例，可在设备详情切换；首页状态卡与数值不代表真实检测。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>New device only writes to current browser demo data; parameters are protocol doc summary, no real Broker connection.</p><p class="from-phone">[Moved out of phone frame] Device online/offline status is sample, can be switched in device details; home status card and values do not represent real detection.</p></div>'),
    # ===== health detail =====
    ('<p>按当前宠物展示活动、生命体征、睡眠和消化等健康示例数据，支持进入指标详情和专业报告。</p>',
     '<p>Shows health sample data of activity, vital signs, sleep and digestion by current pet, supports entering metric details and professional reports.</p>'),
    ('<li>选择宠物，切换 Today、7 Days 或指定日期，数据和趋势同步变化。</li>',
     '<li>Select pet, switch Today, 7 Days or specified date, data and trend change accordingly.</li>'),
    ('<li>点击指标卡查看详情；点击报告入口查看当前宠物的专业报告。</li>',
     '<li>Tap metric card to view details; tap report entry to view current pet\'s professional report.</li>'),
    ('<li>点击健康检测观看检测进度，结果回到当前宠物；通过记录和兽医入口进入后续流程。</li>',
     '<li>Tap health detection to view detection progress, result returns to current pet; enter follow-up flow via records and vet entry.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>图表由网页组件绘制，可响应切换；数据为演示数据，不代表真实检测或医学判断。</p><p class="from-phone">【手机框迁出】健康指标与趋势为示例数据，不代表真实检测或医学判断。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Charts drawn by web components, responsive to switching; data is demo data, does not represent real detection or medical judgment.</p><p class="from-phone">[Moved out of phone frame] Health metrics and trends are sample data, do not represent real detection or medical judgment.</p></div>'),
    # ===== ai detail =====
    ('<p>以对话形式演示健康解释、状态查询和养宠建议，当前宠物决定对话上下文。</p>',
     '<p>Demo health explanation, status query and pet care advice in conversation form, current pet determines conversation context.</p>'),
    ('<li>在顶部切换宠物，分别保留各只宠物的对话记录。</li>',
     '<li>Switch pet at top, conversation records of each pet kept separately.</li>'),
    ('<li>输入问题并发送，或点击建议问题，查看基于示例数据生成的预设回复。</li>',
     '<li>Type question and send, or tap suggested question, view preset replies generated based on sample data.</li>'),
    ('<li>点击健康数据、专业报告或在线兽医，继续体验关联流程。</li>',
     '<li>Tap health data, professional report or online vet to continue experiencing linked flow.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>回复来自本地规则和示例模板，没有连接真实 AI 模型；不会发送网络请求。</p><p class="from-phone">【手机框迁出】AI 管家回复来自本地预设规则与模板，没有连接真实 AI 模型，也不会发送网络请求。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Replies come from local rules and sample templates, no real AI model connected; no network requests sent.</p><p class="from-phone">[Moved out of phone frame] AI Butler replies come from local preset rules and templates, no real AI model connected, no network requests sent.</p></div>'),
    # ===== discover detail =====
    ('<p>按评审截图改为搜索栏 + 话题筛选 + 双列瀑布流卡片；卡片统一为图片轮播、标题、两行简述与发布人信息，保留社区浏览、互动、发布和作者主页。</p>',
     '<p>Changed per review screenshot to search bar + topic filter + double-column waterfall cards; cards unified as image carousel, title, two-line summary and publisher info, keeping community browse, interaction, publish and author homepage.</p>'),
    ('<li>顶部搜索栏按标题、副文本、作者与话题实时筛选卡片。</li>',
     '<li>Top search bar filters cards in real time by title, subtitle, author and topic.</li>'),
    ('<li>切换 For You / Following / Health / Training / Nutrition / Care；最右侧圆形按钮打开 Stories 作者列表。</li>',
     '<li>Switch For You / Following / Health / Training / Nutrition / Care; rightmost circular button opens Stories author list.</li>'),
    ('<li>卡片顶部图片有多张时每 3 秒自动轮播并显示指示点；图片下方依次是标题、两行简述、发布人头像与名称及点赞次数。</li>',
     '<li>If multiple images at card top, auto carousel every 3 seconds with indicator dots; below image in order: title, two-line summary, publisher avatar and name, and like count.</li>'),
    ('<li>点击卡片进入帖子详情，支持点赞、收藏、评论、多图切换及话题聚合。</li>',
     '<li>Tap card to enter post details, supports like, favorite, comment, multi-image switch and topic aggregation.</li>'),
    ('<li>右上角加号发布图文，新内容进入信息流与个人主页；底部悬浮胶囊导航切换五个主模块。</li>',
     '<li>Plus at top-right to publish image-text, new content enters feed and personal homepage; bottom floating pill navigation switches five main modules.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>点赞、评论、关注和图文文字保存在当前浏览器；上传图片仅在当前打开会话保留，不会发布到真实社区。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Like, comment, follow and image-text text saved in current browser; uploaded images kept only in current open session, not published to real community.</p></div>'),
    # ===== profile detail =====
    ('<p>沿用当前 Demo 的个人资料、社交统计、宠物入口与内容宫格布局。</p>',
     '<p>Uses current Demo personal info, social stats, pet entry and content grid layout.</p>'),
    ('<li>点击个人资料编辑昵称、所在地和简介，保存后同步展示。</li>',
     '<li>Tap personal info to edit nickname, location and bio, saved and displayed in sync.</li>'),
    ('<li>点击 Posts、Followers、Friends 查看对应列表；切换 Moments、Liked 查看内容。</li>',
     '<li>Tap Posts, Followers, Friends to view corresponding lists; switch Moments, Liked to view content.</li>'),
    ('<li>点击 My pets 管理宠物，点击右上角进入会员或设置中心。</li>',
     '<li>Tap My pets to manage pets, tap top-right to enter membership or settings center.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>示例账号默认 Kevin；社交数据反映当前演示中的内容和互动，不代表真实账号。</p><p class="from-phone">【手机框迁出】会员标识为演示状态，不产生真实订阅或扣款。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Sample account defaults to Kevin; social data reflects current demo content and interaction, does not represent real account.</p><p class="from-phone">[Moved out of phone frame] Membership tag is demo status, no real subscription or charge incurred.</p></div>'),
    # ===== monitor detail =====
    ('<p>历史页面：展示画面区、看护控制及 AI Wellness Snapshot（本期无对应设备）。</p>',
     '<p>History page: shows display area, watch controls and AI Wellness Snapshot (no corresponding device this period).</p>'),
    ('<li>查看示例画面和看护指标；本期无实时看护设备时显示空状态。</li>',
     '<li>View sample display and watch metrics; empty state shown when no real-time watch device this period.</li>'),
    ('<li>点击 Listen、Talk 和 Play Sound，体验按钮状态与控制反馈。</li>',
     '<li>Tap Listen, Talk and Play Sound to experience button status and control feedback.</li>'),
    ('<li>切换检测框显示，查看模拟识别事件；进入宠物语言翻译或返回设备选择。</li>',
     '<li>Switch detection box display, view simulated recognition events; enter pet language translation or return to device selection.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>本期设备仅智能背带与智能狗窝，不含摄像头；本页按历史内容保留，无对应设备时显示空状态。画面使用项目自带照片，不调用摄像头、麦克风或真实视频服务。</p><p class="from-phone">【手机框迁出】实时看护画面与检测事件均为模拟，不调用摄像头、麦克风或真实视频服务；画面为模拟画面。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Devices this period are only Smart Dog Harness and Smart Dog House, no camera; this page kept as historical content, empty state shown when no corresponding device. Display uses project-owned photos, no camera, microphone or real video service called.</p><p class="from-phone">[Moved out of phone frame] Real-time watch display and detection events are all simulated, no camera, microphone or real video service called; display is simulated.</p></div>'),
]

count = 0
miss = 0
for old, new in repls:
    n = t.count(old)
    if n == 0:
        miss += 1
        print('MISS: ' + old[:90])
    else:
        t = t.replace(old, new)
        count += n
        print('{:4d}x  {}'.format(n, old[:60]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(t)

print('\nBatch 2 done: {} replacements, {} missed'.format(count, miss))
