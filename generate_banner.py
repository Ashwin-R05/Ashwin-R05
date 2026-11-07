#!/usr/bin/env python3
"""
Option 2: Live SOC Telemetry & Defense Stream Profile Hero Banner (dark.svg & light.svg).
Cybersecurity Command Center HUD + Real-time Streaming Security Logs & Telemetry.
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
        "CONSOLE_BG": "#050914",
        "CONSOLE_STROKE": "rgba(34,211,238,0.20)",
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
        "CONSOLE_BG": "#F8FAFC",
        "CONSOLE_STROKE": "rgba(8,145,178,0.25)",
    }
}

W = 1180
H = 610
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

def esc(s):
    return html.escape(str(s), quote=True)

def generate_cyber_panel(theme_cfg):
    """
    Generate Left Panel: Cyber Security Command HUD + Live SOC Telemetry Stream Terminal.
    """
    out = []
    a = out.append

    # Panel Header Inside Left Box
    a(f'<text x="200" y="32" text-anchor="middle" font-size="11" letter-spacing="2.5" font-weight="700" fill="{theme_cfg["CYAN"]}">SOC.COMMAND // TELEMETRY STREAM</text>')

    # Top Status Bar
    a(f'<g transform="translate(20, 44)">')
    a(f'  <rect width="360" height="26" rx="6" fill="{theme_cfg["NODE_BG"]}" stroke="{theme_cfg["NODE_STROKE"]}"/>')
    a(f'  <circle cx="15" cy="13" r="4" fill="{theme_cfg["EMERALD"]}">'
      f'    <animate attributeName="opacity" values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/>'
      f'  </circle>')
    a(f'  <text x="26" y="17" font-size="9" font-weight="700" fill="{theme_cfg["EMERALD"]}">DAEMON ACTIVE <tspan fill="{theme_cfg["MUTED"]}">| PING: 0.4ms | ZERO-TRUST: ENFORCED</tspan></text>')
    a(f'</g>')

    # Central Cyber Security HUD Core (Center: cx=200, cy=148)
    cx, cy = 200, 148

    a(f'<g transform="translate({cx},{cy})">')
    
    # Outer Rotating HUD Segmented Ring
    a(f'  <circle cx="0" cy="0" r="58" fill="none" stroke="{theme_cfg["CYAN"]}" stroke-width="1.2" stroke-dasharray="8,5,15,5" opacity="0.65">')
    a(f'    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>')
    a(f'  </circle>')

    # Counter-Rotating Inner Tech Ring
    a(f'  <circle cx="0" cy="0" r="44" fill="none" stroke="{theme_cfg["VIOLET"]}" stroke-width="1" stroke-dasharray="4,4" opacity="0.6">')
    a(f'    <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>')
    a(f'  </circle>')

    # Pulsing Center Cyber Shield
    a(f'  <path d="M 0,-25 L 20,-12 L 20,10 L 0,25 L -20,10 L -20,-12 Z" fill="{theme_cfg["SHIELD_FILL"]}" stroke="{theme_cfg["CYAN"]}" stroke-width="2">')
    a(f'    <animate attributeName="stroke" values="{theme_cfg["CYAN"]};{theme_cfg["EMERALD"]};{theme_cfg["CYAN"]}" dur="3s" repeatCount="indefinite"/>')
    a(f'  </path>')
    
    # Lock Symbol inside Shield
    a(f'  <rect x="-6" y="-2" width="12" height="11" rx="2" fill="{theme_cfg["CYAN"]}"/>')
    a(f'  <path d="M -4,-2 A 4 4 0 0 1 4,-2" fill="none" stroke="{theme_cfg["CYAN"]}" stroke-width="2"/>')
    a(f'  <circle cx="0" cy="3.5" r="1.8" fill="{theme_cfg["PANEL"]}"/>')

    # Scanning Laser Bar passing through core
    a(f'  <line x1="-50" y1="0" x2="50" y2="0" stroke="{theme_cfg["EMERALD"]}" stroke-width="1.5" opacity="0.8">')
    a(f'    <animateTransform attributeName="transform" type="translate" values="0 -40; 0 40; 0 -40" dur="3s" repeatCount="indefinite"/>')
    a(f'    <animate attributeName="opacity" values="0.2;0.9;0.2" dur="3s" repeatCount="indefinite"/>')
    a(f'  </line>')

    # Corner Crosshairs
    a(f'  <line x1="-62" y1="0" x2="-54" y2="0" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="54" y1="0" x2="62" y2="0" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="0" y1="-62" x2="0" y2="-54" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')
    a(f'  <line x1="0" y1="54" x2="0" y2="62" stroke="{theme_cfg["CYAN"]}" stroke-width="1.5"/>')

    # Radar Blips (Pulsing Monitored Nodes)
    a(f'  <circle cx="32" cy="-24" r="3" fill="{theme_cfg["EMERALD"]}"><animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/></circle>')
    a(f'  <circle cx="-35" cy="18" r="2.5" fill="{theme_cfg["CYAN"]}"><animate attributeName="opacity" values="0.3;1;0.3" dur="2.4s" repeatCount="indefinite"/></circle>')
    a(f'  <circle cx="28" cy="28" r="2" fill="{theme_cfg["VIOLET"]}"><animate attributeName="opacity" values="0.2;0.9;0.2" dur="1.8s" repeatCount="indefinite"/></circle>')

    a(f'</g>')

    # Connection line down to Console
    a(f'<path d="M 200,210 L 200,225" stroke="{theme_cfg["STROKE"]}" stroke-width="1.5" stroke-dasharray="3,3"/>')

    # ==================== LIVE SOC TELEMETRY CONSOLE BOX ====================
    # Position: x=20, y=225, width=360, height=245
    a(f'<g transform="translate(20, 225)">')
    
    # Console Shell
    a(f'  <rect width="360" height="245" rx="10" fill="{theme_cfg["CONSOLE_BG"]}" stroke="{theme_cfg["CONSOLE_STROKE"]}">'
      f'    <animate attributeName="stroke" values="{theme_cfg["CONSOLE_STROKE"]};{theme_cfg["STROKE_HI"]};{theme_cfg["CONSOLE_STROKE"]}" dur="4s" repeatCount="indefinite"/>'
      f'  </rect>')

    # Console Header Bar
    a(f'  <rect width="360" height="26" rx="10" fill="{theme_cfg["NODE_BG"]}"/>')
    a(f'  <rect y="18" width="360" height="8" fill="{theme_cfg["NODE_BG"]}"/>')
    a(f'  <line x1="0" y1="26" x2="360" y2="26" stroke="{theme_cfg["BARLINE"]}"/>')
    
    # Tiny terminal window controls
    a(f'  <circle cx="14" cy="13" r="3.5" fill="#EF4444"/>')
    a(f'  <circle cx="26" cy="13" r="3.5" fill="#F59E0B"/>')
    a(f'  <circle cx="38" cy="13" r="3.5" fill="#10B981"/>')
    a(f'  <text x="52" y="16.5" font-size="9" font-weight="700" fill="{theme_cfg["MUTED"]}">soc-stream.sh --live</text>')
    
    # LIVE Pill on header right
    a(f'  <circle cx="304" cy="13" r="3" fill="{theme_cfg["EMERALD"]}">'
      f'    <animate attributeName="opacity" values="1;0.2;1" dur="1s" repeatCount="indefinite"/>'
      f'  </circle>')
    a(f'  <text x="312" y="16.5" font-size="8.5" font-weight="700" fill="{theme_cfg["EMERALD"]}">STREAM</text>')

    # Telemetry Log Entries (Staggered Entrance)
    logs = [
        ("01:04:18", "AUTH", "OAuth2 PKCE Handshake", "PASS", theme_cfg["CYAN"], theme_cfg["EMERALD"], "0.2s"),
        ("01:04:19", "CSPM", "AWS CloudGuard Audit", "0 ERR", theme_cfg["VIOLET"], theme_cfg["EMERALD"], "0.4s"),
        ("01:04:20", "APSEC", "OWASP Top 10 API Shield", "SECURE", theme_cfg["EMERALD"], theme_cfg["CYAN"], "0.6s"),
        ("01:04:21", "GRAPH", "SkillGraph NLP Engine", "ACTIVE", theme_cfg["CYAN"], theme_cfg["VIOLET"], "0.8s"),
        ("01:04:22", "NETWK", "Zero-Trust Perimeter", "LOCKED", theme_cfg["EMERALD"], theme_cfg["EMERALD"], "1.0s"),
    ]

    log_y = 50
    for ts, tag, msg, status, tag_col, stat_col, b_anim in logs:
        a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{b_anim}" fill="freeze"/>')
        # Timestamp
        a(f'    <text x="14" y="{log_y}" font-size="9" fill="{theme_cfg["DIM"]}">{ts}</text>')
        # Tag Badge
        a(f'    <rect x="64" y="{log_y-9}" width="38" height="13" rx="3" fill="{theme_cfg["PILL_BG"]}" stroke="{theme_cfg["PILL_STROKE"]}"/>')
        a(f'    <text x="83" y="{log_y}" text-anchor="middle" font-size="7.5" font-weight="700" fill="{tag_col}">{tag}</text>')
        # Message
        a(f'    <text x="110" y="{log_y}" font-size="9" fill="{theme_cfg["TEXT"]}">{esc(msg)}</text>')
        # Status Pill
        a(f'    <text x="346" y="{log_y}" text-anchor="end" font-size="8.5" font-weight="800" fill="{stat_col}">[{status}]</text>')
        a(f'  </g>')
        log_y += 24

    # Terminal Prompt & Blinking Cursor
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.2s" fill="freeze"/>')
    a(f'    <line x1="14" y1="172" x2="346" y2="172" stroke="{theme_cfg["BARLINE"]}"/>')
    a(f'    <text x="14" y="191" font-size="9.5" fill="{theme_cfg["EMERALD"]}">soc@sec-box:~$ <tspan fill="{theme_cfg["CYAN"]}">threat-hunt --status</tspan>'
      f'<tspan fill="{theme_cfg["CYAN"]}">_<animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/></tspan></text>')
    a(f'  </g>')

    # Bottom Console Metric Ribbon
    a(f'  <g transform="translate(14, 204)">')
    a(f'    <rect width="332" height="26" rx="5" fill="{theme_cfg["NODE_BG"]}" stroke="{theme_cfg["BARLINE"]}"/>')
    a(f'    <text x="12" y="17" font-size="8" font-weight="700" fill="{theme_cfg["DIM"]}">INTRUSIONS: <tspan fill="{theme_cfg["EMERALD"]}">0</tspan></text>')
    a(f'    <line x1="100" y1="6" x2="100" y2="20" stroke="{theme_cfg["BARLINE"]}"/>')
    a(f'    <text x="112" y="17" font-size="8" font-weight="700" fill="{theme_cfg["DIM"]}">UPTIME: <tspan fill="{theme_cfg["CYAN"]}">99.98%</tspan></text>')
    a(f'    <line x1="216" y1="6" x2="216" y2="20" stroke="{theme_cfg["BARLINE"]}"/>')
    a(f'    <text x="228" y="17" font-size="8" font-weight="700" fill="{theme_cfg["DIM"]}">POLICY: <tspan fill="{theme_cfg["VIOLET"]}">ENFORCED</tspan></text>')
    a(f'  </g>')

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
    a(f'<text x="{W/2}" y="29" text-anchor="middle" font-size="12" fill="{t["MUTED"]}">ashwinindira05@gmail.com - % ./soc-command.sh --stream --live</text>')

    # ==================== LEFT PANEL (Live SOC Telemetry & Command HUD) ====================
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
    a(f'  <text x="24" y="32" font-size="11" letter-spacing="2.5" font-weight="700" fill="{t["CYAN"]}">SYSTEM.INFO // CYBERSECURITY &amp; DEV ARCHITECTURE</text>')
    a(f'  <text x="560" y="32" font-size="10" fill="{t["DIM"]}">./ashwin.sh --sec</text>')
    a(f'  <line x1="24" y1="42" x2="660" y2="42" stroke="url(#{gid})" stroke-width="1.5" opacity="0.7"/>')

    # Typewriter Command Line 1: whoami
    a(f'  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.2s" fill="freeze"/>')
    a(f'    <text x="24" y="74" font-size="13" fill="{t["EMERALD"]}">ashwin@sec-box:~$ <tspan fill="{t["CYAN"]}">whoami --verbose</tspan></text>')
    a(f'  </g>')

    # Bio Fields Table (Cybersecurity + Systems focus)
    info_items = [
        ("NAME", "Ashwin R", t["TEXT"], "0.35s"),
        ("ROLE", "B.Tech IT Student | Cybersecurity Specialist & Dev", t["VIOLET"], "0.50s"),
        ("BASE", "Trichy, Tamil Nadu, IN 🇮🇳", t["TEXT"], "0.65s"),
        ("FOCUS", "CloudSec (CSPM) • AppSec (OWASP Top 10) • OAuth2 • DevSecOps", t["CYAN"], "0.80s"),
        ("CORE_STACK", "CloudSec • Python • Node.js • Flutter • Docker • Java", t["EMERALD"], "0.95s"),
        ("STATUS", "⚡ Seeking Cybersecurity Roles & Dev Collaboration", t["EMERALD"], "1.10s"),
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
    a(f'    <text x="24" y="348" font-size="10" letter-spacing="1.5" font-weight="700" fill="{t["DIM"]}">CORE DOMAINS &amp; CAPABILITIES</text>')
    
    tags = ["CloudSec", "OAuth2", "OWASP", "AppSec", "DevSecOps", "Python", "Flutter", "Docker", "Node.js"]
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
    a(f'    <text x="450" y="460" font-size="13" font-weight="800" fill="{t["EMERALD"]}">● AUDITED <tspan font-size="10" font-weight="normal" fill="{t["MUTED"]}">v3.0</tspan></text>')
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
