def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    # celsius = input()
    # 
    celsius = float(input())

    fahrenheit = float(celsius) * 9/5 + 32

    print(fahrenheit)
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    # return value should be float or int value
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
