#include <iostream>

void inSort(int a[], int length);

int main(){
    int a[] = {8, 4, 9, 5, 7, 6, 3, 2};
    inSort(a, 8);
    for(int i = 0; i < 8; i++)
    {
        std::cout << a[i] << " ";
    }
    return 0;
}

void inSort(int a[], int length){
    for(int i = 1; i < length; i++)
    {
        int key = a[i];
        int j = i-1;
        while(j >= 0 && a[j] > key)
        {
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1] = key;
    }
}