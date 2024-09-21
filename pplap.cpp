#include <iostream>
using namespace std;

//chia doi
/*
float f(float x) {
	return pow(x, 3) - x - 1;
}

float chiadoi(float a, float b) {
	float esp = 0.01;
	float c = (a + b) / 2;

	if (f(a) * f(b) < 0) {
		while (f(c) != 0 && fabs(a - b) > esp) {
			c = (a + b) / 2;
			if (f(a) * f(c) < 0)
				b = c;
			else
				a = c;
		}
		return c;
	}
}

int main() {
	cout << chiadoi(1, 2);
}
*/

//lap
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


//day cung
//float f(float x) {
//	return pow(x, 3) + 3 * pow(x, 2) - 3;
//}
//float daycung(float a, float b) {
//	float exp = 0.001;
//	float x;
//	do {
//		x = a - (b - a) * f(a) / (f(b) - f(a));
//		if (f(a) * f(x) < 0)		b = x;
//		else 	a = x;
//	} while (abs(a - b) > exp);
//	return x;
//}
//int main() {
//	float a, b; //(-3;-2)
//	cout << "Nhap 1 khoang ly nghiem a,b: ";
//	cin >> a >> b;
//	cout << "Nghiem gan dung x = " << daycung(a, b);
//}

//tiep tuyen

//float f(float x) {
//	return 5 * pow(x, 3) - 20 * x + 3;
//}
//float fdh(float x) { //f'(x)
//	return 15 * pow(x, 2) - 20;
//}
//float tieptuyen(float a, float b) { //(a,b) = (0,1)
//	float exp = 0.0001;
//	float x = 0; //chon x0=a vi f(a) va f"(x) cung dau 
//	float y;
//	do {
//		y = x;
//		x = y - f(y) / fdh(y);
//	} while (abs(x - y) > exp);
//	return x;
//}
//int main() {
//	float a, b;
//	cout << "Nhap 1 khoang ly nghiem a,b: ";
//	cin >> a >> b;
//	cout << "Nghiem gan dung x = " << tieptuyen(a, b);
//}
