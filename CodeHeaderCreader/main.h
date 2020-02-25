#ifndef _MAIN_
#define _MAIN_

#include "headers.h"
#include "optionMenus.h"
#include "timeMade.h"
#include "bullet.h"
#include "HEAD_FORMAT.h"

using namespace std;

inline void conClean();
inline void optionOne(int &optiontmp,
                          std::vector<std::vector<HEAD_FORMAT>> &dataTrans);
void createFileH(std::vector<std::vector<HEAD_FORMAT>> &allHTrans);
void createFunH(std::vector<std::vector<HEAD_FORMAT>> &allHTrans);
std::vector<std::vector<std::string>> funcInOut(int option);

#endif 