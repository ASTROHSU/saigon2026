import re

with open("index.html", "r") as f:
    html = f.read()

# Dictionary of updates for each event card to simplify text and add data-map-src.
# We will find the cards based on their h4 titles.

updates = [
    {
        "title": r"<h4>飛機降落與通關</h4>",
        "desc": r"<p>星宇 JX711 抵達新山一機場</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3918.8596645399587!2d106.6625!3d10.816667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175292eb63695d3%3A0xa61c2ccf9b5c2c77!2sTan%20Son%20Nhat%20International%20Airport!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Le Corto \(Sunday Brunch\)</h4>",
        "desc": r"<p>✨ 總統級主廚的法式吃到飽早午餐。我們在一樓！</p>",
        "new_desc": "<p>法式吃到飽早午餐</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.2974246851606!2d106.69741!3d10.788544!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0x6bbaabaebe555231!2sLe%20Corto!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>西貢中心郵政局 & 聖母聖殿主教座堂</h4>",
        "desc": r"<p>吃飽後散步過來，欣賞百年法式建築與紅教堂廣場。</p>",
        "new_desc": "<p>百年法式建築與紅教堂廣場</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.4602324213753!2d106.69747!3d10.78000!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0xea2df25b90fdb4c6!2sSaigon%20Central%20Post%20Office!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Ivoire Pastry Boutique</h4>",
        "desc": r"<p>胡志明市最美的法式甜點店，必點招牌「酪梨蛋糕」。</p>",
        "new_desc": "<p>法式甜點</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.4752!2d106.698!3d10.781!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTDCsDQ2JzUxLjYiTiAxMDbCsDQxJzUyLjgiRQ!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Miu Miu Spa</h4>",
        "desc": r"<p>超人氣日系連鎖按摩店，逛累了剛好來按全身 90 分鐘。</p>",
        "new_desc": "<p>精油按摩 90 分鐘</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.000!2d106.699!3d10.778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0x1234567890abcdef!2sMiu%20Miu%20Spa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Bánh Mì Huynh Hoa</h4>",
        "desc": r"<p>最強法國麵包！中午吃到飽，晚餐買回飯店輕鬆吃。</p>",
        "new_desc": "<p>知名越式法國麵包</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.500!2d106.695!3d10.772!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f3f1b95b85%3A0x9876543210fedcba!2sBanh%20Mi%20Huynh%20Hoa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
# Day 2
    {
        "title": r"<h4>Xôi Gà Number One <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>在地經典雞肉糯米飯，體驗道地越式早晨。</p>",
        "new_desc": "<p>雞肉糯米飯</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.6!2d106.69!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sXoi%20Ga%20Number%20One!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Bếp Mẹ Ỉn <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>隱身濱城市場旁的米其林必比登推薦！必吃海鮮煎餅與烤肉米線。</p>",
        "new_desc": "<p>越式海鮮煎餅與烤肉米線</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.7!2d106.69!3d10.76!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBep%20Me%20In!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>咖啡公寓 & 阮惠街步行街 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>感受西貢最繁華的步行街，充滿歷史感與文創氣息的九層樓咖啡公寓。</p>",
        "new_desc": "<p>步行逛街與文創咖啡</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.8!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sThe%20Cafe%20Apartment!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>The Workshop Specialty Coffee <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>藏在老公寓頂樓的精品咖啡殿堂，空間超美。</p>",
        "new_desc": "<p>精品咖啡</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.9!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sThe%20Workshop!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>胡志明市大劇院外圍 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>充滿法式風情的劇院廣場，夜晚打燈後非常浪漫。</p>",
        "new_desc": "<p>劇院廣場散步</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.0!2d106.71!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sOpera%20House!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Pizza 4P's \(Lê Thánh Tôn 創始店\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>✨ 日本職人經營的傳奇披薩店。隱藏在巷弄中，必點「自製布拉塔起司火腿披薩」。</p>",
        "new_desc": "<p>窯烤手工披薩</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.1!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sPizza%204P%27s!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Miu Miu Spa 2 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>距離 Pizza 4P's 超級近！吃飽剛好走過去按到開心回飯店睡覺。</p>",
        "new_desc": "<p>精油或泰式按摩</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.2!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sMiu%20Miu%20Spa%202!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
# Day 3
    {
        "title": r"<h4>粉紅教堂 \(新定教堂\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>著名的粉紅浪漫大教堂，趁早上去人比較少，光線也最美。</p>",
        "new_desc": "<p>知名地標拍照</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.3!2d106.69!3d10.79!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sTan%20Dinh%20Church!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Phở Phượng <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>來越南必喝的極致牛骨湯頭，開啟美好的一天。</p>",
        "new_desc": "<p>越南生牛肉河粉</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.4!2d106.69!3d10.79!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sPho%20Phuong!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4 class=\"highlight-text\">Cocotte <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>✨ 重點推薦。我們之前去過的那家超高 CP 值法式巷弄小館！重溫經典油封鴨與洋蔥湯。</p>",
        "new_desc": "<p>法式小館 (鴨腿與洋蔥湯)</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.5!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sCocotte!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Bosgaurus Coffee Roasters <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>✨ \(依照要求提早咖啡時間\) 風格前衛純白的精品咖啡實驗室，品嚐越南頂級咖啡豆。</p>",
        "new_desc": "<p>實驗室風格精品咖啡</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.6!2d106.71!3d10.79!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBosgaurus%20Coffee!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>西貢動植物園周邊 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>喝完咖啡後在市區的大型綠地與歷史博物館外圍散步消化。</p>",
        "new_desc": "<p>綠地與植物園散步</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.7!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sSaigon%20Zoo!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Miu Miu Spa 1 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>這幾天走路走滿多的，晚上去吃海鮮前，先來預約個舒壓精油按摩吧。</p>",
        "new_desc": "<p>按摩放鬆</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.8!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sMiu%20Miu%20Spa%201!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Miu Miu Spa 1 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>✨ 改到距離飯店比較近的 Miu Miu Spa 1。晚餐前先來鬆一下全身！</p>",
        "new_desc": "<p>按摩放鬆</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.8!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sMiu%20Miu%20Spa%201!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Sol Kitchen & Bar <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>評價極高的質感餐廳，大啖碳烤和牛與西班牙海鮮燉飯。</p>",
        "new_desc": "<p>碳烤和牛與餐酒館</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.9!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sSol%20Kitchen!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
# Day 4
    {
        "title": r"<h4>Bò Né Bà Nũi <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>越式鐵板牛柳加蛋，充滿在地活力的早餐。</p>",
        "new_desc": "<p>越式鐵板牛柳加蛋</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.0!2d106.70!3d10.76!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBo%20Ne!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>戰爭遺跡博物館 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>胡志明市最具代表性的歷史博物館，非常值得一看的深刻展覽。</p>",
        "new_desc": "<p>博物館歷史走讀</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.1!2d106.69!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sWar%20Remnants%20Museum!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Nhà Hàng Ngon \(美味餐廳\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>在超美的法式黃色別墅內，一次吃遍全越南的街頭小吃精華。</p>",
        "new_desc": "<p>越南風味小吃集合</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.2!2d106.69!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sNha%20Hang%20Ngon!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4 class=\"highlight-text\">Vĩnh Khánh \(永慶街螺肉海鮮\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>✨ 重點推薦。全球最酷街道之一！坐在路邊吹風、喝啤酒、體驗風味層次超豐富的越式熱炒海鮮。</p>",
        "new_desc": "<p>越式街頭熱炒海鮮</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.3!2d106.70!3d10.75!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sVinh%20Khanh!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Bùi Viện 碧文街 \(西貢酒吧街\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>越夜越熱鬧的背包客街，可以來散步感受一下狂熱的當地夜生活。</p>",
        "new_desc": "<p>酒吧街體驗</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.4!2d106.69!3d10.76!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBui%20Vien!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
# Day 5
    {
        "title": r"<h4>黎文八公園 \(Công Viên Lê Văn Tám\) <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>退房前，最後感受一下在地的悠閒早晨氣氛。</p>",
        "new_desc": "<p>晨間公園悠閒散步</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.5!2d106.69!3d10.79!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sLe%20Van%20Tam%20Park!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>Bánh Mì Hồng Hoa <i class=\"fa-solid fa-arrow-up-right-from-square\"></i>\s*</h4>",
        "desc": r"<p>離開前再試一間超高分法國麵包，看跟第一天吃的那家誰更厲害！</p>",
        "new_desc": "<p>高分越南法國麵包</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.6!2d106.69!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBanh%20Mi%20Hong%20Hoa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4>老賴羊肉火鍋 <i class=\"fa-solid fa-arrow-up-right-from-square\"></i></h4>",
        "desc": r"<p>當地老饕推薦的特色羊肉爐與羊骨髓煎蛋，吃飽飽去機場。</p>",
        "new_desc": "<p>在地老字號羊肉爐</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.7!2d106.68!3d10.76!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sLau%20De%20Lao%20Lai!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    },
    {
        "title": r"<h4 class=\"highlight-text\">抵達新山一機場 <i class=\"fa-solid fa-plane\"></i></h4>",
        "desc": r"<p>滿載美食回憶，搭上星宇航空平安回家。</p>",
        "new_desc": "<p>JX712 起飛返回台北</p>",
        "map_src": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3918.8!2d106.66!3d10.81!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x317529!2sTan%20Son%20Nhat%20Airport!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw"
    }
]

# We need to add data-map-src to the <div class="glass-card event-card"...> that contains the title
for update in updates:
    title_regex = update["title"]
    desc_regex = update["desc"]
    new_desc = update.get("new_desc", "")
    map_src = update["map_src"]
    
    # Simple strategy: find the index of the title, then search backwards for '<div class="glass-card event-card'
    # and insert data-map-src there.
    # Then replace the description.
    
    match = re.search(title_regex, html)
    if match:
        start_idx = match.start()
        # Search backwards for the class
        card_idx = html.rfind('glass-card event-card', 0, start_idx)
        if card_idx != -1:
            # We want to insert data-map-src right before class=
            class_idx = html.rfind('class="', 0, card_idx + 22) # Should find the precise class attribute start
            # Safest is just replacing 'glass-card event-card' with a version that has the data attribute.
            html = html[:card_idx] + f"data-map-src='{map_src}' " + html[card_idx:]
            
        # Optional: Replace description
        if new_desc:
            # We need to find the description which is usually right after the </a> tag. To be precise, we replace
            # within a small window.
            # actually our regex is literal strings we can just sub.
            # but wait, since html was just modified, indices might change. Let's do string replacement for desc.
            pass

# After adding data attributes, let's just do sequential replacements for the descriptions to be safe.
for update in updates:
    if "new_desc" in update:
        html = re.sub(update["desc"], update["new_desc"], html)

with open("index.html", "w") as f:
    f.write(html)
print("Updated event cards with data attributes and new descriptions.")
