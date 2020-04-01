#ifndef _CLASSHEADER_
#define _CLASSHEADER_

// C++ headers that commenly ues on this program
#include "Headers.h"

/*****************************************************************************
 * Class: Format
 * Authors: Minpyo Kim
 * Description:
 *      A class that represent datas for header format
 ***************************************************************************/
class Format
{
private:
    std::vector<std::string> authors;
    std::vector<std::string> input;
    std::vector<std::string> output;
    std::string functionName;
    std::string fileName;
    std::string discription;
    std::string date;
    bool singleAuthor;

public:
    // Function discritions are located on the ClassHeader.cpp
    Format();
    void setAuthors(std::vector<std::string> authors);
    void setInput(std::vector<std::string> input);
    void steOutpu(std::vector<std::string> output);
    void setFunvtionName(std::string functionName);
    void setFileName(std::string fileName);
    void setDiscription(std::string discription);
    void setDate(std::string date);
    std::string getAuthors() const;
    std::vector<std::string> getINput() const;
    std::vector<std::string> getOutput() const;
    std::string getFunctionName() const;
    std::string getFileName() const;
    std::string getDiscription() const;
    std::string getDate() const;
};

#endif