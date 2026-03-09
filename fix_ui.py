import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Fix Boarding Passes (Translate to Chinese & Compact)
old_bp_pattern = r'<!-- Realistic Boarding Pass 1 -->.*?<!-- Slide 3: Accommodation -->'
new_bps = """<!-- Compact Boarding Pass 1 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; flex-direction: column; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid var(--c-border); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <!-- Top Header -->
                        <div style="background: var(--c-primary); color: white; padding: 0.5rem 1.5rem; display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-weight: 700; letter-spacing: 1px; font-size: 1rem;"><i class="fa-solid fa-plane"></i> 星宇航空 STARLUX</div>
                            <div style="font-size: 0.8rem; opacity: 0.9; letter-spacing: 1px;">登機證 BOARDING PASS</div>
                        </div>
                        
                        <!-- Main Content -->
                        <div style="display: flex; background: white; flex-wrap: wrap;">
                            <!-- Left Section (Main details) -->
                            <div style="flex: 2; min-width: 280px; padding: 1.5rem; border-right: 2px dashed var(--c-border); display: flex; flex-direction: column;">
                                <!-- Passenger & Flight Info -->
                                <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">旅客姓名 Passenger</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">HSU / MINGEN & SYU / FANGYI</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">航班 Flight</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-primary);">JX 711</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">日期 Date</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">03/29 (週日)</div>
                                    </div>
                                </div>
                                
                                <!-- Route Info -->
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="flex: 1;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">台北 TPE</div>
                                        <div style="font-size: 2rem; font-weight: 900; line-height: 1.1; color: var(--c-text);">07:40</div>
                                        <div style="font-size: 0.8rem; font-weight: 700; color: var(--c-primary);">T2 第一航廈 (等同)</div>
                                    </div>
                                    
                                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted); padding: 0 0.5rem;">
                                        <div style="width: 100%; height: 2px; background: var(--c-border); position: relative; margin: 0.5rem 0;">
                                            <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light); font-size: 1.2rem; background: white; padding: 0 5px;"></i>
                                        </div>
                                        <span style="font-size: 0.7rem;">航程 3H 35M</span>
                                    </div>
                                    
                                    <div style="flex: 1; text-align: right;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">胡志明市 SGN</div>
                                        <div style="font-size: 2rem; font-weight: 900; line-height: 1.1; color: var(--c-text);">10:15</div>
                                        <div style="font-size: 0.8rem; font-weight: 700; color: var(--c-primary);">T2 第二航廈</div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Right Section (Stub) -->
                            <div style="flex: 1; min-width: 150px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; background: rgba(0,0,0,0.02);">
                                <div>
                                    <div style="font-size: 0.7rem; color: var(--c-text-muted);">登機時間 Boarding</div>
                                    <div style="font-weight: 900; font-size: 1.5rem; color: var(--c-primary-light);">07:00</div>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">登機門 Gate</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">TBD</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">座位 Seat</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">TBD</div>
                                    </div>
                                </div>
                                <div style="margin-top: 0.5rem; text-align: center; font-size: 1.5rem; opacity: 0.15; letter-spacing: -2px; overflow: hidden; white-space: nowrap;">
                                    |||||||||||||||||
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Compact Boarding Pass 2 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; flex-direction: column; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid var(--c-border); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <!-- Top Header -->
                        <div style="background: var(--c-primary-light); color: white; padding: 0.5rem 1.5rem; display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-weight: 700; letter-spacing: 1px; font-size: 1rem;"><i class="fa-solid fa-plane"></i> 星宇航空 STARLUX</div>
                            <div style="font-size: 0.8rem; opacity: 0.9; letter-spacing: 1px;">登機證 BOARDING PASS</div>
                        </div>
                        
                        <!-- Main Content -->
                        <div style="display: flex; background: white; flex-wrap: wrap;">
                            <!-- Left Section (Main details) -->
                            <div style="flex: 2; min-width: 280px; padding: 1.5rem; border-right: 2px dashed var(--c-border); display: flex; flex-direction: column;">
                                <!-- Passenger & Flight Info -->
                                <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">旅客姓名 Passenger</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">HSU / MINGEN & SYU / FANGYI</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">航班 Flight</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-primary);">JX 714</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">日期 Date</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">04/02 (週四)</div>
                                    </div>
                                </div>
                                
                                <!-- Route Info -->
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="flex: 1;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">胡志明市 SGN</div>
                                        <div style="font-size: 2rem; font-weight: 900; line-height: 1.1; color: var(--c-text);">18:05</div>
                                        <div style="font-size: 0.8rem; font-weight: 700; color: var(--c-primary);">T2 第二航廈</div>
                                    </div>
                                    
                                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted); padding: 0 0.5rem;">
                                        <div style="width: 100%; height: 2px; background: var(--c-border); position: relative; margin: 0.5rem 0;">
                                            <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light); font-size: 1.2rem; background: white; padding: 0 5px;"></i>
                                        </div>
                                        <span style="font-size: 0.7rem;">航程 3H 30M</span>
                                    </div>
                                    
                                    <div style="flex: 1; text-align: right;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">台北 TPE</div>
                                        <div style="font-size: 2rem; font-weight: 900; line-height: 1.1; color: var(--c-text);">22:35</div>
                                        <div style="font-size: 0.8rem; font-weight: 700; color: var(--c-primary);">T2 第一航廈 (等同)</div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Right Section (Stub) -->
                            <div style="flex: 1; min-width: 150px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; background: rgba(0,0,0,0.02);">
                                <div>
                                    <div style="font-size: 0.7rem; color: var(--c-text-muted);">登機時間 Boarding</div>
                                    <div style="font-weight: 900; font-size: 1.5rem; color: var(--c-primary-light);">17:25</div>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">登機門 Gate</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">TBD</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.7rem; color: var(--c-text-muted);">座位 Seat</div>
                                        <div style="font-weight: 700; font-size: 1rem; color: var(--c-text);">TBD</div>
                                    </div>
                                </div>
                                <div style="margin-top: 0.5rem; text-align: center; font-size: 1.5rem; opacity: 0.15; letter-spacing: -2px; overflow: hidden; white-space: nowrap;">
                                    |||||||||||||||||
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Slide 3: Accommodation -->"""
html = re.sub(old_bp_pattern, new_bps, html, flags=re.DOTALL)


# 2. Fix Dining Highlights (Carousel & Image aspect ratio & Fix text contrast)
dining_pattern = r'<section class="slide">.*?<h2>🍽️ 必吃餐飲亮點</h2>.*?</section>'
new_dining = """<section class="slide">
            <div class="content-wrapper" style="max-width: 100%;">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>🍽️ 必吃餐飲亮點</h2>
                    <p>左右滑動查看為妳預訂的重點大餐，極致的味蕾享受</p>
                </div>
                
                <!-- Horizontal Carousel Container -->
                <div class="carousel-container" style="display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 1.5rem; padding: 1rem 5vw 2rem 5vw; width: 100vw; -webkit-overflow-scrolling: touch;">
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: #eee; margin-bottom: 1rem;">
                            <img src="https://l.urusai.cc/Alsuk.png" alt="Le Corto" style="width: 100%; height: auto; object-fit: contain; aspect-ratio: 4/3; display: block;">
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">法式奢華早午餐</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">Le Corto Sunday Brunch</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">抵達第一天的華麗開場！總統級主廚法式吃到飽早午餐，生蠔與精緻法餐的完美結合。</p>
                        </div>
                    </div>
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: #eee; margin-bottom: 1rem;">
                            <img src="https://i.urusai.cc/kRRKQ.png" alt="Pizza 4P's" style="width: 100%; height: auto; object-fit: contain; aspect-ratio: 4/3; display: block;">
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">傳奇窯烤披薩</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">Pizza 4P's</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">日本職人經營，隱藏巷弄的極致美味。必吃自製布拉塔起司生火腿披薩，體驗亞洲最強披薩。</p>
                        </div>
                    </div>
                    
                    <!-- NEW ITEM instead of Vinh Khanh -->
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.05); border: 2px dashed var(--c-border); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; aspect-ratio: 4/3;">
                            <div style="text-align: center; color: var(--c-text-muted); opacity: 0.6;">
                                <i class="fa-solid fa-camera" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                                <div style="font-size: 0.8rem;">請在此放入真實照片</div>
                            </div>
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">知名越式法國麵包</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">Bánh Mì Huỳnh Hoa</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">胡志明市最知名的法國麵包排隊名店！香酥法國麵包夾著滿滿的紮實火腿肉凍與特製肝醬。</p>
                        </div>
                    </div>
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: #eee; margin-bottom: 1rem;">
                            <img src="https://l.urusai.cc/2vCOE.png" alt="Cocotte 法式餐酒館" style="width: 100%; height: auto; object-fit: contain; aspect-ratio: 4/3; display: block;">
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">高 CP 法國小館</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">Cocotte 法式餐酒館</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">重溫記憶中的味道！隱身檳城市場旁，必點經典油封鴨腿與洋蔥湯，享受道地氛圍。</p>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""
html = re.sub(dining_pattern, new_dining, html, flags=re.DOTALL)


# 3. Fix Activities Highlights
activities_pattern = r'<section class="slide">\s*<div class="content-wrapper">\s*<div style="text-align: center; margin-bottom: 2rem;">\s*<h2>✨ 特色遊玩</h2>.*?</div>\s*</div>\s*</section>'
new_activities = """<section class="slide">
            <div class="content-wrapper" style="max-width: 100%;">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>✨ 特色遊玩</h2>
                    <p>左右滑動深度感受西貢的歷史魅力與放鬆日常</p>
                </div>
                
                <!-- Horizontal Carousel Container -->
                <div class="carousel-container" style="display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 1.5rem; padding: 1rem 5vw 2rem 5vw; width: 100vw; -webkit-overflow-scrolling: touch;">
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.05); border: 2px dashed var(--c-border); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; aspect-ratio: 4/3;">
                            <div style="text-align: center; color: var(--c-text-muted); opacity: 0.6;">
                                <i class="fa-solid fa-camera" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                                <div style="font-size: 0.8rem;">請在此放入真實照片</div>
                            </div>
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">網美地標</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">百年法式建築群</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">散步於綠意盎然的街道，欣賞夢幻粉紅教堂、壯麗聖母院及百年郵政局的建築之美。</p>
                        </div>
                    </div>
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.05); border: 2px dashed var(--c-border); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; aspect-ratio: 4/3;">
                            <div style="text-align: center; color: var(--c-text-muted); opacity: 0.6;">
                                <i class="fa-solid fa-camera" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                                <div style="font-size: 0.8rem;">請在此放入真實照片</div>
                            </div>
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">舒壓首選</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">Miu Miu Spa 頂級按摩</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">連續三天安排不同的放鬆療程！從日式指壓到精油按摩，徹底洗滌身心疲憊。</p>
                        </div>
                    </div>
                    
                    <div class="bento-item glass-card" style="flex: 0 0 320px; scroll-snap-align: center; display: flex; flex-direction: column; padding: 1rem; border-radius: 16px; background: white;">
                        <div style="width: 100%; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.05); border: 2px dashed var(--c-border); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; aspect-ratio: 4/3;">
                            <div style="text-align: center; color: var(--c-text-muted); opacity: 0.6;">
                                <i class="fa-solid fa-camera" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                                <div style="font-size: 0.8rem;">請在此放入真實照片</div>
                            </div>
                        </div>
                        <div style="color: var(--c-text); padding: 0 0.5rem;">
                            <span style="display: inline-block; background: var(--c-tag-bg); color: var(--c-primary); font-size: 0.75rem; font-weight: bold; padding: 0.35rem 0.85rem; border-radius: 100px; margin-bottom: 0.5rem;">越夜越美麗</span>
                            <h3 style="color: var(--c-primary-light); font-size: 1.3rem;">高空酒吧與步行街</h3>
                            <p style="font-size: 0.95rem; line-height: 1.5; color: var(--c-text-muted);">穿梭於九層樓的文創咖啡公寓，晚上前往 Blank Lounge 俯瞰繁華浪漫的西貢夜景。</p>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>"""
html = re.sub(activities_pattern, new_activities, html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)
print("Updated Boarding Passes and Bento-Grid Carousels.")
