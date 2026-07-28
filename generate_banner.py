#!/usr/bin/env python3
"""
Generate theme-aware animated profile hero banners (dark.svg & light.svg) for Ashwin R.

Features:
- Navy / Cyan / Violet / Emerald dark & light theme palettes matching the profile aesthetics.
- Outer terminal window frame with red/yellow/green control buttons & status title.
- Left Panel: Animated Skill Radar Chart (Pentagon/Hexagon radar grid with skill polygon,
  rotating radar sweep ray, pulsing vertex dots, and percentage badges).
- Right Panel: Typewriter-style terminal info block (whoami, role, location, degree, stack, status, contact),
  tech badge pills row, and dynamic metrics footer bar.
"""
import os, sys, math, html

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
        "STROKE_HI": "rgba(34,211,238,0.60)",
        "BARLINE": "rgba(255,255,255,0.08)",
        "PILL_BG": "rgba(124,58,237,0.25)",
        "PILL_STROKE": "rgba(167,139,250,0.45)",
        "RADAR_GRID": "rgba(34,211,238,0.18)",
        "RADAR_FILL": "url(#radarGradDark)",
        "SWEEP_COLOR": "rgba(34,211,238,0.25)",
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
        "RADAR_GRID": "rgba(8,145,178,0.20)",
        "RADAR_FILL": "url(#radarGradLight)",
        "SWEEP_COLOR": "rgba(8,145,178,0.20)",
    }
}

W = 1180
H = 610
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

def esc(s):
    return html.escape(str(s), quote=True)

def generate_radar(cx, cy, r, theme_cfg):
    """
    Generate the animated skill radar chart SVG elements.
    Axes: 6 skills (Hexagon).
    """
    skills = [
        ("Flutter & Dart", 0.95),
        ("Frontend Web", 0.90),
        ("Node & Express", 0.82),
        ("Java & DSA", 0.85),
        ("Python & Scripts", 0.80),
        ("Database & SQL", 0.78),
    ]
    n = len(skills)
    angles = [-math.pi/2 + i * (2 * math.pi / n) for i in range(n)]
    
    out = []
    a = out.append

    # Outer section header inside panel
    a(f'<text x="{cx}" y="{cy - r - 35}" text-anchor="middle" font-size="11" letter-spacing="2.5" font-weight="700" fill="{theme_cfg["CYAN"]}">VISUAL.MAP // SKILL.RADAR</text>')

    # Concentric Grid Rings (20%, 40%, 60%, 80%, 100%)
    for frac in [0.2, 0.4, 0.6, 0.8, 1.0]:
        pts = []
        for ang in angles:
            px = cx + r * frac * math.cos(ang)
            py = cy + r * frac * math.sin(ang)
            pts.append(f"{px:.1f},{py:.1f}")
        pts_str = " ".join(pts)
        stroke_w = "1.5" if frac == 1.0 else "1"
        dash = "" if frac == 1.0 else 'stroke-dasharray="3,3"'
        a(f'<polygon points="{pts_str}" fill="none" stroke="{theme_cfg["RADAR_GRID"]}" stroke-width="{stroke_w}" {dash}/>')

    # Radial Axis Lines
    for ang in angles:
        ax = cx + r * math.cos(ang)
        ay = cy + r * math.sin(ang)
        a(f'<line x1="{cx}" y1="{cy}" x2="{ax:.1f}" y2="{ay:.1f}" stroke="{theme_cfg["RADAR_GRID"]}" stroke-width="1.2"/>')

    # Radar Rotating Scanner Ray
    a(f'<g transform="translate({cx},{cy})">')
    a(f'  <g>')
    a(f'    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>')
    a(f'    <line x1="0" y1="0" x2="0" y2="{-r}" stroke="{theme_cfg["CYAN"]}" stroke-width="2" opacity="0.8"/>')
    a(f'    <path d="M 0 0 L 0 {-r} A {r} {r} 0 0 1 {r*0.5:.1f} {-r*0.866:.1f} Z" fill="{theme_cfg["SWEEP_COLOR"]}"/>')
    a(f'  </g>')
    a(f'</g>')

    # Skill Polygon calculation
    poly_pts = []
    vertex_coords = []
    for i, (name, val) in enumerate(skills):
        ang = angles[i]
        px = cx + r * val * math.cos(ang)
        py = cy + r * val * math.sin(ang)
        poly_pts.append(f"{px:.1f},{py:.1f}")
        vertex_coords.append((px, py, name, val, ang))

    poly_str = " ".join(poly_pts)

    # Animated Skill Area Polygon
    a(f'<g>')
    a(f'  <polygon points="{poly_str}" fill="{theme_cfg["RADAR_FILL"]}" opacity="0">'
      f'    <animate attributeName="opacity" from="0" to="0.45" dur="1s" begin="0.3s" fill="freeze"/>'
      f'  </polygon>')
    a(f'  <polygon points="{poly_str}" fill="none" stroke="{theme_cfg["CYAN"]}" stroke-width="2.5" stroke-linejoin="round" opacity="0">'
      f'    <animate attributeName="opacity" from="0" to="1" dur="1s" begin="0.3s" fill="freeze"/>'
      f'  </polygon>')
    a(f'</g>')

    # Vertex Nodes & Labels
    for i, (px, py, name, val, ang) in enumerate(vertex_coords):
        b_time = 0.4 + i * 0.1
        # Pulsing vertex node
        a(f'<g opacity="0">')
        a(f'  <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{b_time:.2f}s" fill="freeze"/>')
        a(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{theme_cfg["CYAN"]}">'
          f'    <animate attributeName="r" values="4;8;4" dur="2.4s" begin="{b_time:.2f}s" repeatCount="indefinite"/>'
          f'    <animate attributeName="opacity" values="0.9;0.2;0.9" dur="2.4s" begin="{b_time:.2f}s" repeatCount="indefinite"/>'
          f'  </circle>')
        a(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{theme_cfg["TEXT"]}" stroke="{theme_cfg["CYAN"]}" stroke-width="1.8"/>')
        a(f'</g>')

        # Label Positioning
        lx = cx + (r + 26) * math.cos(ang)
        ly = cy + (r + 20) * math.sin(ang)
        align = "middle"
        if math.cos(ang) > 0.3:
            align = "start"
            lx += 4
        elif math.cos(ang) < -0.3:
            align = "end"
            lx -= 4

        pct_str = f"{int(val * 100)}%"
        a(f'<g opacity="0">')
        a(f'  <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="{b_time + 0.2:.2f}s" fill="freeze"/>')
        a(f'  <text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{align}" font-size="10" font-weight="700" fill="{theme_cfg["TEXT"]}">{esc(name)}</text>')
        a(f'  <text x="{lx:.1f}" y="{ly + 13:.1f}" text-anchor="{align}" font-size="9.5" font-weight="600" fill="{theme_cfg["CYAN"]}">{pct_str}</text>')
        a(f'</g>')

    return "".join(out)

def generate_svg(theme_name):
    t = THEMES[theme_name]
    gid = f"accent_b_{theme_name}"
    radar_gid = f"radarGrad_{theme_name}"
    sweep_gid = f"sweepGrad_{theme_name}"
    
    s = []
    a = s.append

    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-label="Ashwin R Profile Banner">')
    
    # Definitions & Gradients
    a('<defs>')
    a(f'  <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">')
    a(f'    <stop offset="0" stop-color="{t["VIOLET2"]}"><animate attributeName="stop-color" values="{t["VIOLET2"]};{t["CYAN"]};{t["EMERALD"]};{t["VIOLET2"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'    <stop offset="0.5" stop-color="{t["CYAN"]}"><animate attributeName="stop-color" values="{t["CYAN"]};{t["EMERALD"]};{t["VIOLET2"]};{t["CYAN"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'    <stop offset="1" stop-color="{t["EMERALD"]}"><animate attributeName="stop-color" values="{t["EMERALD"]};{t["VIOLET2"]};{t["CYAN"]};{t["EMERALD"]}" dur="10s" repeatCount="indefinite"/></stop>')
    a(f'  </linearGradient>')
    
    a(f'  <linearGradient id="radarGradDark" x1="0" y1="0" x2="1" y2="1">')
    a(f'    <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.6"/>')
    a(f'    <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.2"/>')
    a(f'  </linearGradient>')

    a(f'  <linearGradient id="radarGradLight" x1="0" y1="0" x2="1" y2="1">')
    a(f'    <stop offset="0%" stop-color="#0891B2" stop-opacity="0.5"/>')
    a(f'    <stop offset="100%" stop-color="#6D28D9" stop-opacity="0.25"/>')
    a(f'  </linearGradient>')

    a(f'  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">')
    a(f'    <feGaussianBlur stdDeviation="4" result="blur"/>')
    a(f'    <feComposite in="SourceGraphic" in2="blur" operator="over"/>')
    a(f'  </filter>')
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
    a(f'<text x="{W/2}" y="29" text-anchor="middle" font-size="12" fill="{t["MUTED"]}">ashwinindira05@gmail.com — % ./profile.sh --live</text>')

    # ==================== LEFT PANEL (Skill Radar) ====================
    a(f'<g transform="translate(36, 84)">')
    a(f'  <rect width="400" height="492" rx="12" fill="{t["PANEL"]}" stroke="{t["STROKE"]}">'
      f'    <animate attributeName="stroke" values="{t["STROKE"]};{t["STROKE_HI"]};{t["STROKE"]}" dur="4s" repeatCount="indefinite"/>'
      f'  </rect>')
    a(generate_radar(200, 260, 130, t))
    a(f'</g>')

    # ==================== RIGHT PANEL (Terminal Info) ====================
    a(f'<g transform="translate(460, 84)">')
    a(f'  <rect width="684" height="492" rx="12" fill="{t["PANEL"]}" stroke="{t["STROKE"]}">'
      f'    <animate attributeName="stroke" values="{t["STROKE"]};{t["STROKE_HI"]};{t["STROKE"]}" dur="4s" begin="1s" repeatCount="indefinite"/>'
      f'  </rect>')
    
    # Right Header
    a(f'  <text x="24" y="32" font-size="11" letter-spacing="2.5" font-weight="700" fill="{t["CYAN"]}">SYSTEM.INFO // DEVELOPER PROFILE</text>')
    a(f'  <text x="560" y="32" font-size="10" fill="{t["DIM"]}">./ashwin.sh --live</text>')
    a(f'  <line x1="24" y1="42" x2="660" y2="42" stroke="url(#{gid})" stroke-width="1.5" opacity="0.7"/>')

    # Typewriter Command Line 1: whoami
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.2s" fill="freeze"/>')
    a(f'    <text x="24" y="74" font-size="13" fill="{t["EMERALD"]}">ashwin@dev-box:~$ <tspan fill="{t["CYAN"]}">whoami</tspan></text>')
    a(f'  </g>')

    # Bio Fields Table
    info_items = [
        ("NAME", "Ashwin R", t["TEXT"], "0.35s"),
        ("ROLE", "B.Tech IT Student / Flutter & Frontend Developer", t["VIOLET"], "0.50s"),
        ("BASE", "Trichy, Tamil Nadu, IN 🇮🇳", t["TEXT"], "0.65s"),
        ("DEGREE", "B.Tech Information Technology", t["MUTED"], "0.80s"),
        ("CORE_STACK", "Flutter • Dart • React • Node.js • Java • Python", t["CYAN"], "0.95s"),
        ("STATUS", "⚡ Open for Internships & Open-Source Collaboration", t["EMERALD"], "1.10s"),
        ("CONTACT", "ashwinindira05@gmail.com", t["VIOLET"], "1.25s"),
    ]

    start_y = 108
    for i, (label, val, col, b_anim) in enumerate(info_items):
        cur_y = start_y + i * 32
        a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{b_anim}" fill="freeze"/>')
        a(f'    <text x="24" y="{cur_y}" font-size="11.5" font-weight="700" fill="{t["MUTED"]}">{label:<11}: </text>')
        a(f'    <text x="135" y="{cur_y}" font-size="11.5" font-weight="600" fill="{col}">{esc(val)}</text>')
        a(f'  </g>')

    # Blinking Terminal Cursor after contact line
    a(f'  <text x="365" y="{start_y + 6 * 32}" font-size="13" font-weight="bold" fill="{t["CYAN"]}">_<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/></text>')

    # Tech Stack Pill Badges Row
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.4s" fill="freeze"/>')
    a(f'    <text x="24" y="348" font-size="10" letter-spacing="1.5" font-weight="700" fill="{t["DIM"]}">HIGHLIGHTED TECH</text>')
    
    tags = ["Flutter", "Dart", "React", "Node.js", "Express", "Java", "Python", "MongoDB", "Git"]
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
    a(f'    <text x="230" y="441" font-size="9" font-weight="700" fill="{t["DIM"]}">PRIMARY FOCUS</text>')
    a(f'    <text x="230" y="460" font-size="14" font-weight="800" fill="{t["VIOLET"]}">Flutter &amp; Web</text>')
    a(f'    <line x1="430" y1="430" x2="430" y2="462" stroke="{t["BARLINE"]}"/>')
    
    # Metric 3
    a(f'    <text x="450" y="441" font-size="9" font-weight="700" fill="{t["DIM"]}">SYSTEM STATUS</text>')
    a(f'    <text x="450" y="460" font-size="13" font-weight="800" fill="{t["EMERALD"]}">● ONLINE <tspan font-size="10" font-weight="normal" fill="{t["MUTED"]}">v2.5</tspan></text>')
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
