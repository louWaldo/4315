#include <iostream>
#include <string>
using namespace std;

void slice(int start, int end, int step, int distance, int* a, int* b){
    int j = 0;
    for (int i = start; i < end; i += step)
    {
        b[j] = a[i];
        j++;
    }
    for (int i = 0; i < distance; i++)
    {
        cout << b[i] << endl;
    }
}


int main(){
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int b[10];
    int start;
    int end;
    int step;

    cout << "start: ";
    std::cin >> start;
    cout << "end: ";
    std::cin >> end;
    cout << "step: ";
    std::cin >>step;

    int distance = (end - start)/step;

    slice(start, end, step, distance, a, b);

}