#ifndef _HEAD_FORMAT_
#define _HEAD_FORMAT_

#include "headers.h"

class HEAD_FORMAT
{
private:
    std::string proName;
    std::string funName;
    std::string author;
    std::string filenName;
    std::string date;
    std::string descrive;
    std::vector<std::vector<std::string>> input;
    std::vector<std::vector<std::string>> output;

public:
    HEAD_FORMAT();
    HEAD_FORMAT(std::string proName, std::string funName, std::string author,
                std::string fileName, std::string date, std::string descrive,
                std::vector<std::vector<std::string>> input,
                std::vector<std::vector<std::string>> output);
    void setProName(std::string pronName);
    void setFunName(std::string funName);
    void setAuthor(std::string author);
    void setFileName(std::string fileName);
    void setDate(std::string date);
    void setDescrive(std::string descrive);
    void setInput(std::vector<std::vector<std::string>> input);
    void setOutput(std::vector<std::vector<std::string>> output);
    std::string getProName() const;
    std::string getFunNsme() const;
    std::string getAuthor() const;
    std::string getFileName() const;
    std::string getDate() const;
    std::string getDescrive() const;
    std::vector<std::vector<std::string>> getInput() const;
    std::vector<std::vector<std::string>> getOutput() const;
};
#endif
