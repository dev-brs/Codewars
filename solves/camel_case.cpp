//https://www.codewars.com/kata/517abf86da9663f1d2000003

#include <string>
#include <iostream>

using namespace std;

string to_camel_case(string text)
{
    string msg;
    bool capitalizeNext = false;

    for (auto c : text)
    {
        if (c == '-' || c == '_')
        {
            capitalizeNext = true;
        }
        else
        {
            if (capitalizeNext)
            {
                msg += toupper(c);
                capitalizeNext = false;
            }
            else
            {
                msg += c;
            }
        }
    }

    return msg;
}