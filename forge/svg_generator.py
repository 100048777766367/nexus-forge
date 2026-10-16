import math

class GenerativeSVGArt:
    """Sinh tranh đồ họa Vector SVG dựa trên nhịp đập Kuramoto và ma trận Siêu XOR"""
    @staticmethod
    def render(artifact_id, epoch, decision, coherence_r, palette="sacred"):
        # Tính toán góc pha hình học
        angle_step = (2.0 * math.pi) / 14.0
        center_x, center_y = 250, 250
        radius = 180 * (0.6 + coherence_r * 0.4)

        # Bảng màu
        colors = ["#FFD700", "#FF4500", "#00FFFF", "#7FFF00", "#FF1493", "#9400D3", "#00FA9A"]
        if palette == "sacred":
            bg_color = "#0B0C10"
            ring_color = "#66FCF1"
            core_color = "#45A29E"
            accent_color = "#C5C6C7"
        else:
            bg_color = "#1A1A2E"
            ring_color = "#E94560"
            core_color = "#0F3460"
            accent_color = "#16213E"

        paths = []
        nodes = []
        for i in range(14):
            theta = i * angle_step + (decision * 2.0 * math.pi)
            x = center_x + radius * math.cos(theta)
            y = center_y + radius * math.sin(theta)
            nodes.append((x, y))

        # Nối các đường tương quan chéo n x n
        for i in range(14):
            for j in range(i + 1, 14):
                if (i + j) % 2 == 0:
                    x1, y1 = nodes[i]
                    x2, y2 = nodes[j]
                    opacity = round(0.15 + (decision * 0.3), 3)
                    paths.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ring_color}" stroke-width="1.2" stroke-opacity="{opacity}" />')

        # Vòng tròn trung tâm và nơ-ron ngoại vi
        node_circles = []
        for idx, (x, y) in enumerate(nodes):
            c = colors[idx % len(colors)]
            r = 6.0 + (math.sin(idx + decision * 10) * 2.5)
            node_circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}" filter="url(#glow)" />')

        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{core_color}" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="{bg_color}" stop-opacity="1"/>
    </radialGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="500" height="500" fill="url(#bgGrad)"/>
  <!-- Lưới tương quan thần kinh Indra -->
  <g>
    {''.join(paths)}
  </g>
  <!-- Vòng hào quang trung tâm -->
  <circle cx="{center_x}" cy="{center_y}" r="{radius * 0.45:.1f}" fill="none" stroke="{accent_color}" stroke-dasharray="4 6" stroke-width="1.5" opacity="0.6"/>
  <circle cx="{center_x}" cy="{center_y}" r="{radius * 0.2:.1f}" fill="{ring_color}" opacity="0.25" filter="url(#glow)"/>
  <circle cx="{center_x}" cy="{center_y}" r="8" fill="#FFFFFF" filter="url(#glow)"/>
  <!-- Nơ-ron vệ tinh -->
  {''.join(node_circles)}
  <!-- Chú thích số hóa -->
  <text x="250" y="465" text-anchor="middle" fill="#FFFFFF" font-family="monospace" font-size="12" letter-spacing="2">NEXUS ARTIFACT #{artifact_id}</text>
  <text x="250" y="482" text-anchor="middle" fill="{ring_color}" font-family="monospace" font-size="9" opacity="0.8">EPOCH #{epoch} | COHERENCE R={coherence_r*100:.1f}%</text>
</svg>"""
        return svg
