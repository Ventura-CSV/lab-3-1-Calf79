def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))
    if number>=100:
        range=3
    else: 
        if number>=50:
         range=2
        else:
         range=1
        
    """
    Make your code here
    """

    print(f'Range is {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()
