#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <yadafuncs.h>

static int f_append;
static int f_create;
static int f_delete;
static int f_read;
static int f_write;

int main(int argc, char** argv) {
    FILE* fptr;
    while (1) {
        int option_index;
        struct option long_opt[] =
        {
            {"append",  required_argument,  &f_append,  1},
            {"create",  required_argument,  &f_create,  1},
            {"delete",  required_argument,  &f_delete,  1},
            {"read",    required_argument,  &f_read,    1},
            {"write",   required_argument,  &f_write,   1},
            {NULL,      0,                  NULL,       0}
        };

        int opt;
        opt = getopt_long(argc, argv, "-:a:c:d:e:r:w:", long_opt, &option_index);

        if (opt == -1) break;

        switch (opt) {
            case 0:
                //0 = no_argument, 1 = required_argument, 2 = optional_argument
                //TODO: investigate if the arbitrary alphabitzation of the below
                //      condition order is optimal/necessary.
                if      (f_append) yd_append();
                else if (f_create) yd_create();
                else if (f_delete) yd_delete();
                else if (f_read) yd_read();
                else if (f_write) yd_write();
                else printf("idk what happend :(\n");
                break;
            case 'a':
                yd_append();
                break;
            case 'c':
                yd_create();
                break;
            case 'd':
                yd_delete();
                break;
            case 'r':
                yd_read();
                break;
            case 'w':
                yd_write();
                break;
            case '?':
                printf("Unknown option '%c'\n", optopt);
                break;
            case ':':
                printf("Missing option argument for '%c'\n", optopt);
                break;
        }
    }
    return 0;
}
