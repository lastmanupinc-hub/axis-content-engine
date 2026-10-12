#!/usr/bin/env python3
"""Content consistency engine. See README."""
import argparse, datetime, json, textwrap
from pathlib import Path
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)
PILLARS = [
    {"name": "Sovereign / Deterministic AI Systems", "keywords": ["deterministic AI", "sovereign AI", "reproducible AI"], "angle": "Architecture and risk for high-stakes systems"},
    {"name": "Engine-Ready 3D Generation", "keywords": ["AI 3D model", "prompt to mesh", "Unity Unreal export"], "angle": "Validated, engine-ready meshes with provenance"},
    {"name": "AI Tool Directories & Launch", "keywords": ["AI app directory", "list AI tools"], "angle": "Discovery and proof for AI-built apps"},
    {"name": "Practical AI for Builders", "keywords": ["AI web apps", "prompt systems"], "angle": "Hands-on systems that ship"}
]
TOPIC_BANK = [
    "How to build reproducible 3D assets that export cleanly to Unity and Unreal",
    "Deterministic AI pipelines vs probabilistic generation",
    "What engine-ready actually means for AI-generated 3D meshes",
    "Provenance and hash-verified assets in game workflows",
    "Common failure modes when generating 3D characters for engines",
    "Self-hosted vs hosted AI 3D generation trade-offs",
    "From prompt to production: validation rules that catch bad meshes",
    "Practical architecture patterns for sovereign AI tools"
]
BACKLINK_OPPORTUNITIES = [
    {"type": "Directory", "target": "Product Hunt", "action": "Launch tools with clear demo", "priority": "High"},
    {"type": "Directory", "target": "AI tool directories", "action": "Submit accurate listings", "priority": "High"},
    {"type": "Community", "target": "Reddit (r/gamedev, r/Unity3D, r/UnrealEngine)", "action": "Share technical value posts", "priority": "High"},
    {"type": "Platforms", "target": "LinkedIn + newsletter", "action": "Weekly posts linking back to owned sites", "priority": "High"},
    {"type": "Profiles", "target": "Consistent bios", "action": "Same positioning everywhere", "priority": "High"}
]
def generate_calendar(start_date, weeks=8):
    items = []
    for week in range(weeks):
        for i in range(2):
            pillar = PILLARS[(week + i) % len(PILLARS)]
            topic = TOPIC_BANK[(week * 2 + i) % len(TOPIC_BANK)]
            items.append({
                "date": (start_date + datetime.timedelta(days=week*7 + i*3)).isoformat(),
                "pillar": pillar["name"],
                "topic": topic,
                "format": "Long-form guide" if i == 0 else "Supporting / LinkedIn",
                "target_keyword": pillar["keywords"][0]
            })
    return items
def generate_outline(topic):
    return textwrap.dedent(f"""
# Outline: {topic}

## Structure
1. Hook / Problem
2. Core method or framework
3. Implementation details
4. Results / what good looks like
5. Next actions + CTA

## Notes
- Primary keyword early.
- Internal links and consistent author bio.
- Distribute useful versions to communities.
""").strip()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--calendar", action="store_true")
    parser.add_argument("--weeks", type=int, default=8)
    parser.add_argument("--outline", type=str)
    parser.add_argument("--backlinks", action="store_true")
    args = parser.parse_args()
    start = datetime.date.today()
    if args.calendar:
        cal = generate_calendar(start, args.weeks)
        (OUTPUT_DIR / "content_calendar.json").write_text(json.dumps(cal, indent=2))
        md = ["# Content Calendar\n"]
        for item in cal:
            md.append(f"- **{item['date']}** | {item['format']} | {item['pillar']}\n  Topic: {item['topic']}\n")
        (OUTPUT_DIR / "content_calendar.md").write_text("\n".join(md))
        print("Calendar written")
    if args.outline:
        (OUTPUT_DIR / "outline.md").write_text(generate_outline(args.outline))
        print("Outline written")
    if args.backlinks:
        lines = ["# Backlink opportunities\n"]
        for o in BACKLINK_OPPORTUNITIES:
            lines.append(f"## {o['target']} ({o['priority']})\n- {o['action']}\n")
        (OUTPUT_DIR / "backlinks.md").write_text("\n".join(lines))
        print("Backlinks written")
if __name__ == "__main__":
    main()
