#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int main(void)
{
	char str[500]="Dolfh zdv ehjlqqlqj wr jhw yhub wluhg ri vlwwlqj eb khu vlvwhu rq wkh edqn, dqg ri kdylqj qrwklqj wr gr: rqfh ru wzlfh vkh kdg shhshg lqwr wkh errn khu vlvwhu zdv uhdglqj, exw lw kdg qr slfwxuhv ru frqyhuvdwlrqv lq lw, 'dqg zkdw lv wkh xvh ri d errn,' wkrxjkw Dolfh 'zlwkrxw slfwxuhv ru frqyhuvdwlrq?'";
	//scanf("%s", str);

	int i,size = 0;
	size = strlen(str);
	for (i = 0; i < size; i++)
	{
	

		if ('D'<= str[i] && str[i]<= 'Z')
		{
		
			printf("%c", str[i]-3);
		}
		else if ('A' <= str[i]&&str[i] <= 'C')
		{
			printf("%c", str[i] + 23);

		}
		else if ('d' <= str[i] && str[i] <= 'z')
		{

			printf("%c", str[i] - 3);
		}
		else if ('a' <= str[i] && str[i] <= 'c')
		{
			printf("%c", str[i] + 23);

		}
		else
		{
			printf("%c", str[i]);
		}


	}
	getchar();
	
}

