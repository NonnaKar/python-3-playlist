# write to a file 
with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there, python is awesome!')


#  amend to a file    
with open('files/write.txt', 'a') as write_file:    
    write_file.write('\nI love it so much, I dream in python')

# new line character - \n 
quotes = [
    '\nI can resist everything exept temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:    
    write_file.writelines(quotes )