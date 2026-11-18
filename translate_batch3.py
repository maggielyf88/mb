with open('index.html', 'r', encoding='utf-8') as f:
    t = f.read()

repls = [
    # ===== pets =====
    ('<!-- ===== 我的宠物 · 宠物列表：修改以下文字即可 ===== -->', '<!-- ===== My pets · Pet list: Edit text below ===== -->'),
    ('<h2>我的宠物 · 宠物列表</h2>', '<h2>My pets · Pet list</h2>'),
    ('<p class="lead">管理每一位家庭成员。</p>', '<p class="lead">Manage every family member.</p>'),
    ('<p>显示当前演示账号的宠物，连接宠物详情、建档和关联设备。</p>', '<p>Shows pets of current demo account, connects pet details, profile creation and device linking.</p>'),
    ('<li>点击宠物卡查看详情；点击添加宠物填写资料。</li>', '<li>Tap pet card to view details; tap Add pet to fill in info.</li>'),
    ('<li>新增、编辑或删除后，首页和健康页的宠物选择同步更新。</li>', '<li>After add, edit or delete, pet selection on Home and Health pages updates in sync.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>宠物资料保存在当前浏览器；删除前需要确认，并解除演示设备关联。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Pet info saved in current browser; confirmation needed before delete, and demo device link removed.</p></div>'),
    # ===== pet-edit =====
    ('<!-- ===== 宠物建档 · 新增与编辑：修改以下文字即可 ===== -->', '<!-- ===== Pet profile · Add & edit: Edit text below ===== -->'),
    ('<h2>宠物建档 · 新增与编辑</h2>', '<h2>Pet profile · Add & edit</h2>'),
    ('<p class="lead">按评审截图重建的 Add Pet 表单。</p>', '<p class="lead">Add Pet form rebuilt per review screenshot.</p>'),
    ('<p>改为 3 个标签卡的分步流程：① Connect device（扫码绑定 / 选择已有设备 / 暂不绑定）；② Pet profile（犬种照片+名称选择、两列 10 字段、新增下次疫苗接种时间）；③ Photos（8 角度照片）→ 完成提示 → 进入 Home。顶部标签卡可点击回跳。</p>',
     '<p>Changed to 3-tab step wizard: ① Connect device (scan bind / choose existing device / bind later); ② Pet profile (breed photo + name select, two-column 10 fields, added next vaccination time); ③ Photos (8 angle photos) → done hint → enter Home. Top tabs clickable to jump back.</p>'),
    ('<li>步骤①：选 Scan 后点 Scan QR code 自动填入示例 IMEI；标题与说明已改为“Scan a device or genetic test box”，可扫描设备或基因检测盒子；选 Use an existing device 从下拉挑设备，若设备已绑定其他宠物会弹窗询问是否变更主人；也可选 I'll link a device later 跳过。</li>',
     '<li>Step ①: choose Scan then tap Scan QR code to auto-fill sample IMEI; title and desc changed to "Scan a device or genetic test box", can scan device or genetic test box; choose Use an existing device to pick from dropdown, if device already bound to other pet a dialog asks whether to change owner; also can choose I'll link a device later to skip.</li>'),
    ('<li>步骤②：点“小型 / 中型 / 大型”快速筛选可切换相关尺寸的犬种卡片；点犬种照片卡自动填入 Breed；字段校验宠物名与体重必填。</li>',
     '<li>Step ②: tap Small / Medium / Large quick filter to switch breed cards of corresponding size; tap breed photo card to auto-fill Breed; field validation requires Pet name and Weight.</li>'),
    ('<li>步骤③：点击虚线照片框选本地图片预览；新建时必须凑齐 8 张才能保存，编辑已有宠物时不重复要求。</li>',
     '<li>Step ③: tap dashed photo box to select local image for preview; new pet must have all 8 photos to save, editing existing pet does not repeat requirement.</li>'),
    ('<li>Save & Finish 后显示 All set! 完成页，点 Go to Home 进入首页；设备绑定/主人变更在保存时生效。</li>',
     '<li>After Save & Finish shows All set! done page, tap Go to Home to enter Home; device binding / owner change takes effect on save.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>照片仅保存在当前浏览器会话，使用 blob URL 预览，不上传服务器；犬种照片使用现有示例狗图，仅用于演示选择交互。App 内文案按项目约定使用英文，参考截图为中文界面。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Photos only saved in current browser session, preview via blob URL, not uploaded to server; breed photos use existing sample dog images, for demo selection interaction only. App text follows project convention in English, reference screenshot is Chinese UI.</p></div>'),
    # ===== pet-detail =====
    ('<!-- ===== 宠物详情：修改以下文字即可 ===== -->', '<!-- ===== Pet details: Edit text below ===== -->'),
    ('<h2>宠物详情</h2>', '<h2>Pet details</h2>'),
    ('<p class="lead">围绕一只宠物查看资料和设备。</p>', '<p class="lead">View info and devices around one pet.</p>'),
    ('<p>聚合宠物基础信息、健康记录、关联设备与编辑入口。关联设备按该宠物过滤：Lucky 2 台、Milo 1 台、Coco 无设备（显示 No devices linked yet.）。</p>',
     '<p>Aggregates pet basic info, health records, linked devices and edit entry. Linked devices filtered by this pet: Lucky 2 units, Milo 1 unit, Coco no devices (shows No devices linked yet.).</p>'),
    ('<li>编辑资料、进入健康页、查看健康记录。</li>', '<li>Edit info, enter health page, view health records.</li>'),
    ('<li>Genetic Test：跟踪基因检测并在线查看报告；Vaccination records：查看接种记录与下次接种时间。</li>',
     '<li>Genetic Test: track genetic test and view report online; Vaccination records: view vaccination records and next vaccination time.</li>'),
    ('<li>点击关联设备查看详情；删除宠物前确认，删除后回到宠物列表。</li>',
     '<li>Tap linked device to view details; confirm before delete pet, returns to pet list after delete.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>切换到该宠物详情时会设置当前宠物，后续健康和 AI 页面沿用该上下文。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Switching to this pet details sets current pet; subsequent Health and AI pages use this context.</p></div>'),
    # ===== records =====
    ('<!-- ===== 健康记录：修改以下文字即可 ===== -->', '<!-- ===== Health records: Edit text below ===== -->'),
    ('<h2>健康记录</h2>', '<h2>Health records</h2>'),
    ('<p class="lead">让每条记录都有对应宠物。</p>', '<p class="lead">Every record has a corresponding pet.</p>'),
    ('<p>按当前宠物展示疫苗及健康记录。</p>', '<p>Shows vaccination and health records by current pet.</p>'),
    ('<li>添加记录，填写名称、日期、下次日期与备注。</li>', '<li>Add record, fill name, date, next date and remarks.</li>'),
    ('<li>编辑或删除已有记录，列表立即更新。</li>', '<li>Edit or delete existing record, list updates immediately.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>记录仅在本地保存，不会同步到医疗或设备系统。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Records saved locally only, not synced to medical or device systems.</p></div>'),
    # ===== record-edit =====
    ('<!-- ===== 新增／编辑健康记录：修改以下文字即可 ===== -->', '<!-- ===== Add/edit health record: Edit text below ===== -->'),
    ('<h2>新增／编辑健康记录</h2>', '<h2>Add / Edit health record</h2>'),
    ('<p class="lead">记录一次接种或健康事件。</p>', '<p class="lead">Record a vaccination or health event.</p>'),
    ('<p>演示健康记录表单和保存流程。</p>', '<p>Demo health record form and save flow.</p>'),
    ('<li>填写记录名称、发生日期、可选的下次日期与备注。</li>', '<li>Fill record name, occurrence date, optional next date and remarks.</li>'),
    ('<li>校验日期顺序，保存后返回当前宠物的健康记录列表。</li>', '<li>Validate date order, after save returns to current pet's health record list.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>所填信息仅属于当前选中宠物。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Filled info belongs only to currently selected pet.</p></div>'),
    # ===== genetic =====
    ('<!-- ===== Genetic Test：修改以下文字即可 ===== -->', '<!-- ===== Genetic Test: Edit text below ===== -->'),
    ('<h2>Genetic Test 基因检测</h2>', '<h2>Genetic Test</h2>'),
    ('<p class="lead">扫码试剂盒，跟踪检测状态，在线查看报告。</p>', '<p class="lead">Scan kit, track detection status, view report online.</p>'),
    ('<p>按当前宠物展示基因检测记录，状态分为 Sample submitted（送检中）、Testing in progress（检测中，只读）、Report ready（报告可查看）。</p>',
     '<p>Shows genetic test records by current pet, status divided into Sample submitted (submitted), Testing in progress (testing, read-only), Report ready (report viewable).</p>'),
    ('<li>Add Genetic Test：扫码 → 宠物基本信息（可编辑）→ 确认生成送检中记录。</li>',
     '<li>Add Genetic Test: scan → Pet basic info (editable) → confirm to generate submitted record.</li>'),
    ('<li>送检中可录入物流单号；检测中不可编辑；报告就绪后可在线查看 Genetic Test Report。</li>',
     '<li>Submitted status can enter tracking number; Testing status not editable; after Report ready can view Genetic Test Report online.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>两个 Simulate 按钮用于演示状态流转，非真实送检；数据仅本地保存。报告为示例，不构成医疗诊断。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Two Simulate buttons for demo status transition, not real submission; data saved locally only. Report is sample, does not constitute medical diagnosis.</p></div>'),
    # ===== genetic-new =====
    ('<!-- ===== New Genetic Test：修改以下文字即可 ===== -->', '<!-- ===== New Genetic Test: Edit text below ===== -->'),
    ('<h2>新增 Genetic Test</h2>', '<h2>New Genetic Test</h2>'),
    ('<p class="lead">两步完成送检登记。</p>', '<p class="lead">Complete submission registration in two steps.</p>'),
    ('<p>第一步 Scan kit 扫描试剂盒二维码；第二步 Pet info 展示该宠物基本信息并允许编辑。</p>',
     '<p>Step 1 Scan kit scans kit QR code; Step 2 Pet info shows pet basic info and allows editing.</p>'),
    ('<li>点击 Scan QR code 生成试剂盒编号并进入信息确认页。</li>',
     '<li>Tap Scan QR code to generate kit number and enter info confirmation page.</li>'),
    ('<li>核对或修改宠物信息后点 Confirm &amp; create record，生成送检中记录并返回列表。</li>',
     '<li>After check or modify pet info tap Confirm &amp; create record to generate submitted record and return to list.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>扫码为模拟动作，不调用摄像头；试剂盒编号为示例值。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Scan is simulated action, no camera called; kit number is sample value.</p></div>'),
    # ===== genetic-report =====
    ('<!-- ===== Genetic Test Report：修改以下文字即可 ===== -->', '<!-- ===== Genetic Test Report: Edit text below ===== -->'),
    ('<h2>Genetic Test Report 检测报告</h2>', '<h2>Genetic Test Report</h2>'),
    ('<p class="lead">在线查看宠物基因检测报告。</p>', '<p class="lead">View pet genetic test report online.</p>'),
    ('<p>展示品种成分、遗传健康风险与性状三部分，附报告编号与生成日期。</p>',
     '<p>Shows breed composition, genetic health risks and traits three parts, with report number and generation date.</p>'),
    ('<li>从报告就绪的检测记录点 View Genetic Test Report 进入。</li>',
     '<li>From report-ready detection record tap View Genetic Test Report to enter.</li>'),
    ('<li>点 Back to Genetic Test 返回检测列表。</li>', '<li>Tap Back to Genetic Test to return to detection list.</li>'),
    ('<div class="callout"><h3>演示范围</h3><p>报告内容为示例数据，仅供演示，不构成兽医诊断。</p></div>',
     '<div class="callout"><h3>Demo scope</h3><p>Report content is sample data, for demo only, does not constitute vet diagnosis.</p></div>'),
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

print('\nBatch 3 done: {} replacements, {} missed'.format(count, miss))
