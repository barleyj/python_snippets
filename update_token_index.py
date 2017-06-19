def get_fields():
    for x in range(20):
        yield 'foo.bar{0}'.format(x)
        
def update_token_index():

    fields = get_fields()
    
    if not fields:
        return False

    
