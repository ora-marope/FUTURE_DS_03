# FUTURE_DS_03 – Marketing Funnel & Conversion Performance Analysis

**Intern:** MAROPE ORATILE
**CIN:** FIT/MAR26/DS15648
**Domain:** Data Science & Analytics – Future Interns
**Task:** Task 3 – Marketing Funnel & Conversion Performance Analysis

---

## 📌 Objective
Analyze marketing funnel data to identify conversion drop-offs, channel performance, and opportunities to improve lead-to-customer conversion.

---

## 📊 Key KPIs

| Metric | Value |
|--------|-------|
| Total Customers | 2,240 |
| Final Campaign Conversion Rate | 14.9% |
| Avg Spend per Customer | $606 |
| Best Performing Channel | In-Store |
| Lowest Campaign Acceptance | Campaign 2 (1.3%) |
| Highest Campaign Acceptance | Campaign 4 (7.5%) |

---

## 🔍 Key Findings

### 1. Campaign 2 Is a Major Drop-Off Point
Campaign 2 had only a **1.3% acceptance rate** — far below every other campaign. This is a critical funnel drop-off. Something about that campaign failed — whether it was the offer, timing, messaging, or target audience. It needs to be investigated and rebuilt before running again.

### 2. In-Store Is the Dominant Purchase Channel
Despite the digital age, **in-store purchases (12,970) outperform web (9,150) and catalog (5,963)** combined proportionally. Customers still prefer the physical experience for this brand. This means in-store experience, layout, and staff are key conversion levers that shouldn't be neglected in favor of digital-only strategies.

### 3. High Spenders Convert Better
Converted customers spend significantly more on average than those who didn't convert. This means the campaigns are reaching and resonating with high-value customers — the challenge is expanding that reach to medium-spend customers who haven't converted yet.

### 4. Recency Matters — Recent Buyers Convert More
Customers who purchased recently (0–20 days ago) convert at a much higher rate than those who haven't engaged in 80–100 days. The funnel is losing customers the longer they go without interaction. Re-engagement campaigns targeting dormant customers are critical.

### 5. Wines and Meat Drive the Most Revenue
These two categories account for the majority of total spend. Marketing campaigns that feature or bundle these products are likely to generate the highest ROI.

### 6. Education Level Influences Conversion
Higher education levels correlate with higher conversion rates. This suggests the messaging and product positioning resonates more with educated segments — an opportunity to tailor communication for other segments.

---

## 💡 Recommendations

1. **Kill or completely redesign Campaign 2** — A 1.3% acceptance rate means it's not working. Analyze what was different about it (offer? timing? audience?) and fix it before spending more budget there.

2. **Double down on in-store experience** — Since store purchases dominate, invest in in-store promotions, loyalty programs, and staff training. This is where customers actually convert.

3. **Launch re-engagement campaigns for dormant customers** — Target customers who haven't purchased in 60+ days with a personalized offer. The data shows recency is directly tied to conversion — don't let customers go cold.

4. **Bundle Wines and Meat in campaign offers** — These are the highest-spend categories. Featuring them prominently in campaigns will attract the high-value customers most likely to convert.

5. **Segment campaigns by customer profile** — High-income, higher-education customers convert better. Build targeted messaging for different segments rather than one-size-fits-all campaigns.

6. **Test web channel improvements** — Web purchases are strong but trail in-store. Improving the online experience (faster checkout, better recommendations) could shift more volume online and reduce overhead costs.

---

## 🛠️ Tools Used
- Python (pandas, numpy, matplotlib)
- Dataset: Marketing Campaign Dataset (2,240 customers, 29 features)

---

## 📁 Files

| File | Description |
|------|-------------|
| `funnel_analysis.py` | Full Python analysis script |
| `marketing_campaign.csv` | Original dataset |
| `funnel_dashboard.png` | 7-chart visual dashboard |
| `README.md` | This report |

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib
python funnel_analysis.py
```
