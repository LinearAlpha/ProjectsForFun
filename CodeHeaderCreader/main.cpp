#include "headers.h"
#include "timeMade.h"
#include "bullet.h"
#include "HEAD_FORMAT.h"

using namespace std;

inline void conClean();
inline void menu(int &optionTmp);
inline void createMenu(int &optionTmp);
inline void oprionOneMenu(int &optiontmp, vector<HEAD_FORMAT> &dataTrans);
void createFileH(vector<HEAD_FORMAT> &allFuncHTrans);
void createFuncH();

int main()
{
    int option = 0;
    bool flag = true;
    vector<HEAD_FORMAT> allFuncH;
    do
    {
        conClean();
        cout << "Header creader!!!\n\n"
             << "Today is: " << lTime(1) << endl;
        cout << "UTC: " << utcTime(1) << "\n\n";
        menu(option);
        if (option == 0)
        {
            flag = false;
            conClean();
            cout << "\n\nGood bay and Thank you!!!!!!!\n\n\n";
        }
        else if (option == 1)
        {
            conClean();
            oprionOneMenu(option, allFuncH);
        }
        else if (option == 2)
        {
            /* code */
        }
    } while (flag);
}

inline void conClean()
{
    // For unix
    system("clear");

    // // For Windows
    // system("CLS")
}

inline void menu(int &optionTmp)
{
    cout << "0. Exit" << endl;
    cout << "1. Create or edit Header" << endl;
    cout << "2. Read or edit Created Header" << endl;
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

inline void oprionOneMenu(int &optiontmp, vector<HEAD_FORMAT> &dataTrans)
{
    do
    {
        cout << "Local: " << lTime(1) << "\nUTC: " << utcTime(1) << "\n\n";
        string tmp;
        createMenu(optiontmp);
        switch (optiontmp)
        {
        case 1:
            createFileH(dataTrans);
            cout << "\n\ncreted\n\n";
            break;
        case 2:

            break;
        default:
            break;
        }
    } while (optiontmp != 0);
}

void createFileH(vector<HEAD_FORMAT> &allFuncHTrans)
{
    HEAD_FORMAT headTmp;
    std::string tmp;
    cout << "\n\tProgram Name: ";
    getline(cin, tmp);
    headTmp.setProName(tmp);
    cout << "\tFile Name: ";
    getline(cin, tmp);
    headTmp.setFileName(tmp);
    headTmp.setDate(lTime(2));
    cout << "\tDescrive: ";
    getline(cin, tmp);
    headTmp.setDescrive(tmp);
    allFuncHTrans.push_back(headTmp);
}
