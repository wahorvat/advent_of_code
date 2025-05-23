import string
from collections import defaultdict

with open("../../../aoc_inputs/day 5.txt") as file:
    data = file.read()

def process_text(inp):
    rules = []
    updates = []
    found_blank = False
    
    for line in inp:
        line = line.strip()
        if not line and not found_blank:
            found_blank = True
            continue
        if not found_blank:
            rules.append(line)
        elif line:  # Only add non-empty lines to updates
            updates.append(line)
    
    return rules, updates

def order_rule_dict(rules):
    order_dict = defaultdict(list)
    
    for rule in rules:
        left, right = rule.split('|')
        order_dict[left].append(right)
    
    return order_dict

def is_valid_update(update_pages, order_rules):
    """Check if an update is in the correct order according to rules."""
    # Convert to list if it's a string
    if isinstance(update_pages, str):
        pages = update_pages.split(',')
    else:
        pages = update_pages
    
    # For each page, check if any pages that should come after it are before it
    for i, page in enumerate(pages):
        # Get all pages that should come after this page
        pages_after = order_rules.get(page, [])
        
        # Check if any of these pages appear before the current page
        for j in range(i):
            if pages[j] in pages_after:
                return False
    
    return True

def get_middle_page(update_pages):
    """Get the middle page number from an update."""
    if isinstance(update_pages, str):
        pages = update_pages.split(',')
    else:
        pages = update_pages
    
    middle_index = len(pages) // 2
    return int(pages[middle_index])

def answer1(inp):
    rules, updates = process_text(inp.splitlines())
    order_rules = order_rule_dict(rules)
    
    valid_updates = []
    total = 0
    
    for update in updates:
        if is_valid_update(update, order_rules):
            valid_updates.append(update)
            middle_page = get_middle_page(update)
            total += middle_page
    
    return total

ans1 = answer1(data)
print(f"Answer 1: {ans1}")