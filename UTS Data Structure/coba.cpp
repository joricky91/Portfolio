#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;

struct mobil{
    char plat[8];
    int jenis;
    int layanan[3];
    int masuk;
    int keluar;
    struct mobil *next;
}*head = NULL, *ptr;

void newNode(char in_plat[8], int in_jenis, int in_layanan[3], int in_masuk, int in_keluar){
    struct mobil *ptr;
    int i = 0;
    struct mobil *tmp = (struct mobil *)malloc(sizeof(struct mobil));
    tmp->jenis = in_jenis;
    while(in_plat[i]){
        tmp->plat[i] = in_plat[i];
        i++;
    }
    i = 0;
    tmp->layanan[0] = in_layanan[0];
    tmp->layanan[1] = in_layanan[1];
    tmp->layanan[2] = in_layanan[2];
    tmp->masuk = in_masuk;
    tmp->keluar = in_keluar;
    tmp->next = NULL;
    if (head == NULL){
        head = tmp;
    }
    else{
        ptr = head;
        while (ptr->next != NULL){
            ptr = ptr->next;
        }
        ptr->next = tmp;
    }
}

void print(){
    struct mobil *ptr;
    ptr = head;
    if (ptr == NULL){
        cout << "Kosong" << endl;
    }
    else{
        while (ptr != NULL){
            cout << "Plat Nomor : " << ptr->plat << endl;
            cout << "Jenis : " << ptr->jenis << endl;
            cout << "Layanan : ";
            for (int i=0; i<3; i++){
                 cout << ptr->layanan[i] << ",";
            }
            cout << endl;
            
            cout << "Waktu Masuk : " << ptr->masuk << endl;
            cout << "Waktu Selesai : " << ptr->keluar << endl;

            ptr = ptr->next;
        }
    }
}

void inputData(){
    char in_plat[8];
    int in_jenis;
    int in_layanan[3];
    int in_masuk;
    int in_keluar;

    cout << "Masukkan No. Plat : ";
    cin >> in_plat;
    cout << "Masukkan Jenis Mobil (Kecil(1), Sedang(2), Besar(3), Truck(4) : ";
    cin >> in_jenis;
    cout << "Masukkan layanan yang ingin dilakukan (Cuci(1), Vakum(2), Poles(3)) : ";
    cin >> in_layanan[0];
    cin >> in_layanan[1];
    cin >> in_layanan[2];
    cout << "Masukkan jam mulai : ";
    cin >> in_masuk;
    cout << "Masukkan jam selesai : ";
    cin >> in_keluar;
    newNode(in_plat, in_jenis, in_layanan, in_masuk, in_keluar);
}

int totalBayar(){
    ptr = head;
    int total = 0, i=0;
    while(ptr->layanan[i]){
    if(ptr->jenis == 1){
        if(ptr->layanan[i] == 1){
            total += 50000;
        }
        else if(ptr->layanan[i] == 2){
            total += 35000;
        }
        else if(ptr->layanan[i] == 3){
            total += 125000;
        }
    }
    else if(ptr->jenis == 2){
        if(ptr->layanan[i] == 1){
            total += 60000;
        }
        else if(ptr->layanan[i] == 2){
            total += 40000;
        }
        else if(ptr->layanan[i] == 3){
            total += 150000;
        }
    }
    else if(ptr->jenis == 3){
        if(ptr->layanan[i] == 1){
            total += 70000;
        }
        else if(ptr->layanan[i] == 2){
            total += 50000;
        }
        else if(ptr->layanan[i] == 3){
            total += 200000;
        }
    }
    else if(ptr->jenis == 4){
        if(ptr->layanan[i] == 1){
            total += 70000;
        }
        else if(ptr->layanan[i] == 2){
            total += 40000;
        }
    }
    i++;
    }
    return total;
}

void writeFile(){
    ofstream myfile;
    myfile.open("datamobil.txt");
    myfile << head->plat;
    myfile << ";";
    myfile << head->jenis;
    myfile << ";";
    myfile << head->masuk;
    myfile << ";";
    myfile << head->keluar;
    myfile.close();
}


int main(){
int pilihan;
while (1){
    cout << "Cuci Mobil Wash-Wash" << endl;
    cout << "1. Input Data" << endl;
    cout << "2. Print Data" << endl;
    cout << "3. Total Harga" << endl;
    cout << "4. Exit" << endl;
    cout << "Silahkan Pilih Menu (Angka Saja) : ";
    cin >> pilihan;
    if (pilihan == 1){
        inputData();
        writeFile();
    }
    else if (pilihan == 2){
        print();
    }
    else if (pilihan == 3){
        int totalbayar;
        totalbayar = totalBayar();
        cout << totalbayar << endl;
    }
    else if (pilihan == 4){
        break;
    }
}
return 0;
}
