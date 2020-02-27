#ifndef _MAIN_
#define _MAIN_

#include "headers.h"
#include "sourceMenu.h"
#include "timeMade.h"
#include "bullet.h"
#include "HEAD_FORMAT.h"

inline void conClean();
inline void optionOne(int &optiontmp,
                      std::vector<std::vector<HEAD_FORMAT>> &dataTrans);
void createFileH(std::vector<std::vector<HEAD_FORMAT>> &allHTrans);
void createFunH(std::vector<std::vector<HEAD_FORMAT>> &allHTrans);
std::vector<std::vector<std::string>> funcInput();
std::vector<std::vector<std::string>> funcOutput();
std::string outputFormat(HEAD_FORMAT const &dataTrans,
                         std::string const optionName, int const numChar,
                         bool const option);

#endif