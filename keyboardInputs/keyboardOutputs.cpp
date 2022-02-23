#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#include <vector>
using namespace std;


void Vkrun(CHAR chr)
{
	SHORT key;
	UINT mappedkey;
	INPUT input = { 0 };
	key = VkKeyScan(chr); // converts the key to a keystroke(a single depression of key on keyboard)
	mappedkey = MapVirtualKey(LOBYTE(key), 0); // maps a virtual-key code into a scan code
	input.type = INPUT_KEYBOARD;
	input.ki.dwFlags = KEYEVENTF_SCANCODE;
	input.ki.wScan = mappedkey;
	SendInput(1, &input, sizeof(input));
	Sleep(30);
	input.ki.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP;
	SendInput(1, &input, sizeof(input));
}

void Vkothers(char key)
{
	UINT mappedkey;
	INPUT input = { 0 };
	mappedkey = MapVirtualKey(LOBYTE(key), 0); // maps a virtual-key code into a scan code
	input.type = INPUT_KEYBOARD;
	input.ki.dwFlags = KEYEVENTF_SCANCODE;
	input.ki.wScan = mappedkey;
	SendInput(1, &input, sizeof(input));
	Sleep(30);
	input.ki.dwFlags = KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP;
	SendInput(1, &input, sizeof(input));
}



int main(){

	//Loading data
	ifstream data("hundred.csv");// file object data
	if(!data.is_open()) {cout << "ERROR: File didnt open." << endl; return 0;}

	std::vector <string> anArray;
	string temp;
	while(data.peek()!=EOF)
    {
		getline(data,temp,',');
		anArray.push_back(temp);

		getline(data,temp,',');
		anArray.push_back(temp);

		getline(data,temp,',');
		anArray.push_back(temp);

		getline(data,temp,',');
		anArray.push_back(temp);

		getline(data,temp,'\n');
		anArray.push_back(temp);
	}
	data.close();
	for (int i = 0; i < anArray.size(); i++){
				cout << anArray[i] << '\n';
	}


	//Typing and execution
 	while (true){
		
		Sleep(100);
		if (GetAsyncKeyState(VK_NUMPAD0)) {// exit
			return 0;
		}
		
		if (GetAsyncKeyState(VK_NUMPAD2)) {// left mouse button click
			INPUT iNPUT = { 0 };
			iNPUT.type = INPUT_MOUSE;
			iNPUT.mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
			SendInput(1, &iNPUT, sizeof(iNPUT));
			ZeroMemory(&iNPUT, sizeof(iNPUT));
			iNPUT.type = INPUT_MOUSE;
			iNPUT.mi.dwFlags = MOUSEEVENTF_LEFTUP;
			SendInput(1, &iNPUT,sizeof(iNPUT));
			Sleep(500);
		}

		if (GetAsyncKeyState(VK_NUMPAD1)) {
		string word;			
			for (int j = 0; j < anArray.size(); j++){
				word = anArray[j];
				Vkrun('/');
				for (int i = 0; i < word.size(); i++){
					char chr = word[i];
					Vkrun(chr);
				}
				Vkothers(13);// carriage return, sends decimal val of char.
				Vkothers(32);// spacebar
				Sleep(1000);
				if (GetAsyncKeyState(VK_NUMPAD0)) {// exit
					return 0;
				}
			}
		}
	}
}

//
//g++ -o runProgram keyboardOutputs.cpp
//seems python394 build is a virtual env and python and python3 seems same.