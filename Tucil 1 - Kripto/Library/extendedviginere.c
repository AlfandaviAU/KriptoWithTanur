// Extended viginere for binary files
// Main reference : Tugas besar Sistem Operasi IF2230
// fileloader.c, https://github.com/Lock1/OS-IF2230/blob/main/other/fileloader.c
#define __USE_MINGW_ANSI_STDIO
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILE_SIZE 8192*8192
typedef unsigned char byte;

void clear(byte *ptr, int length) {
    for (int i = 0; i < length; i++)
        ptr[i] = '\0';
}

int extendedViginereBinary(char *sourcefile, char *targetfile, char *key, int is_encrypting) {
    // Load entire file and save to buffer
    FILE *input  = fopen(sourcefile, "rb");
    FILE *target = fopen(targetfile, "wb");
    if (target == NULL || input == NULL)
        return 1;

    byte *inputbuffer = (byte *) malloc(MAX_FILE_SIZE*sizeof(byte));
    clear(inputbuffer, MAX_FILE_SIZE);

    printf("Reading input file...\n");
    char c;
    fseek(input, 0L, SEEK_END);
    size_t inputfilesize = ftell(input);
    rewind(input);

    size_t onetenthfilesize = inputfilesize / 10;
    printf("%s : %llu bytes\n", sourcefile, (unsigned long long) inputfilesize);
    for (size_t i = 0; i < inputfilesize; i++) {
        if (!(i % onetenthfilesize))
            printf("#");
        c = getc(input);
        inputbuffer[i] = (byte) c;
    }
    fclose(input);

    // Moving key to buffer
    byte *keybuffer = (byte *) malloc(MAX_FILE_SIZE*sizeof(byte));
    clear(keybuffer, MAX_FILE_SIZE);
    size_t keyIndex = 0;
    for (size_t i = 0; i < inputfilesize; i++) {
        if (keyIndex == strlen(key))
            keyIndex = 0;
        keybuffer[i] = (byte) key[keyIndex++];
    }

    // Extended Viginere Cipher
    // Abusing 1 byte data type for modulo 0xFF
    if (is_encrypting)
        printf("\n\nEncrypting...\n");
    else
        printf("\n\nDecrypting...\n");

    byte *targetbuffer = (byte *) malloc(MAX_FILE_SIZE*sizeof(byte));
    clear(targetbuffer, MAX_FILE_SIZE);
    for (size_t i = 0; i < inputfilesize; i++) {
        if (!(i % onetenthfilesize))
            printf("#");

        if (is_encrypting)
            targetbuffer[i] = inputbuffer[i] + keybuffer[i];
        else
            targetbuffer[i] = inputbuffer[i] - keybuffer[i];
    }

    // Writing file
    fwrite(targetbuffer, inputfilesize, 1, target);

    if (is_encrypting)
        printf("\nEncryption completed\n");
    else
        printf("\nDecryption completed\n");
    printf("%s : %llu bytes\n\n", targetfile, (unsigned long long) inputfilesize);

    fclose(target);
    return 0;
}
