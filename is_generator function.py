def is_generator(g,p):
    results = set()
    # g^1 mod p
    current_value = g % p
    for k in range(1,p): # from 1 to p-1
        results.add(current_value)
        # g^(k+1) mod p
        current_value = (current_value * g) % p

    if len(results) == p-1:
        print(f'{g} is a generator for F{p}.')
    else:
        print(f'{g} is not a generator for F{p}.')
        
is_generator(3,29)
    

    


