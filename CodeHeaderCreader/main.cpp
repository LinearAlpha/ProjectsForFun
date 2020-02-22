#include "headers.h"
#include "timeMade.h"
#include "bullet.h"

using namespace std;

inline void menu(int &optionTmp);
inline void createMenu(int &optionTmp);

int main()
{
    int option = 0;
    do
    {
        cout << "Header creader!!!\n\n" << "Today is: " << lTime(1) << endl;
        cout << "UTC: " << utcTime(1);
        menu(option);
        if (option == 1)
        {
            system("CLS");
            option = 0;
            cout << "Local: " << lTime(1) << endl;
            cout << "UTC: " << utcTime(1) << "\n\n";
            do
            {
                createMenu(option);
                switch (option)
                {
                case 1:

                    break;
                default:
                    break;
                }
            } while (option != 0);
        }
        else if (option == 2)
        {
            /* code */
        }

    } while (!(option));
}

inline void menu(int &optionTmp)
{
    cout << "0. Exit";
    cout << "1. Create Header" << endl;
    cout << "2. Read Created Header" << endl;
    cout << ">> ";
    cin >> optionTmp;
    bulProof(optionTmp, 0, 2);
}

inline void createMenu(int &optionTmp)
{
    cout << "0. Return to the main menu" << endl;
    cout << "1. Create project file header" << endl;
    cout << "2. Create function header" << endl;
    cout << ">>";
    cin >> optionTmp;
    bulProof(optionTmp, 0, 2);
}