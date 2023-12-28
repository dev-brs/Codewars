//https://www.codewars.com/kata/541c8630095125aba6000c00

#include <stdio.h>
#include <stdlib.h>

int digital_root(int n)
{
    int n_digits=0;
    int sum=0;
    int aux=n;

    while(n>=10)
    {
        aux=n;
        sum=0;
        n_digits=0;

        do
        {
            aux/=10;
            n_digits++;
        }while(aux!=0);
        for(int a=0; a<n_digits;a++)
        {    
            sum+=n%10;
            aux=(n-n%10)/10;
            n=aux;    
        }    
        n=sum;
    }
    printf("%d",sum);
    return n;
}