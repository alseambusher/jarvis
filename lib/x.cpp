//To port to other os without xdotool,xwit,xprop edit this file
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void test(){
    system("ls");
}
void _exe(char * command){
    system(command);
}
