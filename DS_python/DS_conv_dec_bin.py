## importation des modules

## declaration des constante

## declaration des fonction
def dec_to_bin(nb_dec:int)->str:
    """
    @input nb_dec: type int
    
    revoie une chaine de caractere contenant la  conversion en binaire de nb_dec
    """
    if nb_dec == 0:
        return '0'
    elif nb_dec == 1:
        return '1'
    else:
        return dec_to_bin(nb_dec//2) + str(nb_dec % 2)
    
def bin_to_dec(nb_bin:str)->int:
    """
    @input nb_bin: type str
    
    revoie un contenant la conversion en decimal de nb_bin
    """
    if nb_bin == "0":
        return 0
    elif nb_bin == "1":
        return 1
    else:
        if nb_bin[-1] == "0":
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
    
def rom_to_dec(nb_rom:str)->int:
    if nb_rom == 'M':
        return 1000
    elif nb_rom == 'D':
        return 500
    elif nb_rom == 'C':
        return 100
    elif nb_rom == 'L':
        return 50
    elif nb_rom == 'X':
        return 10
    elif nb_rom == 'V':
        return 5
    elif nb_rom == 'I':
        return 1
    else:
        if nb_rom[0] == 'M':
            add = 1000
        elif nb_rom[0] == 'D':
            add = 500
        elif nb_rom[0] == 'C':
            add = 100
        elif nb_rom[0] == 'L':
            add = 50
        elif nb_rom[0] == 'X':
            add = 10
        elif nb_rom[0] == 'V':
            add = 5
        elif nb_rom[0] == 'I':
            add = 1
        try:
            if rom_to_dec(nb_rom[1]) > add:
                add = -add
        except:
            pass
        return rom_to_dec(nb_rom[1:]) + add


def dec_to_rom(nb_dec:int)->str:
    if nb_dec >= 1000:
        add = 'M'
    elif nb_dec >= 900 and nb_dec < 1000:
        add = 'CM'
    elif nb_dec >= 990 and nb_dec < 1000:
        add = 'XM'
     elif nb_dec >= 999 and nb_dec < 1000:
        add = 'IM'
    elif nb_dec >= 500:
        add = 'D'
    elif nb_dec >= 400 and nb_dec < 500:
        add = 'CD'
    elif nb_dec >= 490 and nb_dec < 500:
        add = 'XD'
    elif nb_dec >= 499 and nb_dec < 500:
        add = 'ID'
    elif nb_dec >= 100:
        add = 'C'
    elif nb_dec >= 90 and nb_dec < 100:
        add = 'XC'
    elif nb_dec >= 99 and nb_dec < 100:
        add = 'IC'
    elif nb_dec >= 50:
        pass
    


## declaration des class

## fonction principal
def main():
    print(dec_to_bin(28))
    print(bin_to_dec('101011'))
    print(rom_to_dec('MMXXIV'))

## programme principal
if __name__ == '__main__':
    main()