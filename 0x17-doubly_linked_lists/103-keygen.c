#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s username\n", argv[0]);
        return 1;
    }

    char *username = argv[1];

    // Keygen algorithm (replace this with your keygen logic)
    // Example: Concatenate the username with a secret string
    char key[100];
    sprintf(key, "%s_secret_key", username);

    // Print the generated key
    printf("%s\n", key);

    return 0;
}

