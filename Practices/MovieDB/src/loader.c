#include "_headers/movieDB.h"

FILE * loadFile() {
    FILE * dbFile = fopen("../Files/movies.txt", "rb+");

    if (!dbFile) {
        printf("File loading Error!\n");
        exit(1);
    } else {
        return dbFile;
    }
}