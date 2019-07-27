#!/usr/bin/python3

def main():
	import cppyy

	# Bring Cobject header file into cppyy
	# All class definition and implentations are included in this file
	cppyy.include('Cobject.h')

	# Initialize new Cobject instance
	print('c = cppyy.gbl.Cobject(): ')
	c = cppyy.gbl.Cobject()
	print('')

	# Call Cobject member function // shows stdout works
	print('c.print_hello_world():\t ')
	c.print_hello_world()

	# Type conversions:
	i = c.get_int()		# int -> int
	print('c.i:\t %d' % (i))

	f = c.get_double() 	# double -> float
	print('c.d:\t %f' % (f))
	
	ch = c.get_char() 	# char -> str
	print('c.c:\t %c' % (ch))

	s = c.get_string()	# string -> str	
	print('c.str:\t %s' % (s))

	ls = c.get_vec_int()	# vector<int> -> list
	ls = list(ls)
	print('c.vec:\t %s' % (str(ls)))

	dic = c.get_map()	# unordered_map<string, string> -> dict
	dic = dict(dic)
	print('c.map:\t %s' % (str(dic)))
	
	# Type conversions to numpy types

	# short -> np.dtype(np.int16)
        # int -> np.dtype(np.int32)
        # long -> np.dtype(np.int64)
        # float -> np.dtype(np.float32)
        # double -> np.dtype(np.float64)
	print('')


	# Manipulating class data
	print('c.vec[0]:\t %d' % (c.vec[0]))
	c.vec[0] = 18
	print('c.vec[0]:\t %d' % (c.vec[0]))

	print('c.vec.size():\t %d' % (c.get_vec_int().size()))
	c.vec.push_back(2)
	print('c.vec.size():\t %d' % (c.get_vec_int().size()))

	print('c.map["pineapple"]:\t %s' % (c.get_map()['pineapple']))
	# cannot reassign unordered_map data like this
	# c.map['pineapple'] = 'gold'

	print('')

	# Since int types don't change, 
	# the C++ function Cobject::add(int, int) is able to accept native Python integers.
	two_num_sum = c.add(5, 2)
	print('c.add(5, 2):\t %d' % (two_num_sum))

	# Since vector<int> must be converted to a list to use in Python,
	# the C++ function Cobject::add(vector<int>) is not able to accept a native Python list.
	# If you can give this function a C++ vector<int> object, it still works though. 
	ls_sum = c.add(c.get_vec_int())
	print('c.add(vec):\t %d' % (ls_sum))


if __name__ == "__main__":
        main()
