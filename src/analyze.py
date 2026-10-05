"""
Vijana Tubonge — TikTok survey analysis

Purpose
-------
Reproducibly summarise reach, engagement, perceptions, perceived influence,
and referral/service-use indicators from the approved survey workbook.

This script intentionally avoids causal language: the underlying design is
cross-sectional and self-reported.
"""

from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd


DEFAULT_INPUT = Path("data/Assessment_of_Youth_Engagement_Awareness_and_Health_Service_Uptake_through_the_Vijana_Tubonge_TikTok_Platform_.xlsx")
OUTPUT_DIR = Path("outputs")


def pct(num: int, den: int) -> float:
    return round(100 * num / den, 1) if den else float("nan")


def main(input_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(
            f"Data file not found: {input_path}\n"
            "See data/README.md for the expected location and privacy guidance."
        )

    df = pd.read_excel(input_path, sheet_name="clean")
    OUTPUT_DIR.mkdir(exist_ok=True)

    heard_col = "Have you heard of the Vijana Tubonge TikTok account?"
    follow_col = "Do you follow Vijana Tubonge on TikTok?"
    watch_col = "How often do you watch Vijana Tubonge content?"
    comfort_col = "How comfortable are you asking health questions on Vijana Tubonge?"
    trust_col = "Do you trust health information provided by Vijana Tubonge?"
    safe_col = "I feel safe and respected engaging with Vijana Tubonge health content."
    knowledge_col = "Vijana Tubonge has increased my knowledge about health services."
    encouraged_col = "Content from Vijana Tubonge has encouraged me to seek health services when needed."
    confidence_col = "I feel more confident making health decisions after following Vijana Tubonge."
    before_col = "Before following Vijana Tubonge, were you aware of youth-friendly health services?"
    after_col = "Has Vijana Tubonge improved your understanding of how and where to access health services?"
    referred_col = "Have you ever been referred by Vijana Tubonge to a health or support service?"
    accessed_col = "Did you access the referred services"
    helpful_col = "If yes, How helpdul was the service?"

    total = len(df)
    aware = int(df[heard_col].eq("Yes").sum())
    followers = df[df[follow_col].eq("Yes")].copy()
    n_followers = len(followers)

    referred = followers[followers[referred_col].eq("Yes")].copy()
    accessed = referred[referred[accessed_col].eq("Yes")].copy()

    indicators = [
        ("Reach", "Awareness of Vijana Tubonge", aware, total, "All survey respondents"),
        ("Reach", "Followership among those aware", n_followers, aware, "Respondents aware of Vijana Tubonge"),
        ("Engagement", "Watch 3–5 times per week", int(followers[watch_col].eq("3-5 Times a week").sum()), n_followers, "Followers"),
        ("Engagement", "Watch daily", int(followers[watch_col].eq("Daily").sum()), n_followers, "Followers"),
        ("Trust & safety", "Comfortable / very comfortable asking questions",
         int(followers[comfort_col].isin(["Very Comfortable", " Comfortable"]).sum()), n_followers, "Followers"),
        ("Trust & safety", "Trust health information",
         int(followers[trust_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Trust & safety", "Feel safe and respected",
         int(followers[safe_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Perceived influence", "Report increased health knowledge",
         int(followers[knowledge_col].isin(["Agree", "Strongly Agree"]).sum()), n_followers, "Followers"),
        ("Perceived influence", "Encouraged to seek services",
         int(followers[encouraged_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Perceived influence", "More confident in health decisions",
         int(followers[confidence_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Awareness", "Aware of youth-friendly services before following",
         int(followers[before_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Awareness", "Improved understanding of where/how to access services",
         int(followers[after_col].eq("Yes").sum()), n_followers, "Followers"),
        ("Referral", "Referred to a health/support service",
         len(referred), n_followers, "Followers"),
        ("Referral", "Accessed referred service",
         len(accessed), len(referred), "Followers who reported a referral"),
        ("Referral", "Found accessed service helpful / very helpful",
         int(accessed[helpful_col].isin(["Very Helpful", "Very Helpful ", "Helpul"]).sum()),
         len(accessed), "Followers who accessed a referred service"),
    ]

    out = pd.DataFrame(indicators, columns=["Domain", "Indicator", "Numerator", "Denominator", "Population"])
    out["Percent"] = [pct(a, b) for a, b in zip(out["Numerator"], out["Denominator"])]
    out.to_csv(OUTPUT_DIR / "key_indicators.csv", index=False)

    print(f"Loaded {total:,} records.")
    print(f"Awareness: {aware:,}/{total:,} ({pct(aware,total)}%)")
    print(f"Followers among aware: {n_followers:,}/{aware:,} ({pct(n_followers,aware)}%)")
    print(f"Referral pathway: {len(referred):,} referred → {len(accessed):,} accessed")
    print(f"Saved: {OUTPUT_DIR / 'key_indicators.csv'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    main(args.input)
