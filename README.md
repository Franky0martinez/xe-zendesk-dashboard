# APAC Helpdesk Zendesk Dashboard

Streamlit wrapper that serves a slim build of the APAC Help Desk Zendesk productivity dashboard over a public URL.

## What's in here

- `streamlit_app.py` — embeds `Zendesk_Dashboard.html` in an iframe via `streamlit.components.v1.html`.
- `Zendesk_Dashboard.html` — a slim build of the original dashboard. The 42 MB inline JSON has been gzip-compressed and base64-encoded inside a `<script id="dashDataGz">` block, with a 2-line synchronous decode via [pako](https://github.com/nodeca/pako) loaded from jsDelivr. Renders identically to the original, ~24× smaller.

## Refreshing the data

The full 42 MB dashboard is regenerated outside this repo by `refresh_dashboard.py` in `Xe_APAC_Zendesk_Data/Dashboard/`. To update the deployed dashboard:

1. Run the refresh locally to rebuild the full `Zendesk_Dashboard.html`
2. Re-run the slim-build transform that produced this repo's HTML (gzip the embedded JSON, replace the inline data block, swap the loader to pako). See commit history of this file for the exact transformation.
3. Commit and push — Streamlit Cloud auto-redeploys.

## Local preview

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```
