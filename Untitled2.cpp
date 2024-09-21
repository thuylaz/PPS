#include<bits/stdc++.h>
using namespace std;


float f(float x) {
	return 3 * pow(x, 3) - 10 * x + 5; //khai bao ham f(x)
}
float g(float x) {
	return pow(((10*x-5)/3), 1.0 / 3.0); //ham tuong duong f(x)
}
float lap(float a, float b) {
	float exp = 0.01;
	float x = a;
	float y;
	do {
		y = x;
		x = g(x);
	} while (abs(x - y) > exp);
	return x;
}
int main() {
	float a, b;
	cout << "nhap 1 khoang ly nghiem a,b: ";
	cin >> a >> b;
	cout << "nghiem gan dung: " << lap(a, b);
}
