#include<stdio.h>
int main(void)
{
    int angle1,angle2,angle3,sum;
    printf("Enter 3 angles of triangle: ");
    scanf("%d %d %d",&angle1,&angle2,&angle3);
    sum = angle1 + angle2 + angle3;

    if(sum==180 && angle1 !=0 && angle2 != 0 && angle3 != 0)
        printf("Valid triangle.\n");
    else
        printf("Invalid Triangle.\n");
return 0;

}