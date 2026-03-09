import re

with open("index.html", "r") as f:
    content = f.read()

# Extract header and container start
head_match = re.search(r'(.*?<div class="presentation-container">)', content, flags=re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract tail
tail_match = re.search(r'(</div>\s*<!-- Navigation Controls -->.*)', content, flags=re.DOTALL)
tail = tail_match.group(1) if tail_match else ""

slide1_hero = """
        <!-- Slide 1: Hero & Todo -->
        <section class="slide">
            <div class="content-wrapper">
                <div class="hero-content" style="margin-bottom: 2rem;">
                    <h1>2026 越南胡志明蜜月旅行 🇻🇳</h1>
                    <p>3 月 29 日 - 4 月 2 日 · 五天四夜專屬精緻探索</p>
                </div>
                
                <div style="max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); padding: 2rem; border-radius: 20px; border: 1px solid var(--c-border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <h3 style="color: var(--c-primary); margin-bottom: 1.5rem;"><i class="fa-solid fa-list-check"></i> 行前待辦事項</h3>
                    <ul style="list-style: none; padding: 0; text-align: left;">
                        <li style="margin-bottom: 1rem; display: flex; align-items: center; font-size: 1.1rem;"><input type="checkbox" style="margin-right: 15px; width: 20px; height: 20px;"> 辦理越南電子簽證 (e-Visa)</li>
                        <li style="margin-bottom: 1rem; display: flex; align-items: center; font-size: 1.1rem;"><input type="checkbox" style="margin-right: 15px; width: 20px; height: 20px;"> 預訂機場來回接駁車</li>
                        <li style="margin-bottom: 1rem; display: flex; align-items: center; font-size: 1.1rem;"><input type="checkbox" style="margin-right: 15px; width: 20px; height: 20px;"> 預訂 Pizza 4P's 與 Le Corto</li>
                        <li style="margin-bottom: 1rem; display: flex; align-items: center; font-size: 1.1rem;"><input type="checkbox" style="margin-right: 15px; width: 20px; height: 20px;"> 購買網卡 (eSIM)</li>
                        <li style="margin-bottom: 1rem; display: flex; align-items: center; font-size: 1.1rem;"><input type="checkbox" style="margin-right: 15px; width: 20px; height: 20px;"> 預約 Miu Miu Spa 療程</li>
                    </ul>
                </div>
            </div>
        </section>
"""

slide2_transport = """
        <!-- Slide 2: Transportation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>✈️ 交通資訊</h2>
                    <p>精選星宇航空，舒適開啟蜜月之旅</p>
                </div>
                <div class="hero-cards">
                    <div class="glass-card info-card">
                        <div class="icon-wrapper">
                            <i class="fa-solid fa-plane-departure"></i>
                        </div>
                        <div class="info-text">
                            <span class="label">去程航班 (台灣桃園 TPE → 胡志明 SGN)</span>
                            <span class="value">星宇航空 JX711</span>
                            <span class="sub-value">07:50 起飛 · 10:15 抵達<br><strong style="color: var(--c-primary);">💡 建議 05:30 抵達桃機</strong></span>
                        </div>
                    </div>
                    <div class="glass-card info-card">
                        <div class="icon-wrapper">
                            <i class="fa-solid fa-plane-arrival"></i>
                        </div>
                        <div class="info-text">
                            <span class="label">回程航班 (胡志明 SGN → 台灣桃園 TPE)</span>
                            <span class="value">星宇航空 JX712</span>
                            <span class="sub-value">11:15 起飛 · 15:40 抵達<br>滿載回憶的返家之路</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

slide3_accom = """
        <!-- Slide 3: Accommodation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>🏨 住宿企劃</h2>
                    <p>隱身於繁華邊緣的高質感綠洲</p>
                </div>
                <div class="glass-card info-card" style="max-width: 800px; margin: 0 auto; text-align: left;">
                    <h3 style="font-size: 1.5rem; color: var(--c-primary); margin-bottom: 1rem;">Signature by M Village Hai Bà Trưng</h3>
                    <p style="margin-bottom: 1rem; line-height: 1.6;">
                        <strong>📍 絕佳的地理位置：</strong> 位於第三郡與第一郡交界，旺中帶靜。<br>
                        <strong>🚶 散步綠地：</strong> 正前方就是黎文八綠地公園，走路 2 分鐘直達超有名的「粉紅教堂」。<br>
                        <strong>🚗 出入方便：</strong> 去機場或市區熱門景點（如大劇院、郵局）叫 Grab 都在 10 多分鐘內。<br>
                        <strong>✨ 住宿風格：</strong> 充滿熱帶植栽的現代極簡風設計，非常適合情侶蜜月放鬆。
                    </p>
                    <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=800&auto=format&fit=crop" style="width: 100%; border-radius: 10px; margin-top: 1rem;" alt="Hotel Preview">
                </div>
            </div>
        </section>
"""

slide4_dining = """
        <!-- Slide 4: Dining -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>🍽️ 必吃餐飲亮點</h2>
                    <p>為妳預訂的重點大餐，極致的味蕾享受</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1590846406792-0adc7f928f1d?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">法式奢華早午餐</span>
                            <h3>Le Corto Sunday Brunch</h3>
                            <p>抵達第一天的華麗開場！總統級主廚法式吃到飽早午餐，生蠔與精緻法餐的完美結合。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">傳奇窯烤披薩</span>
                            <h3>Pizza 4P's</h3>
                            <p>日本職人經營，隱藏巷弄的極致美味。必吃自製布拉塔起司生火腿披薩，體驗亞洲最強披薩。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1559847127-ec14eebbba3f?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">越式街頭熱炒</span>
                            <h3>Vĩnh Khánh 永慶街</h3>
                            <p>全球最酷街道之一！坐在路邊吹風、喝啤酒，體驗高低層次豐富的螺肉與熱炒海鮮。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1594246830760-441d6363c375?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">高 CP 法國小館</span>
                            <h3>Cocotte 法式餐酒館</h3>
                            <p>重溫記憶中的味道！隱身檳城市場旁，必點經典油封鴨腿與洋蔥湯，享受道地氛圍。</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

slide5_activities = """
        <!-- Slide 5: Activities -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>✨ 特色遊玩</h2>
                    <p>深度感受西貢的歷史魅力與放鬆日常</p>
                </div>
                <div class="bento-grid">
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1542646279-992a7e44a706?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">網美地標</span>
                            <h3>百年法式建築群</h3>
                            <p>散步於綠意盎然的街道，欣賞夢幻粉紅教堂、壯麗聖母院及百年郵政局的建築之美。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">舒壓首選</span>
                            <h3>Miu Miu Spa 全身按摩</h3>
                            <p>胡志明頂級日系連鎖 SPA！安排了多天的療程，逛街逛累了就來鬆一下筋骨，寵愛自己。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1681284710186-b41e8c78c3c4?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">文化走讀</span>
                            <h3>戰爭遺跡博物館</h3>
                            <p>深刻了解越南歷史的必去展覽，真實展現越戰紀錄，震撼且發人深省。</p>
                        </div>
                    </div>
                    <div class="bento-item glass-card" style="--bg-url: url('https://images.unsplash.com/photo-1603598516480-45ff3b8606ab?q=80&w=600&auto=format&fit=crop');">
                        <div class="bento-overlay"></div>
                        <div class="bento-content">
                            <span class="tag">越夜越美麗</span>
                            <h3>咖啡公寓與步行街</h3>
                            <p>穿梭於九層樓的文創咖啡公寓，晚上再來 Bùi Viện 碧文街感受狂熱的當地夜生活。</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Slide 6 is the itinerary slide. We will extract it from the existing content.
# It starts at `<section class="slide active" style="overflow-y: auto;">`
slide6_match = re.search(r'(<section class="slide active".*?</section>)', content, flags=re.DOTALL)
if slide6_match:
    slide6_itinerary = slide6_match.group(1).replace('<section class="slide active"', '<section class="slide"')
    # Simplified texts in Slide 6 are already done via regex in the previous python script!
else:
    slide6_itinerary = "<!-- Slide 6 Placeholder -->"

slide7_budget = """
        <!-- Slide 7: Budget -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>💰 花費預算 (兩人)</h2>
                    <p>精打細算的蜜月基金</p>
                </div>
                <div style="max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); padding: 2rem; border-radius: 20px; border: 1px solid var(--c-border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <table style="width: 100%; border-collapse: collapse; text-align: left;">
                        <thead>
                            <tr style="border-bottom: 2px solid var(--c-primary);">
                                <th style="padding: 1rem; color: var(--c-primary); font-size: 1.1rem;">項目 (Item)</th>
                                <th style="padding: 1rem; color: var(--c-primary); font-size: 1.1rem; text-align: right;">概估金額 (NTD)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">✈️ 星宇航空來回機票</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$20,000</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">🏨 飯店住宿 (4晚)</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$9,000</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">🍽️ 重點餐廳 (Le Corto/4P's/Cocotte)</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$8,000</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">🍲 街頭小吃與日常開銷</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$5,000</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">💆 SPA 按摩與門票</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$5,000</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--c-border);">
                                <td style="padding: 1rem;">🚗 當地交通 (Grab/機場接送)</td>
                                <td style="padding: 1rem; text-align: right; font-weight: 600;">$3,000</td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td style="padding: 1.5rem 1rem; font-size: 1.2rem; font-weight: bold; color: var(--c-primary);">總計 (Total)</td>
                                <td style="padding: 1.5rem 1rem; text-align: right; font-size: 1.5rem; font-weight: bold; color: var(--c-primary);">$50,000</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        </section>
"""

new_content = head + slide1_hero + slide2_transport + slide3_accom + slide4_dining + slide5_activities + slide6_itinerary + slide7_budget + tail

with open("index.html", "w") as f:
    f.write(new_content)
print("Rewrote index.html with 7 slides.")
