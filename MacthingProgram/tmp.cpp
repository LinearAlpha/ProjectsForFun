#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>


int main()
{
    string mod1, mod2, tmp1, tmp2, save;
vector<string> vecMod1, vecMod2, vecTmp, vectmp2;
fstream originalFile("test1.csv", ios::in);
if (originalFile.is_open())
{
    while (getline(originalFile, mod1))
    {
        vecMod1.push_back(mod1);
        cout << mod1 << endl;
    }
    originalFile.close();
}
fstream secondFile("test2.csv", ios::in);
if (secondFile.is_open())
{
    while (getline(secondFile, mod2))
    {
        vecMod2.push_back(mod2);
        cout << mod2 << endl;
    }
    secondFile.close();
}
for (int i = 0; i < vecMod1.size(); i++)
{
    tmp1 = vecMod1[i];
    tmp1 = tmp1.erase(0, tmp1.find(',') + 1);
    tmp1 = tmp1.substr(0, tmp1.find(','));
    cout << tmp1 << endl;
    int flag = 0;
    for (int k = 0; k < vectmp2.size(); k++)
    {
        if (tmp1 == vectmp2[k])
            flag = 1;
    }
    if (flag == 0)
    {
        for (int j = 0; j < vecMod2.size(); j++)
        {
            tmp2 = vecMod2[j];
            tmp2 = tmp2.substr(0, tmp2.find(','));
            cout << tmp2 << endl;

            if (tmp1.compare(tmp2) == 0)
            {
                vecTmp.push_back(vecMod2[j]);
                vectmp2.push_back(tmp1);
                break;
            }
        }
    }
}
string location, qyt, num;
vector<string> tmpSave, tmpSave2, numLoc;
for (int i = 0; i < vecTmp.size(); i++)
{
    tmp1 = vecTmp[i];
    tmp1 = tmp1.substr(0, tmp1.find(','));
    for (int j = 0; j < vecMod1.size(); j++)
    {
        tmp2 = vecMod1[j];
        tmp2 = tmp2.erase(0, tmp2.find(',') + 1);
        tmp2 = tmp2.substr(0, tmp2.find(','));
        if (tmp1.compare(tmp2) == 0)
        {
            string tmp;
            location = vecMod1[j].substr(0, vecMod1[j].find(','));
            tmpSave.push_back(location);
            tmp = vecMod1[j].erase(0, vecMod1[j].find(',') + 1);
            tmp = tmp.erase(0, tmp.find(',') + 1);
            qyt = tmp.substr(0, tmp.find(','));
            tmpSave2.push_back(qyt);
            int number = j + 1;
            num = to_string(number);
            numLoc.push_back(num);
        }
    }
    mod1 = vecTmp[i];
    location = tmpSave[0];
    qyt = tmpSave2[0];
    num = numLoc[0];
    if (tmpSave.size() > 1)
    {
        for (int k = 1; k < tmpSave.size(); k++)
        {
            if (tmpSave[k].length() != 0)
                location = location + '/' + tmpSave[k];
            if (tmpSave2[k].length() != 0)
                qyt = qyt + '/' + tmpSave2[k];
            num = num + '/' + numLoc[k];
        }
    }
    int toNum = 0;
    for (int a = 0; a < tmpSave2.size(); a++)
    {
        int x = atoi(tmpSave2[a].c_str());
        toNum += x;
    }
    tmpSave.clear();
    tmpSave2.clear();
    numLoc.clear();
    mod1 = mod1 + ',' + location + ',' + qyt + ',' + num + ',' + to_string(toNum);
    vecTmp[i] = mod1;
}
fstream reasultFile("test3.csv", ios::out);
if (reasultFile.is_open())
{
    reasultFile << "Part #, Qty , Cost ,Truck Count, Var , ABS Var , Location , QTY , Spreadsheet Row(s), totalQTY\n";
    for (int i = 0; i < vecMod2.size(); i++)
    {
        string strout;
        strout = vecMod2[i];
        tmp1 = vecMod2[i];
        tmp1 = tmp1.substr(0, tmp1.find(','));
        for (int j = 0; j < vecTmp.size(); j++)
        {
            tmp2 = vecTmp[j];
            tmp2 = tmp2.substr(0, tmp2.find(','));
            if (tmp1.compare(tmp2) == 0)
            {
                strout = vecTmp[j];
                break;
            }
        }
        reasultFile << strout << "\n";
    }
    reasultFile.close();
}
fstream reasultFile2("test4.csv", ios::out);
if (reasultFile2.is_open())
{
    reasultFile2 << "Part #, Qty , Cost ,Truck Count, Var , ABS Var , Location , QTY , Spreadsheet Row(s), totalQTY\n";
    for (int i = 0; i < vecTmp.size(); i++)
        reasultFile2 << vecTmp[i] << "\n";
    reasultFile2.close();
}

}

