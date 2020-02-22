#include "timeMade.h"

std::string lTime(const int option)
{
    std::time_t now = std::time(0);
    std::tm* ltm = std::localtime(&now);
    int year = 1900 + ltm->tm_year;
    int month = 1 + ltm->tm_mon;
    int day = ltm->tm_mday;
    int hour = ltm->tm_hour;
    int minute = ltm->tm_min;
    int second = ltm->tm_sec;
    std::string tmp;
    if (option == 1)
        tmp = std::to_string(month) + "/" + std::to_string(day) + "/" +
              std::to_string(year) + '\n' + std::to_string(hour) + ":" +
              std::to_string(minute) + ":" + std::to_string(second);
    else if (option == 2)
        tmp = std::to_string(month) + "/" + std::to_string(day) + "/" +
              std::to_string(year);
    return tmp;
}

std::string utcTime(const int option)
{
    std::time_t now = std::time(0);
    std::tm* gmtm = std::gmtime(&now);
    int year = 1900 + gmtm->tm_year;
    int month = 1 + gmtm->tm_mon;
    int day = gmtm->tm_mday;
    int hour = gmtm->tm_hour;
    int minute = gmtm->tm_min;
    int second = gmtm->tm_sec;
    std::string tmp;
    if (option == 1)
        tmp = std::to_string(month) + "/" + std::to_string(day) + "/" +
              std::to_string(year) + '\n' + std::to_string(hour) + ":" +
              std::to_string(minute) + ":" + std::to_string(second);
    else if (option == 2)
        tmp = std::to_string(month) + "/" + std::to_string(day) + "/" +
              std::to_string(year);
    return tmp;
}