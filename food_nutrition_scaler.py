import pandas as pd

# Load files
survey_df = pd.read_csv("/Users/marsguy/Desktop/Research/Unit conversion using AI/final output.csv")
ref_df = pd.read_csv("/Users/marsguy/Desktop/Research/Unit conversion using AI/FPED_1112.csv")

# Track unmatched food codes
unmatched_codes = set()

def scale_nutrition(row):
    food_code = row['food_code']
    ref_row = ref_df[ref_df['FOODCODE'] == food_code]
    
    if ref_row.empty:
        unmatched_codes.add(food_code)
        return pd.Series()
    else:
        try:
            # Ensure we're only working with numeric columns
            numeric_cols = ref_row.select_dtypes(include=['number']).columns
            scaled_values = ref_row[numeric_cols].mul(row['serving_size_by_100'], axis=0)
            
            # Combine with description
            return pd.concat([
                ref_row[['DESCRIPTION']],
                scaled_values
            ], axis=1).iloc[0]
        except Exception as e:
            print(f"Error processing food code {food_code}: {str(e)}")
            unmatched_codes.add(food_code)
            return pd.Series()

# Apply scaling
output_df = survey_df.join(
    survey_df.apply(scale_nutrition, axis=1)
)

# Save output
output_df.to_csv("/Users/marsguy/Desktop/Research/Unit conversion using AI/FPED_CH.csv", index=False)

# Print unmatched codes
print("Unmatched food codes:", unmatched_codes)
with open("/Users/marsguy/Desktop/Research/Unit conversion using AI/unmatched_codes.txt", "w") as f:
    f.write("\n".join(map(str, unmatched_codes)))