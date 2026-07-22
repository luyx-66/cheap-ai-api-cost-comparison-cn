"""使用有来源和核对日期的价格数据估算 AI API 成本。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def estimate(provider: dict, usage: dict) -> dict:
    text = (
        usage["input_tokens"] / 1_000_000 * provider.get("input_per_million", 0)
        + usage["output_tokens"] / 1_000_000 * provider.get("output_per_million", 0)
    )
    images = usage["images"] * provider.get("image_unit_price", 0)
    video = usage["video_seconds"] * provider.get("video_second_price", 0)
    return {
        "provider": provider["name"],
        "currency": provider.get("currency", "USD"),
        "text_cost": round(text, 6),
        "image_cost": round(images, 6),
        "video_cost": round(video, 6),
        "total_cost": round(text + images + video, 6),
        "source": provider.get("source"),
        "checked_at": provider.get("checked_at"),
        "illustrative": bool(provider.get("illustrative", False)),
    }


def validate(providers: list[dict]) -> None:
    required = {"name", "currency", "source", "checked_at"}
    for provider in providers:
        missing = required - provider.keys()
        if missing:
            raise ValueError(f"{provider.get('name', 'provider')} missing: {', '.join(sorted(missing))}")
        numeric = ("input_per_million", "output_per_million", "image_unit_price", "video_second_price")
        if any(float(provider.get(field, 0)) < 0 for field in numeric):
            raise ValueError("Prices cannot be negative")


def main() -> None:
    parser = argparse.ArgumentParser(description="便宜 AI API 价格对比计算器")
    parser.add_argument("pricing", type=Path)
    parser.add_argument("--input-tokens", type=int, default=0)
    parser.add_argument("--output-tokens", type=int, default=0)
    parser.add_argument("--images", type=int, default=0)
    parser.add_argument("--video-seconds", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if min(args.input_tokens, args.output_tokens, args.images, args.video_seconds) < 0:
        parser.error("Usage values cannot be negative")

    providers = json.loads(args.pricing.read_text(encoding="utf-8"))
    validate(providers)
    usage = {"input_tokens": args.input_tokens, "output_tokens": args.output_tokens, "images": args.images, "video_seconds": args.video_seconds}
    rows = sorted((estimate(provider, usage) for provider in providers), key=lambda row: row["total_cost"])
    result = {"usage": usage, "warning": "illustrative=true 表示演示数据，不能用于真实购买决策", "results": rows}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
