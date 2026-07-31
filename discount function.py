def apply_discount(price, discount):
    if type(price) is bool or not isinstance(price, (int, float)):
        return 'The price should be a number.'
        
    if type(discount) is bool or not isinstance(discount, (int, float)):
        return 'The discount should be a number.'
        
    if price <= 0:
        return 'The price should be greater than 0.'
        
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100.'
        
    return price - (price * discount / 100)