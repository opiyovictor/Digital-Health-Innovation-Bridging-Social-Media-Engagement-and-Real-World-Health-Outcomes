# Data

The original analysis was conducted from a survey workbook containing individual-level responses.

**The raw respondent-level workbook is intentionally not committed to this public-facing repository by default.** Before publishing it, confirm that the dataset is de-identified and that the consent, ethics approval and data-owner permissions allow public release.

## Run locally

Place the analysis workbook here:

`data/Assessment_of_Youth_Engagement_Awareness_and_Health_Service_Uptake_through_the_Vijana_Tubonge_TikTok_Platform_.xlsx`

The workbook should contain a worksheet named `clean`.

Then run:

```bash
python src/analyze.py
```

If you are working with a different approved data file, pass its path:

```bash
python src/analyze.py --input path/to/approved_data.xlsx
```
