//To port to other os without xdotool edit this file
#include<stdlib.h>
void test(){
    system("ls");
}
void _exe(char * command){
    system(command);
}
