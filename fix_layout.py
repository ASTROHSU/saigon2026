import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Remove To-Do from Slide 1
todo_pattern = r'<div style="max-width: 600px; margin: 0 auto; background: rgba\(255.*?</ul>\s*</div>'
todo_match = re.search(todo_pattern, html, flags=re.DOTALL)
if todo_match:
    todo_html = todo_match.group(0)
    html = html[:todo_match.start()] + html[todo_match.end():]
else:
    todo_html = ""

# 2. Add To-Do to the end of Slide 7 (Budget)
budget_table_pattern = r'(<table.*?</table>\s*</div>\s*)(</div>\s*</section>)'
budget_match = re.search(budget_table_pattern, html, flags=re.DOTALL)
if budget_match and todo_html:
    # We will insert it right after the budget table's div.
    new_budget_content = budget_match.group(1) + "\n" + todo_html + "\n" + budget_match.group(2)
    html = html[:budget_match.start()] + new_budget_content + html[budget_match.end():]

with open("index.html", "w") as f:
    f.write(html)
print("Updated Slide 1 and Budget slide.")
