import re

with open("index.html", "r") as f:
    html = f.read()

replacement = """<div class="hero-cards" style="flex-direction: column; align-items: center; max-width: 850px; margin: 0 auto; gap: 2rem;">
                    
                    <!-- Realistic Boarding Pass 1 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; flex-direction: column; border-radius: 16px; overflow: hidden; position: relative; border: 1px solid var(--c-border); box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                        <!-- Top Header -->
                        <div style="background: var(--c-primary); color: white; padding: 0.8rem 2rem; display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-weight: 700; letter-spacing: 2px; font-size: 1.1rem;"><i class="fa-solid fa-plane"></i> STARLUX AIRLINES</div>
                            <div style="font-size: 0.8rem; opacity: 0.9; letter-spacing: 1px;">BOARDING PASS</div>
                        </div>
                        
                        <!-- Main Content -->
                        <div style="display: flex; background: white; flex-wrap: wrap;">
                            <!-- Left Section (Main details) -->
                            <div style="flex: 2; min-width: 300px; padding: 2rem; border-right: 2px dashed var(--c-border); display: flex; flex-direction: column;">
                                <!-- Passenger & Flight Info -->
                                <div style="display: flex; justify-content: space-between; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Passenger Name</div>
                                        <div style="font-weight: 700; font-size: 1.05rem; color: var(--c-text);">HSU / MINGEN & SYU / FANGYI</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Flight</div>
                                        <div style="font-weight: 700; font-size: 1.1rem; color: var(--c-primary);">JX 711</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Date</div>
                                        <div style="font-weight: 700; font-size: 1.1rem; color: var(--c-text);">29 MAR</div>
                                    </div>
                                </div>
                                
                                <!-- Route Info -->
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="flex: 1;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">TAIPEI (TPE)</div>
                                        <div style="font-size: 2.5rem; font-weight: 900; line-height: 1.2; color: var(--c-text);">07:40</div>
                                        <div style="font-size: 0.9rem; font-weight: 700; color: var(--c-primary); margin-top: 0.2rem;">Terminal 2</div>
                                    </div>
                                    
                                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted); padding: 0 1rem;">
                                        <div style="width: 100%; height: 2px; background: var(--c-border); position: relative; margin: 1rem 0;">
                                            <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light); font-size: 1.5rem; background: white; padding: 0 10px;"></i>
                                        </div>
                                        <span style="font-size: 0.75rem; letter-spacing: 1px;">3H 35M</span>
                                    </div>
                                    
                                    <div style="flex: 1; text-align: right;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">HO CHI MINH (SGN)</div>
                                        <div style="font-size: 2.5rem; font-weight: 900; line-height: 1.2; color: var(--c-text);">10:15</div>
                                        <div style="font-size: 0.9rem; font-weight: 700; color: var(--c-primary); margin-top: 0.2rem;">Terminal 2</div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Right Section (Stub) -->
                            <div style="flex: 1; min-width: 180px; padding: 2rem; display: flex; flex-direction: column; justify-content: space-between; background: rgba(0,0,0,0.02);">
                                <div>
                                    <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Boarding Time</div>
                                    <div style="font-weight: 900; font-size: 1.8rem; color: var(--c-primary-light);">07:00</div>
                                </div>
                                
                                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Gate</div>
                                        <div style="font-weight: 700; font-size: 1.2rem; color: var(--c-text);">TBD</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Seat</div>
                                        <div style="font-weight: 700; font-size: 1.2rem; color: var(--c-text);">TBD</div>
                                    </div>
                                </div>
                                
                                <div style="margin-top: 1.5rem; text-align: center; font-family: 'Courier New', Courier, monospace; letter-spacing: -2px; font-size: 2.5rem; opacity: 0.2; transform: scaleY(1.5);">
                                    |||||||||||||||||||||
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Realistic Boarding Pass 2 -->
                    <div class="glass-card" style="width: 100%; padding: 0; display: flex; flex-direction: column; border-radius: 16px; overflow: hidden; position: relative; border: 1px solid var(--c-border); box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                        <!-- Top Header -->
                        <div style="background: var(--c-primary-light); color: white; padding: 0.8rem 2rem; display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-weight: 700; letter-spacing: 2px; font-size: 1.1rem;"><i class="fa-solid fa-plane"></i> STARLUX AIRLINES</div>
                            <div style="font-size: 0.8rem; opacity: 0.9; letter-spacing: 1px;">BOARDING PASS</div>
                        </div>
                        
                        <!-- Main Content -->
                        <div style="display: flex; background: white; flex-wrap: wrap;">
                            <!-- Left Section (Main details) -->
                            <div style="flex: 2; min-width: 300px; padding: 2rem; border-right: 2px dashed var(--c-border); display: flex; flex-direction: column;">
                                <!-- Passenger & Flight Info -->
                                <div style="display: flex; justify-content: space-between; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Passenger Name</div>
                                        <div style="font-weight: 700; font-size: 1.05rem; color: var(--c-text);">HSU / MINGEN & SYU / FANGYI</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Flight</div>
                                        <div style="font-weight: 700; font-size: 1.1rem; color: var(--c-primary);">JX 714</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Date</div>
                                        <div style="font-weight: 700; font-size: 1.1rem; color: var(--c-text);">02 APR</div>
                                    </div>
                                </div>
                                
                                <!-- Route Info -->
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="flex: 1;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">HO CHI MINH (SGN)</div>
                                        <div style="font-size: 2.5rem; font-weight: 900; line-height: 1.2; color: var(--c-text);">18:05</div>
                                        <div style="font-size: 0.9rem; font-weight: 700; color: var(--c-primary); margin-top: 0.2rem;">Terminal 2</div>
                                    </div>
                                    
                                    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; color: var(--c-text-muted); padding: 0 1rem;">
                                        <div style="width: 100%; height: 2px; background: var(--c-border); position: relative; margin: 1rem 0;">
                                            <i class="fa-solid fa-plane" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--c-primary-light); font-size: 1.5rem; background: white; padding: 0 10px;"></i>
                                        </div>
                                        <span style="font-size: 0.75rem; letter-spacing: 1px;">3H 30M</span>
                                    </div>
                                    
                                    <div style="flex: 1; text-align: right;">
                                        <div style="font-size: 0.8rem; color: var(--c-primary-light); font-weight: bold;">TAIPEI (TPE)</div>
                                        <div style="font-size: 2.5rem; font-weight: 900; line-height: 1.2; color: var(--c-text);">22:35</div>
                                        <div style="font-size: 0.9rem; font-weight: 700; color: var(--c-primary); margin-top: 0.2rem;">Terminal 2</div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Right Section (Stub) -->
                            <div style="flex: 1; min-width: 180px; padding: 2rem; display: flex; flex-direction: column; justify-content: space-between; background: rgba(0,0,0,0.02);">
                                <div>
                                    <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Boarding Time</div>
                                    <div style="font-weight: 900; font-size: 1.8rem; color: var(--c-primary-light);">17:25</div>
                                </div>
                                
                                <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Gate</div>
                                        <div style="font-weight: 700; font-size: 1.2rem; color: var(--c-text);">TBD</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 0.75rem; color: var(--c-text-muted); text-transform: uppercase;">Seat</div>
                                        <div style="font-weight: 700; font-size: 1.2rem; color: var(--c-text);">TBD</div>
                                    </div>
                                </div>
                                
                                <div style="margin-top: 1.5rem; text-align: center; font-family: 'Courier New', Courier, monospace; letter-spacing: -2px; font-size: 2.5rem; opacity: 0.2; transform: scaleY(1.5);">
                                    |||||||||||||||||||||
                                </div>
                            </div>
                        </div>
                    </div>

                </div>"""

pattern = r'<div class="hero-cards"\s*style="flex-direction: column; align-items: center; max-width: 700px; margin: 0 auto;">(.*?)</div>\s*</div>\s*</section>'
html = re.sub(pattern, replacement + '\n            </div>\n        </section>', html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)
print("Updated Boarding Passes!")
