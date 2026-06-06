"""
BCG-style text exhibit renderer.
Wraps any table or list in BCG slide conventions:
headline, body, BCG opinion callout, source footer, so-what footer.
Usage: python3 exhibit.py
"""


def render_exhibit(
    headline: str,
    body_lines: list,
    bcg_opinion: str,
    sources: list,
    so_what: str,
    width: int = 70,
) -> str:
    sep = "=" * width
    thin = "-" * width

    sections = [sep, _wrap(headline.upper(), width), thin]
    sections.extend(body_lines)
    sections += [
        thin,
        "[BCG 의견]",
        _wrap(bcg_opinion, width),
        thin,
        "Source: " + ", ".join(sources) + ", BCG analysis",
        thin,
        _wrap("**특히, " + so_what + "**", width),
        sep,
    ]
    return "\n".join(sections)


def render_sensitivity(
    wacc_range: list,
    tgr_range: list,
    ev_grid: list,
    base_wacc: float,
    base_tgr: float,
) -> str:
    col_w = 10
    header = f"{'EV ($M)':>{col_w}}" + "".join(
        f"TGR {t:.1%}"[:col_w].rjust(col_w) for t in tgr_range
    )
    sep = "-" * len(header)
    lines = [sep, header, sep]

    for i, w in enumerate(wacc_range):
        note = " [BASE]" if abs(w - base_wacc) < 0.001 else ""
        row = f"WACC {w:.0%}"[:col_w].rjust(col_w)
        for j, t in enumerate(tgr_range):
            flag = "*" if (abs(w - base_wacc) < 0.001 and abs(t - base_tgr) < 0.001) else " "
            row += f"{flag}{ev_grid[i][j]:>8.0f}".rjust(col_w)
        lines.append(row + note)

    lines.append(sep)
    return "\n".join(lines)


def _wrap(text: str, width: int) -> str:
    words = text.split()
    lines, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 <= width:
            current = (current + " " + word).strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return "\n".join(lines)


if __name__ == "__main__":
    # Synthetic example -- replace with outputs from projection.py
    print(render_exhibit(
        headline="Subject DCF | EV ~$147B, implied price $52.00/주",
        body_lines=[
            "  Base revenue (2024A): $96,800M",
            "  5-yr revenue CAGR:    18.4%",
            "  WACC:                 10.0%",
            "  Terminal growth:       2.5%",
            "  Enterprise Value:   $146,900M  /  약 205.7조 원",
            "  Equity Value:       $165,900M  /  약 232.3조 원",
            "  Implied price/share:  $52.00",
            "  TV as % of EV:        72%",
        ],
        bcg_opinion=(
            "TV가 EV의 72% 수준으로 terminal growth 가정에 민감. "
            "WACC 1pp 상승 시 EV ~12% 하락. "
            "성장률 가정은 업종 평균 대비 상단 -- 추가 검증 필요."
        ),
        sources=["회사 공개 자료", "BCG 추정"],
        so_what=(
            "TV 비중 70%+ 확인 -> "
            "terminal growth 가정 재검토 및 업종 비교군 추가 분석 권고"
        ),
    ))

    print()

    wacc_range = [0.08, 0.09, 0.10, 0.11, 0.12]
    tgr_range = [0.015, 0.020, 0.025, 0.030, 0.035]
    ev_grid = [
        [195000, 210000, 228000, 250000, 278000],
        [175000, 188000, 203000, 221000, 243000],
        [158000, 169000, 182000, 197000, 215000],
        [143000, 153000, 164000, 177000, 192000],
        [130000, 139000, 148000, 160000, 173000],
    ]
    print(render_sensitivity(wacc_range, tgr_range, ev_grid, 0.10, 0.025))
