"""
FCF projection table generator -- BCG finance-model Mode B.
Produces Revenue-to-FCF bridge as text table.
Usage: python3 projection.py
"""

import math


def build_projection(
    base_revenue: float,
    growth_rates: list,
    ebitda_margin: float,
    da_pct: float,
    capex_pct: float,
    nwc_pct: float,
    tax_rate: float,
    base_year: int = 2024,
) -> dict:
    """Return projection dict keyed by year label."""
    rows = {}
    prev_revenue = base_revenue
    prev_nwc = base_revenue * nwc_pct

    for i, g in enumerate(growth_rates):
        year = f"{base_year + i + 1}F"
        rev = prev_revenue * (1 + g)
        ebitda = rev * ebitda_margin
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - tax_rate)
        capex = rev * capex_pct
        nwc = rev * nwc_pct
        delta_nwc = nwc - prev_nwc
        fcf = nopat + da - capex - delta_nwc

        rows[year] = {
            "Revenue": rev,
            "EBITDA": ebitda,
            "EBIT": ebit,
            "NOPAT": nopat,
            "D&A": da,
            "CapEx": -capex,
            "DNWC": -delta_nwc,
            "Unlevered FCF": fcf,
        }
        prev_revenue = rev
        prev_nwc = nwc

    return rows


def _cagr(start: float, end: float, periods: int) -> float:
    if start <= 0 or end <= 0 or periods == 0:
        return float("nan")
    return (end / start) ** (1 / periods) - 1


def render_projection(proj: dict, unit: str = "$M") -> str:
    years = list(proj.keys())
    metrics = list(next(iter(proj.values())).keys())
    scale = 1_000_000
    col_w = 10
    label_w = 22

    header = f"{'(단위: ' + unit + ')':>{label_w}}" + "".join(
        f"{y:>{col_w}}" for y in years
    ) + f"{'CAGR':>{col_w}}"
    sep = "-" * len(header)
    lines = [sep, header, sep]

    for metric in metrics:
        values = [proj[y][metric] / scale for y in years]
        c = _cagr(values[0], values[-1], len(values) - 1)
        cagr_str = f"{c:.1%}" if not math.isnan(c) else "n/a"
        row = f"{metric:>{label_w}}" + "".join(
            f"{v:>{col_w}.1f}" for v in values
        ) + f"{cagr_str:>{col_w}}"
        lines.append(row)

    lines.append(sep)
    return "\n".join(lines)


if __name__ == "__main__":
    # Replace with actual inputs (revenue in absolute $, not $M)
    proj = build_projection(
        base_revenue=96_800_000_000,
        growth_rates=[0.25, 0.22, 0.18, 0.15, 0.12],
        ebitda_margin=0.16,
        da_pct=0.03,
        capex_pct=0.04,
        nwc_pct=0.05,
        tax_rate=0.21,
        base_year=2024,
    )

    print(render_projection(proj))
    print("\nSource: BCG analysis")
    print(
        "\n**특히, FCF는 추정 기간 내 흑자 전환 예상 -> "
        "따라서 운전자본 조달 방안 선행 검토 권고**"
    )
