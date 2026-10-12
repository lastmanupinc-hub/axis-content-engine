# AXIS Content Engine

Generate consistent professional content calendars and outlines for AI systems, engine-ready 3D generation, and related builder topics.

## What it does

- Multi-week content calendars focused on searchable professional topics
- Detailed outlines with structure and draft starters
- Legitimate external mention / backlink opportunity lists
- GitHub Pages frontend (handles stored only in your browser)
- Optional scheduled GitHub Action that regenerates the calendar weekly

## Realistic limits

This system helps with consistent, high-quality professional content and external signals. It does **not** remove or suppress public court records or news coverage. Rankings for name queries against high-authority sources change slowly (if at all) and require sustained quality plus real external mentions.

Full auto-posting to Instagram, LinkedIn, or TikTok requires official APIs, business accounts, app reviews, and compliance with platform terms. The system generates drafts you review and publish. Browser automation for posting is fragile and often violates rules.

## Quick start

1. In repo Settings → Pages, set source to Deploy from branch `main` / root.
2. Open the published site, enter Instagram / LinkedIn / TikTok handles, and generate calendars or outlines.
3. Download or copy results. Enable the Action under the Actions tab if you want weekly regeneration.

## Local use

```bash
python content_engine.py --calendar --weeks 12
python content_engine.py --outline "validation rules for AI 3D meshes"
python content_engine.py --backlinks
```

Outputs go to `output/`. Optional `config.json` can override pillars and topics.

## Security / privacy

- Social handles are stored only in localStorage on the frontend. Nothing is sent to a server.
- The Action uses the default `GITHUB_TOKEN` with contents:write only for committing generated files.
- Review generated content before publishing.

## License

MIT
