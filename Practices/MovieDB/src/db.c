#include "_headers/movieDB.h"

#define N_MAX_MOVIE_TITLE 40

typedef struct {
    char title[N_MAX_MOVIE_TITLE];
    float rating;
} SingleMovieInfo;

// void clearIBuffer(void) {
//     char c;

//     // while ((c = getchar()) == '\n')
//     //     continue;

//     c = getchar();
// }

void dataBasing(FILE * fPtr) {
    unsigned char nItems;
    char dummy;

    fscanf(fPtr, "%hhu", &nItems);
    // printf("%hhu\n", nItems);
    dummy = fgetc(fPtr);

    SingleMovieInfo movies[nItems];

    for (unsigned char i = 0; i < nItems; i++) {
        fgets(movies[i].title, N_MAX_MOVIE_TITLE, fPtr);
        dummy = fgetc(fPtr);

        fscanf(fPtr, "%f", &movies[i].rating);
        dummy = fgetc(fPtr);
    }

    for (unsigned char i = 0; i < nItems; i++) {
        printf("movies%hhu.title => %s", i, movies[i].title);

        printf("movies%hhu.rating => %.2f\n", i, movies[i].rating);
    }

    fclose(fPtr);
}