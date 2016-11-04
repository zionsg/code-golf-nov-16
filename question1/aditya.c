#include <stdio.h>
#include<string.h>
int main(){
   char a[100];
   int i,j,k;
   scanf("%s",a);
   for(k=0;k<strlen(a);k++){
      for(i=k;i<strlen(a);i++){
         for(j=0;j<=i-k;j++)
            printf("%c",a[i]);
      }
      printf("\n");
   }
}//182 chars
