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