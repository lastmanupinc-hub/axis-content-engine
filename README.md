# AXIS Content Engine

Automated content calendar and outline generator for professional visibility around AI systems, engine-ready 3D generation, and related builder work.

## What it does

- Generates multi-week content calendars focused on searchable professional topics.
- Produces detailed outlines.
- Lists legitimate external mention / backlink opportunities.
- Provides a GitHub Pages frontend where you can input social handles and generate plans.
- Includes a GitHub Action that can run on a schedule to regenerate calendars.

## Realistic limits

This system helps with consistent, high-quality professional content and external signals. It does **not** remove or suppress public court records or news coverage. Rankings for name queries against high-authority sources (government, major news) change slowly, if at all, and require sustained quality plus real external mentions.

Full auto-posting to Instagram, LinkedIn, or TikTok requires their official APIs, business accounts, app reviews, and compliance with their terms. The system generates drafts and calendars you can review and publish. Browser automation for posting is fragile and often violates platform rules.

## Quick start

1. Enable GitHub Pages on the `main` branch (or `/docs` if preferred) from the repo Settings.
2. Open the published site and enter your Instagram, LinkedIn, and TikTok handles.
3. Generate calendars and outlines.
4. Optionally enable the scheduled workflow in `.github/workflows/generate.yml`.

## Local use

```bash
python content_engine.py --calendar --weeks 12
python content_engine.py --outline "validation rules for AI 3D meshes"
python content_engine.py --backlinks
```

Outputs go to `output/`.

## Social input

The Pages frontend stores your handles locally in the browser (localStorage) so generated posts can reference them in bios or CTAs. No data is sent anywhere.
