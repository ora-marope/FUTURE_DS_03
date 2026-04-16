# ============================================================
# Task 3: Marketing Funnel & Conversion Performance Analysis
# Future Interns – Data Science & Analytics
# Intern: MAROPE ORATILE | CIN: FIT/MAR26/DS15648
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings("ignore")

# ── LOAD & CLEAN DATA ──────────────────────────────────────
df = pd.read_csv("marketing_campaign.csv", sep='\t')
df = pd.DataFrame([x.split(';') for x in df.iloc[:,0]], columns=df.columns[0].split(';'))

num_cols = ['Income','MntWines','MntFruits','MntMeatProducts','MntFishProducts',
            'MntSweetProducts','MntGoldProds','NumDealsPurchases','NumWebPurchases',
            'NumCatalogPurchases','NumStorePurchases','NumWebVisitsMonth',
            'AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5',
            'Response','Recency']
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df['TotalSpend']   = df[['MntWines','MntFruits','MntMeatProducts',
                           'MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)
df['TotalPurchases'] = df[['NumWebPurchases','NumCatalogPurchases','NumStorePurchases']].sum(axis=1)

# ── KPI SUMMARY ────────────────────────────────────────────
print("=" * 50)
print("   MARKETING FUNNEL ANALYSIS – KPI SUMMARY")
print("=" * 50)
print(f"  Total Customers          : {len(df):,}")
print(f"  Final Conversion Rate    : {df['Response'].mean()*100:.1f}%")
print(f"  Avg Spend per Customer   : ${df['TotalSpend'].mean():.0f}")
print(f"  Web Purchases            : {df['NumWebPurchases'].sum():,}")
print(f"  Catalog Purchases        : {df['NumCatalogPurchases'].sum():,}")
print(f"  Store Purchases          : {df['NumStorePurchases'].sum():,}")
print()
for i in range(1, 6):
    print(f"  Campaign {i} Acceptance   : {df[f'AcceptedCmp{i}'].mean()*100:.1f}%")
print("=" * 50)

# ── DASHBOARD ──────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")
BLUE,GREEN,ORANGE,PURPLE,RED = "#2563EB","#16A34A","#EA580C","#7C3AED","#DC2626"

fig = plt.figure(figsize=(20, 14))
fig.patch.set_facecolor("#F8FAFC")
gs  = GridSpec(3, 3, figure=fig, hspace=0.48, wspace=0.38)

fig.text(0.5, 0.98, "Marketing Funnel & Conversion Performance Dashboard",
         ha="center", fontsize=17, fontweight="bold", color="#1E293B")
fig.text(0.5, 0.955,
         f"Total Customers: {len(df):,}   |   Conversion Rate: {df['Response'].mean()*100:.1f}%   |   Avg Spend: ${df['TotalSpend'].mean():.0f}",
         ha="center", fontsize=11, color="#64748B")

# (A) Campaign acceptance rates
ax1 = fig.add_subplot(gs[0, :2])
camp_rates = [df[f'AcceptedCmp{i}'].mean()*100 for i in range(1,6)] + [df['Response'].mean()*100]
labels = ['Campaign 1','Campaign 2','Campaign 3','Campaign 4','Campaign 5','Final Response']
bar_colors = [GREEN if v == max(camp_rates) else RED if v == min(camp_rates) else BLUE for v in camp_rates]
bars = ax1.bar(labels, camp_rates, color=bar_colors, edgecolor='white', width=0.55)
for bar, val in zip(bars, camp_rates):
    ax1.text(bar.get_x()+bar.get_width()/2, val+0.1, f"{val:.1f}%", ha='center', fontsize=10, fontweight='bold')
ax1.set_title("Campaign Acceptance Rates Across Funnel", fontweight="bold", fontsize=12)
ax1.set_ylabel("Acceptance Rate %")
ax1.set_ylim(0, max(camp_rates)*1.3)

# (B) Channel performance donut
ax2 = fig.add_subplot(gs[0, 2])
channels = [df['NumWebPurchases'].sum(), df['NumCatalogPurchases'].sum(), df['NumStorePurchases'].sum()]
ax2.pie(channels, labels=['Web','Catalog','Store'], autopct='%1.1f%%',
        colors=[BLUE, ORANGE, GREEN], startangle=90, wedgeprops=dict(width=0.55))
ax2.set_title("Purchases by Channel", fontweight="bold", fontsize=12)

# (C) Spend by product category
ax3 = fig.add_subplot(gs[1, 0])
prod_spend = pd.Series({
    'Wines': df['MntWines'].sum(), 'Meat': df['MntMeatProducts'].sum(),
    'Gold': df['MntGoldProds'].sum(), 'Fish': df['MntFishProducts'].sum(),
    'Sweets': df['MntSweetProducts'].sum(), 'Fruits': df['MntFruits'].sum()
}).sort_values()
ax3.barh(prod_spend.index, prod_spend.values, color=PURPLE, edgecolor='white')
ax3.set_title("Total Spend by Product Category", fontweight="bold", fontsize=12)
ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v/1000:.0f}K"))

# (D) Income vs Total Spend
ax4 = fig.add_subplot(gs[1, 1])
sample = df.dropna(subset=['Income']).sample(500, random_state=42)
ax4.scatter(sample['Income'], sample['TotalSpend'], alpha=0.3, s=15, color=BLUE)
ax4.set_title("Income vs Total Spend", fontweight="bold", fontsize=12)
ax4.set_xlabel("Income ($)")
ax4.set_ylabel("Total Spend ($)")
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v/1000:.0f}K"))

# (E) Conversion by education
ax5 = fig.add_subplot(gs[1, 2])
edu_conv = df.groupby('Education')['Response'].mean().mul(100).sort_values()
ax5.barh(edu_conv.index, edu_conv.values, color=ORANGE, edgecolor='white')
ax5.set_title("Conversion Rate by Education", fontweight="bold", fontsize=12)
ax5.set_xlabel("Conversion Rate %")
for i,(idx,val) in enumerate(edu_conv.items()):
    ax5.text(val+0.1, i, f"{val:.1f}%", va='center', fontsize=9)

# (F) Recency vs conversion
ax6 = fig.add_subplot(gs[2, :2])
df['RecencyBucket'] = pd.cut(df['Recency'], bins=[0,20,40,60,80,100],
                              labels=['0-20','21-40','41-60','61-80','81-100'])
rec_conv = df.groupby('RecencyBucket')['Response'].mean().mul(100)
ax6.bar(rec_conv.index, rec_conv.values, color=[GREEN,BLUE,ORANGE,RED,PURPLE], edgecolor='white', width=0.5)
ax6.set_title("Conversion Rate by Recency (days since last purchase)", fontweight="bold", fontsize=12)
ax6.set_xlabel("Days Since Last Purchase")
ax6.set_ylabel("Conversion Rate %")
for i,val in enumerate(rec_conv.values):
    ax6.text(i, val+0.1, f"{val:.1f}%", ha='center', fontsize=10, fontweight='bold')

# (G) Avg spend: converted vs not
ax7 = fig.add_subplot(gs[2, 2])
spend_conv = df.groupby('Response')['TotalSpend'].mean()
ax7.bar(['Not Converted','Converted'], spend_conv.values, color=[RED, GREEN], edgecolor='white', width=0.4)
ax7.set_title("Avg Spend:\nConverted vs Not", fontweight="bold", fontsize=12)
ax7.set_ylabel("Avg Total Spend ($)")
for i,val in enumerate(spend_conv.values):
    ax7.text(i, val+5, f"${val:.0f}", ha='center', fontsize=11, fontweight='bold')

plt.savefig("funnel_dashboard.png", dpi=150, bbox_inches="tight", facecolor="#F8FAFC")
print("\n✅ Dashboard saved: funnel_dashboard.png")
