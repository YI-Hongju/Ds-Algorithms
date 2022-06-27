#include "_headers/movieDB.h"

int main(void) {
    FILE *fPtr = loadFile();
    // printf("%p\n", fPtr); // Test code

    dataBasing(fPtr); // TODOs
    return 0;
}