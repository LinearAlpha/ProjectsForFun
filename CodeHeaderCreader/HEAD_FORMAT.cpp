#include "HEAD_FORMAT.h"

HEAD_FORMAT::HEAD_FORMAT() {}
HEAD_FORMAT::HEAD_FORMAT(std::string proName, std::string funName, 
                         std::string author, std::string fileName,
                         std::string date, std::string descrive)
{
    setProName(proName);
    setFunName(funName);
    setAuthor(author);
    setFileName(fileName);
    setDate(date);
    setDescrive(descrive);
}
void HEAD_FORMAT::setProName(std::string pronNameTrans)
{
    this->proName = pronNameTrans;
}
void HEAD_FORMAT::setFunName(std::string funNameTrans)
{
    this->funName = funNameTrans;
}
void HEAD_FORMAT::setAuthor(std::string authorTrans)
{
    this->author = authorTrans;
}
void HEAD_FORMAT::setFileName(std::string fileNameTreans)
{
    this->filenName = fileNameTreans;
}
void HEAD_FORMAT::setDate(std::string dateTreans)
{
    this->date = dateTreans;
}
void HEAD_FORMAT::setDescrive(std::string descriveTrans)
{
    this->descrive = descriveTrans;
}
std::string HEAD_FORMAT::getProName() const
{
    return proName;
}
std::string HEAD_FORMAT::getFunNsme() const
{
    return funName;
}
std::string HEAD_FORMAT::getAuthor() const
{
    return author;
}
std::string HEAD_FORMAT::getFileName() const
{
    return filenName;
}
std::string HEAD_FORMAT::getDate() const
{
    return date;
}
std::string HEAD_FORMAT::getDescrive() const
{
    return descrive;
}
