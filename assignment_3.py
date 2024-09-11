# function calculate_discount

def calculate_discount (price, discount_percent):
    """
# parameters:
    price(float):the original price of the item

    discount_percent (float):The discount percentage to be applied

Returns:
float:The final price after discount or the original price if no discount is applied
"""
    if discount_percent >= 20:
        discount_amount = (price*discount_percent )/ 100
        final_price = price - discount_amount
        
    else:
        final_price = price
    return final_price
def main():
    try:
        #Prompt user for input
        price = float (input ("What is the original price of the item?"))
        discount_percent = float (input ("What is the discount percentage?"))

        #calculate the final rice
        final_price = calculate_discount(price,discount_percent)

        # Print the result
        print(f"The final price after applying the discount is:${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()


    
   
   
