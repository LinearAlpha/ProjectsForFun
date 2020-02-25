#ifndef _OPTIONMENUS_
#define _OPTIONMENUS_

#include "headers.h"
#include "bullet.h"

inline void menu(int &optionTmp)
{
    std::cout << "0. Exit" << std::endl;
    std::cout << "1. Create or edit Header" << std::endl;
    std::cout << "2. Read or edit Created Header" << std::endl;
    std::cout << ">> ";
    std::cin >> optionTmp;
    // cheking user input to make sure it is integer val within option
    bulProof(optionTmp, 0, 2);
}

inline void createMenu(int &optionTmp)
{
    std::cout << "0. Return to the main menu" << std::endl;
    std::cout << "1. Create project file header" << std::endl;
    std::cout << "2. Create function header" << std::endl;
    std::cout << ">>";
    std::cin >> optionTmp;
    // cheking user input to make sure it is integer val within option
    bulProof(optionTmp, 0, 2);
}

inline void optionSubMenu(int &optionTmp, std::string opName)
{
    std::cout << "\n\nYou entered" << opName << "\n"
         << "0. To return to menu\n"
         << "1. To continu\n"
         << ">>";
    std::cin >> optionTmp;
    // cheking user input to make sure it is integer val within option
    bulProof(optionTmp, 0, 1);
    std::cout << std::endl;
}

inline void optionSubMenu(int &optionTmp)
{
    std::cout << "\t\tAuto date format mm/dd/yyyy\n"
         << "\t\t0. Auto current date\n"
         << "\t\t1. Manula date\n"
         << "\t\t>> ";
    std::cin >> optionTmp;
    // cheking user input to make sure it is integer val within option
    bulProof(optionTmp, 0, 1);
}


#endif // ! _OPTIONMENUS_