import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Fix the malformed data-map-src attribute inside class
# It currently looks like: class="data-map-src='...' glass-card event-card" or similar
# We want to change to: class="glass-card event-card" data-map-src="..."
# The regex looks for: class="data-map-src='([^']+)'(.*?)?" 
# Or: <div class="data-map-src='([^']+)'([^"]*)"
pattern1 = r'class="data-map-src=\'([^\']+)\'([^"]*)"'
html = re.sub(pattern1, r'class="\2" data-map-src="\1"', html)

# Some might be just `<div class="data-map-src='...' glass-card event-card"`
pattern2 = r'<div class="data-map-src=\'([^\']+)\'([^"]*)"'
html = re.sub(pattern2, r'<div class="\2" data-map-src="\1"', html)

# In case there are doubled ones from earlier mistakes:
# class="data-map-src='...' data-map-src='...' glass-card"
pattern3 = r'data-map-src=\'([^\']+)\' data-map-src=\'[^\']+\''
html = re.sub(pattern3, r'data-map-src="\1"', html)

# 2. Extract To-Do list and move it to a new slide
todo_pattern = r'<div\s*style="max-width: 600px; margin: 0 auto; background: rgba\(255,255,255,0\.8\); backdrop-filter: blur\(10px\); padding: 2rem; border-radius: 20px; border: 1px solid var\(--c-border\); box-shadow: 0 10px 30px rgba\(0,0,0,0\.05\);">\s*<h3 style="color: var\(--c-primary\); margin-bottom: 1\.5rem;"><i class="fa-solid fa-list-check"></i>\s*行前待辦事項</h3>.*?</ul>\s*</div>'

todo_match = re.search(todo_pattern, html, flags=re.DOTALL)
if todo_match:
    todo_html = todo_match.group(0)
    # Remove from current location
    html = html.replace(todo_html, '')
    
    # Create new slide
    new_slide = f"""
        <!-- Slide 8: To-Do List -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>📝 行前待辦事項</h2>
                    <p>給老公的小任務清單，確保一切順利</p>
                </div>
                {todo_html}
            </div>
        </section>
"""
    # Insert before the closing container div
    html = html.replace('    </div>\n\n    <!-- Navigation Controls -->', new_slide + '    </div>\n\n    <!-- Navigation Controls -->')

with open("index.html", "w") as f:
    f.write(html)
print("Fixed map attributes and moved To-Do list to new slide.")
