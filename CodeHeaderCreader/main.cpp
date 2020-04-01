/*****************************************************************************
 * Project: Header creader
 * File: Main.cpp
 * Authors: Minpyo Kim
 * Date: 04/01/2020 ~ 
 * Description:
 *      It creates head for the programming projects by the option it can 
 *      choose inbetween file and function header.
 ***************************************************************************/
#include "BulletProof.h"
#include "Headers.h"

inline void cleanTerminal();
inline void mainMenu(int &option);
inline void subMenuLag(int &option);

using namespace std;

int main()
{
    cleanTerminal();
    bool flag = true;
    cout << "Welcome to Header Creater!!!!\n"
         << endl;
    int option;
    do
    {
        mainMenu(option);
        switch (option)
        {
        case 1:
            subMenuLag(option);
            if (option != 0)

                break;
        default:
            flag = false;
            cleanTerminal();
            cout << "Thank you for using!!!!!" << endl;
            cout << "Any kind of bug or problme please email:" << endl;
            cout << "kim00922@umn.edu\n"
                 << endl;
            break;
        }
    } while (flag);
}

/*****************************************************************************
 * Function: cleanTerminal
 * Authors: Minpyo Kim
 * Description:
 *      Clearn the terminal screen
 ***************************************************************************/
inline void cleanTerminal()
{
    system("clear");
}

/*****************************************************************************
 * Function: mainMenu
 * Authors: Minpyo Kim
 * Description:
 *      Print option main option entery, and returen user option choose.
 * Input:
 *      int& option - user chose of the oprion (pointer)
 ***************************************************************************/
inline void mainMenu(int &option)
{
    cout << "What kind of header do you what to create." << endl;
    cout << "1. File Header" << endl;
    cout << "2. Function Header" << endl;
    cout << "0. Exit" << endl;
    cout << ">> ";
    cin >> option;
    // Check user input
    bulProof(option, 0, 2);
}

/*****************************************************************************
 * Function: subMenuLag
 * Authors: Minpyo Kim
 * Description:
 *      Print option main option entery, and returen user option choose.
 * Input:
 *      int& option - user chose of the oprion (pointer)
 ***************************************************************************/
inline void subMenuLag(int &option)
{
    cout << "\tWhat is your language" << endl;
    cout << "\t1. C/C++" << endl;
    cout << "\t2. Python" << endl;
    cout << "\t0. Return to Main Menu" << endl;
    cout << "\t>> ";
    cin >> option;
    // Check user input
    bulProof(option, 0, 2);
    if (option == 0)
        cout << "\n\n\n";
}