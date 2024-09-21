#include <bits/stdc++.h>
using namespace std;
float f(float x){
	return pow(x,3)+3*pow(x,2)-3;
} 
float daycung(float a, float b){
	float exp = 0.001;
	float x; 
	do{
		x = a-(b-a)*f(a)/(f(b)-f(a));
		if(f(a)*f(x)<0)		b = x;
		else 	a = x;
	}while(abs(a-b)>exp);
	return x;
}
int main(){
	float a,b; //(-3;-2)
	cout<<"Nhap 1 khoang ly nghiem a,b: ";
	cin>>a>>b;
	cout<<"Nghiem gan dung x = "<<daycung(a,b);
}
