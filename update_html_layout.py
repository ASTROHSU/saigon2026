import re

with open("index.html", "r") as f:
    html = f.read()

# Slide 2: Transportation Redesign
slide2_old = re.search(r'<!-- Slide 2: Transportation -->(.*?)</section>', html, flags=re.DOTALL)
slide2_new = """<!-- Slide 2: Transportation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2>✈️ 航班資訊</h2>
                    <p>星宇航空，舒適開啟蜜月之旅</p>
                </div>
                <div class="hero-cards" style="flex-direction: column; align-items: center; max-width: 700px; margin: 0 auto;">
                    
                    <!-- Boarding Pass 1 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; border-radius: 16px; overflow: hidden; position: relative;">
                        <!-- Left stub -->
                        <div style="background: var(--c-primary); color: white; padding: 2rem; width: 130px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-right: 2px dashed rgba(255,255,255,0.5);">
                            <i class="fa-solid fa-plane-departure" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                            <span style="font-size: 0.9rem; font-weight: bold;">去程</span>
                            <span style="font-size: 0.8rem; opacity: 0.8;">Departure</span>
                        </div>
                        <!-- Right main -->
                        <div style="padding: 2rem; flex: 1; display: flex; align-items: center; justify-content: space-between;">
                            <div>
                                <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">TAIPEI</div>
                                <div style="font-size: 2.5rem; font-weight: 900; line-height: 1;">TPE</div>
                                <div style="font-size: 1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">07:50</div>
                                <div style="font-size: 0.8rem; color: var(--c-text-muted);">(建議 05:30 抵達)</div>
                            </div>
                            
                            <div style="display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted);">
                                <span style="font-size: 0.8rem; font-weight: 700;">JX711</span>
                                <div style="width: 80px; height: 2px; background: var(--c-border); margin: 0.5rem 0; position: relative;">
                                    <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light);"></i>
                                </div>
                                <span style="font-size: 0.75rem;">3h 25m</span>
                            </div>
                            
                            <div style="text-align: right;">
                                <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">HO CHI MINH</div>
                                <div style="font-size: 2.5rem; font-weight: 900; line-height: 1;">SGN</div>
                                <div style="font-size: 1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">10:15</div>
                            </div>
                        </div>
                    </div>

                    <!-- Boarding Pass 2 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; border-radius: 16px; overflow: hidden; position: relative;">
                        <!-- Left stub -->
                        <div style="background: var(--c-primary-light); color: white; padding: 2rem; width: 130px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-right: 2px dashed rgba(255,255,255,0.5);">
                            <i class="fa-solid fa-plane-arrival" style="font-size: 2rem; margin-bottom: 0.5rem;"></i>
                            <span style="font-size: 0.9rem; font-weight: bold;">回程</span>
                            <span style="font-size: 0.8rem; opacity: 0.8;">Return</span>
                        </div>
                        <!-- Right main -->
                        <div style="padding: 2rem; flex: 1; display: flex; align-items: center; justify-content: space-between;">
                            <div>
                                <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">HO CHI MINH</div>
                                <div style="font-size: 2.5rem; font-weight: 900; line-height: 1;">SGN</div>
                                <div style="font-size: 1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">11:15</div>
                            </div>
                            
                            <div style="display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted);">
                                <span style="font-size: 0.8rem; font-weight: 700;">JX712</span>
                                <div style="width: 80px; height: 2px; background: var(--c-border); margin: 0.5rem 0; position: relative;">
                                    <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light);"></i>
                                </div>
                                <span style="font-size: 0.75rem;">3h 25m</span>
                            </div>
                            
                            <div style="text-align: right;">
                                <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">TAIPEI</div>
                                <div style="font-size: 2.5rem; font-weight: 900; line-height: 1;">TPE</div>
                                <div style="font-size: 1.2rem; font-weight: 700; color: var(--c-primary); margin-top: 0.5rem;">15:40</div>
                                <div style="font-size: 0.8rem; color: var(--c-text-muted);">滿載回憶</div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""
if slide2_old:
    html = html.replace(slide2_old.group(0), slide2_new)

# Slide 3: Accommodation Redesign
slide3_old = re.search(r'<!-- Slide 3: Accommodation -->(.*?)</section>', html, flags=re.DOTALL)
slide3_new = """<!-- Slide 3: Accommodation -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>🏨 住宿：城市中心的綠洲</h2>
                    <p>Signature by M Village Hai Bà Trưng</p>
                </div>
                <div class="split-layout" style="grid-template-columns: 1fr 1fr; gap: 2rem; max-width: 1000px; margin: 0 auto; align-items: stretch;">
                    <div class="glass-card" style="padding: 2rem; display: flex; flex-direction: column; justify-content: center; text-align: left;">
                        <h3 style="font-size: 1.5rem; color: var(--c-primary); margin-bottom: 1.5rem;">為什麼選這裡做為蜜月住宿？</h3>
                        <p style="margin-bottom: 1rem; line-height: 1.6; font-size: 1.05rem;">
                            <strong>📍 旺中帶靜：</strong> 位於熱鬧的第一郡邊緣（第三郡交界），既能享受市區的便利，又不用忍受市區中央的吵雜。<br><br>
                            <strong>🚶 綠意與地標：</strong> 每天早上出門，正前方就是佔地廣闊的黎文八綠地公園；走路 2 分鐘就能抵達著名的「粉紅教堂」。<br><br>
                            <strong>✨ 質感空間：</strong> M Village 系列以充滿熱帶植栽和現代極簡的設計聞名，是非常適合情侶放鬆、拍照的唯美空間。
                        </p>
                    </div>
                    <div class="glass-card" style="padding: 0; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.03); border: 2px dashed var(--c-border); border-radius: 16px; min-height: 300px;">
                        <div style="text-align: center; color: var(--c-text-muted);">
                            <i class="fa-solid fa-image" style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.5;"></i>
                            <p>【請在此放入飯店真實照片】</p>
                        </div>
                        <!-- TODO: Insert actual hotel <img> here instead of the placeholder div -->
                    </div>
                </div>
            </div>
        </section>"""
if slide3_old:
    html = html.replace(slide3_old.group(0), slide3_new)

# Sub Slide 4 & 5 (Dining & Activities) Background Removal & Placeholder insertion
# We will do a generic replacement for bento items
# Find all style="--bg-url: url('...');" and remove them
html = re.sub(r'style="--bg-url: url\([^)]+\);"|style="--bg-url: url\(&#39;.*?&#39;\);"', 'style="background: var(--c-bg-glass);"', html)
# Add placeholder box to each bento item content
placeholder_html = """
                            <div style="margin-top: 1rem; background: rgba(0,0,0,0.05); border: 1px dashed var(--c-text-muted); padding: 1rem; text-align: center; border-radius: 8px;">
                                <i class="fa-solid fa-camera" style="opacity: 0.5;"></i> <span style="font-size: 0.8rem; opacity: 0.7;">請在此放入真實照片</span>
                            </div>
"""
# Since we replaced the images and the background was dark before, let's fix the bento text color in CSS instead, 
# or just change .bento-content text color inline where we see bento-content since it's now a light background instead of image.
html = html.replace('<div class="bento-content">', '<div class="bento-content" style="color: var(--c-text);">' + placeholder_html)
html = html.replace('<div class="bento-overlay"></div>', '') # Remove dark overlay

# Fix Slide 6 scrolling.
html = html.replace('<section class="slide" style="overflow-y: auto;">', '<section class="slide">')

with open("index.html", "w") as f:
    f.write(html)
print("Updated Slides 2, 3, 4, 5, 6 UI elements.")
