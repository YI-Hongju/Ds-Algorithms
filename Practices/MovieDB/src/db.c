#include "_headers/movieDB.h"

#define N_MAX_MOVIE_TITLE 40

typedef struct {
    char title[N_MAX_MOVIE_TITLE];
    float rating;
} SingleMovieInfo;

void dataBasing(FILE * fPtr) {
    unsigned char nItems;

    fscanf(fPtr, "%hhu", &nItems);
    // printf("%hhu\n", nItems);

    SingleMovieInfo movies[nItems];

    for (unsigned char i = 0; i < nItems; i++) {
        fgets(movies[i].title, N_MAX_MOVIE_TITLE, fPtr);
        fscanf(fPtr, "%f", &movies[i].rating);
    }

    for (unsigned char i = 0; i < nItems; i++) {
        // fgets(movies[i].title, N_MAX_MOVIE_TITLE, fPtr);
        printf("movies%hhu.title => %s", i, movies[i].title);

        // fscanf(fPtr, "%f", &nItems);
        printf("movies%hhu.rating => %f\n", i, movies[i].rating);
    }

    fclose(fPtr);
}