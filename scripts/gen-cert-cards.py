"""Generate the 5 certification card SVGs (theme-consistent, static).

Each card is its own small image so the README can wrap it in an <a href>.
Links inside an SVG loaded via <img> are inert in browsers, so per-cert
clickability requires one image per cert.
"""
from pathlib import Path
from html import escape

W, H = 580, 140
OUT = Path("assets")

CARDS = [
    ("DATABRICKS", "Databricks Certified Data Engineer Associate",
     "Credential ID: 154048816", 0),
    ("AWS", "AWS Certified Cloud Practitioner",
     "Credential ID: 800e79a761cf486393469258de816904", 1),
    ("BOARD", "Foundations of Building in Board",
     "Credential ID: hxyhscorty6c", 2),
    ("BOARD", "Building a Planning Solution in Board",
     "Credential ID: jtow7eh8s72e", 3),
    ("BOARD", "Expanding Board in Your Organization",
     "Credential ID: a57dmshak2x9", 4),
]

FILES = [
    "cert-databricks.svg", "cert-aws.svg",
    "cert-board-foundations.svg", "cert-board-planning.svg",
    "cert-board-expanding.svg",
]

TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}">
  <rect width="{W}" height="{H}" rx="14" fill="#190B12" stroke="#C77B9B" stroke-opacity=".24"/>
  <rect x="0" y="0" width="3" height="{H}" rx="1.5" fill="#C77B9B"/>
  <text x="26" y="34" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="11.5" letter-spacing="2.6" fill="#C77B9B">{provider}</text>
  <text x="26" y="74" font-family="Georgia,'Iowan Old Style','Palatino Linotype','Times New Roman',serif" font-size="21" font-weight="300" fill="#F8F0F3">{name}</text>
  <text x="26" y="114" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="#B6A3AC">{cred}</text>
</svg>
"""

for (provider, name, cred, _), fn in zip(CARDS, FILES):
    (OUT / fn).write_text(
        TPL.format(W=W, H=H, provider=provider, name=escape(name), cred=escape(cred), label=escape(name)),
        encoding="utf-8",
    )
    print("wrote", OUT / fn)
