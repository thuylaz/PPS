#include <bits/stdc++.h>
using namespace std;
float f(float x){
	return 5*pow(x,3)-20*x+3;
} 
float fdh(float x){ //f'(x)
	return 15*pow(x,2)-20;
}
float tieptuyen(float a, float b){ //(a,b) = (0,1)
	float exp = 0.0001;
	float x = 0; //chon x0=a vi f(a) va f"(x) cung dau 
	float y;
	do{
		y = x;
		x = y - f(y)/fdh(y);
	}while(abs(x-y)>exp);
	return x;
}
int main(){
	float a,b;
	cout<<"Nhap 1 khoang ly nghiem a,b: ";
	cin>>a>>b;
	cout<<"Nghiem gan dung x = "<<tieptuyen(a,b);
}
