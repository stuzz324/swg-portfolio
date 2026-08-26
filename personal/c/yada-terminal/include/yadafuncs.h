#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <getopt.h>
#include <sys/stat.h>

//TODO
/*
 --This section needs some refactoring/fixing:
    +-Fully implementing error codes.                                       -|
    +-Optimizing error catching (implement error codes).                    -|
    +-Other small optimizations including buffer size, repeated             ||
      function scope variable declarations, proper use of fopen()/fclose()
      int returns (error codes).                                            -|
 */

int yd_append() {
    FILE* fptr;
    char buffer[64];
    fptr = fopen(optarg, "a");

    printf("Please write text: \n");
    scanf("%[^\n]", buffer);

    if (fputs(buffer, fptr) == EOF) {
        perror("Failed to write");
        fclose(fptr);
        return -1;
    }

    fclose(fptr);
    return 0;
}

int yd_create() {
    FILE* fptr;
    struct stat buf;
    if (stat(optarg, &buf) == 0) {
        printf("Error creating file: '%s' already exists!\n", optarg);
        return -1;
    }
    printf("Creating file '%s'\n", optarg);
    if ((fptr = fopen(optarg, "w")) == NULL) {
        perror("Error opening file");
        return -1;
    }
    //fptr = fopen(optarg, "w");

    fclose(fptr);

    //ensure file exists now
    if (stat(optarg, &buf) == -1) {
        perror("Creation failed");
        return -1;
    }

    return 0;
}

int yd_delete() {
    struct stat buf;

    // if (stat(optarg, &buf) != 0) {
    //     printf("File '%s' doesn't exist; cannot delete file!'\n", optarg);
    //     return -1;
    // }

    if (remove(optarg) != 0) {
        perror("Error deleting file");
        return -1;
    }

    printf("File '%s' deleted!\n", optarg);

    return 0;
}

int yd_read() {
    FILE* fptr;
    char buffer[64];
    fptr = fopen(optarg, "r");

    if (fptr == NULL) {
        perror("Error opening file");
        return -1;
    }

    while (fgets(buffer, 64, fptr) != NULL)
        printf("%s", buffer);
    printf("\n");

    fclose(fptr);
    return 0;
}

int yd_write() {
    char buffer[64];
    FILE* fptr = fopen(optarg, "w");

    if (fptr == NULL) {
        perror("Error opening file");
        return -1;
    }

    printf("Please write text: \n");
    scanf("%[^\n]", buffer);

    if (fputs(buffer, fptr) == EOF) {
        perror("Error writing to file");
        fclose(fptr);
        return -1;
    }

    fclose(fptr);
    return 0;
}
