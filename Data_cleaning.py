import pandas as pd

def clean_data():
    # Load datasets
    womens_western = pd.read_csv("women_westernwear.csv")
    mens_western = pd.read_csv("mens_westernwear.csv")
    laptops = pd.read_csv("laptops.csv")
    mobs = pd.read_csv("mobiles.csv")
    baby = pd.read_csv("baby.csv")
    food = pd.read_csv("food.csv")
    footwear = pd.read_csv("women_footwear.csv")
    furni = pd.read_csv("furn.csv")
    books = pd.read_csv("books.csv")

    # Process all datasets
    for df in [books, furni, footwear, food, baby, mobs, mens_western, womens_western, laptops]:
        # Remove commas in price columns and convert to numeric
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        df['Original Prices'] = df['Original Prices'].str.replace(',', '').astype(float)

        # Clean and convert discount rates
        df['Discount rates'] = df['Discount rates'].str.replace('% off', '', regex=False)
        df['Discount rates'] = pd.to_numeric(df['Discount rates'], errors='coerce').fillna(0).astype(int)

    # Drop rows with missing values
    books_nona = books.dropna()
    furni_nona = furni.dropna()
    baby_nona = baby.dropna()
    laptops_nona = laptops.dropna()
    footwear_nona = footwear.dropna()
    womens_western_nona = womens_western.dropna()
    food_nona = food.dropna()
    mobs_nona = mobs.dropna()
    mens_western_nona = mens_western.dropna()

    # Assign categories using .loc to avoid warnings
    books_nona.loc[:, 'Category'] = 'Books'
    furni_nona.loc[:, 'Category'] = 'Furniture'
    baby_nona.loc[:, 'Category'] = 'Baby'
    laptops_nona.loc[:, 'Category'] = 'Laptops'
    footwear_nona.loc[:, 'Category'] = 'Footwear'
    womens_western_nona.loc[:, 'Category'] = 'Women Westernwear'
    food_nona.loc[:, 'Category'] = 'Food'
    mobs_nona.loc[:, 'Category'] = 'Mobiles'
    mens_western_nona.loc[:, 'Category'] = 'Men Westernwear'

    # Combine datasets
    combined_data = pd.concat([
        books_nona, furni_nona, baby_nona, laptops_nona,
        footwear_nona, womens_western_nona, food_nona,
        mobs_nona, mens_western_nona
    ], ignore_index=True)

    return combined_data

if __name__ == "__main__":
    # Clean the data and save it to a CSV
    data = clean_data()
    data.to_csv("/Users/vedantbrahmbhatt/Desktop/Flipkart_DA/cleaned_data.csv", index=False)
    print("Data cleaning complete. Cleaned file saved as 'cleaned_data.csv'.")

   