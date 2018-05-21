'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

def num_routes (dim):

  rt_loc = [1,2,3]
  dn_loc = [2,0,1]
  tr_loc = [2,2,6]
  dct_list = {
    '1' : 3,
  }
  dbl_loc = [0,0,0]

  x = 0

  while(x < dim):
    
    rt_loc = tr_loc
    dn_loc[0] = dn_loc[0] + 1
    hldr = dn_loc[2]
    add_to_dict = []

    for key in dct_list:
      hldr = hldr + dct_list[key]
      add_to_dict.append(hldr)

      if(int(key) == rt_loc[1] - 1):
        dbl = hldr + rt_loc[2]
        dct_list['1'] = dct_list['1'] + 1
  
    last_key = str(rt_loc[1])
    dct_list[last_key] = dbl
    add_to_dict.append(dbl)
    dic_list = {}
    
    z = 1
    for elem in add_to_dict:
      dct_list[str(z)] = add_to_dict[z - 1]
      z = z + 1

    dbl_loc[2] = dbl * 2
    dbl_loc[0] = dn_loc[0]
    dbl_loc[1] = rt_loc[1] + 1
    tr_loc = dbl_loc

    x = x + 1
  
  return(tr_loc[2])

print(num_routes(18))
