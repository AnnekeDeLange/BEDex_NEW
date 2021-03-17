# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print('Leek is '+str(leek_price)+' euro per kilo.') # keep - part of assignment
leeks_ordered = 'leek 4'
### last_name_len = len(player[player.find(' ')+1:]) expample syntax
## print(leeks_ordered[leeks_ordered.find(' ')+1])
## print(type(leek_price))
sum_total_leeks = ( int(leeks_ordered[leeks_ordered.find(' ')+1]) * leek_price)
print(sum_total_leeks) # keep - part of assignment
broccoli_price = 2.34
broccoli_ordered = 'broccoli 1.6'
ordered_kilos_broccoli = broccoli_ordered[broccoli_ordered.find(' ')+1:]
# print(ordered_kilos_broccoli)
# print(type(float(ordered_kilos_broccoli)))
# sum_total_broccolis = round( float(broccoli_ordered[broccoli_ordered.find(' ')+1:]) * broccoli_price,2)
sum_total_broccolis = round( float(ordered_kilos_broccoli) * broccoli_price, 2)
# print(sum_total_broccolis) 
# print(rounded_sum_total_broccolis)
# print('\''+str(ordered_kilos_broccoli)+'kg broccoli costs 500.34e'+'\'') # keep - part of assignment
# print(str(ordered_kilos_broccoli)+'kg broccoli costs 3.74e') # keep - part of assignment
print(str(ordered_kilos_broccoli)+'kg broccoli costs '+ str(sum_total_broccolis)+'e') # keep - part of assignment
