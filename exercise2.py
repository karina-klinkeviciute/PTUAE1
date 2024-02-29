'''
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True ``` ```
'''
def sleep_in(weekday, vacation):
    if vacation is True:
        return True
    elif weekday != True:
        return True
    else:
        return False

result = sleep_in(True, True)
print(result)
