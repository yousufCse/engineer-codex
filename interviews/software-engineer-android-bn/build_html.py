"""Build the study web page from the Markdown guide.

The Markdown file stays the source. Run after any change:
    python3 build_html.py
No extra packages: a small Markdown converter for the subset this guide uses
(headings, paragraphs, nested lists, fenced code, tables, blockquotes, links).
Output: android-interview-prep-15-days-bn.html (same folder).
"""
import html
import pathlib
import re

FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([\w+-]*)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HR = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def inline(text: str) -> str:
    keep = []

    def stash(value: str) -> str:
        keep.append(value)
        return f"\x00{len(keep) - 1}\x00"

    text = re.sub(r"(`+)(.+?)\1", lambda m: stash(f"<code>{html.escape(m.group(2).strip())}</code>"), text)
    text = re.sub(r'<a id="[\w-]+"></a>', lambda m: stash(m.group(0)), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"&lt;(https?://[^\s&]+)&gt;", r'<a href="\1">\1</a>', text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*(?![\s*])(.+?)(?<![\s*])\*(?![*\w])", r"<em>\1</em>", text)
    # A line break before a bold label (e.g. "**A:**") stays a line break.
    text = re.sub(r"\n(?=<strong>)", "<br>\n", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], text)


def starts_block(line: str) -> bool:
    if FENCE.match(line) or HEADING.match(line) or HR.match(line):
        return True
    if re.match(r"^\s{0,3}>", line):
        return True
    m = LIST_ITEM.match(line)
    return bool(m and len(m.group(1)) <= 3)


def split_row(row: str) -> list:
    row = row.strip().strip("|")
    cells, cur, in_code = [], "", False
    for ch in row:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def blocks(lines: list) -> str:
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        fence = FENCE.match(line)
        if fence:
            indent, mark, lang = len(fence.group(1)), fence.group(2), fence.group(3)
            body, i = [], i + 1
            while i < n and not lines[i].strip().startswith(mark):
                raw = lines[i]
                body.append(raw[min(indent, len(raw) - len(raw.lstrip(" "))):])
                i += 1
            i += 1
            cls = f' class="language-{lang}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(body))}</code></pre>")
            continue
        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            i += 1
            continue
        if HR.match(line):
            out.append("<hr>")
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < n and TABLE_SEP.match(lines[i + 1]):
            head = split_row(line)
            rows, i = [], i + 2
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        if re.match(r"^\s{0,3}>", line):
            quoted = []
            while i < n and lines[i].strip() and (re.match(r"^\s{0,3}>", lines[i]) or not starts_block(lines[i])):
                quoted.append(re.sub(r"^\s{0,3}> ?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{blocks(quoted)}</blockquote>")
            continue
        item = LIST_ITEM.match(line)
        if item and len(item.group(1)) <= 3:
            html_list, i = parse_list(lines, i)
            out.append(html_list)
            continue
        para = [line.strip()]
        i += 1
        while i < n and lines[i].strip() and not starts_block(lines[i]) and not (
                lines[i].lstrip().startswith("|") and i + 1 < n and TABLE_SEP.match(lines[i + 1])):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(chr(10).join(para))}</p>")
    return "\n".join(out)


def parse_list(lines: list, i: int):
    first = LIST_ITEM.match(lines[i])
    base = len(first.group(1))
    ordered = first.group(2)[0].isdigit()
    start = int(re.match(r"\d+", first.group(2)).group(0)) if ordered else 1
    items, n = [], len(lines)
    while i < n:
        m = LIST_ITEM.match(lines[i])
        if not m or len(m.group(1)) != base or m.group(2)[0].isdigit() != ordered:
            break
        content_indent = len(m.group(1)) + len(m.group(2)) + 1
        body, i = [m.group(3)], i + 1
        while i < n:
            line = lines[i]
            if not line.strip():
                j = i
                while j < n and not lines[j].strip():
                    j += 1
                nxt = lines[j] if j < n else ""
                indent = len(nxt) - len(nxt.lstrip(" "))
                if j < n and indent >= min(content_indent, base + 2):
                    body.extend([""] * (j - i))
                    i = j
                    continue
                break
            indent = len(line) - len(line.lstrip(" "))
            sub = LIST_ITEM.match(line)
            if sub and indent <= base:
                break
            if indent >= min(content_indent, base + 2):
                body.append(line[min(indent, content_indent):])
            elif not starts_block(line):
                body.append(line.strip())
            else:
                break
            i += 1
        items.append(f"<li>{blocks(body)}</li>")
    tag = "ol" if ordered else "ul"
    attr = f' start="{start}"' if ordered and start != 1 else ""
    return f"<{tag}{attr}>" + "".join(items) + f"</{tag}>", i

HERE = pathlib.Path(__file__).parent
SRC = HERE / "android-interview-prep-15-days-bn.md"
OUT = HERE / "android-interview-prep-15-days-bn.html"


def strip_section(md: str, anchor: str) -> str:
    """Remove a '## <a id="anchor">' section up to the next '## ' heading."""
    start = md.find(f'## <a id="{anchor}"></a>')
    if start == -1:
        return md
    nxt = md.find("\n## ", start + 4)
    return md[:start] + (md[nxt + 1:] if nxt != -1 else "")


def main() -> None:
    md = SRC.read_text()
    # The page builds its own contents list and progress tracker.
    md = strip_section(md, "toc")
    md = strip_section(md, "tracker")
    md = md.replace("> **অগ্রগতি দেখতে:** গাইডের শেষে আছে [অনুশীলনের খাতা](#tracker)। সব প্রশ্ন এক লাইনে, টিক দেওয়ার বাক্সসহ।\n", "")
    body = blocks(md.split("\n"))
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body)
    body = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1)
    title = re.sub("<[^>]+>", "", title_match.group(1)) if title_match else "Android Interview Prep"
    OUT.write_text(TEMPLATE.replace("{{TITLE}}", title).replace("{{BODY}}", body))
    print(f"wrote {OUT.name}")


TEMPLATE = r"""<!doctype html>
<html lang="bn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Android Interview Prep</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{
  --bg:#f6f7f9;--surface:#ffffff;--surface2:#f2f4f7;--line:#e4e7ec;--line2:#d0d5dd;
  --text:#101828;--text2:#344054;--muted:#667085;
  --accent:#4f46e5;--accent-2:#0ea5e9;--accent-soft:#eef2ff;--accent-line:#c7d2fe;
  --good:#079455;--good-soft:#ecfdf3;--warn:#d92d20;--warn-soft:#fef3f2;--warn-line:#fecdca;
  --star:#dc6803;--star-soft:#fffaeb;--dia:#1570ef;--dia-soft:#eff8ff;--ring:#7a5af8;--ring-soft:#f4f3ff;
  --answer:#f8f9ff;--code-bg:#0f172a;--code-text:#e2e8f0;
  --shadow-sm:0 1px 2px rgba(16,24,40,.05);
  --shadow:0 1px 3px rgba(16,24,40,.06),0 4px 12px rgba(16,24,40,.04);
  --shadow-lg:0 12px 32px rgba(16,24,40,.10);
  --radius:16px;--header-h:64px;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0b0d12;--surface:#12151c;--surface2:#181c25;--line:#252a35;--line2:#343a46;
  --text:#f2f4f7;--text2:#cfd4dc;--muted:#98a2b3;
  --accent:#8b93ff;--accent-2:#38bdf8;--accent-soft:#1c1d3a;--accent-line:#2f3270;
  --good:#47cd89;--good-soft:#0b2a1c;--warn:#f97066;--warn-soft:#2d1412;--warn-line:#55231e;
  --star:#fdb022;--star-soft:#2b1f08;--dia:#53b1fd;--dia-soft:#0b2238;--ring:#a48afb;--ring-soft:#211a3d;
  --answer:#141a2a;--code-bg:#0a0e17;--code-text:#e2e8f0;
  --shadow-sm:none;--shadow:0 1px 0 rgba(255,255,255,.02);--shadow-lg:0 12px 32px rgba(0,0,0,.45);}}
:root[data-theme="dark"]{
  --bg:#0b0d12;--surface:#12151c;--surface2:#181c25;--line:#252a35;--line2:#343a46;
  --text:#f2f4f7;--text2:#cfd4dc;--muted:#98a2b3;
  --accent:#8b93ff;--accent-2:#38bdf8;--accent-soft:#1c1d3a;--accent-line:#2f3270;
  --good:#47cd89;--good-soft:#0b2a1c;--warn:#f97066;--warn-soft:#2d1412;--warn-line:#55231e;
  --star:#fdb022;--star-soft:#2b1f08;--dia:#53b1fd;--dia-soft:#0b2238;--ring:#a48afb;--ring-soft:#211a3d;
  --answer:#141a2a;--code-bg:#0a0e17;--code-text:#e2e8f0;
  --shadow-sm:none;--shadow:0 1px 0 rgba(255,255,255,.02);--shadow-lg:0 12px 32px rgba(0,0,0,.45);}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text2);
  font-family:"Inter","Noto Sans Bengali",system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:16.5px;line-height:1.8;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--accent);text-decoration:none;text-underline-offset:3px}
a:hover{text-decoration:underline}
strong{color:var(--text);font-weight:650}
::selection{background:var(--accent-soft)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:6px}

/* ---------- header ---------- */
.topbar{position:sticky;top:0;z-index:30;display:flex;gap:10px;align-items:center;height:var(--header-h);
  padding:0 20px;background:color-mix(in srgb,var(--surface) 82%,transparent);
  -webkit-backdrop-filter:saturate(180%) blur(14px);backdrop-filter:saturate(180%) blur(14px);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;color:var(--text);white-space:nowrap;letter-spacing:-.01em}
.brand .logo{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;color:#fff;font-size:15px;
  background:linear-gradient(135deg,var(--accent),var(--accent-2));box-shadow:0 4px 12px rgba(79,70,229,.35)}
.tabs{display:flex;background:var(--surface2);border:1px solid var(--line);border-radius:12px;padding:3px;margin-left:8px}
.tab{border:0;background:none;color:var(--muted);font:600 13.5px/1 Inter,"Noto Sans Bengali",sans-serif;padding:8px 12px;border-radius:9px;cursor:pointer;white-space:nowrap}
.tab[aria-pressed="true"]{background:var(--surface);color:var(--text);box-shadow:var(--shadow-sm),0 0 0 1px var(--line)}
.search{flex:1;min-width:0;max-width:380px;margin-left:auto;padding:9px 14px 9px 36px;border-radius:11px;border:1px solid var(--line);
  background:var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='none' stroke='%23667085' stroke-width='2' stroke-linecap='round'%3E%3Ccircle cx='7' cy='7' r='5'/%3E%3Cpath d='m11 11 3.5 3.5'/%3E%3C/svg%3E") no-repeat 12px center;
  color:var(--text);font:inherit;font-size:14.5px}
.search:focus{outline:none;border-color:var(--accent-line);box-shadow:0 0 0 4px var(--accent-soft)}
.chips{display:flex;gap:6px}
.chip,.btn{font:600 13px/1 Inter,"Noto Sans Bengali",sans-serif;padding:9px 12px;border-radius:10px;border:1px solid var(--line);
  background:var(--surface);color:var(--text2);cursor:pointer;white-space:nowrap;transition:background .15s,border-color .15s}
.chip:hover,.btn:hover{border-color:var(--line2);background:var(--surface2)}
.chip[aria-pressed="true"]{background:var(--text);border-color:var(--text);color:var(--surface)}
.btn[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.menu-btn{display:none}
.progress-wrap{position:sticky;top:var(--header-h);z-index:29;height:2px;background:transparent}
.progress-bar{height:2px;width:0;background:linear-gradient(90deg,var(--accent),var(--accent-2));transition:width .3s}

/* ---------- layout ---------- */
.layout{display:flex;max-width:1360px;margin:0 auto}
nav.side{position:sticky;top:calc(var(--header-h) + 2px);align-self:flex-start;width:300px;flex:none;
  height:calc(100vh - var(--header-h) - 2px);overflow-y:auto;padding:20px 14px 60px;border-right:1px solid var(--line);font-size:14px;line-height:1.5;scrollbar-width:thin}
nav.side .grp{margin-bottom:2px}
nav.side .grp-title{display:grid;grid-template-columns:1fr auto;gap:8px;align-items:center;width:100%;padding:8px 10px;border:0;background:none;
  color:var(--text);font:600 14px/1.45 Inter,"Noto Sans Bengali",sans-serif;text-align:left;cursor:pointer;border-radius:9px}
nav.side .grp-title:hover{background:var(--surface2)}
nav.side .count:empty{display:none}
nav.side .count{font:600 11.5px Inter,sans-serif;color:var(--muted);background:var(--surface2);padding:2px 7px;border-radius:99px}
nav.side ul{list-style:none;margin:2px 0 8px;padding:0 0 0 10px;border-left:1px solid var(--line);margin-left:14px}
nav.side li a{display:block;padding:5px 10px;border-radius:7px;color:var(--muted);font-size:13.5px}
nav.side li a:hover{background:var(--surface2);text-decoration:none;color:var(--text)}
nav.side li a.active{color:var(--accent);background:var(--accent-soft);font-weight:600}
nav.side li a.done .nid{background:var(--good-soft);color:var(--good)}
nav.side .grp.closed ul{display:none}
nav.side .nid{font:700 11px Inter,sans-serif;color:var(--muted);margin-right:6px;padding:1px 6px;border-radius:5px;background:var(--surface2)}
nav.side .pri-mini{font-size:10px;margin-right:5px}
nav.side .pri-mini.star{color:var(--star)} nav.side .pri-mini.dia{color:var(--dia)} nav.side .pri-mini.ring{color:var(--ring)}
main{flex:1;min-width:0;padding:28px 40px 140px;max-width:900px;margin:0 auto}
main h2{font-size:25px;line-height:1.35;color:var(--text);letter-spacing:-.015em;margin:64px 0 16px}
main h3{font-size:19px;line-height:1.45;color:var(--text);letter-spacing:-.01em}
main h4{font-size:16.5px;color:var(--text)}
[id]{scroll-margin-top:calc(var(--header-h) + 20px)}
p,li{color:var(--text2)}
blockquote{margin:16px 0;padding:12px 18px;border-left:3px solid var(--accent-line);background:var(--surface2);border-radius:0 12px 12px 0}
blockquote p{margin:6px 0}
table{border-collapse:separate;border-spacing:0;width:100%;margin:16px 0;font-size:14.5px;display:block;overflow-x:auto;
  border:1px solid var(--line);border-radius:12px;background:var(--surface)}
th,td{padding:10px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
tr:last-child td{border-bottom:0}
th{background:var(--surface2);color:var(--text);font-weight:650;font-size:13.5px;white-space:nowrap}
code{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:.85em;background:var(--surface2);border:1px solid var(--line);
  padding:1px 6px;border-radius:6px;color:var(--text)}
:not(pre) > code{overflow-wrap:anywhere}
.codebox{margin:16px 0;border-radius:14px;overflow:hidden;background:var(--code-bg);border:1px solid #1e293b;box-shadow:var(--shadow)}
.codebox .code-head{display:flex;justify-content:space-between;align-items:center;padding:7px 12px 7px 16px;background:#111a2e;border-bottom:1px solid #1e293b;
  font:600 12px Inter,sans-serif;color:#94a3b8;text-transform:uppercase;letter-spacing:.06em}
.codebox .copy{font:600 12px Inter,"Noto Sans Bengali",sans-serif;color:#cbd5e1;background:#1e293b;border:0;border-radius:7px;padding:5px 10px;cursor:pointer;text-transform:none;letter-spacing:0}
.codebox .copy:hover{background:#334155}
pre{margin:0;padding:16px 18px;overflow-x:auto;line-height:1.6;background:var(--code-bg)}
pre code{background:none;border:0;padding:0;font-size:13px;color:var(--code-text)}
hr{border:0;border-top:1px solid var(--line);margin:32px 0}
li > p{margin:2px 0}
ul,ol{padding-left:22px}
li{margin:3px 0}

/* ---------- hero ---------- */
.hero{position:relative;overflow:hidden;border-radius:24px;padding:40px 36px 32px;color:#e2e8f0;
  background:
    radial-gradient(900px 360px at 0% -20%,rgba(99,102,241,.55),transparent 60%),
    radial-gradient(700px 300px at 100% 0%,rgba(14,165,233,.40),transparent 60%),
    #0b1020;box-shadow:var(--shadow-lg)}
.hero::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.35;
  background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);
  background-size:32px 32px;mask-image:linear-gradient(180deg,#000,transparent 85%)}
.hero > *{position:relative}
.hero .kicker{display:inline-flex;gap:8px;align-items:center;font:600 12.5px Inter,"Noto Sans Bengali",sans-serif;color:#c7d2fe;
  background:rgba(99,102,241,.18);border:1px solid rgba(165,180,252,.25);padding:5px 12px;border-radius:99px}
.hero h1{margin:16px 0 10px;color:#fff;font-size:36px;line-height:1.25;letter-spacing:-.02em;font-weight:750}
.hero .sub{margin:0 0 22px;color:#cbd5e1;font-size:16.5px;max-width:640px}
.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:0 0 20px}
.stat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:12px 14px}
.stat b{display:block;font:750 24px/1.2 Inter,sans-serif;color:#fff}
.stat span{font-size:13px;color:#94a3b8}
.hero-bar{height:6px;border-radius:99px;background:rgba(255,255,255,.12);overflow:hidden;margin:0 0 22px}
.hero-bar i{display:block;height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#818cf8,#38bdf8);transition:width .4s}
.hero-cta{display:flex;flex-wrap:wrap;gap:10px}
.cta{font:650 15px/1 Inter,"Noto Sans Bengali",sans-serif;padding:13px 18px;border-radius:12px;border:1px solid transparent;cursor:pointer}
.cta.primary{background:#fff;color:#0b1020}
.cta.primary:hover{background:#e0e7ff}
.cta.ghost{background:rgba(255,255,255,.08);color:#fff;border-color:rgba(255,255,255,.18)}
.cta.ghost:hover{background:rgba(255,255,255,.14)}
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0 8px}
.plan{text-align:left;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px;cursor:pointer;box-shadow:var(--shadow);
  font:inherit;color:var(--text2);transition:transform .15s,box-shadow .15s,border-color .15s}
.plan:hover{transform:translateY(-2px);box-shadow:var(--shadow-lg);border-color:var(--accent-line)}
.plan .days{font:750 22px Inter,"Noto Sans Bengali",sans-serif;color:var(--text)}
.plan .what{font-size:14px;color:var(--muted);margin-top:2px}
.plan .mark{display:inline-block;margin-top:10px;font:700 12px Inter,sans-serif;padding:3px 9px;border-radius:99px}
.plan.p7 .mark{background:var(--star-soft);color:var(--star)}
.plan.p10 .mark{background:var(--dia-soft);color:var(--dia)}
.plan.p15 .mark{background:var(--ring-soft);color:var(--ring)}
.legend{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:13.5px;color:var(--muted);margin:10px 0 0}
.legend b.s{color:var(--star)} .legend b.d{color:var(--dia)} .legend b.r{color:var(--ring)}

/* ---------- part banner ---------- */
main h2.part-banner{display:grid;grid-template-columns:auto 1fr;gap:4px 18px;align-items:center;margin:80px 0 20px;padding:22px 24px;
  background:var(--surface);border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}
h2.part-banner .num{grid-row:1 / span 3;width:58px;height:58px;border-radius:16px;display:grid;place-items:center;
  font:800 20px Inter,sans-serif;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent-2));letter-spacing:-.02em}
h2.part-banner .eyebrow{font:700 12px Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
h2.part-banner .pt{font-size:22px;line-height:1.35;color:var(--text)}
h2.part-banner .pbar{display:flex;align-items:center;gap:10px;font:600 12px Inter,"Noto Sans Bengali",sans-serif;color:var(--muted)}
h2.part-banner .pbar i{flex:1;max-width:220px;height:5px;border-radius:99px;background:var(--surface2);overflow:hidden}
h2.part-banner .pbar i b{display:block;height:100%;width:0;background:var(--good);border-radius:99px;transition:width .3s}

/* ---------- question cards ---------- */
.q{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:6px 26px 18px;margin:20px 0;box-shadow:var(--shadow);transition:border-color .2s}
.q:hover{border-color:var(--line2)}
.q.lesson{border-color:var(--accent-line);background:linear-gradient(180deg,var(--accent-soft),var(--surface) 160px)}
.q.lesson h3{color:var(--accent)}
.q-head{display:flex;gap:12px;align-items:flex-start;justify-content:space-between}
.q-head h3{flex:1;min-width:0;display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;margin:18px 0 8px}
.qid{font:700 12px Inter,sans-serif;padding:3px 8px;border-radius:7px;background:var(--surface2);border:1px solid var(--line);color:var(--muted)}
.pri{font:700 11.5px Inter,"Noto Sans Bengali",sans-serif;padding:3px 8px;border-radius:7px}
.pri.star{background:var(--star-soft);color:var(--star)}
.pri.dia{background:var(--dia-soft);color:var(--dia)}
.pri.ring{background:var(--ring-soft);color:var(--ring)}
.q-title{flex-basis:100%;font-weight:700;margin-top:4px}
.done-box{flex:none;margin-top:18px;display:flex;align-items:center;gap:7px;font:600 13px Inter,"Noto Sans Bengali",sans-serif;
  padding:7px 12px;border-radius:10px;border:1px solid var(--line);cursor:pointer;user-select:none;color:var(--muted);background:var(--surface)}
.done-box input{accent-color:var(--good);width:16px;height:16px;margin:0}
.q.is-done{border-color:color-mix(in srgb,var(--good) 35%,var(--line))}
.q.is-done .done-box{background:var(--good-soft);color:var(--good);border-color:color-mix(in srgb,var(--good) 40%,transparent)}
.meta{background:var(--surface2);border-radius:12px;padding:10px 16px;margin:4px 0 14px;font-size:15px}
.meta p{margin:4px 0}
p.label-learn{margin:14px 0 2px}
p.label-learn > strong:first-child{display:inline-flex;align-items:center;gap:6px;font:700 13px Inter,"Noto Sans Bengali",sans-serif;color:var(--accent);margin-right:4px}
p.label-learn > strong:first-child::before{content:"";width:16px;height:2px;background:var(--accent);border-radius:2px}
.answer{background:var(--answer);border:1px solid var(--accent-line);border-left:4px solid var(--accent);border-radius:14px;padding:6px 18px 8px;margin:16px 0}
.answer blockquote{border:0;background:none;padding:0;margin:6px 0;font-size:16.5px;color:var(--text)}
.answer blockquote p{color:var(--text)}
.answer .pair{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:8px 0}
.answer .pair blockquote{margin:0;padding:12px 14px;border-radius:12px;background:var(--surface);border:1px solid var(--line)}
.answer .pair blockquote:not(.bn)::before{content:"English";display:block;font:700 11.5px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:4px}
.answer blockquote.bn{background:var(--surface2);font-size:16px}
.answer blockquote.bn strong:first-child{display:block;font:700 12px Inter,"Noto Sans Bengali",sans-serif;color:var(--good);margin-bottom:2px}
@media (max-width:900px){.answer .pair{grid-template-columns:1fr}}
.ans-label{margin:10px 0 0;font-size:13px}
.ans-label strong{color:var(--accent);font:700 12.5px Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase}
.ans-tools{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 4px}
.reveal{display:none}
body.practice .answer:not(.shown) > :not(.ans-label):not(.ans-tools){display:none}
body.practice .answer:not(.shown) .reveal{display:inline-block;background:var(--accent);border-color:var(--accent);color:#fff}
body.practice .answer:not(.shown) .speak{display:none}
p.keywords{font-size:14px}
p.keywords code{display:inline-block;margin:3px 2px;padding:3px 10px;border-radius:99px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-line);font-size:12.5px}
p.example{background:var(--good-soft);border:1px solid color-mix(in srgb,var(--good) 30%,transparent);border-radius:12px;padding:10px 16px;font-size:15.5px}
p.example strong:first-child{color:var(--good)}
p.example strong:first-child::before{content:"💡 "}
p.warn{background:var(--warn-soft);border:1px solid var(--warn-line);border-radius:12px;padding:10px 16px;font-size:15px}
p.warn strong:first-child{color:var(--warn)}
details.fu{margin:12px 0;border:1px solid var(--line);border-radius:12px;padding:4px 16px;background:var(--surface)}
details.fu summary{cursor:pointer;font:600 14.5px Inter,"Noto Sans Bengali",sans-serif;color:var(--text);padding:8px 0;list-style:none}
details.fu summary::-webkit-details-marker{display:none}
details.fu summary::before{content:"›";display:inline-block;margin-right:8px;transition:transform .15s;color:var(--muted)}
details.fu[open] summary::before{transform:rotate(90deg)}
p.see-also{margin:14px 0 4px;font-size:13.5px;color:var(--muted)}
p.see-also a{display:inline-block;margin:3px 2px;padding:3px 11px;border-radius:99px;border:1px solid var(--line);background:var(--surface2);color:var(--text2);font-weight:500}
p.see-also a:hover{border-color:var(--accent-line);color:var(--accent);text-decoration:none}
.pager{display:flex;justify-content:space-between;gap:10px;margin:16px 0 2px;padding-top:12px;border-top:1px solid var(--line);font:600 13px Inter,"Noto Sans Bengali",sans-serif}
.pager a{padding:6px 12px;border-radius:9px;color:var(--muted)}
.pager a:hover{background:var(--surface2);color:var(--text);text-decoration:none}
.hidden{display:none!important}
.empty{display:none;padding:60px 20px;text-align:center;color:var(--muted)}
.to-top{position:fixed;right:20px;bottom:20px;z-index:20;width:44px;height:44px;border-radius:14px;border:1px solid var(--line);
  background:var(--surface);color:var(--text);font-size:17px;cursor:pointer;box-shadow:var(--shadow-lg)}

/* ---------- interview page ---------- */
body.drill-mode .layout,body.drill-mode .search,body.drill-mode .chips,body.drill-mode #practiceBtn,body.drill-mode .menu-btn,body.drill-mode .to-top{display:none}
.drill{max-width:760px;margin:0 auto;padding:28px 16px 140px}
.drill-top{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;margin-bottom:16px}
.drill-top select{font:600 14.5px Inter,"Noto Sans Bengali",sans-serif;padding:10px 14px;border-radius:12px;border:1px solid var(--line);background:var(--surface);color:var(--text);max-width:100%}
.drill-count{font:600 13.5px Inter,"Noto Sans Bengali",sans-serif;color:var(--muted)}
.drill-card{background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:26px 26px 18px;box-shadow:var(--shadow-lg);min-height:240px}
.drill-card h3{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;font-size:23px;line-height:1.45;color:var(--text);margin:0 0 14px}
.drill-card .answer{display:none}
.drill-card.revealed .answer{display:block}
.drill-card .ans-tools{display:none!important}
.drill-card .after{display:none}
.drill-card.revealed .after{display:block}
.drill-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0;position:sticky;bottom:0;padding:12px 0;
  background:linear-gradient(180deg,transparent,var(--bg) 30%)}
.drill-actions button{font:650 15.5px Inter,"Noto Sans Bengali",sans-serif;padding:14px 10px;border-radius:14px;border:1px solid var(--line);background:var(--surface);color:var(--text);cursor:pointer;box-shadow:var(--shadow-sm)}
.drill-actions button:hover{border-color:var(--line2)}
.drill-actions .big{grid-column:1 / -1;background:var(--accent);border-color:var(--accent);color:#fff}
.drill-actions .good{background:var(--good);border-color:var(--good);color:#fff}
.drill-hint{font-size:14px;color:var(--muted);text-align:center}
.drill-done{text-align:center;padding:30px 10px}

/* ---------- responsive ---------- */
@media (max-width:1100px){.chips .chip-label{display:none}}
@media (max-width:980px){
  .menu-btn{display:inline-block}
  nav.side{position:fixed;left:0;top:0;height:100vh;z-index:40;background:var(--surface);width:min(320px,86vw);
    transform:translateX(-100%);transition:transform .25s;box-shadow:var(--shadow-lg);padding-top:24px}
  body.nav-open nav.side{transform:none}
  body.nav-open::after{content:"";position:fixed;inset:0;z-index:35;background:rgba(10,12,20,.45)}
  main{padding:20px 18px 120px}
  .brand .name{display:none}
}
@media (max-width:640px){
  :root{--header-h:auto}
  .topbar{flex-wrap:wrap;gap:8px;padding:10px 14px;height:auto}
  .brand{order:0}
  .tabs{order:1;margin-left:0}
  #practiceBtn{order:2;margin-left:auto}
  #themeBtn{order:3}
  .menu-btn{order:-1}
  .search{order:4;flex-basis:100%;max-width:none}
  .chips{order:5;flex-basis:100%;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .chips .chip-label{display:inline}
  .progress-wrap{top:0}
  nav.side{top:0;height:100vh}
  [id]{scroll-margin-top:84px}
  body.compact .search,body.compact .chips{display:none}
  body{font-size:16px}
  .hero{padding:28px 20px 22px;border-radius:20px}
  .hero h1{font-size:27px}
  .hero-stats{gap:8px}
  .stat{padding:10px}
  .stat b{font-size:20px}
  .plans{grid-template-columns:1fr}
  main h2.part-banner{padding:16px;gap:2px 14px;border-radius:18px}
  h2.part-banner .num{width:46px;height:46px;font-size:17px;border-radius:13px}
  h2.part-banner .pt{font-size:18.5px}
  .q{padding:4px 16px 14px;border-radius:14px}
  .q-head h3{font-size:17.5px}
  .done-box{padding:6px 9px}
  .drill-card{padding:20px 18px 14px;border-radius:20px}
  .drill-card h3{font-size:19.5px}
}
@media print{.topbar,nav.side,.to-top,.ans-tools,.pager,.done-box{display:none!important}.answer > *{display:block!important}}
</style>
</head>
<body>
<div class="topbar">
  <button class="btn menu-btn" id="menuBtn" aria-label="সূচিপত্র">☰</button>
  <div class="brand"><span class="logo">A</span><span class="name">Android Interview Prep</span></div>
  <div class="tabs" role="group" aria-label="Page">
    <button class="tab" id="tabRead" aria-pressed="true">📖 পড়ুন</button>
    <button class="tab" id="tabDrill" aria-pressed="false">🎤 Interview</button>
  </div>
  <input class="search" id="search" type="search" placeholder="খুঁজুন… (যেমন: coroutine, Keystore, K12)">
  <div class="chips" role="group" aria-label="Priority filter">
    <button class="chip" data-f="all" aria-pressed="true">সব</button>
    <button class="chip" data-f="star" aria-pressed="false">★ <span class="chip-label">৭ দিন</span></button>
    <button class="chip" data-f="dia" aria-pressed="false">★◆ <span class="chip-label">১০ দিন</span></button>
    <button class="chip" data-f="todo" aria-pressed="false">বাকি</button>
  </div>
  <button class="btn" id="practiceBtn" aria-pressed="false" title="উত্তর লুকিয়ে রাখুন">🎯 Practice</button>
  <button class="btn" id="themeBtn" title="Light / dark">◐</button>
</div>
<div class="progress-wrap"><div class="progress-bar" id="progressBar"></div></div>
<div class="layout">
  <nav class="side" id="side" aria-label="সূচিপত্র"></nav>
  <main id="content">
    <div class="hero">
      <span class="kicker">Native Android · Kotlin · 2026</span>
      <h1>{{TITLE}}</h1>
      <p class="sub">প্রশ্ন সহজ English-এ। বোঝানো বাংলায়। উত্তর মুখে বলার মতো সহজ English-এ। আগে concept বুঝুন, তারপর নিজের ভাষায় বলুন।</p>
      <div class="hero-stats">
        <div class="stat"><b id="statTotal">0</b><span>মোট প্রশ্ন</span></div>
        <div class="stat"><b id="statDone">0</b><span>পারি ✓</span></div>
        <div class="stat"><b id="statStar">0/0</b><span>★ প্রশ্ন শেষ</span></div>
      </div>
      <div class="hero-bar"><i id="heroBar"></i></div>
      <div class="hero-cta">
        <button class="cta primary" id="ctaRead">📖 পড়া শুরু করুন</button>
        <button class="cta ghost" id="ctaDrill">🎤 Interview practice</button>
      </div>
    </div>
    <div class="plans">
      <button class="plan p7" data-go="plan-7"><div class="days">৭ দিন</div><div class="what">শুধু ★ প্রশ্ন। দিনে ৫–৬ ঘণ্টা।</div><span class="mark">★</span></button>
      <button class="plan p10" data-go="plan-10"><div class="days">১০ দিন</div><div class="what">★ আর ◆ প্রশ্ন।</div><span class="mark">★ ◆</span></button>
      <button class="plan p15" data-go="plan-15"><div class="days">১৫ দিন</div><div class="what">সব প্রশ্ন, ধীরে আর গভীরে।</div><span class="mark">★ ◆ ○</span></button>
    </div>
    <div class="legend"><span><b class="s">★</b> অবশ্যই</span><span><b class="d">◆</b> জরুরি</span><span><b class="r">○</b> গভীর</span><span>🎯 Practice = উত্তর লুকানো</span><span>🔊 = English উত্তর শুনুন</span></div>
    {{BODY}}
    <div class="empty" id="empty">কিছু পাওয়া যায়নি। Filter বা search বদলে দেখুন।</div>
  </main>
</div>
<section class="drill" id="drill" hidden>
  <div class="drill-top">
    <select id="drillScope" aria-label="কোন প্রশ্ন"></select>
    <span class="drill-count" id="drillCount"></span>
  </div>
  <div class="drill-card" id="drillCard"></div>
  <div class="drill-actions">
    <button class="big" id="dReveal">👀 উত্তর দেখুন</button>
    <button id="dSpeak">🔊 শুনুন</button>
    <button id="dAgain">↻ আবার পড়ব</button>
    <button id="dRead">📖 পুরো ব্যাখ্যা</button>
    <button class="good" id="dKnow">✓ পারি, পরেরটা</button>
  </div>
  <p class="drill-hint">প্রশ্নটা জোরে পড়ুন → নিজে ১ মিনিট English-এ বলুন → তারপর উত্তর দেখে মিলিয়ে নিন। Keyboard: Space = উত্তর, → = পরেরটা।</p>
</section>
<button class="to-top" id="toTop" title="উপরে">↑</button>
<script>
(function(){
  const store = {
    get(k, d){ try{ const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); }catch(e){ return d; } },
    set(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)); }catch(e){} }
  };
  const KEY = 'aip-done-v1';
  let jumping = 0;  // time of the last link jump; the mobile header stays small during it
  const done = new Set(store.get(KEY, []));
  const main = document.getElementById('content');

  // 1. Group the flat pandoc output into part sections and question cards.
  const nodes = Array.from(main.children).filter(n => !n.classList.contains('hero') && n.id !== 'empty');
  let group = null, card = null;
  const groups = [];
  nodes.forEach(n => {
    if (n.tagName === 'H2') {
      card = null;
      const a = n.querySelector('a[id]');
      group = { el: n, id: a ? a.id : n.id, title: n.textContent.trim(), cards: [], isPart: !!(a && a.id.startsWith('part-')) };
      groups.push(group);
      return;
    }
    if (n.tagName === 'H3') {
      const a = n.querySelector('a[id]');
      card = document.createElement('section');
      card.className = 'q';
      n.before(card);
      const head = document.createElement('div');
      head.className = 'q-head';
      card.appendChild(head);
      head.appendChild(n);
      const t = n.textContent;
      if (a) {
        card.dataset.id = a.id;
        card.id = 'card-' + a.id;
        card.dataset.pri = t.includes('★') ? 'star' : t.includes('◆') ? 'dia' : t.includes('○') ? 'ring' : 'none';
        card.classList.add('pri-' + card.dataset.pri);
        const lab = document.createElement('label');
        lab.className = 'done-box';
        lab.innerHTML = '<input type="checkbox"> পারি';
        head.appendChild(lab);
        const cb = lab.querySelector('input');
        const thisCard = card;  // `card` changes as the loop goes on
        cb.checked = done.has(a.id);
        thisCard.classList.toggle('is-done', cb.checked);
        cb.addEventListener('change', () => {
          cb.checked ? done.add(a.id) : done.delete(a.id);
          store.set(KEY, Array.from(done));
          thisCard.classList.toggle('is-done', cb.checked);
          refreshProgress();
        });
      } else {
        card.classList.add('lesson');
      }
      if (group) group.cards.push(card);
      return;
    }
    if (n.tagName === 'HR' && card) { n.remove(); card = null; return; }
    if (card) card.appendChild(n);
  });

  // 2. Inside each card: answer box (practice mode + speech) and collapsible follow-ups.
  const ANSWER_LABELS = ['Answer (English)', 'How to say it (English)', 'Say while coding (English)'];
  document.querySelectorAll('section.q').forEach(c => {
    Array.from(c.children).forEach(p => {
      if (p.tagName !== 'P') return;
      const strong = p.querySelector('strong');
      if (!strong) return;
      const label = strong.textContent.trim().replace(/:$/, '');
      if (ANSWER_LABELS.includes(label)) {
        const box = document.createElement('div');
        box.className = 'answer';
        p.before(box);
        p.classList.add('ans-label');
        box.appendChild(p);
        // Take the following blockquote(s) or text until the next bold label.
        let nx = box.nextElementSibling;
        while (nx && !(nx.tagName === 'P' && nx.querySelector(':scope > strong:first-child') && nx !== p)) {
          const next = nx.nextElementSibling;
          box.appendChild(nx);
          if (nx.tagName === 'BLOCKQUOTE') { if (!next || next.tagName !== 'BLOCKQUOTE') break; }
          nx = next;
        }
        // Bangla copy first, English after: show them side by side on wide screens.
        const quotes = Array.from(box.querySelectorAll(':scope > blockquote'));
        const bnQuotes = quotes.filter(q => q.textContent.trim().normalize('NFC').startsWith('বাংলায়'.normalize('NFC')));
        bnQuotes.forEach(q => q.classList.add('bn'));
        if (bnQuotes.length && quotes.length > bnQuotes.length) {
          const pair = document.createElement('div');
          pair.className = 'pair';
          quotes[0].before(pair);
          quotes.forEach(q => pair.appendChild(q));
          strong.textContent = label.replace('(English)', '').trim() + ' — আগে বাংলা, তারপর English';
        }
        const tools = document.createElement('div');
        tools.className = 'ans-tools';
        tools.innerHTML = '<button class="btn reveal">👀 উত্তর দেখুন</button><button class="btn speak">🔊 শুনুন</button>';
        box.appendChild(tools);
        tools.querySelector('.reveal').onclick = () => box.classList.add('shown');
        tools.querySelector('.speak').onclick = () => speak(box);
      } else if (label === 'Follow-up') {
        const list = p.nextElementSibling;
        if (!list || (list.tagName !== 'UL' && list.tagName !== 'OL')) return;
        const d = document.createElement('details');
        d.className = 'fu';
        d.open = !document.body.classList.contains('practice');
        d.innerHTML = '<summary>Follow-up প্রশ্ন (' + list.children.length + ')</summary>';
        p.replaceWith(d);
        d.appendChild(list);
      }
    });
  });

  function speak(box){
    if (!('speechSynthesis' in window)) { alert('এই browser-এ speech নেই।'); return; }
    speechSynthesis.cancel();
    const text = Array.from(box.querySelectorAll('blockquote:not(.bn)')).map(b => b.innerText).join(' ').replace(/[“”"]/g, '');
    const u = new SpeechSynthesisUtterance(text || box.innerText);
    u.lang = 'en-US'; u.rate = 0.9;
    const v = speechSynthesis.getVoices().find(v => /en[-_](US|GB)/.test(v.lang));
    if (v) u.voice = v;
    speechSynthesis.speak(u);
  }

  // 2b. Decorate: part banners, ID and priority badges, labelled blocks.
  groups.forEach(g => {
    if (!g.isPart) return;
    const a = g.el.querySelector('a[id]');
    const m = g.el.textContent.match(/^\s*(Part\s+\w+)\s*—\s*(.*)$/);
    if (!m) return;
    g.el.className = 'part-banner';
    g.el.innerHTML = '';
    g.el.appendChild(a);
    const label = m[1].replace(/^Part\s+/, '');
    g.el.insertAdjacentHTML('beforeend', '<span class="num"></span><span class="eyebrow"></span><span class="pt"></span><span class="pbar"><i><b></b></i><em></em></span>');
    g.el.querySelector('.num').textContent = /^\d$/.test(label) ? '0' + label : label;
    g.el.querySelector('.eyebrow').textContent = m[1];
    g.bannerBar = g.el.querySelector('.pbar b');
    g.bannerText = g.el.querySelector('.pbar em');
    g.el.querySelector('.pt').textContent = m[2];
    g.title = m[1] + ' — ' + m[2];
  });
  const PRI = { '★': 'star', '◆': 'dia', '○': 'ring' };
  document.querySelectorAll('section.q[data-id] .q-head h3').forEach(h => {
    const a = h.querySelector('a[id]');
    const m = h.textContent.match(/^\s*([A-Z][\w-]*)\.\s*([★◆○])?\s*(.*)$/s);
    if (!m) return;
    h.innerHTML = '';
    if (a) h.appendChild(a);
    h.insertAdjacentHTML('beforeend', '<span class="qid"></span>' + (m[2] ? '<span class="pri ' + PRI[m[2]] + '">' + m[2] + '</span>' : '') + '<span class="q-title"></span>');
    h.querySelector('.qid').textContent = m[1];
    h.querySelector('.q-title').textContent = m[3];
  });
  const LABEL_CLASS = { 'বুঝে নিন': 'label-learn', 'Key words': 'keywords', 'ভুল করবেন না': 'warn', 'আরও দেখুন': 'see-also', 'সহজ উদাহরণ': 'example' };
  document.querySelectorAll('section.q').forEach(c => {
    let meta = null;
    Array.from(c.children).forEach(p => {
      const s = p.tagName === 'P' && p.querySelector(':scope > strong:first-child');
      const label = s ? s.textContent.trim().replace(/:$/, '').normalize('NFC') : '';
      if (label === 'প্রশ্নটা মানে' || label === 'অন্যভাবেও জিজ্ঞেস করে') {
        if (!meta) { meta = document.createElement('div'); meta.className = 'meta'; p.before(meta); }
        meta.appendChild(p);
        return;
      }
      meta = null;
      const cls = Object.keys(LABEL_CLASS).find(k => k.normalize('NFC') === label);
      if (cls) p.classList.add(LABEL_CLASS[cls]);
    });
  });

  // 3. Sidebar.
  const side = document.getElementById('side');
  const openGroups = new Set(store.get('aip-open-v1', []));
  groups.forEach(g => {
    const qs = g.cards.filter(c => c.dataset.id);
    const wrap = document.createElement('div');
    wrap.className = 'grp';
    const btn = document.createElement('button');
    btn.className = 'grp-title';
    btn.innerHTML = '<span></span><span class="count"></span>';
    btn.firstChild.textContent = g.title;
    wrap.appendChild(btn);
    g.navCount = btn.lastChild;
    g.qs = qs;
    if (qs.length) {
      const ul = document.createElement('ul');
      qs.forEach(c => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + c.dataset.id;
        const h = c.querySelector('h3'), qid = h.querySelector('.qid'), pri = h.querySelector('.pri');
        if (qid) {
          a.innerHTML = '<b class="nid"></b>' + (pri ? '<b class="pri-mini ' + pri.className.split(' ')[1] + '">' + pri.textContent + '</b>' : '') + '<span></span>';
          a.querySelector('.nid').textContent = qid.textContent;
          a.querySelector('span').textContent = h.querySelector('.q-title').textContent;
        } else {
          a.textContent = h.textContent.trim();
        }
        a.dataset.for = c.dataset.id;
        li.appendChild(a); ul.appendChild(li);
        c.navLink = a; c.navLi = li;
      });
      wrap.appendChild(ul);
      // Groups start closed; the viewer's opened groups are remembered.
      wrap.classList.toggle('closed', !openGroups.has(g.id));
      btn.onclick = () => {
        wrap.classList.toggle('closed');
        wrap.classList.contains('closed') ? openGroups.delete(g.id) : openGroups.add(g.id);
        store.set('aip-open-v1', Array.from(openGroups));
      };
    } else {
      btn.onclick = () => go(g.id);
    }
    g.navWrap = wrap;
    side.appendChild(wrap);
  });
  // Part titles also jump to the part.
  side.querySelectorAll('.grp-title').forEach((b, i) => b.addEventListener('dblclick', () => go(groups[i].id)));

  // 4. Progress.
  const allQs = Array.from(document.querySelectorAll('section.q[data-id]'));
  function refreshProgress(){
    const n = allQs.filter(c => done.has(c.dataset.id)).length;
    document.getElementById('progressBar').style.width = (100 * n / allQs.length) + '%';
    document.getElementById('heroBar').style.width = (100 * n / allQs.length) + '%';
    const stars = allQs.filter(c => c.dataset.pri === 'star');
    const sDone = stars.filter(c => done.has(c.dataset.id)).length;
    document.getElementById('statTotal').textContent = allQs.length;
    document.getElementById('statDone').textContent = n;
    document.getElementById('statStar').textContent = sDone + '/' + stars.length;
    groups.forEach(g => {
      if (!g.bannerBar || !g.qs.length) return;
      const k = g.qs.filter(c => done.has(c.dataset.id)).length;
      g.bannerBar.style.width = (100 * k / g.qs.length) + '%';
      g.bannerText.textContent = k + ' / ' + g.qs.length + ' পারি';
    });
    groups.forEach(g => { if (g.qs.length) g.navCount.textContent = g.qs.filter(c => done.has(c.dataset.id)).length + '/' + g.qs.length; });
    allQs.forEach(c => c.navLink && c.navLink.classList.toggle('done', done.has(c.dataset.id)));
  }
  refreshProgress();

  // 5. Filters and search.
  let filter = 'all';
  const search = document.getElementById('search');
  function applyFilter(){
    const q = search.value.trim().toLowerCase();
    let shown = 0;
    allQs.forEach(c => {
      const p = c.dataset.pri;
      let ok = filter === 'all' || (filter === 'star' && p === 'star') || (filter === 'dia' && (p === 'star' || p === 'dia')) || (filter === 'todo' && !done.has(c.dataset.id));
      if (ok && q) ok = c.dataset.id === q || c.textContent.toLowerCase().includes(q);
      c.classList.toggle('hidden', !ok);
      if (c.navLi) c.navLi.classList.toggle('hidden', !ok);
      if (ok) shown++;
    });
    const filtering = filter !== 'all' || q;
    // While filtering, hide lessons and non-question blocks, and open the sidebar groups.
    document.querySelectorAll('section.q.lesson').forEach(l => l.classList.toggle('hidden', !!filtering));
    groups.forEach(g => {
      const any = g.qs.some(c => !c.classList.contains('hidden'));
      g.navWrap.classList.toggle('hidden', !!filtering && !any);
      if (filtering && any) g.navWrap.classList.remove('closed');
      // Free text under a heading (not in a card) is hidden while filtering.
      let n = g.el.nextElementSibling;
      while (n && n.tagName !== 'H2') {
        if (!n.matches('section.q')) n.classList.toggle('hidden', !!filtering);
        n = n.nextElementSibling;
      }
      g.el.classList.toggle('hidden', !!filtering && !any);
    });
    document.getElementById('empty').style.display = shown ? 'none' : 'block';
  }
  document.querySelectorAll('.chip').forEach(ch => ch.onclick = () => {
    filter = ch.dataset.f;
    document.querySelectorAll('.chip').forEach(x => x.setAttribute('aria-pressed', x === ch));
    applyFilter();
  });
  search.addEventListener('input', applyFilter);

  function clearFilters(){
    if (filter === 'all' && !search.value) return;
    filter = 'all'; search.value = '';
    document.querySelectorAll('.chip').forEach(x => x.setAttribute('aria-pressed', x.dataset.f === 'all'));
    applyFilter();
  }

  // 6. Links always work: clear filters if the target is hidden, then scroll.
  function go(id, push){
    const el = document.getElementById(id);
    if (!el) return false;
    if (document.body.classList.contains('drill-mode')) setMode('read');
    if (el.closest('.hidden')) clearFilters();
    if (innerWidth <= 640) { document.body.classList.add('compact'); jumping = Date.now(); }
    const target = el.closest('section.q') || el.closest('h2') || el;
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (push !== false) history.pushState(null, '', '#' + id);
    document.body.classList.remove('nav-open');
    return true;
  }
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = decodeURIComponent(a.getAttribute('href').slice(1));
    if (id && go(id)) e.preventDefault();
  });
  window.addEventListener('popstate', () => { const id = location.hash.slice(1); if (id) go(id, false); });
  if (location.hash) setTimeout(() => go(decodeURIComponent(location.hash.slice(1)), false), 50);

  // 7. Highlight the current question in the sidebar.
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting || !en.target.navLink) return;
      side.querySelectorAll('a.active').forEach(x => x.classList.remove('active'));
      en.target.navLink.classList.add('active');
    });
  }, { rootMargin: '-80px 0px -70% 0px' });
  allQs.forEach(c => io.observe(c));

  // 8. Practice mode, theme, menu, back to top.
  const practiceBtn = document.getElementById('practiceBtn');
  function setPractice(on){
    document.body.classList.toggle('practice', on);
    practiceBtn.setAttribute('aria-pressed', on);
    document.querySelectorAll('details.fu').forEach(d => d.open = !on);
    document.querySelectorAll('.answer.shown').forEach(b => b.classList.remove('shown'));
    store.set('aip-practice', on);
  }
  practiceBtn.onclick = () => setPractice(!document.body.classList.contains('practice'));
  setPractice(store.get('aip-practice', false));

  const themeBtn = document.getElementById('themeBtn');
  const savedTheme = store.get('aip-theme', null);
  if (savedTheme) document.documentElement.dataset.theme = savedTheme;
  themeBtn.onclick = () => {
    const dark = document.documentElement.dataset.theme
      ? document.documentElement.dataset.theme === 'dark'
      : matchMedia('(prefers-color-scheme: dark)').matches;
    const next = dark ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    store.set('aip-theme', next);
  };
  document.getElementById('menuBtn').onclick = () => document.body.classList.toggle('nav-open');
  main.addEventListener('click', () => document.body.classList.remove('nav-open'));
  document.getElementById('toTop').onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });

  // Hero buttons, plan cards, code copy.
  document.getElementById('ctaRead').onclick = () => go('how-to-use');
  document.getElementById('ctaDrill').onclick = () => setMode('drill');
  document.querySelectorAll('.plan[data-go]').forEach(b => b.onclick = () => go(b.dataset.go));
  document.querySelectorAll('main pre').forEach(pre => {
    const box = document.createElement('div');
    box.className = 'codebox';
    const code = pre.querySelector('code');
    const lang = code && (code.className.match(/language-([\w+-]+)/) || [])[1];
    box.innerHTML = '<div class="code-head"><span></span><button class="copy">Copy</button></div>';
    box.querySelector('span').textContent = lang || 'code';
    pre.before(box);
    box.appendChild(pre);
    const btn = box.querySelector('.copy');
    btn.onclick = () => {
      const done = () => { btn.textContent = 'Copied ✓'; setTimeout(() => btn.textContent = 'Copy', 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(pre.innerText).then(done, () => {});
    };
  });

  // On small screens, hide search and filters while scrolling down; show them when scrolling up.
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY, small = innerWidth <= 640;
    if (Date.now() - jumping < 1200) { lastY = y; return; }
    if (!small || document.activeElement === search) { document.body.classList.remove('compact'); lastY = y; return; }
    if (y > lastY + 8 && y > 200) document.body.classList.add('compact');
    else if (y < lastY - 8) document.body.classList.remove('compact');
    lastY = y;
  }, { passive: true });

  // 9. Previous / next links under every question.
  allQs.forEach((c, i) => {
    const pager = document.createElement('div');
    pager.className = 'pager';
    const link = (q, label) => {
      if (!q) return '<span></span>';
      const id = q.querySelector('.qid') ? q.querySelector('.qid').textContent : q.dataset.id;
      return '<a href="#' + q.dataset.id + '">' + label.replace('%', id) + '</a>';
    };
    pager.innerHTML = link(allQs[i - 1], '← %') + link(allQs[i + 1], '% →');
    c.appendChild(pager);
  });

  // 10. Interview page: one question at a time, like a flashcard.
  const drill = document.getElementById('drill');
  const scopeSel = document.getElementById('drillScope');
  const drillCard = document.getElementById('drillCard');
  const scopes = [['star', '★ ৭ দিনের প্রশ্ন'], ['dia', '★◆ ১০ দিনের প্রশ্ন'], ['all', 'সব প্রশ্ন'], ['todo', 'যেগুলো এখনো "পারি" হয়নি']];
  scopes.forEach(([v, t]) => scopeSel.add(new Option(t, v)));
  groups.filter(g => g.qs.length && g.isPart).forEach(g => scopeSel.add(new Option(g.title, 'part:' + g.id)));
  scopeSel.value = store.get('aip-drill-scope', 'star');
  if (!scopeSel.value) scopeSel.value = 'star';
  let deck = [], pos = 0;
  function buildDeck(){
    const s = scopeSel.value;
    let list = allQs;
    if (s === 'star') list = allQs.filter(c => c.dataset.pri === 'star');
    else if (s === 'dia') list = allQs.filter(c => c.dataset.pri === 'star' || c.dataset.pri === 'dia');
    else if (s === 'todo') list = allQs.filter(c => !done.has(c.dataset.id));
    else if (s.startsWith('part:')) list = (groups.find(g => g.id === s.slice(5)) || { qs: [] }).qs;
    deck = list.map(c => c.dataset.id);
    for (let i = deck.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [deck[i], deck[j]] = [deck[j], deck[i]]; }
    pos = 0;
    store.set('aip-drill-scope', s);
    showCard();
  }
  function showCard(){
    drillCard.classList.remove('revealed');
    const count = document.getElementById('drillCount');
    if (pos >= deck.length) {
      drillCard.innerHTML = '<div class="drill-done"><h3>🎉 এই সেট শেষ!</h3><p>আবার শুরু করতে উপরের তালিকা থেকে একটা সেট বেছে নিন।</p></div>';
      count.textContent = deck.length + ' / ' + deck.length;
      return;
    }
    const src = document.getElementById('card-' + deck[pos]);
    count.textContent = (pos + 1) + ' / ' + deck.length + (done.has(deck[pos]) ? '  ·  ✓ আগে পেরেছেন' : '');
    drillCard.innerHTML = '';
    drillCard.appendChild(src.querySelector('.q-head h3').cloneNode(true));
    const meta = src.querySelector('.meta');
    if (meta) drillCard.appendChild(meta.cloneNode(true));
    src.querySelectorAll('.answer').forEach(a => { const n = a.cloneNode(true); n.classList.add('shown'); drillCard.appendChild(n); });
    const after = document.createElement('div');
    after.className = 'after';
    ['p.keywords', 'details.fu', 'p.warn'].forEach(sel => { const n = src.querySelector(sel); if (n) after.appendChild(n.cloneNode(true)); });
    after.querySelectorAll('details').forEach(d => d.open = false);
    drillCard.appendChild(after);
    drillCard.querySelectorAll('[id]').forEach(n => n.removeAttribute('id'));
  }
  function next(){ pos++; showCard(); window.scrollTo({ top: 0 }); }
  document.getElementById('dReveal').onclick = () => drillCard.classList.add('revealed');
  document.getElementById('dSpeak').onclick = () => { drillCard.classList.add('revealed'); speak(drillCard.querySelector('.answer') || drillCard); };
  document.getElementById('dAgain').onclick = () => { if (pos < deck.length) deck.push(deck[pos]); next(); };
  document.getElementById('dKnow').onclick = () => {
    const id = deck[pos];
    if (id && !done.has(id)) {
      const cb = document.querySelector('#card-' + id + ' .done-box input');
      cb.checked = true;
      cb.dispatchEvent(new Event('change'));
    }
    next();
  };
  document.getElementById('dRead').onclick = () => { const id = deck[pos]; setMode('read'); if (id) setTimeout(() => go(id), 30); };
  scopeSel.onchange = buildDeck;
  document.addEventListener('keydown', e => {
    if (!document.body.classList.contains('drill-mode') || e.target.matches('input,select,textarea')) return;
    if (e.key === ' ') { e.preventDefault(); drillCard.classList.add('revealed'); }
    if (e.key === 'ArrowRight') next();
  });
  function setMode(mode){
    const isDrill = mode === 'drill';
    document.body.classList.toggle('drill-mode', isDrill);
    drill.hidden = !isDrill;
    document.getElementById('tabRead').setAttribute('aria-pressed', !isDrill);
    document.getElementById('tabDrill').setAttribute('aria-pressed', isDrill);
    store.set('aip-mode', mode);
    if (isDrill) { buildDeck(); window.scrollTo({ top: 0 }); }
  }
  document.getElementById('tabRead').onclick = () => setMode('read');
  document.getElementById('tabDrill').onclick = () => setMode('drill');
  if (location.hash === '#interview' || (!location.hash && store.get('aip-mode', 'read') === 'drill')) setMode('drill');
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
