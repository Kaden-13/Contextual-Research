/* Draws the accessibility annotation layer on top of a wireframe.
   Everything is read from the real markup, so annotations cannot drift from the HTML:
   1. Landmarks (header, nav, main, aside, footer, labelled sections) get an outline and a tag.
   2. Every keyboard focusable element gets a numbered badge in DOM (tab) order.
   3. Key ARIA states and live regions get a yellow callout.
   Load the page with ?annotate to turn the layer on. */
(function () {
  if (!location.search.includes("annotate")) return;
  document.body.classList.add("wf-annotated");
  const layer = document.createElement("div");
  layer.setAttribute("aria-hidden", "true");
  layer.style.cssText = "position:absolute;left:0;top:0;width:100%;pointer-events:none;z-index:999";
  document.body.appendChild(layer);
  const box = (el) => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
  const tag = (x, y, text, css) => { const t = document.createElement("div"); t.textContent = text;
    t.style.cssText = `position:absolute;left:${x}px;top:${y}px;font:600 11px/1.25 Inter,Arial,sans-serif;padding:2px 5px;white-space:nowrap;${css}`;
    layer.appendChild(t); return t; };

  // 1. Landmarks
  const LM = { HEADER: ["banner", "#0B5CAD"], NAV: ["navigation", "#7A1FA2"], MAIN: ["main", "#0A7A3E"], ASIDE: ["complementary", "#B35C00"], FOOTER: ["contentinfo", "#0B5CAD"], SECTION: ["region", "#555555"], FORM: ["search", "#7A1FA2"] };
  document.querySelectorAll("header.site, nav, main, aside, footer.site, section[aria-labelledby], form[role=search]").forEach((el) => {
    const [role, color] = LM[el.tagName]; const b = box(el);
    const o = document.createElement("div");
    o.style.cssText = `position:absolute;left:${b.x - 3}px;top:${b.y - 3}px;width:${b.w + 6}px;height:${b.h + 6}px;border:2.5px dashed ${color}`;
    layer.appendChild(o);
    let name = el.getAttribute("aria-label");
    if (!name && el.getAttribute("aria-labelledby")) name = document.getElementById(el.getAttribute("aria-labelledby")).textContent.trim();
    const explicitRole = el.getAttribute("role");
    const label = `<${el.tagName.toLowerCase()}> role=${explicitRole || role}${name ? ` "${name}"` : ""}`;
    tag(b.x - 3, b.y - 19, label, `background:${color};color:#fff`);
  });

  // 2. Tab order
  const sel = 'a[href], button:not([disabled]), input:not([type=hidden]):not([disabled]), select, textarea, summary, [tabindex="0"]';
  let n = 0; const order = [];
  document.querySelectorAll(sel).forEach((el) => {
    const b = box(el); if (!b.w || !b.h) return;
    n += 1; order.push(n);
    tag(b.x - 12, b.y - 10, String(n), "background:#D00000;color:#fff;border-radius:10px;min-width:12px;text-align:center;font-size:11px");
  });

  // 3. ARIA states and live regions
  const attrs = ["aria-current", "aria-expanded", "aria-live", "aria-haspopup"];
  document.querySelectorAll("[aria-current],[aria-expanded],[aria-live],[role=status],[role=alert],[aria-haspopup]").forEach((el) => {
    if (el.closest('[aria-hidden="true"]')) return;
    const parts = [];
    const r = el.getAttribute("role"); if (r === "status" || r === "alert") parts.push(`role=${r}`);
    attrs.forEach((a) => { if (el.hasAttribute(a)) parts.push(`${a}="${el.getAttribute(a)}"`); });
    if (!parts.length) return;
    const b = box(el);
    const css = "background:#FFE45C;color:#1a1a1a;border:1px solid #1a1a1a";
    if (el.hasAttribute("aria-current")) tag(b.x, b.y + b.h - 4, parts.join("  "), css);
    else if (b.w > 400) tag(b.x + b.w, b.y - 9, parts.join("  "), css + ";transform:translateX(-100%)");
    else tag(b.x + b.w + 4, b.y + Math.max(0, b.h / 2 - 9), parts.join("  "), css);
  });

  window.__tabCount = n;
})();
