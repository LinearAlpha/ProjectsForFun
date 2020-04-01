#include "ClassHeader.h"

/*****************************************************************************
 * Default Constructor
 ***************************************************************************/
Format::Format() {}

/*****************************************************************************
 * Function: setAuthors
 * Authors: Minpyo Kim
 * Description:
 *      Sets private value of authors in the class
 * Input:
 *      vector<string> authors - name of the authors of fucntion or file
 ***************************************************************************/
void Format::setAuthors(std::vector<std::string> authors)
{
    int numAuthor = authors.size();
    // If there is only one authors, returns single author value for true
    if (numAuthor == 1)
        Format::singleAuthor = true;
    else
        Format::singleAuthor = false;
    Format::authors = authors;
}

/*****************************************************************************
 * Function: setInput
 * Authors: Minpyo Kim
 * Description:
 *      Sets private value of input in the class
 * Input:
 *      vector<string> input - name and type of the input and discription
 ***************************************************************************/
void Format::setInput(std::vector<std::string> input) 
{
    Format::input = input;
}

/*****************************************************************************
 * Function: setInput
 * Authors: Minpyo Kim
 * Description:
 *      Sets private value of input in the class
 * Input:
 *      vector<string> input - name and type of the input and discription
 ***************************************************************************/
void Format::steOutpu(std::vector<std::string> output)
{
    Format::output = output;
}

void Format::setFunvtionName(std::string functionName)
{
    Format::functionName = functionName;
}

void Format::setFileName(std::string fileName)
{
    Format::fileName = fileName;
}

void Format::setDiscription(std::string discription)
{
    Format::discription = discription;
}

void Format::setDate(std::string date)
{
    Format::date = date;
}

std::string Format::getAuthors() const
{
    std::string tmp;
    if (Format::singleAuthor)
        tmp = authors.at(0);
    else
    {
        int numAuthors = authors.size();
        for (int i = 0; i < numAuthors; i++)
        {
            if (i == 0)
                tmp = authors.at(i);
            else
                tmp = tmp + "," + authors.at(i);
        }
    }
    return tmp;
}

std::vector<std::string> Format::getINput() const
{
    return input;
}

std::vector<std::string> Format::getOutput() const
{
    return output;
}

std::string Format::getFunctionName() const
{
    return functionName;
}

std::string Format::getFileName() const
{
    return fileName;
}

std::string Format::getDiscription() const
{
    return discription;
}

std::string Format::getDate() const
{
    return date;
}