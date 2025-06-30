import pandas as pd
import os

# Paths to dataset files
legit_path = os.path.join("data", "top-1m.csv")
phish_path = os.path.join("data", "phishing_urls_48K.csv")

# Load datasets
print("📥 Loading datasets...")
legit_df = pd.read_csv(legit_path)
phish_df = pd.read_csv(phish_path)

# Add labels
legit_df["label"] = 0  # Legitimate
phish_df["label"] = 1  # Phishing

# Merge
print("🔗 Merging datasets...")
merged_df = pd.concat([legit_df, phish_df], ignore_index=True)

# Shuffle
print("🔀 Shuffling data...")
merged_df = merged_df.sample(frac=1).reset_index(drop=True)

# Save merged dataset
output_path = os.path.join("data", "merged_dataset.csv")
merged_df.to_csv(output_path, index=False)

print(f"✅ Merged dataset saved as '{output_path}'")