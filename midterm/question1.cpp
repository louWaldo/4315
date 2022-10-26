#include <iostream>
#include <string>




int main()
{
    int list[] = {1, 2, 3, 4};
    std::string s_list[] = {"dog", "cat", "horse", "puppy"};
    for(int i = 0; i < 4; i++)
    {
        std::cout << list[i];
        std::cout << s_list[i];
    }
}