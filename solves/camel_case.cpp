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