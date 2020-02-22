#include "bullet.h"

inline void cleanPipe()
{
    std::cin.clear();
    std::cin.ignore(1000, '\n');
}

void bulProof(int& input, const int lowBound, const int upBound)
{
    bool flag = true;
    while (flag)
    {
        cleanPipe();
        if (std::cin.fail())
        {
            std::cout << "\n\tPlease enter number within range" << std::endl;
            std:: cout << ">>";
            std::cin >> input;
        }
        else if (lowBound > input || input > upBound)
        {
            std::cout << "\n\tPlease enter a number between"
                    << lowBound << " and " << upBound << std::endl;
            std::cout << ">>";
            std::cin >> input;
        }
        else
            flag = false;
    }
}