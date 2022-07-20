
print(f'{"MTG CARDS":-^45}') #string with max 45 characters aligned center with bars 
l = ('Narset, Enlightened Master', 1.29, 'Teferi, Time Raveler', 18.91, 'Jace, Mind Sculptor', 46.89,
'Narset, Parter of Veils', 1.67, 'Narset Transcendent', 7.50, 'Chandra, Torch of Defiance ', 11.27,
"Eslspeth, Sun's Nemesis", 0.95, 'Kaya, Orzhov Usurper', 2.70)



for c in range(0, len(l)) :
    if c % 2 == 0 :
        print(f'{l[c]:-<45}', end=' ') #string with max 45 characters aligned left with bars , dont jump line using end=' '
    else  :
        print(f'US$ {l[c]:>5.2f}') #string with max 5 characters aligned right with 2 numbers after comma
