#include "_headers/movieDB.h"

#define N_MAX_MOVIE_TITLE 40

typedef struct {
    char title[N_MAX_MOVIE_TITLE];
    float rating;
} SingleMovieInfo;

void dataBasing(FILE * fPtr) {
    unsigned char nItems;
    char dummy;

    fscanf(fPtr, "%hhu", &nItems);
    dummy = fgetc(fPtr);

    SingleMovieInfo movies[nItems];

    for (unsigned char i = 0; i < nItems; i++) {
        fgets(movies[i].title, N_MAX_MOVIE_TITLE, fPtr);

        fscanf(fPtr, "%f", &movies[i].rating);
        dummy = fgetc(fPtr);
    }

    fclose(fPtr);
}