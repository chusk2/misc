def factorize(num_list):
    factorized_denoms = {}
    for item in num_list:
        factorized_denoms[item] = {}
        num = item
        divisor = 2  # start checking divisors from 2
        # as long as quotient is less than 1, keep on factorizing
        while num > 1:
            # keep factorizing with current divisor while is possible
            while num % divisor == 0:
                # add divisor to list of factors of item
                if divisor not in factorized_denoms[item].keys():
                    factorized_denoms[item][divisor] = 1
                    num //= divisor  # use the quotient as new dividend
                # divisor was already in list of factors of item, so add +1
                else:
                    factorized_denoms[item][divisor] += 1
                    num //= divisor
            # if while loop has ended, try with a superior divisor
            divisor += 1
    # dictionary with minimum common multiplier
    mcm_factors = {}
    # iterate over the factorizations of each denominator
    for factor in factorized_denoms.values():
        for k, v in factor.items():  # k = divisor, v = power of divisor
            # if divisor is already in list and the new factorization
            # has a greater power, substitute with the greatest power
            # common divisors powered to the maximum power
            if k in mcm_factors.keys() and v > mcm_factors[k]:
                # replace old power with the newer and greater one
                mcm_factors[k] = v
            else:
                # if it is a new divisor, just add it the list
                mcm_factors[k] = v
    return mcm_factors
