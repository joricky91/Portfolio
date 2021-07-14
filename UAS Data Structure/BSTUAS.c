#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Sumber Project : https://www.geeksforgeeks.org dengan penyesuaian dan perubahan variabel */

struct info_buku{
    char judul[50];
    int nomor_entri;
    char tajuk_entri[10];
    struct info_buku *left;
    struct info_buku *right;
    struct info_buku *next;
}*root = NULL;

struct Queue{
    int nomor_entri;
    char judul[50];
    struct Queue *next;
};

struct info_buku* newNode(int nomor, char* author, int author_length, char* title, int title_length){
    struct info_buku *temp = (struct info_buku *)malloc(sizeof(struct info_buku));
    temp->nomor_entri = nomor;
    strcpy(temp->tajuk_entri, author);
    strcpy(temp->judul, title);
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

struct info_buku* insertBST(struct info_buku* root, int nomor, char* author, int author_length, char* title, int title_length){
    if (root == NULL){
        return newNode(nomor, author, author_length, title, title_length);
    }
    if (nomor < root->nomor_entri){
        root->left = insertBST(root->left, nomor, author, author_length, title, title_length);
    }
    else if (nomor > root->nomor_entri){
        root->right = insertBST(root->right, nomor, author, author_length, title, title_length);
    }
    return root;
}

void inorder(struct info_buku *root) 
{ 
    if (root != NULL) 
    { 
        inorder(root->left); 
        printf("Nomor Entri : %d", root->nomor_entri); 
        printf("\n");
        printf("Penulis : ");
        printf("%s", root->tajuk_entri);
        printf("\n");
        printf("Judul Buku : ");
        printf("%s", root->judul);
        printf("\n");
        inorder(root->right); 
    } 
} 

struct info_buku* minValueNode(struct info_buku* node) 
{ 
    struct info_buku* current = node; 
    while (current && current->left != NULL) 
        current = current->left; 
  
    return current; 
} 

struct info_buku* deleteNode(struct info_buku* root, int nomor) { 
    if (root == NULL) return root; 
    
    if (nomor < root->nomor_entri){
        root->left = deleteNode(root->left, nomor); 
    }
    else if (nomor > root->nomor_entri) {
        root->right = deleteNode(root->right, nomor); 
    }
    else{ 
        if (root->left == NULL) { 
            struct info_buku *temp = root->right; 
            free(root); 
            return temp; 
        } 
        else if (root->right == NULL) { 
            struct info_buku *temp = root->left; 
            free(root); 
            return temp; 
        } 
        else{
            struct info_buku *temp = minValueNode(root->right); 
            root->nomor_entri = temp->nomor_entri;  
            root->right = deleteNode(root->right, temp->nomor_entri); 
        }
        return root;
    }   
} 

struct Queue* tambahQueue(struct Queue *head, int nomor, char* title, int title_length) { 
    struct Queue *temp = (struct Queue *)malloc(sizeof(struct Queue)); 
    struct Queue *tail = head;

    temp->nomor_entri = nomor;
    strcpy(temp->judul, title);
    temp->next = NULL; 
    if (head == NULL){
        head = temp;
        return temp;
    }
    while (tail->next != NULL){
        tail = tail->next;
        tail->next = temp;
        return temp;
    }
  
} 

struct Queue* newQueue(struct info_buku *root, struct Queue *head, int nomor){
    char* title[50];
    if (root->nomor_entri == nomor){
        printf("Masukkan Nomor Entri Buku : ");
        scanf("%d", &nomor);
        printf("Masukkan Judul Buku : ");
        scanf("%s", title);
        head = tambahQueue(head, nomor, root->judul, sizeof(root->judul));
        return head;
    }
    if (root->left != NULL){
        if (root->nomor_entri > nomor){
            newQueue(root->left, head, nomor);
        }
    }
    if (root->right != NULL){
        if (root->nomor_entri < nomor){
            newQueue(root->right, head, nomor);
        }
    }
}

void deleteQueue(struct Queue *head){
    struct Queue *del;
    if (head == NULL){
        printf ("List is empty\n");
    }
    else{
        del = head;
        head = head->next;
        free (del);
    }
}

void printQueue(struct Queue *head){
    struct Queue *temp = head;
    while (temp != NULL){
        printf("Judul : %s", temp->judul);
        printf("\n");
        printf("Nomor Entri : %d", temp->nomor_entri);
        printf("\n");
        temp = temp->next;
    }
}

int cari_buku(struct info_buku *root, int nomor){
    if (root->nomor_entri == nomor){
        return 1;
    }
    else if (root == NULL){
        return 0;
    }
    if (root->left != NULL){
        if (root->nomor_entri > nomor) { 
            cari_buku(root->left, nomor); 
        } 
    }
    if (root->right != NULL){
        if (root->nomor_entri < nomor) { 
            cari_buku(root->right, nomor); 
        }  
    }
}

int main(){
    int choice, nomor, author_length, title_length;
    char author[10];
    char title[50];
    struct info_buku *root = NULL;
    struct Queue *head = NULL;
    while (1){
        printf("1. Input Book\n");
        printf("2. Search Book\n");
        printf("3. Borrow Book\n");
        printf("4. Return Book\n");
        printf("5. Print Book List\n");
        printf("6. Print Queue\n");
        printf("7. Exit\n");
        printf("Silahkan Pilih Menu : ");
        scanf("%d", &choice);
        if (choice == 1){
            printf("Masukkan Judul Buku : ");
            scanf("%s", title);
            printf("Masukkan Nomor Entri : ");
            scanf("%d", &nomor);
            printf("Masukkan Pengarang (Inisial) : ");
            scanf("%s", author);
            if (root == NULL){
                root = insertBST(root, nomor, author, author_length, title, title_length);
            }
            else{
                insertBST(root, nomor, author, author_length, title, title_length);
            }
        }
        else if (choice == 2){
            if (root == NULL){
                printf("Kosong\n");
            }
            else if (root != NULL){
                printf("Masukkan Nomor Entri Buku yang Ingin Dicari : ");
                scanf("%d", &nomor);
                cari_buku(root, nomor);
                if (cari_buku(root, nomor == 1)){
                    printf("Buku Tersedia\n");
                }
                else{
                    printf("Buku Tidak Tersedia\n");
                }
            } 
        }
        else if (choice == 3){
            if (root == NULL){
                printf ("Kosong\n");
            }
            if (root != NULL){
                printf("Masukkan Judul Buku yang Ingin Dipinjam : ");
                scanf("%s", title);
                printf("Masukkan Nomor Entri Buku : ");
                scanf("%d", &nomor);
                if (cari_buku(root, nomor == 1)){
                    printf ("Buku Tersedia\n");
                    head = newQueue(root, head, nomor);
                    root = deleteNode(root, nomor);
                }
                else{
                    printf ("Buku Tidak Tersedia\n");
                }
            }
        }
        else if (choice == 4){
            struct Queue *head;
            int hari;
            
            if (head != NULL){
                printf("Masukkan Judul Buku yang Dikembalikan : ");
                scanf("%s", title);
                printf("Masukkan Nomor Entri Buku : ");
                scanf("%d", &nomor);
                printf("Masukkan Durasi Peminjaman Buku : ");
                scanf("%d hari", &hari);
                if (root == NULL){
                    printf("Masukkan Judul Buku : ");
                    scanf("%s", title);
                    printf("Masukkan Nomor Entri : ");
                    scanf("%d", &nomor);
                    printf("Masukkan Pengarang (Inisial) : ");
                    scanf("%s", author);
                    root = insertBST(root, nomor, author, author_length, title, title_length);
                }
                else{
                    printf("Masukkan Judul Buku : ");
                    scanf("%s", title);
                    printf("Masukkan Nomor Entri : ");
                    scanf("%d", &nomor);
                    printf("Masukkan Pengarang (Inisial) : ");
                    scanf("%s", author);
                    insertBST(root, nomor, author, author_length, title, title_length);
                }
                deleteQueue(head);
            }
            else{
                printf("Kosong\n");
            }
        }
        else if (choice == 5){
            inorder(root);
        }
        else if (choice == 6){
            printQueue(head);
        }
        else if (choice == 7){
            break;
        }
    }
    return 0;
}
