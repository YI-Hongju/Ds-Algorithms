#include "_headers/movieDB.h"

int main(void) {
    FILE *dbFile = loadFile();
    printf("%p\n", dbFile); // Test code

    // dataBasing(dbFile); // TODOs
    return 0;
}