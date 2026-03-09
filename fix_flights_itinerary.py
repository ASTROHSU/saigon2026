import re

with open("index.html", "r") as f:
    html = f.read()

# Flight 1
html = html.replace('1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">07:50</div>', '1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">07:40</div>')
html = html.replace('(建議 05:30 抵達)', '(建議 05:40 抵達)')
html = html.replace('1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">10:15</div>', '1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">10:05</div>')

# Flight 2
html = html.replace('1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">11:15</div>', '1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">18:05</div>')
html = html.replace('>JX712<', '>JX714<')
html = html.replace('1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">15:40</div>', '1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">22:30</div>')

# Overhaul itinerary
new_itinerary = """<!-- Left Column: Scrolling Itinerary -->
                    <div class="itinerary-column">
                        <div class="day-header">
                            <h2>總行程表 <span class="date-badge">五天四夜</span></h2>
                            <p>滑動查看每一天的精彩安排，右側地圖會同步顯示當日路線</p>
                        </div>

                        <!-- Day 1 List -->
                        <div class="day-section" id="day-1-list">
                            <h3 class="day-title" style="margin-top: 1rem; margin-bottom: 0.5rem; color: var(--c-primary); border-bottom: 2px solid var(--c-border); padding-bottom: 0.5rem;">
                                Day 1: 3/29 週日</h3>
                            <div class="daily-events">
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3918.8596645399587!2d106.6625!3d10.816667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175292eb63695d3%3A0xa61c2ccf9b5c2c77!2sTan%20Son%20Nhat%20International%20Airport!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">10:05</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">✈️ 抵達新山一機場</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.2974246851606!2d106.69741!3d10.788544!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0x6bbaabaebe555231!2sLe%20Corto!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-primary);">
                                    <div class="time-col" style="color: var(--c-success);"><span class="time-text">12:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍽️ Le Corto 法式早午餐</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.4602324213753!2d106.69747!3d10.78000!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0xea2df25b90fdb4c6!2sSaigon%20Central%20Post%20Office!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">15:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">📸 百年建築巡禮 & 下午茶</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.000!2d106.699!3d10.778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4ae1b95b85%3A0x1234567890abcdef!2sMiu%20Miu%20Spa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">17:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">💆 Miu Miu Spa 舒壓按摩</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.3!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sPizza%204P%27s!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">19:30</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍕 Pizza 4P's 窯烤披薩</h4></div>
                                </div>
                            </div>
                        </div>

                        <!-- Day 2 List -->
                        <div class="day-section" id="day-2-list">
                            <h3 class="day-title" style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--c-primary); border-bottom: 2px solid var(--c-border); padding-bottom: 0.5rem;">
                                Day 2: 3/30 週一</h3>
                            <div class="daily-events">
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.500!2d106.695!3d10.772!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f3f1b95b85%3A0x9876543210fedcba!2sBanh%20Mi%20Huynh%20Hoa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">09:30</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🥖 Bánh Mì Huỳnh Hoa</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.4!2d106.69!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sWar%20Remnants%20Museum!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">11:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🏛️ 戰爭遺跡博物館</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.8!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sThe%20Cafe%20Apartment!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">15:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">☕ 咖啡公寓與步行街</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.9!2d106.70!3d10.76!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sVinh%20Khanh%20Street!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">19:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍻 永慶街 越式熱炒海鮮</h4></div>
                                </div>
                            </div>
                        </div>

                        <!-- Day 3 List -->
                        <div class="day-section" id="day-3-list">
                            <h3 class="day-title" style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--c-primary); border-bottom: 2px solid var(--c-border); padding-bottom: 0.5rem;">
                                Day 3: 3/31 週二</h3>
                            <div class="daily-events">
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.3!2d106.69!3d10.79!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sTan%20Dinh%20Church!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">09:30</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">⛪ 粉紅教堂 & 生牛河粉</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.7!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sSaigon%20Zoo!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-primary);">
                                    <div class="time-col" style="color: var(--c-success);"><span class="time-text">13:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍽️ Cocotte 法式小館</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.8!2d106.70!3d10.78!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sMiu%20Miu%20Spa%201!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">16:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">☕ 動植物園散步 & SPA</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.9!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sSol%20Kitchen!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">19:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🌮 Sol Kitchen 拉丁美洲餐酒館</h4></div>
                                </div>
                            </div>
                        </div>

                        <!-- Day 4 List -->
                        <div class="day-section" id="day-4-list">
                            <h3 class="day-title" style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--c-primary); border-bottom: 2px solid var(--c-border); padding-bottom: 0.5rem;">
                                Day 4: 4/1 週三</h3>
                            <div class="daily-events">
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.0!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sAu%20Parc!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">10:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍳 澳式早午餐 & 安東市場</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.4!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sMiu%20Miu%20Spa!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">14:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">💇‍♀️ 越式洗頭體驗 & 按摩</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.5!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sHoa%20Tuc!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">18:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🌺 Hoa Túc 網美越式料理</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.6!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBlank%20Lounge!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">21:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🍸 高空酒吧 Blank Lounge</h4></div>
                                </div>
                            </div>
                        </div>

                        <!-- Day 5 List -->
                        <div class="day-section" id="day-5-list">
                            <h3 class="day-title" style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--c-primary); border-bottom: 2px solid var(--c-border); padding-bottom: 0.5rem;">
                                Day 5: 4/2 週四</h3>
                            <div class="daily-events">
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.7!2d106.70!3d10.77!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f4!2sBen%20Thanh%20Market!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px; border-left: 4px solid var(--c-text-muted);">
                                    <div class="time-col"><span class="time-text">10:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🛍️ 最後採買 & 享受飯店</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.9!2d106.66!3d10.81!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175292!2sTan%20Son%20Nhat%20International%20Airport!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">14:00</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">🚕 出發前往機場</h4></div>
                                </div>
                                <div class="event-card" data-map-src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3921.9!2d106.66!3d10.81!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175292!2sTan%20Son%20Nhat%20International%20Airport!5e0!3m2!1sen!2stw!4v1709876543210!5m2!1sen!2stw" style="background: var(--c-bg-glass); border-radius: 12px;">
                                    <div class="time-col"><span class="time-text">18:05</span></div>
                                    <div class="event-details"><h4 style="margin:0; font-size: 1rem;">✈️ JX714 滿載回憶返台</h4></div>
                                </div>
                            </div>
                        </div>

                    </div>"""

# Replace the old itinerary-column with the new one
old_itinerary_pattern = r'<!-- Left Column: Scrolling Itinerary -->.*?</div>\s*<!-- Right Column: Map -->'
html = re.sub(old_itinerary_pattern, new_itinerary + '\n\n                    <!-- Right Column: Map -->', html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)
print("Updated flights and rewrote itinerary list exactly.")
