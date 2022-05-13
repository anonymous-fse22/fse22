from typing import Optional
# 
# Approximating the exponential function correctly (Python)
# 
# Copyright (c) 2020 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/approximating-eulers-number-correctly
# 



# For example: compute_exp(20000, 4) = "7.3891"
def compute_exp(x: int, accuracy: int) -> Optional[int]:
    # if accuracy < 0:
    # 	raise ValueError()
    # if x < 0:
    # 	raise ValueError("Negative numbers not supported")
    # if x == 0:
    # 	return format_decimal(10 ** accuracy, accuracy)
    
    extra_precision = 4
    accuracy_scaler = 10 ** accuracy
    extra_scaler    = 10 ** extra_precision
    full_scaler = accuracy_scaler * extra_scaler
    
    sum_low  = 0
    sum_high = 0
    term_low  = full_scaler
    term_high = full_scaler
    floor_x = x // accuracy_scaler
    i = 0
    itr = 0
    while True:
        if term_low <= 0:
            break
        if itr >= 100:
            break
        sum_low  = sum_low + term_low
        sum_high = sum_high + term_high
        term_low = term_low  * x
        term_low = term_low // accuracy_scaler
        high_accuracy_scaler = accuracy_scaler + 1
        term_high = term_high * x
        term_high = term_high // high_accuracy_scaler
        
        if i > floor_x:
            if term_high < extra_scaler:
                sum_upper_bound = sum_high + term_high
                temp: int = sum_low // extra_scaler
                temp = round(temp)
                upper: int = sum_upper_bound // extra_scaler
                upper = round(upper)
                if upper == temp:
                    # Note: The number of terms used is i+1
                    return temp
        
        i = i + 1
        term_low  = term_low  // i
        term_high = term_high // i
        term_high = term_high + 1
        itr = itr + 1

    return None


def test_approx_exp() -> None:
    res = compute_exp(3, 2)
    assert res == 103

test_approx_exp()
