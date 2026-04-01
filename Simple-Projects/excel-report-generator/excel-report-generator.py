import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
import os

def load_and_clean(filepath):
    """Load and clean the raw sales data."""
    df = pd.read_csv(filepath)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.title()
    
    # Clean Date column
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    
    # Clean text columns
    df['Sales Person'] = df['Sales Person'].str.strip().str.title().fillna('Unknown')
    df['Region'] = df['Region'].str.strip().str.title().fillna('Unknown')
    df['Product'] = df['Product'].str.strip().str.title().fillna('Unknown')
    
    # Clean numeric columns
    df['Units'] = pd.to_numeric(df['Units'], errors='coerce').fillna(0)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
    
    # Calculate Revenue
    df['Revenue'] = df['Units'] * df['Price']
    
    # Drop rows where Revenue could not be calculated
    df = df.dropna(subset=['Revenue']).reset_index(drop=True)
    
    return df


def salesperson_summary(df):
    """Generate summary by Sales Person."""
    summary = df.groupby('Sales Person').agg(
        Total_Revenue=('Revenue', 'sum'),
        Total_Units=('Units', 'sum'),
        Total_Orders=('Revenue', 'count')
    ).reset_index()

    summary = summary.sort_values('Total_Revenue', ascending=False)
    return summary


def region_summary(df):
    """Find best performing product in each region."""
    region_product = df.groupby(['Region', 'Product'])['Revenue'].sum().reset_index()
    best_per_region = region_product.loc[region_product.groupby('Region')['Revenue'].idxmax()]
    best_per_region.columns = ['Region', 'Best_Product', 'Revenue']
    best_per_region = best_per_region.sort_values('Revenue', ascending=False)
    return best_per_region


def write_report(cleaned_df, salesperson_df, region_df, output_file):
    """Write data to Excel with professional formatting."""
    try:
        # Delete existing file if it exists to avoid permission issues
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except:
                pass

        # Write Excel file
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            cleaned_df.to_excel(writer, sheet_name='Cleaned Data', index=False)
            salesperson_df.to_excel(writer, sheet_name='Summary by SalesPerson', index=False)
            region_df.to_excel(writer, sheet_name='Summary by Region', index=False)


        # Load workbook for formatting
        wb = load_workbook(output_file)

        header_font = Font(name='Arial', size=11, bold=True, color='FFFFFF')
        header_fill = PatternFill('solid', start_color="1F3864")
        center_align = Alignment(horizontal='center')

        for sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            
            # Format header row
            for cell in ws[1]:
                cell.font = header_font
                cell.fill = header_fill
                cell.alignment = center_align

            # Auto-adjust column widths
            for column in ws.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = max_length + 2
                ws.column_dimensions[column_letter].width = adjusted_width

        wb.save(output_file)
        print(f"✅ Successfully created report: {output_file}")

    except PermissionError:
        print("❌ Permission error. Please close any open Excel files and try again.")
    except Exception as e:
        print(f"❌ Error saving file: {e}")


def main():
    df = load_and_clean('raw_sales.csv')
    df2 = salesperson_summary(df)
    df3 = region_summary(df)
    write_report(df, df2, df3, 'sales_report.xlsx')


if __name__ == "__main__":
    main()