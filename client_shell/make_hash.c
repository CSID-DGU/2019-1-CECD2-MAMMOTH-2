#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <string.h>

int file_sha256(char *path, char* hashstr);
void trans_string(unsigned char hash[SHA256_DIGEST_LENGTH], char *output);

int main(int argc, char *argv[])
{             
        char *path = argv[1];
        char hash_str[65];
        FILE *f = fopen("new_hash.txt", "w");
        if(f == NULL)
        {
                printf("Error opening File\n");
                exit(1);
        }
        file_sha256(path, hash_str);
        //printf("%s\n", hash_str);
        fprintf(f, hash_str);
        fclose(f);
        return 0;
}

int file_sha256(char * path, char *hashstr)
{
        unsigned char hash[SHA256_DIGEST_LENGTH];
        const int bufSize = 2048;

        SHA256_CTX sha256;

        FILE *file = fopen(path, "rb");
        if(!file)
        {
                printf("File open error\n");
                return -1;
        }
        //printf("File open\n\n");

        SHA256_Init(&sha256);
        //printf("sha256 init\n");

        int readlen = 0;
        unsigned char *read_buf = (unsigned char*)malloc(bufSize + 1);

        if(!read_buf) return -1;

        while((readlen = fread(read_buf, 1, bufSize, file)))
        {
                SHA256_Update(&sha256, read_buf, readlen);
                memset(read_buf, 0x00, bufSize);
        }
        //printf("File read\n\n");

        SHA256_Final(hash, &sha256);

        trans_string(hash, hashstr);

        fclose(file);

        if(read_buf)
                free(read_buf);
}

void trans_string(unsigned char hash[SHA256_DIGEST_LENGTH], char* output)
{
        int i = 0;

        for(i = 0; i < SHA256_DIGEST_LENGTH; i++)
        {
                sprintf(output+ (i*2), "%02x", hash[i]);
        }
        output[64] = 0;
}


