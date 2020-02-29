#include "main.h"

using namespace std;

int main()
{
    int option = 0;
    bool flag = true;
    // index 0 for fileH and index 1 for funH
    vector<vector<HEAD_FORMAT>> allH(2, vector<HEAD_FORMAT>());
    do
    {
        conClean(); // cleaning terminal
        cout << "Header creader!!!\n\n"
             << "Today is: " << lTime(1) << endl;
        cout << "UTC: " << utcTime(1) << "\n\n";
        menu(option); // print main options for this program
        conClean();   // cleaning terminal
        // exit
        if (option == 0)
        {
            flag = false;
            cout << "\n\nGood bay and Thank you!!!!!!!\n\n\n";
        }
        // Create or edit Header
        else if (option == 1)
        {
            optionOne(option, allH);
        }
        // Read or edit Created Header
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

inline void optionOne(int &optiontmp,
                      vector<vector<HEAD_FORMAT>> &dataTrans)
{
    int flag = 0; // flag for submenus
    // flag for the do loop is original option
    do
    {
        bool optionOne = true;
       // bool optionTwo = true;
        cout << "Local: " << lTime(1) << "\nUTC: " << utcTime(1) << "\n\n";
        string tmp;
        createMenu(optiontmp);
        switch (optiontmp)
        {
        case 1:
            if (optionOne)
            {
                optionSubMenu(i, "file header creater");
                optionOne = false;
            }
            if (i == 1)
                createFileH(dataTrans);
            break;
        case 2:
            // printing sub menu to check user entered right menu
            optionSubMenu(flag, " function header creater");
            if (flag == 1)
                createFunH(dataTrans);
            break;
        default:
            break;
        }
    } while (optiontmp != 0);
}

void createFileH(vector<vector<HEAD_FORMAT>> &allHTrans)
{
    HEAD_FORMAT headTmp;
    string tmp;
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
    // To determine auto time or manual
    optionSubMenu(i);
    // i == 0, auto
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
    // 2D vector, indext 0 fileH
    allHTrans[0].push_back(headTmp);
    cout << "\n\nCreted\n\n";
}

void createFunH(vector<vector<HEAD_FORMAT>> &allHTrans)
{
    HEAD_FORMAT headTmp;
    string tmp;
    cout << "\n\nFunction name: ";
    getline(cin, tmp);
    headTmp.setProName(tmp);
    cout << "\tAuthor: ";
    getline(cin, tmp);
    headTmp.setAuthor(tmp);
    // reall funInOut to get function input and output
    headTmp.setInput(funcInput());
    headTmp.setOutput(funcOutput());
    int i;
    // To determine auto time or manual
    optionSubMenu(i);
    // i == 0, auto
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
    // 2D vector, indext 1 funH
    allHTrans[1].push_back(headTmp);
    cout << "\n\nCreted\n\n";
}

vector<vector<string>> funcInput()
{
    // index 0, name of func
    // index 1 descrive
    vector<vector<string>> tmp(2, vector<string>());
    int count;
    cout << "\tHow many input do you have?\n"
         << ">> ";
    cin >> count;
    // cheking user input to make sure it is integer val within option
    bulProof(count, 0, 1000);
    for (int i = 0; i < count; i++)
    {
        string tmpNa, tmpDes;
        cout << "Name of the input\n"
             << "- ";
        getline(cin, tmpNa);
        // index 0, name function
        tmp[0].push_back(tmpNa);
        cout << "Description\n"
             << "-  ";
        getline(cin, tmpDes);
        // index 1, descrive
        tmp[1].push_back(tmpDes);
    }
    return tmp;
}

vector<vector<string>> funcOutput()
{
    // index 0, name of func
    // index 1 descrive
    vector<vector<string>> tmp(2, vector<string>());

    int count;
    cout << "\tOut puts\n"
         << "\tHow many output do you have?\n"
         << ">> ";
    cin >> count;
    // cheking user input to make sure it is integer val within option
    bulProof(count, 0, 1000);
    for (int i = 0; i < count; i++)
    {
        string tmpNa, tmpDes;
        cout << "Name of the output\n"
             << ">> ";
        getline(cin, tmpNa);
        tmp[0].push_back(tmpNa);
        cout << "Description\n"
             << ">> ";
        getline(cin, tmpDes);
        tmp[1].push_back(tmpDes);
    }
    return tmp;
}

string outputFormat(HEAD_FORMAT const &dataTrans, string const optionName,
                    int const numChar, bool const option)
{
    string tmpTrans, tmp, tmpChrL;
    for (int i = 0; i < numChar; i++)
        tmp = tmp + "*";
    tmpTrans = tmp + "\n* " + optionName + ": ";
    if (option)
    {
        tmpChrL = dataTrans.getFileName();
        int num = tmpChrL.size() + optionName.size() + 4;
        if (num <= numChar)
            tmp = tmp + tmpChrL + "\n";
        else if (num > numChar)
        {
            string tmpSec;
            num = optionName.size() + 4;
        }
    }
    return tmp;
}
