#include <iostream>
#include <vector>
#include <cstring>
#include <sstream>
#include <fstream>
#include <stack>

using namespace std;

bool is_op(char value)
{
	if (value == '+' || value == '-' || value == '*' || value == '/')
		return true;
}

bool is_less_than_or_eq(char value1, char value2)
{
	if (value1 == '/' || value1 == '*')
	{
		if (value2 == '+' || value2 == '-')
			return false;
	}
	return true;
}

int main(int argc, char * argv[])
{
	vector< char > cv;
	vector< string >name;
	string input_line;

	getline(cin, input_line);
	for (int i = 0; i < input_line.size(); i++) {
		if (input_line[i] != ' ') {
			cv.push_back(input_line[i]);
			
			// Create the names for the nodes
			//stringstream out;
			//out << cv.size() - 1;
			//name.push_back("n" + out.str());
		}
	}

	// Parse the tree into RPN
	stack<char> op_stack;
	vector<char> output;

	for (int i = 0; i < cv.size(); i++)
	{
		if (cv[i] >= '1' && cv[i] <= '9')
			output.push_back(cv[i]);
		else if (is_op(cv[i]))
		{
			if (op_stack.size() == 0)
				op_stack.push(cv[i]);
			else
			{
				if (is_less_than_or_eq(cv[i], op_stack.top()))
				{
					for (int j = op_stack.size(); j > 0; j--)
					{
						if (is_less_than_or_eq(cv[i], op_stack.top()))
						{
							output.push_back(op_stack.top());
							op_stack.pop();
						}
						else
							break;
					}
					op_stack.push(cv[i]);
				}
				else
				{
					op_stack.push(cv[i]);
				}
			}
		}
		else if (cv[i] == '(')
		{
			op_stack.push('(');
		}
		else if (cv[i] == ')')
		{
			while (op_stack.top() != '(')
			{
				output.push_back(op_stack.top());
				op_stack.pop();
			}
			op_stack.pop();
		}
	}

	for (int i = 0; i < op_stack.size(); i++)
	{
		output.push_back(op_stack.top());
		op_stack.pop();
		if (op_stack.size() == 1)
			output.push_back(op_stack.top());
	}

	for (int i = 0; i < output.size(); i++)
		cout << output[i] << endl;

	/*ofstream file;
	file.open("graph.dot");
	file << "digraph G {\n\t";
	file.close();
	file.open("graph.dot", ios::app);

	for (int i = 0; i < cv.size(); i++) {
		//cout << cv[i] << endl;
		if ((cv[i] == '*' || cv[i] == '/' || cv[i] == '+' || cv[i] == '-') &&
			(cv[i - 1] == '*' || cv[i - 1] == '/' || cv[i - 1] == '+' || cv[i - 1] == '-')) {
			file << name[i] << " [label = \"" << cv[i] << "\"];\n\t";
			file << name[i - 1] << " [label = \"" << cv[i - 1] << "\"];\n\t";

			file << name[i] << "->" << name[i - 1] << "\n\t";
			file << name[i] << "->" << name[i - 4] << "\n\t";
		}
		else if (cv[i] == '*' || cv[i] == '/' || cv[i] == '+' || cv[i] == '-') {
			file << name[i] << " [label = \"" << cv[i] << "\"];\n\t";
			file << name[i - 1] << " [label = \"" << cv[i - 1] << "\"];\n\t";
			file << name[i - 2] << " [label = \"" << cv[i - 2] << "\"];\n\t";

			file << name[i] << "->" << name[i - 1] << "\n\t";
			file << name[i] << "->" << name[i - 2] << "\n\t";
		}
	}
	file << "\n}";
	file.close();*/

	return 0;
}