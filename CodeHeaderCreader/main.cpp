#include "headers.h"
#include "timeMade.h"
#include "bullet.h"
#include "HEAD_FORMAT.h"

using namespace std;

inline void conClean();
inline void menu(int &optionTmp);
inline void createMenu(int &optionTmp);
inline void oprionOneMenu(int &optiontmp,
                          vector<vector<HEAD_FORMAT>> &dataTrans);
inline void optionSubMenu(int &optionTmp, string opName);
inline void optionSubMenu(int &optionTmp);
void createFileH(vector<vector<HEAD_FORMAT>> &allHTrans);
void createFunH(vector<vector<HEAD_FORMAT>> &allHTrans);
vector<vector<string>> funcInOut(int option);

int main()
{
    int option = 0;
    bool flag = true;
    // index 1 for fileH and index 2 for funH
    vector<vector<HEAD_FORMAT>> allH(2, vector<HEAD_FORMAT>());

    do
    {
        conClean();
        cout << "Header creader!!!\n\n"
             << "Today is: " << lTime(1) << endl;
        cout << "UTC: " << utcTime(1) << "\n\n";
        menu(option);
        conClean();
        if (option == 0)
        {
            flag = false;
            cout << "\n\nGood bay and Thank you!!!!!!!\n\n\n";
        }
        else if (option == 1)
        {
            oprionOneMenu(option, allH);
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

inline void oprionOneMenu(int &optiontmp,
                          vector<vector<HEAD_FORMAT>> &dataTrans)
{
    int i = 0;
    do
    {
        cout << "Local: " << lTime(1) << "\nUTC: " << utcTime(1) << "\n\n";
        string tmp;
        createMenu(optiontmp);
        switch (optiontmp)
        {
        case 1:
            optionSubMenu(i, "file header creater");
            if (i == 1)
                createFileH(dataTrans);
            else
                break;
        case 2:
            optionSubMenu(i, " function header creater");
            createFunH(dataTrans);
            break;
        default:
            break;
        }
    } while (optiontmp != 0);
}

inline void optionSubMenu(int &optionTmp, string opName)
{
    cout << "\n\nYou entered" << opName << "\n"
         << "0. To return to menu\n"
         << "1. To continu\n"
         << ">>";
    cin >> optionTmp;
    bulProof(optionTmp, 0, 1);
}

inline void optionSubMenu(int &optionTmp)
{
    cout << "\t\tAuto date format mm/dd/yyyy\n"
         << "\t\t0. Auto current date\n"
         << "\t\t1. Manula date\n"
         << "\t\t>> ";
    cin >> optionTmp;
    bulProof(optionTmp, 0, 1);
}

void createFileH(vector<vector<HEAD_FORMAT>> &allHTrans)
{
    HEAD_FORMAT headTmp;
    std::string tmp;
    cout << "\n\tProgram Name: ";
    getline(cin, tmp);
    headTmp.setProName(tmp);
    cout << "\tAuthor: ";
    getline(cin, tmp);
    headTmp.setAuthor(tmp);
    cout << "\tFile Name: ";
    getline(cin, tmp);
    headTmp.setFileName(tmp);
    int i;
    // to determine auto date or manual
    optionSubMenu(i);
    if (i == 0)
        headTmp.setDate(lTime(2));
    else
    {
        cout << "\tDate: ";
        getline(cin, tmp);
        headTmp.setDate(tmp);
    }
    cout << "\tDescrive: ";
    getline(cin, tmp);
    headTmp.setDescrive(tmp);
    allHTrans[1].push_back(headTmp);
    cout << "\n\nCreted\n\n";
}

void createFunH(vector<vector<HEAD_FORMAT>> &allHTrans)
{
    HEAD_FORMAT headTmp;
    std::string tmp;
    cout << "\n\nFunction name: ";
    getline(cin, tmp);
    headTmp.setProName(tmp);
    cout << "\tAuthor: ";
    getline(cin, tmp);
    headTmp.setAuthor(tmp);
    headTmp.setInput(funcInOut(1));
    headTmp.setOutput(funcInOut(2));
    getline(cin, tmp);
    headTmp.setFileName(tmp);
    int i;
    // to determine auto date or manual
    optionSubMenu(i);
    if (i == 0)
        headTmp.setDate(lTime(2));
    else
    {
        cout << "\tDate: ";
        getline(cin, tmp);
        headTmp.setDate(tmp);
    }
    cout << "\tDescrive: ";
    getline(cin, tmp);
    headTmp.setDescrive(tmp);
    allHTrans[0].push_back(headTmp);
    cout << "\n\nCreted\n\n";
}

vector<vector<string>> funcInOut(int option)
{
    vector<vector<string>> tmp(2, vector<string>());
    if (option == 1)
    {
        int count;
        cout << "\tOut puts\n" << "\tHow many input do you have?\n" << ">> ";
        cin >> count;
        bulProof(count, 0, 1000);
        for (int i = 0; i < count; i++)
        {
            string tmpNa, tmpDes;
            cout << "Name of the input\n" << ">> ";
            getline(cin, tmpNa);
            tmp[0].push_back(tmpNa);
            cout << "Description\n" << ">> ";
            getline(cin, tmpDes); 
            tmp[1].push_back(tmpDes);
        }
    }
    else if (option == 2)
    {
                int count;
        cout << "\tOut puts\n" << "\tHow many output do you have?\n" << ">> ";
        cin >> count;
        bulProof(count, 0, 1000);
        for (int i = 0; i < count; i++)
        {
            string tmpNa, tmpDes;
            cout << "Name of the output\n" << ">> ";
            getline(cin, tmpNa);
            tmp[0].push_back(tmpNa);
            cout << "Description\n" << ">> ";
            getline(cin, tmpDes); 
            tmp[1].push_back(tmpDes);
        }
    }
    return tmp;
}
