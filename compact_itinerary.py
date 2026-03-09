import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Extract the Todo list which is currently somewhere in Slide 7 (Budget).
# Actually, wait, let's find the Todo section. It starts with '<div style="max-width: 600px...'
# and has '行前待辦事項'.
todo_pattern = r'<div style="max-width: 600px; margin: 0 auto; background: rgba(?:[^<]+|<(?!/div>))*<h3[^>]*>.*?行前待辦事項.*?</ul>\s*</div>'
todo_match = re.search(todo_pattern, html, flags=re.DOTALL)
todo_html = ""
if todo_match:
    todo_html = todo_match.group(0)
    # Remove it from its current location
    html = html[:todo_match.start()] + html[todo_match.end():]

# Create Slide 8 for Todo list
slide8_html = f"""
        <!-- Slide 8: To-Do List -->
        <section class="slide">
            <div class="content-wrapper">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h2>📝 行前待辦事項</h2>
                    <p>出發前的完美準備</p>
                </div>
                {todo_html}
            </div>
        </section>
"""

# Append Slide 8 right before the closing </div> of the presentation-container
# The presentation-container closes before '<!-- Navigation Controls -->'
nav_controls_idx = html.find('<!-- Navigation Controls -->')
if nav_controls_idx != -1:
    container_end_idx = html.rfind('</div>', 0, nav_controls_idx)
    if container_end_idx != -1:
        html = html[:container_end_idx] + slide8_html + html[container_end_idx:]

# 2. Compact the itinerary list. We want to remove the <p> description and <span class="distance-badge">
# inside the .event-details of .event-card.
# Essentially, keep only the <h4> element inside .event-details.
# We will find all <div class="event-details"> ... </div> and strip out <p> and <span class="distance-badge">
details_pattern = re.compile(r'(<div class="event-details">)(.*?)(</div>)', flags=re.DOTALL)

def simplify_details(match):
    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)
    
    # Remove <p>...</p>
    content = re.sub(r'<p>.*?</p>', '', content, flags=re.DOTALL)
    # Remove <span class="distance-badge">...</span>
    content = re.sub(r'<span class="distance-badge">.*?</span>', '', content, flags=re.DOTALL)
    
    return prefix + content + suffix

html = details_pattern.sub(simplify_details, html)

with open("index.html", "w") as f:
    f.write(html)
print("Compacted itinerary and added Slide 8.")
