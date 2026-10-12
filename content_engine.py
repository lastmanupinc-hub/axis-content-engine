#!/usr/bin/env python3
"""AXIS Content Engine — hardened generator for professional content calendars and outlines."""
import argparse
import datetime
import json
import sys
import textwrap
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

DEFAULT_PILLARS = [
    {
        "name": "Sovereign / Deterministic AI Systems",
        "keywords": ["deterministic AI", "sovereign AI", "reproducible AI", "AI risk review"],
        "angle": "Architecture, protocols, and risk for high-stakes systems"
    },
    {
        "name": "Engine-Ready 3D Generation",
        "keywords": ["AI 3D model", "prompt to mesh", "Unity Unreal export", "validated 3D assets"],
        "angle": "Prompt → validated, engine-ready meshes with provenance"
    },
    {
        "name": "AI Tool Directories & Launch",
        "keywords": ["AI app directory", "list AI tools", "AI product launch"],
        "angle": "Discovery and verifiable proof for AI-built apps"
    },
    {
        "name": "Practical AI for Builders",
        "keywords": ["AI web apps", "prompt systems", "AI for developers"],
        "angle": "Hands-on systems and workflows that ship"
    }
]

DEFAULT_TOPICS = [
    "How to build reproducible 3D assets that export cleanly to Unity and Unreal",
    "Deterministic AI pipelines vs probabilistic generation: when each is appropriate",
    "What engine-ready actually means for AI-generated 3D meshes",
    "Provenance and hash-verified assets in game development workflows",
    "Common failure modes when generating 3D characters for real engines",
    "Self-hosted vs hosted AI 3D generation: trade-offs for studios",
    "From prompt to production: validation rules that catch bad meshes early",
    "Practical architecture patterns for sovereign AI tools",
    "Listing and verifying AI apps for acquisition readiness",
    "Newsletter and content systems that compound for technical founders"
]

BACKLINKS = [
    {"type": "Directory", "target": "Product Hunt", "action": "Launch with clear demo and story", "priority": "High"},
    {"type": "Directory", "target": "AI tool directories (There's An AI For That, Futurepedia, etc.)", "action": "Accurate, maintained listings", "priority": "High"},
    {"type": "Community", "target": "Reddit (r/gamedev, r/Unity3D, r/UnrealEngine, r/LocalLLaMA)", "action": "Technical value posts only", "priority": "High"},
    {"type": "Platforms", "target": "LinkedIn articles + newsletter", "action": "Weekly posts with links back to owned sites", "priority": "High"},
    {"type": "Profiles", "target": "Consistent bios across platforms", "action": "Same name, positioning, and links everywhere", "priority": "High"},
    {"type": "Guest", "target": "Game-dev / AI engineering blogs", "action": "Pitch technical guest posts", "priority": "Medium"},
    {"type": "Technical", "target": "GitHub + discussions", "action": "Useful open code or validation rules", "priority": "Medium"}
]

def load_config():
    cfg_path = Path("config.json")
    if cfg_path.exists():
        try:
            data = json.loads(cfg_path.read_text())
            if isinstance(data, dict):
                return data
        except Exception as e:
            print(f"Warning: could not load config.json ({e}), using defaults", file=sys.stderr)
    return {"pillars": DEFAULT_PILLARS, "topics": DEFAULT_TOPICS}

def generate_calendar(start_date: datetime.date, weeks: int = 8, pillars=None, topics=None):
    if weeks < 1 or weeks > 52:
        raise ValueError("weeks must be between 1 and 52")
    pillars = pillars or DEFAULT_PILLARS
    topics = topics or DEFAULT_TOPICS
    items = []
    for week in range(weeks):
        for i in range(2):
            pillar = pillars[(week + i) % len(pillars)]
            topic = topics[(week * 2 + i) % len(topics)]
            items.append({
                "date": (start_date + datetime.timedelta(days=week * 7 + i * 3)).isoformat(),
                "pillar": pillar["name"],
                "topic": topic,
                "format": "Long-form guide" if i == 0 else "Supporting post",
                "target_keyword": pillar["keywords"][0] if pillar.get("keywords") else ""
            })
    return items

def generate_outline(topic: str, handles: dict | None = None) -> str:
    bio_parts = []
    if handles:
        if handles.get("ig"): bio_parts.append(f"IG: {handles['ig']}")
        if handles.get("li"): bio_parts.append(f"LinkedIn: {handles['li']}")
        if handles.get("tt"): bio_parts.append(f"TikTok: {handles['tt']}")
    bio = " | ".join(bio_parts) if bio_parts else "Add social handles in the UI or config"

    return textwrap.dedent(f"""
    # Outline: {topic}

    ## Working titles
    - {topic}
    - Practical guide: {topic}
    - What builders need to know about {topic}

    ## Structure
    1. **Hook / Problem** (150–200 words)
       Specific pain the reader has right now. Why common approaches fail.
    2. **Core method or framework** (400–600 words)
       Clear steps or principles with concrete examples.
    3. **Implementation details** (300–500 words)
       Process, common mistakes, and how to avoid them.
    4. **Results / what good looks like** (150–200 words)
       Proof points or before/after where available.
    5. **Next actions + CTA**
       Link to tool, related post, or owned site.

    ## SEO / distribution notes
    - Primary keyword in title, early, and one heading.
    - Internal links to related content and product pages.
    - Consistent author bio: {bio}
    - Link to jonathanarvay.com and related AXIS properties.
    - Share useful versions in relevant communities (value first).

    ## Draft starter (expand as needed)
    Most teams hit the same wall when trying to {topic.lower()}. The usual path produces output that looks fine in a preview but breaks in a real engine or production pipeline. This piece walks through a practical approach that prioritizes validation, reproducibility, and clear ownership of the result.
    """).strip()

def write_csv(items, path):
    lines = ["date,format,pillar,topic,keyword"]
    for it in items:
        lines.append(f"{it['date']},{it['format']},{it['pillar']},\"{it['topic']}\",{it['target_keyword']}")
    path.write_text("\n".join(lines) + "\n")

def main():
    parser = argparse.ArgumentParser(description="AXIS Content Engine")
    parser.add_argument("--calendar", action="store_true")
    parser.add_argument("--weeks", type=int, default=8)
    parser.add_argument("--outline", type=str)
    parser.add_argument("--backlinks", action="store_true")
    parser.add_argument("--handles", type=str, help="JSON string of handles")
    parser.add_argument("--all", action="store_true", help="Generate calendar, outline sample, and backlinks")
    args = parser.parse_args()

    cfg = load_config()
    start = datetime.date.today()
    handles = {}
    if args.handles:
        try:
            handles = json.loads(args.handles)
        except Exception:
            print("Warning: invalid --handles JSON", file=sys.stderr)

    generated = False

    if args.calendar or args.all:
        try:
            cal = generate_calendar(start, args.weeks, cfg.get("pillars"), cfg.get("topics"))
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        (OUTPUT_DIR / "content_calendar.json").write_text(json.dumps({"generated": start.isoformat(), "items": cal}, indent=2))
        md = [f"# Content Calendar (generated {start.isoformat()})\n"]
        for item in cal:
            md.append(f"- **{item['date']}** | {item['format']} | {item['pillar']}\n  Topic: {item['topic']}\n  Keyword: {item['target_keyword']}\n")
        (OUTPUT_DIR / "content_calendar.md").write_text("\n".join(md))
        write_csv(cal, OUTPUT_DIR / "content_calendar.csv")
        print(f"Wrote {len(cal)} calendar items (json/md/csv)")
        generated = True

    if args.outline or args.all:
        topic = args.outline or "Engine-ready AI 3D assets"
        (OUTPUT_DIR / "outline.md").write_text(generate_outline(topic, handles))
        print("Wrote outline.md")
        generated = True

    if args.backlinks or args.all:
        lines = [f"# Legitimate external mention opportunities\nGenerated {start.isoformat()}\n", "Prioritize real value over volume.\n"]
        for o in BACKLINKS:
            lines.append(f"## {o['target']} ({o['priority']})\n- {o['action']}\n")
        (OUTPUT_DIR / "backlinks.md").write_text("\n".join(lines))
        print("Wrote backlinks.md")
        generated = True

    if not generated:
        parser.print_help()

if __name__ == "__main__":
    main()
