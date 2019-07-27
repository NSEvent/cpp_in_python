// Kevin Tang
// Started 7/17/2019

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

class Cobject {
public:
	Cobject() { std::cout << "Created new Cobject instance." << std::endl; }

	void print_hello_world() {
		std::cout << 
		"Hello World! This print function was ultimately called from a C++ member function using cppyy.\n" <<
		"To get a better idea of how a C++ class is imported, look at main.py and Cobject.h,\n" <<
		"Notice that main.py was able to instantiate Cobject and access member functions below.\n\n"; 
	}

	int get_int() { return i; }

	double get_double() { return d; }

	char get_char() { return c; }

	std::string get_string() { return str; }

	std::vector<int> get_vec_int() { return vec; }

	std::unordered_map<string, string> get_map() { return map; }

	
	int add(int num1, int num2) { return num1 + num2; }
	int add(vector<int> v) {
		int sum = 0;
		for(auto num: v) sum += num; 
		return sum;
	}

	int i = 81;
	double d = 81.81;
	char c = 'K';
	std::string str = "Testing C++ std::string and how it converts to a Python string";
	std::vector<int> vec = {5, 4, 3, 2, 1};
	std::unordered_map<string, string> map = {{"strawberry", "red"}, {"blueberry", "blue"},
						  {"orange", "orange"}, {"pineapple", "yellow"}};
}; 
