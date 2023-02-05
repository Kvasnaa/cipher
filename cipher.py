alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher (work_text, shift_num, direction):
    end_text = ""
    for one_letter in work_text:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if direction == "encode":
                new_index = index + shift_num
                end_text += alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift_num
                end_text += alphabet[new_index]    
        else:
            end_text += one_letter
    print(f"Vaše operace byla {direction} s výsledkem: {end_text}")

lets_continue = "yes"
while lets_continue == "yes":
    direction = input("Napište 'encode' pro zakódování a 'decode' pro odkódování: ").lower()
    text = input("Zadejte pracovní text/slovo: ").lower()
    shift = int(input("Zadejte o kolik chcete text/slovo posunout: "))
    cipher(text, shift, direction)
    lets_continue = input("Zadejte 'yes' pro další práci a 'no' pro ukončení programu.\n").lower()

