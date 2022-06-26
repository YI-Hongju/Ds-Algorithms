#include "_headers/movieDB.h"

void dataBasing(FILE * file) {
    unsigned char nItems[2] = {0, };

    fscanf(file, "%hhu\n", nItems);

    printf("%hhu\n", nItems);
}