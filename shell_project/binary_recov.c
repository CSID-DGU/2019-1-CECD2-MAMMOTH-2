#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]){
    FILE* fp1; // segmentation file
    FILE* fp2; // server_hash.txt
    FILE* fp3; // server_cert.csr
    int size;
    unsigned char buf1[64] = {0}; // hash value
    unsigned char buf2[956] = {0}; //csr value
    fp1 = fopen(argv[1],"ab+");
    fp2 = fopen("server_cert.csr", "w");
    fp3 = fopen("server_hash.txt", "w");
    if(fp1==NULL)
        return 0;
    fseek(fp1, 0, SEEK_END);
    size = ftell(fp1);
    fseek(fp1, 0, SEEK_SET);
    //printf("%d\n", size);
    fseek(fp1, size-1020, SEEK_SET);
    fread(buf2, 956, 1, fp1);
    fwrite(buf2, 1, sizeof(buf2), fp2);
    //printf("Saved CSR file\n");
    fseek(fp1, size-64, SEEK_SET);
    fread(buf1, 64, 1, fp1);
    fwrite(buf1, 1, sizeof(buf1), fp3);
    fseek(fp1, 0, SEEK_SET);
    int fd1 = fileno(fp1);
    ftruncate(fd1,size-1020);
    fclose(fp1);
    fclose(fp2);
    fclose(fp3);
}
