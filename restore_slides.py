import re

with open("index.html", "r") as f:
    html = f.read()

restored_slides = """        <!-- Slide 1: Hero -->
        <section class="slide">
            <div class="content-wrapper">
                <div class="hero-content" style="margin-bottom: 2rem;">
                    <h1>2026 越南胡志明蜜月旅行 🇻🇳</h1>
                    <p>3 月 29 日 - 4 月 2 日 · 五天四夜專屬精緻探索</p>
                </div>
            </div>
        </section>

        <!-- Slide 2: Transportation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>✈️ 航班資訊</h2>
                    <p>星宇航空，舒適開啟蜜月之旅</p>
                </div>
                <div class="hero-cards" style="flex-direction: column; align-items: center; max-width: 850px; margin: 0 auto; gap: 2rem;">
                    
                    <!-- Compact Boarding Pass 1 -->
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

        <!-- Slide 3: Accommodation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>🏨 住宿：城市中心的綠洲</h2>
                    <p>Signature by M Village Hai Bà Trưng</p>
                </div>
                <div class="split-layout"
                    style="grid-template-columns: 1fr 1fr; gap: 2rem; max-width: 1000px; margin: 0 auto; align-items: stretch;">
                    <div class="glass-card"
                        style="padding: 2rem; display: flex; flex-direction: column; justify-content: center; text-align: left;">
                        <h3 style="font-size: 1.5rem; color: var(--c-primary); margin-bottom: 1.5rem;">為什麼選這間做為蜜月住宿？
                        </h3>
                        <p style="margin-bottom: 1rem; line-height: 1.6; font-size: 1.05rem;">
                            <strong>📍 旺中帶靜：</strong> 位於熱鬧的第一郡邊緣（第三郡交界），既能享受市區的便利，又不用忍受市區中央的吵雜。<br><br>
                            <strong>🚶 綠意與地標：</strong> 每天早上出門，正前方就是佔地廣闊的黎文八綠地公園；走路 2 分鐘就能抵達著名的「粉紅教堂」。<br><br>
                            <strong>✨ 質感空間：</strong> M Village 系列以充滿熱帶植栽和現代極簡的設計聞名，是非常適合情侶放鬆、拍照的唯美空間。
                        </p>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div class="glass-card"
                            style="padding: 0; border-radius: 16px; overflow: hidden; height: 200px;">
                            <img src="https://l.urusai.cc/VGMW2.png" alt="Signature by M Village Room"
                                style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="glass-card"
                            style="padding: 0; border-radius: 16px; overflow: hidden; height: 200px;">
                            <img src="https://l.urusai.cc/qdPcb.png" alt="Signature by M Village Pool/Exterior"
                                style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Slide 4: Dining -->
"""

# The file currently has <!-- Slide 1: Hero & Todo --> directly followed by the Dining highlight `<section class="slide">`.
# I will replace `        <!-- Slide 1: Hero & Todo -->\n        <section class="slide">`
# with the restored content plus the start of Slide 4.
pattern = r'        <!-- Slide 1: Hero & Todo -->\n        <section class="slide">'
replacement = restored_slides + '        <section class="slide">'

if '<!-- Slide 1: Hero & Todo -->' in html:
    html = html.replace('        <!-- Slide 1: Hero & Todo -->\n        <section class="slide">', replacement)

with open("index.html", "w") as f:
    f.write(html)
print("Slides restored successfully!")
