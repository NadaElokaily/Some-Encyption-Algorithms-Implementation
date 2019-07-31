#include <iostream>
#include <string>
#include <conio.h>
using namespace std;
int main()
{
    long long Key=0 ;
    long long tmp=0;
    string PlainText="",CipherText="";
    cin>>Key;
    cin>>PlainText;
    int Size=PlainText.length();
    //cout << Size<<endl;
    for (int i =0; i< Size;i++){
        tmp= (int)PlainText[i]+Key;
        if (tmp>=90){
            tmp-=65;
            tmp-=((tmp/26)*26);
            tmp+=65;
            CipherText[i]=(char)tmp;
        }
        else{
            CipherText[i]=(char)tmp;
        }
        cout<<CipherText[i];
    }
    return 0;
}
