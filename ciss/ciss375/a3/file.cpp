#include <iostream>
#include <vector>
#include <cstring>
#include <sstream>
#include <fstream>

using namespace std;

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
			stringstream out;
			out << cv.size() - 1;
			name.push_back("n" + out.str());
		}
	}

	ofstream file;
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
	file.close();

	return 0;
}