#!/usr/bin/env python3
"""
Generate theme-aware animated profile hero banners (dark.svg & light.svg) for Ashwin R.

Identity: Cybersecurity Enthusiast & Full-Stack Developer Profile.
Features:
- Cyber Command Center HUD aesthetic with navy/cyan/emerald/violet matrix glow.
- Left Panel: Cyber Security System Matrix & Tech Nodes (Flutter AppSec, React WebSec, MongoDB DB Vault, Node.js JWT/RBAC, Python Sec Scripts, Java Crypt DSA).
- XML Valid: All text nodes escaped with html.escape for 100% SVG/XML compliance.
"""
import os, sys, html

THEMES = {
    "dark": {
        "BG": "#070B16",
        "PANEL": "#0A101F",
        "PANEL_CARD": "#0C1426",
        "HEADER_BG": "#0B1222",
        "CYAN": "#22D3EE",
        "CYAN_GLOW": "rgba(34,211,238,0.4)",
        "VIOLET": "#A78BFA",
        "VIOLET2": "#7C3AED",
        "EMERALD": "#10B981",
        "TEXT": "#F8FAFC",
        "MUTED": "#94A3B8",
        "DIM": "#475569",
        "STROKE": "rgba(34,211,238,0.30)",
        "STROKE_HI": "rgba(34,211,238,0.65)",
        "BARLINE": "rgba(255,255,255,0.08)",
        "PILL_BG": "rgba(124,58,237,0.25)",
        "PILL_STROKE": "rgba(167,139,250,0.45)",
        "NODE_BG": "#0E172A",
        "NODE_STROKE": "rgba(34,211,238,0.25)",
        "SHIELD_FILL": "rgba(16,185,129,0.15)",
    },
    "light": {
        "BG": "#F1F5F9",
        "PANEL": "#FFFFFF",
        "PANEL_CARD": "#F8FAFC",
        "HEADER_BG": "#E2E8F0",
        "CYAN": "#0891B2",
        "CYAN_GLOW": "rgba(8,145,178,0.3)",
        "VIOLET": "#7C3AED",
        "VIOLET2": "#6D28D9",
        "EMERALD": "#059669",
        "TEXT": "#0F172A",
        "MUTED": "#475569",
        "DIM": "#94A3B8",
        "STROKE": "rgba(8,145,178,0.35)",
        "STROKE_HI": "rgba(8,145,178,0.65)",
        "BARLINE": "rgba(0,0,0,0.08)",
        "PILL_BG": "rgba(124,58,237,0.12)",
        "PILL_STROKE": "rgba(124,58,237,0.35)",
        "NODE_BG": "#F1F5F9",
        "NODE_STROKE": "rgba(8,145,178,0.30)",
        "SHIELD_FILL": "rgba(5,150,105,0.15)",
    }
}

W = 1180
H = 610
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

def esc(s):
    return html.escape(str(s), quote=True)

def generate_cyber_panel(theme_cfg):
    """
    Generate Left Panel: Cyber Security Command HUD + Interactive Security Tech Nodes.
    """
    out = []
    a = out.append

    # Panel Header Inside Left Box
    a(f'<text x="200" y="32" text-anchor="middle" font-size="11" letter-spacing="2.5" font-weight="700" fill="{theme_cfg["CYAN"]}">CYBER.OPS // THREAT &amp; TECH MATRIX</text>')

    # Cyber HUD Top Security Status Bar
    a(f'<g transform="translate(20, 44)">')
    a(f'  <rect width="360" height="26" rx="6" fill="{theme_cfg["NODE_BG"]}" stroke="{theme_cfg["NODE_STROKE"]}"/>')
    a(f'  <circle cx="15" cy="13" r="4" fill="{theme_cfg["EMERALD"]}">'
      f'    <animate attributeName="opacity" values="1;0.3;1" dur="1.6s" repeatCount="indefinite"/>'
      f'  </circle>')
    a(f'  <text x="26" y="17" font-size="9.5" font-weight="700" fill="{theme_cfg["EMERALD"]}">SECURE NODE <tspan fill="{theme_cfg["MUTED"]}">| AES-256 | OWASP: AUDITED</tspan></text>')
    a(f'</g>')

    # Central Cyber Security HUD Core (Center: cx=200, cy=155)
    cx, cy = 200, 155

    a(f'<g transform="translate({cx},{cy})">')
    
    # Outer Rotating HUD Segmented Ring
    a(f'  <circle cx="0" cy="0" r="62" fill="none" stroke="{theme_cfg["CYAN"]}" stroke-width="1.2" stroke-dasharray="8,5,15,5" opacity="0.65">')
    a(f'    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>')
    a(f'  </circle>')

    # Counter-Rotating Inner Tech Ring
    a(f'  <circle cx="0" cy="0" r="48" fill="none" stroke="{theme_cfg["VIOLET"]}" stroke-width="1" stroke-dasharray="4,4" opacity="0.6">')
    a(f'    <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>')
    a(f'  </circle>')

    # Pulsing Center Cyber Shield
    a(f'  <path d="M 0,-28 L 22,-14 L 22,12 L 0,28 L -22,12 L -22,-14 Z" fill="{theme_cfg["SHIELD_FILL"]}" stroke="{theme_cfg["CYAN"]}" stroke-width="2">')
    a(f'    <animate attributeName="stroke" values="{theme_cfg["CYAN"]};{theme_cfg["EMERALD"]};{theme_cfg["CYAN"]}" dur="3s" repeatCount="indefinite"/>')
    a(f'  </path>')
    
    # Lock Symbol inside Shield
    a(f'  <rect x="-7" y="-2" width="14" height="12" rx="2" fill="{theme_cfg["CYAN"]}"/>')
    a(f'  <path d="M -5,-2 A 5 5 0 0 1 5,-2" fill="none" stroke="{theme_cfg["CYAN"]}" stroke-width="2"/>')
    a(f'  <circle cx="0" cy="4" r="2" fill="{theme_cfg["PANEL"]}"/>')

    # Scanning Laser Bar passing through core
    a(f'  <line x1="-55" y1="0" x2="55" y2="0" stroke="{theme_cfg["EMERALD"]}" stroke-width="1.5" opacity="0.8">')
    a(f'    <animateTransform attributeName="transform" type="translate" values="0 -45; 0 45; 0 -45" dur="3s" repeatCount="indefinite"/>')
    a(f'    <animate attributeName="opacity" values="0.2;0.9;0.2" dur="3s" repeatCount="indefinite"/>')
    a(f'  </line>')

    # Corner Crosshairs
    a(f'  <line x1="-66" y1="0" x2="-58" y2="0" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="58" y1="0" x2="66" y2="0" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="0" y1="-66" x2="0" y2="-58" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="0" y1="58" x2="0" y2="66" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')

    a(f'</g>')

    # Connections from Core to Node Grid
    a(f'<path d="M 200,220 L 200,235 M 200,235 L 105,250 M 200,235 L 295,250" stroke="{theme_cfg["STROKE"]}" stroke-width="1.2" stroke-dasharray="3,3"/>')

    # ==================== TECH & SECURITY NODES GRID (2x3 Matrix) ====================
    nodes = [
        ("Flutter", "App Security", "#02569B", "flutter", 20, 248, "0.2s"),
        ("React", "Web Security", "#61DAFB", "react", 205, 248, "0.35s"),
        ("MongoDB", "NoSQL Vault", "#13AA52", "mongodb", 20, 324, "0.50s"),
        ("Node.js", "JWT & Auth", "#68A063", "nodejs", 205, 324, "0.65s"),
        ("Python", "Sec Scripts", "#3776AB", "python", 20, 400, "0.80s"),
        ("Java & DSA", "Algorithms", "#F89820", "java", 205, 400, "0.95s"),
    ]

    for name, cat, col, icon_t, nx, ny, delay in nodes:
        a(f'<g opacity="0" transform="translate({nx}, {ny})">')
        a(f'  <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay}" fill="freeze"/>')
        
        # Node Box Shell
        a(f'  <rect width="175" height="64" rx="8" fill="{theme_cfg["NODE_BG"]}" stroke="{theme_cfg["NODE_STROKE"]}">'
          f'    <animate attributeName="stroke" values="{theme_cfg["NODE_STROKE"]};{theme_cfg["STROKE_HI"]};{theme_cfg["NODE_STROKE"]}" dur="3.5s" begin="{delay}" repeatCount="indefinite"/>'
          f'  </rect>')

        # Icon Container (Left side of node box)
        a(f'  <g transform="translate(26, 32)">')
        
        if icon_t == "flutter":
            a(f'    <path d="M 6,-14 L 14,-14 L 0,0 L 14,14 L 6,14 L -8,0 Z" fill="#54C5F8"/>')
            a(f'    <path d="M 0,0 L 6,-6 L 14,-6 L 8,0 Z" fill="#01579B"/>')
            a(f'    <path d="M 0,0 L 6,6 L 14,6 L 8,0 Z" fill="#02569B"/>')

        elif icon_t == "react":
            a(f'    <circle cx="0" cy="0" r="3.5" fill="#61DAFB"/>')
            a(f'    <g>')
            a(f'      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>')
            a(f'      <ellipse cx="0" cy="0" rx="15" ry="5.5" fill="none" stroke="#61DAFB" stroke-width="1.4"/>')
            a(f'      <ellipse cx="0" cy="0" rx="15" ry="5.5" fill="none" stroke="#61DAFB" stroke-width="1.4" transform="rotate(60)"/>')
            a(f'      <ellipse cx="0" cy="0" rx="15" ry="5.5" fill="none" stroke="#61DAFB" stroke-width="1.4" transform="rotate(120)"/>')
            a(f'    </g>')

        elif icon_t == "mongodb":
            a(f'    <path d="M 0,-15 C 6,-6 10,2 0,16 C -10,2 -6,-6 0,-15 Z" fill="#13AA52"/>')
            a(f'    <path d="M 0,-15 C 2,-6 5,2 0,16 Z" fill="#3F2A1D" opacity="0.3"/>')
            a(f'    <line x1="0" y1="-14" x2="0" y2="15" stroke="#FFFFFF" stroke-width="0.9" opacity="0.8"/>')

        elif icon_t == "nodejs":
            a(f'    <polygon points="0,-14 12,-7 12,7 0,14 -12,7 -12,-7" fill="#68A063"/>')
            a(f'    <path d="M -4,-4 L -4,4 L 0,6 L 4,4 L 4,-4 Z" fill="{theme_cfg["PANEL"]}"/>')
            a(f'    <circle cx="0" cy="0" r="2.5" fill="#68A063"/>')

        elif icon_t == "python":
            a(f'    <path d="M -2,-14 C -8,-14 -12,-10 -12,-5 C -12,0 -8,0 -8,0 L 0,0 L 0,-4 L -6,-4 C -6,-4 -8,-4 -8,-6 C -8,-8 -6,-10 -2,-10 L 4,-10 L 4,-14 Z" fill="#3776AB"/>')
            a(f'    <path d="M 2,14 C 8,14 12,10 12,5 C 12,0 8,0 8,0 L 0,0 L 0,4 L 6,4 C 6,4 8,4 8,6 C 8,8 6,10 2,10 L -4,10 L -4,14 Z" fill="#FFD43B"/>')
            a(f'    <circle cx="-4" cy="-10" r="1.2" fill="#FFFFFF"/>')
            a(f'    <circle cx="4" cy="10" r="1.2" fill="#FFFFFF"/>')

        elif icon_t == "java":
            a(f'    <path d="M -8,2 L 6,2 L 4,11 C 4,13 -4,13 -6,11 Z" fill="none" stroke="#F89820" stroke-width="1.6"/>')
            a(f'    <path d="M 6,4 C 9,4 9,8 6,8" fill="none" stroke="#F89820" stroke-width="1.4"/>')
            a(f'    <path d="M -4,-3 C -2,-6 -6,-9 -3,-12" fill="none" stroke="#5382A1" stroke-width="1.4"/>')
            a(f'    <path d="M 1,-3 C 3,-6 -1,-9 2,-12" fill="none" stroke="#E24E42" stroke-width="1.4"/>')

        a(f'  </g>')

        # Node Labels & Status Indicator (Fully Escaped)
        a(f'  <text x="48" y="27" font-size="12" font-weight="800" fill="{theme_cfg["TEXT"]}">{esc(name)}</text>')
        a(f'  <text x="48" y="44" font-size="9.5" font-weight="600" fill="{col}">{esc(cat)}</text>')
        
        # Cyber Active Pulse Dot
        a(f'  <circle cx="160" cy="16" r="3" fill="{theme_cfg["CYAN"]}">'
          f'    <animate attributeName="opacity" values="1;0.2;1" dur="2s" begin="{delay}" repeatCount="indefinite"/>'
          f'  </circle>')

        a(f'</g>')

    return "".join(out)

def generate_svg(theme_name):
    t = THEMES[theme_name]
    gid = f"accent_b_{theme_name}"
    
    s = []
    a = s.append

    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-label="Ashwin R Cybersecurity Profile Banner">')
    
    # Definitions & Gradients
    a('<defs>')
    a(f'  <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">')
    a(f'    <stop offset="0" stop-color="{t["VIOLET2"]}"><animate attributeName="stop-color" values="{t["VIOLET2"]};{t["CYAN"]};{t["EMERALD"]};{t["VIOLET2"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'    <stop offset="0.5" stop-color="{t["CYAN"]}"><animate attributeName="stop-color" values="{t["CYAN"]};{t["EMERALD"]};{t["VIOLET2"]};{t["CYAN"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'    <stop offset="1" stop-color="{t["EMERALD"]}"><animate attributeName="stop-color" values="{t["EMERALD"]};{t["VIOLET2"]};{t["CYAN"]};{t["EMERALD"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'  </linearGradient>')
    
    a(f'  <clipPath id="winClip"><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18"/></clipPath>')
    a('</defs>')

    # Outer Window Background & Clip
    a(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="{t["BG"]}"/>')
    a(f'<g clip-path="url(#winClip)">')
    
    # Outer Frame Border Gradient Line
    a(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" fill="none" stroke="url(#{gid})" stroke-width="3" opacity="0.8"/>')

    # Window Header Bar
    a(f'<rect x="2" y="2" width="{W-4}" height="46" fill="{t["HEADER_BG"]}"/>')
    a(f'<line x1="2" y1="48" x2="{W-2}" y2="48" stroke="{t["BARLINE"]}"/>')
    
    # Terminal Control Dots
    a(f'<circle cx="30" cy="25" r="5.5" fill="#ff5f56"/>')
    a(f'<circle cx="50" cy="25" r="5.5" fill="#ffbd2e"/>')
    a(f'<circle cx="70" cy="25" r="5.5" fill="#27c93f"/>')
    a(f'<text x="{W/2}" y="29" text-anchor="middle" font-size="12" fill="{t["MUTED"]}">ashwinindira05@gmail.com - % ./cyber-profile.sh --live</text>')

    # ==================== LEFT PANEL (Cyber Security & Tech Vault) ====================
    a(f'<g transform="translate(36, 84)">')
    a(f'  <rect width="400" height="492" rx="12" fill="{t["PANEL"]}" stroke="{t["STROKE"]}">'
      f'    <animate attributeName="stroke" values="{t["STROKE"]};{t["STROKE_HI"]};{t["STROKE"]}" dur="4s" repeatCount="indefinite"/>'
      f'  </rect>')
    a(generate_cyber_panel(t))
    a(f'</g>')

    # ==================== RIGHT PANEL (Cyber & Dev Terminal Info) ====================
    a(f'<g transform="translate(460, 84)">')
    a(f'  <rect width="684" height="492" rx="12" fill="{t["PANEL"]}" stroke="{t["STROKE"]}">'
      f'    <animate attributeName="stroke" values="{t["STROKE"]};{t["STROKE_HI"]};{t["STROKE"]}" dur="4s" begin="1s" repeatCount="indefinite"/>'
      f'  </rect>')
    
    # Right Header
    a(f'  <text x="24" y="32" font-size="11" letter-spacing="2.5" font-weight="700" fill="{t["CYAN"]}">SYSTEM.INFO // CYBER &amp; DEV PROFILE</text>')
    a(f'  <text x="560" y="32" font-size="10" fill="{t["DIM"]}">./ashwin.sh --sec</text>')
    a(f'  <line x1="24" y1="42" x2="660" y2="42" stroke="url(#{gid})" stroke-width="1.5" opacity="0.7"/>')

    # Typewriter Command Line 1: whoami
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.2s" fill="freeze"/>')
    a(f'    <text x="24" y="74" font-size="13" fill="{t["EMERALD"]}">ashwin@sec-box:~$ <tspan fill="{t["CYAN"]}">whoami --verbose</tspan></text>')
    a(f'  </g>')

    # Bio Fields Table (Cybersecurity + Developer focus)
    info_items = [
        ("NAME", "Ashwin R", t["TEXT"], "0.35s"),
        ("ROLE", "B.Tech IT Student | Cybersecurity & Dev Enthusiast", t["VIOLET"], "0.50s"),
        ("BASE", "Trichy, Tamil Nadu, IN 🇮🇳", t["TEXT"], "0.65s"),
        ("FOCUS", "Web/App Sec (OWASP Top 10) • Network Def • Full-Stack", t["CYAN"], "0.80s"),
        ("CORE_STACK", "Flutter • React • MongoDB • Node.js • Python • Java", t["EMERALD"], "0.95s"),
        ("STATUS", "⚡ Seeking Cybersecurity Internships & Dev Collaboration", t["EMERALD"], "1.10s"),
        ("CONTACT", "ashwinindira05@gmail.com", t["VIOLET"], "1.25s"),
    ]

    start_y = 108
    for i, (label, val, col, b_anim) in enumerate(info_items):
        cur_y = start_y + i * 32
        a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{b_anim}" fill="freeze"/>')
        a(f'    <text x="24" y="{cur_y}" font-size="11.5" font-weight="700" fill="{t["MUTED"]}">{esc(label):<11}: </text>')
        a(f'    <text x="135" y="{cur_y}" font-size="11.5" font-weight="600" fill="{col}">{esc(val)}</text>')
        a(f'  </g>')

    # Blinking Terminal Cursor after contact line
    a(f'  <text x="365" y="{start_y + 6 * 32}" font-size="13" font-weight="bold" fill="{t["CYAN"]}">_<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/></text>')

    # Tech & Security Skill Badges Row
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.4s" fill="freeze"/>')
    a(f'    <text x="24" y="348" font-size="10" letter-spacing="1.5" font-weight="700" fill="{t["DIM"]}">CYBER &amp; DEV CAPABILITIES</text>')
    
    tags = ["Flutter", "React", "AppSec", "Node.js", "OWASP", "Python", "Java", "MongoDB", "NetworkDef"]
    tx = 24
    ty = 360
    for tag in tags:
        tw = len(tag) * 7.5 + 16
        if tx + tw > 650:
            tx = 24
            ty += 26
        a(f'    <rect x="{tx}" y="{ty}" width="{tw:.1f}" height="20" rx="10" fill="{t["PILL_BG"]}" stroke="{t["PILL_STROKE"]}"/>')
        a(f'    <text x="{tx + tw/2:.1f}" y="{ty + 13.5}" text-anchor="middle" font-size="10" font-weight="600" fill="{t["VIOLET"]}">{esc(tag)}</text>')
        tx += tw + 8
    a(f'  </g>')

    # Metrics Footer Card inside Right Panel
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="1.55s" fill="freeze"/>')
    a(f'    <rect x="24" y="420" width="636" height="52" rx="10" fill="{t["PANEL_CARD"]}" stroke="{t["BARLINE"]}"/>')
    
    # Metric 1
    a(f'    <text x="44" y="441" font-size="9" font-weight="700" fill="{t["DIM"]}">PINNED REPOS</text>')
    a(f'    <text x="44" y="460" font-size="14" font-weight="800" fill="{t["CYAN"]}">6 Featured</text>')
    a(f'    <line x1="210" y1="430" x2="210" y2="462" stroke="{t["BARLINE"]}"/>')
    
    # Metric 2
    a(f'    <text x="230" y="441" font-size="9" font-weight="700" fill="{t["DIM"]}">SPECIALTY</text>')
    a(f'    <text x="230" y="460" font-size="14" font-weight="800" fill="{t["VIOLET"]}">Cyber &amp; Dev</text>')
    a(f'    <line x1="430" y1="430" x2="430" y2="462" stroke="{t["BARLINE"]}"/>')
    
    # Metric 3
    a(f'    <text x="450" y="441" font-size="9" font-weight="700" fill="{t["DIM"]}">SECURITY STATUS</text>')
    a(f'    <text x="450" y="460" font-size="13" font-weight="800" fill="{t["EMERALD"]}">● AUDITED <tspan font-size="10" font-weight="normal" fill="{t["MUTED"]}">v2.5</tspan></text>')
    a(f'  </g>')

    a(f'</g>')

    a('</g>') # clip-path group
    a('</svg>')

    return "".join(s)

def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out_dir, exist_ok=True)
    
    for theme, fname in [("dark", "dark.svg"), ("light", "light.svg")]:
        svg_content = generate_svg(theme)
        out_path = os.path.join(out_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Generated {out_path} ({theme}): {len(svg_content)//1024} KB")

if __name__ == "__main__":
    main()
