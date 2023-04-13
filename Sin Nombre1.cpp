#include<stdio.h>
int main(){
	unsigned char a=32,b=69,c=106,d=143,e=180,f=217;
	int x;
	for(x=0;x<=37;x++){
		printf("\n%i-%c \t\t %i-%c \t\t %i-%c \t\t%i-%c \t\t%i-%c\t\t %i-%c \t\t %i-%c ", a,a,b,b,c,c,d,d,e,e,f,f);
		a++,b++,c++,d++,e++,f++;
	}
}
