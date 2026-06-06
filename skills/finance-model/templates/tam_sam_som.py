"""
TAM/SAM/SOM sizing calculator — BCG Q x P waterfall.
Usage: python3 tam_sam_som.py
"""

from dataclasses import dataclass


@dataclass
class MarketLayer:
    name: str
    quantity: float
    price: float
    assumption: str
    source: str
    unit_q: str = "units"
    unit_p: str = "USD"

    @property
    def value_usd_m(self) -> float:
        return self.quantity * self.price / 1_000_000

    @property
    def value_krw_b(self) -> float:
        return self.value_usd_m * 1_400 / 100  # 억 원 (1 USD ~ 1,400 KRW)


def render_waterfall(layers: list, title: str = "시장 규모 추정") -> str:
    lines = ["=" * 60, f"  {title}", "=" * 60]
    for layer in layers:
        lines += [
            f"\n{layer.name}:",
            f"  = {layer.quantity:,.0f} {layer.unit_q}  x  {layer.price:,.0f} {layer.unit_p}",
            f"  -> ${layer.value_usd_m:,.1f}M  /  약 {layer.value_krw_b:,.0f}억 원",
            f"  가정: {layer.assumption}",
            f"  출처: {layer.source}",
        ]
    lines += ["\n" + "-" * 60, "  Source: [출처 목록], BCG analysis", "=" * 60]
    return "\n".join(lines)


def render_methodology(layers: list) -> str:
    lines = ["\n[참고] 추정 방법론 -- Q x P 로직 트리", "-" * 40]
    for layer in layers:
        lines += [
            f"\n{layer.name}:",
            f"  Q: {layer.quantity:,.0f} {layer.unit_q}",
            f"  P: {layer.price:,.0f} {layer.unit_p}",
            f"  채택 근거: {layer.assumption}",
        ]
    return "\n".join(lines)


if __name__ == "__main__":
    # Replace with actual market inputs
    layers = [
        MarketLayer(
            name="TAM (전체 시장)",
            quantity=500_000_000,
            price=1_300,
            assumption="글로벌 소비자 수 x 연간 지출",
            source="[리포트], BCG 추정",
            unit_q="명",
            unit_p="USD/명",
        ),
        MarketLayer(
            name="SAM (접근 가능 시장)",
            quantity=50_000_000,
            price=1_300,
            assumption="타깃 지역 소비자 x 채널 커버리지 10%",
            source="[리포트], BCG 추정",
            unit_q="명",
            unit_p="USD/명",
        ),
        MarketLayer(
            name="SOM (현실적 점유)",
            quantity=2_500_000,
            price=1_300,
            assumption="SAM x 5% 점유율 (영업력 기준 3년 내)",
            source="BCG 추정",
            unit_q="명",
            unit_p="USD/명",
        ),
    ]

    print(render_waterfall(layers))
    print(render_methodology(layers))
    print(
        "\n**특히, SOM은 SAM의 5% 수준 -> "
        "따라서 초기 3년은 채널 파트너십 확보에 집중 권고**"
    )
