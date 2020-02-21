/******************************************************************************
* PROJECT: data organizer
* FILE: FileIO.cpp
* AUTHOR(S): Minpyo Kim
* DATE: 02/21/2020
* DESCRIPTION: This console-based program imitates a product part number, QYT
*              and location organizer.
******************************************************************************/
#include "commonheader.h"
#include "fileIO.h"

/********************************************************************
* Function:	fileChck
* AUTHOR(S): Minpyo Kim
* Description: It is cheking the file is optn or not
* Input: bool check: true for open
* Output: bool true for open
*********************************************************************/

bool fileChck(bool check)
{
    if (check)
        return true;
    else
        throw std::invalid_argument("It is not able to find a file or directory");
}

/********************************************************************
* Function:	readingdata
* AUTHOR(S): Minpyo Kim
* Description: Reading data from cvs file and return vector
* Input: string fileName: name of the file try to open
* Output: vector : data had been readed from file
*********************************************************************/
std::vector<std::string> readingdata(std::string fileName)
{
    std::fstream fileRead(fileName, std::ios::in);
    std::vector<std::string> input;
    std::string tmp;
    if (fileChck(fileRead.is_open()))
    {
        while (std::getline(fileRead, tmp))
            input.push_back(tmp);
    }
    return input;
}

void writeData(std::vector<std::string> out, std::string fileName)
{
    std::fstream fileOut(fileName, std::ios::out);
    int count = out.size();
    if (fileChck(fileOut.is_open()))
    {
        for (int i = 0; i < count; i++)
            fileOut << out[i] << "\n";
    }
    else
        throw std::invalid_argument("It is not able to find a file or directory");
}

void appedOut(std::string out, std::string fileName)
{
    std::fstream fileOut(fileName, std::ios::out | std::ios::app);
    if (fileChck(fileOut.is_open()))
        fileOut << out << "\n";
}