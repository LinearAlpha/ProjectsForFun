#ifndef _FILEIO_
#define _FILEIO_

#include<fstream>
#include<iostream>

// Fubction properties
bool fileChck(bool check);
std::vector<std::string> readingdata(std::string fileName);
void writeData(std::vector<std::string> out, std::string fileName);


#endif

