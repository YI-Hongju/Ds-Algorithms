#include "_headers/movieDB.h"

FILE * loadFile(void) {
    FILE * fPtr = fopen("../Files/movies.txt", "rb+");

    if (!fPtr) {
        printf("File loading Error!\n");
        exit(1);
    } else {
        return fPtr;
    }
}