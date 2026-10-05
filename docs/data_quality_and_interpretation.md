# Data and analytical quality notes

## What was checked

The original workbook contains a `clean` worksheet with 379 survey records and 82 analysis-ready variables. The analysis code also retains the original survey wording where it matters for interpretation.

### Cohort structure

- Total respondents: **379**
- Heard of Vijana Tubonge: **318 (83.9%)**
- Followed Vijana Tubonge: **270 (84.9% of those aware)**

The analysis uses the **270 followers** as the primary cohort for platform engagement, perceptions, knowledge, referral and service-use indicators.

### Denominator discipline

The original project sometimes described every result as being based on followers even where questionnaire skip logic produced missing values. The revised outputs make the denominator explicit for every headline indicator.

For consistency with the original analysis, cohort-level percentages retain the full follower denominator (`n=270`) unless the question explicitly requires a smaller conditional denominator. For the referral pathway:

`270 followers → 110 referred → 106 accessed`

### Important data-quality observation

The dataset includes respondents in age bands above 24 (25–29, 30–34, 35–39 and above 39), even though the project narrative describes adolescents and young people aged 10–24. The repository therefore **does not claim that the analytical sample is exclusively 10–24**. This should be resolved against the original study protocol/questionnaire before publication.

### Interpretation

This is a cross-sectional, self-reported survey. The findings describe **reach, engagement and perceived influence**. They should not be presented as proof that TikTok caused changes in knowledge, confidence or service uptake. The pre/post awareness comparison is retrospective and subject to recall and response bias.

### Privacy

Individual-level survey data should not be committed to a public GitHub repository unless the data owner has explicitly approved public release and the consent/ethics framework permits it. The repository is therefore structured so that raw survey data can remain local.
