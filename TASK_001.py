import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

file_path = r"TASK 01/archive/marketing_campaign.csv"

df = pd.read_csv(file_path, sep="\t")

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

if "Income" in df.columns:
    df["Income"] = df["Income"].fillna(df["Income"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()

if "Income" in df.columns:
    negative_income = (df["Income"] < 0).sum()
    print("\nNegative Income Values:", negative_income)

    if negative_income > 0:
        df = df[df["Income"] >= 0]

if "Year_Birth" in df.columns:
    df["Age"] = 2026 - df["Year_Birth"]

if "Kidhome" in df.columns and "Teenhome" in df.columns:
    df["Total_Children"] = df["Kidhome"] + df["Teenhome"]

spending_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

existing_spending_columns = [
    col for col in spending_columns if col in df.columns
]

df["Total_Spending"] = df[existing_spending_columns].sum(axis=1)

purchase_columns = [
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases"
]

existing_purchase_columns = [
    col for col in purchase_columns if col in df.columns
]

df["Total_Purchases"] = df[existing_purchase_columns].sum(axis=1)

if "Age" in df.columns:
    print("\nAge Range:")
    print("Minimum Age:", df["Age"].min())
    print("Maximum Age:", df["Age"].max())

    before = len(df)

    df = df[
        (df["Age"] >= 18) &
        (df["Age"] <= 100)
    ]

    after = len(df)

    print("Unrealistic Age Records Removed:", before - after)

def find_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    return len(outliers), lower_limit, upper_limit

outlier_columns = [
    "Income",
    "Total_Spending",
    "Total_Purchases"
]

print("\nOutlier Detection:")

for column in outlier_columns:
    if column in df.columns:
        count, lower, upper = find_outliers(column)

        print(f"\n{column}")
        print("Outliers:", count)
        print("Lower Limit:", round(lower, 2))
        print("Upper Limit:", round(upper, 2))

if "Income" in df.columns:
    Q1 = df["Income"].quantile(0.25)
    Q3 = df["Income"].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    df["Income"] = df["Income"].clip(
        lower_limit,
        upper_limit
    )

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

output_folder = "visualizations"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

plt.figure(figsize=(10, 6))
sns.histplot(df["Age"], bins=25, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(f"{output_folder}/01_age_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df["Income"], bins=30, kde=True)
plt.title("Customer Income Distribution")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(f"{output_folder}/02_income_distribution.png", dpi=300)
plt.show()

product_spending = df[existing_spending_columns].sum()

plt.figure(figsize=(10, 6))
sns.barplot(
    x=product_spending.index,
    y=product_spending.values
)
plt.title("Total Spending by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Spending")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/03_product_spending.png", dpi=300)
plt.show()

channel_columns = [
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases"
]

existing_channels = [
    col for col in channel_columns
    if col in df.columns
]

channel_totals = df[existing_channels].sum()

plt.figure(figsize=(9, 6))
sns.barplot(
    x=channel_totals.index,
    y=channel_totals.values
)
plt.title("Purchases by Sales Channel")
plt.xlabel("Sales Channel")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{output_folder}/04_purchase_channels.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Income",
    y="Total_Spending"
)
plt.title("Income vs Total Spending")
plt.xlabel("Income")
plt.ylabel("Total Spending")
plt.tight_layout()
plt.savefig(f"{output_folder}/05_income_vs_spending.png", dpi=300)
plt.show()

if "Education" in df.columns:
    education_spending = (
        df.groupby("Education")["Total_Spending"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=education_spending.index,
        y=education_spending.values
    )
    plt.title("Average Spending by Education Level")
    plt.xlabel("Education")
    plt.ylabel("Average Total Spending")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(
        f"{output_folder}/06_spending_by_education.png",
        dpi=300
    )
    plt.show()

if "Marital_Status" in df.columns:
    marital_spending = (
        df.groupby("Marital_Status")["Total_Spending"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=marital_spending.index,
        y=marital_spending.values
    )
    plt.title("Average Spending by Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Average Total Spending")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(
        f"{output_folder}/07_spending_by_marital_status.png",
        dpi=300
    )
    plt.show()

if "Total_Children" in df.columns:
    children_spending = (
        df.groupby("Total_Children")["Total_Spending"]
        .mean()
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=children_spending.index,
        y=children_spending.values
    )
    plt.title("Average Spending by Number of Children")
    plt.xlabel("Number of Children")
    plt.ylabel("Average Total Spending")
    plt.tight_layout()
    plt.savefig(
        f"{output_folder}/08_spending_by_children.png",
        dpi=300
    )
    plt.show()

if "Response" in df.columns:
    response_counts = df["Response"].value_counts()

    plt.figure(figsize=(8, 6))
    sns.barplot(
        x=response_counts.index.astype(str),
        y=response_counts.values
    )
    plt.title("Marketing Campaign Response")
    plt.xlabel("Response")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(
        f"{output_folder}/09_campaign_response.png",
        dpi=300
    )
    plt.show()

numeric_columns = [
    "Income",
    "Age",
    "Total_Children",
    "Total_Spending",
    "Total_Purchases"
]

existing_numeric = [
    col for col in numeric_columns
    if col in df.columns
]

correlation = df[existing_numeric].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Between Customer Attributes")
plt.tight_layout()
plt.savefig(
    f"{output_folder}/10_correlation_heatmap.png",
    dpi=300
)
plt.show()

highest_product = product_spending.idxmax()

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)

print(
    f"\n1. Highest spending product category: "
    f"{highest_product}"
)

print(
    f"\n2. Average customer spending: "
    f"{df['Total_Spending'].mean():.2f}"
)

print(
    f"\n3. Average purchases per customer: "
    f"{df['Total_Purchases'].mean():.2f}"
)

highest_channel = channel_totals.idxmax()

print(
    f"\n4. Most popular purchasing channel: "
    f"{highest_channel}"
)

if "Response" in df.columns:
    response_rate = df["Response"].mean() * 100

    print(
        f"\n5. Marketing campaign response rate: "
        f"{response_rate:.2f}%"
    )

df.to_csv(
    "cleaned_marketing_campaign.csv",
    index=False
)

print("\n" + "=" * 60)
print("PROJECT COMPLETED")
print("=" * 60)

print("\nCleaned dataset: cleaned_marketing_campaign.csv")
print("Visualizations folder:", output_folder)
print("Final dataset shape:", df.shape)