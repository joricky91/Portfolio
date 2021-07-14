CREATE DATABASE Project_DB;
CREATE TABLE Patients(
	Patient_id INT PRIMARY KEY,
	PatientName VARCHAR(100),
	DateOfBirth DATE,
	Sex CHAR(1),
	Weight INT,
	Height INT
);

CREATE TABLE Doctors(
	Doctor_id INT PRIMARY KEY,
	DoctorName VARCHAR(100),
	DateOfBirth DATE,
	Sex CHAR(1),
	Unit VARCHAR(50)
);

CREATE TABLE Consultations(
 Consultation_id VARCHAR(10) PRIMARY KEY,
 Patient_id INT FOREIGN KEY REFERENCES Patients(Patient_id),
 Doctor_id INT FOREIGN KEY REFERENCES Doctors(Doctor_id),
 VisitDate DATE,
 ConsultationPrice INT,
 Note TEXT
);

CREATE TABLE MedicationLists (
 Medication_id INT PRIMARY KEY,
 MedName VARCHAR(50),
 MedPrice INT,
 MedProducer VARCHAR(100),
 MedStock INT
);

CREATE TABLE MedicationOrders (
	MedOrder_id int PRIMARY KEY,
	Consultation_id VARCHAR(10) FOREIGN KEY REFERENCES Consultations(Consultation_id),
	TotalMedPrice int
);


CREATE TABLE MedicationDetails (
	MedOrder_id int FOREIGN KEY REFERENCES MedicationOrders(MedOrder_id),
	Medication_id int FOREIGN KEY REFERENCES MedicationLists(Medication_id),
	Quantity int
);


/* TRIGERS:
	1. Auto generate Consultation_id
	2. Auto Increment Med Order
*/

CREATE TRIGGER [dbo].IncMedO
ON MedicationOrders
INSTEAD OF INSERT
AS
BEGIN
	DECLARE 
		@maxID INT,
		@cid VARCHAR(10),
		@price INT;
	SELECT @maxID = MAX(MedOrder_id) FROM MedicationOrders;
	SELECT @cid = Consultation_id, @price = TotalMedPrice FROM inserted;

	IF EXISTS(SELECT MedOrder_id FROM MedicationOrders)
		INSERT INTO MedicationOrders (MedOrder_id,Consultation_id, TotalMedPrice)
		VALUES (@maxID+1, @cid, @price)
	ELSE
		INSERT INTO MedicationOrders (MedOrder_id,Consultation_id, TotalMedPrice)
		VALUES (1, @cid, @price)
END;

CREATE TRIGGER [dbo].ConsID
ON Consultations
INSTEAD OF INSERT
AS
BEGIN
	DECLARE 
		@pid INT,
		@doc INT,
		@date DATE,
		@price INT,
		@note VARCHAR(8000),
		@last VARCHAR(10),
		@newID VARCHAR(10);

	SELECT
		@pid = Patient_id,
		@doc = Doctor_id,
		@date = VisitDate,
		@price = ConsultationPrice,
		@note = Note
	FROM inserted;

	DECLARE @prefix VARCHAR(7) = CAST(@doc as VARCHAR(1))+'C'+ FORMAT(getdate(),'MMdd');

	IF EXISTS(SELECT Consultation_id FROM Consultations WHERE Consultation_id LIKE @prefix+'%')
		BEGIN
			SELECT TOP 1 @last = Consultation_id FROM Consultations WHERE Consultation_id LIKE @prefix+'%' ORDER BY Consultation_id DESC;
			SET @newID = @prefix + CAST( (CAST(SUBSTRING(@last,7,LEN(@last)-6) as INT) +1) AS VARCHAR(10));
			INSERT INTO Consultations(Consultation_id, Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note)
			VALUES (@newID,@pid,@doc,@date, @price, @note);
		END;
	ELSE
		INSERT INTO Consultations(Consultation_id, Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note)
		VALUES (@prefix+'1',@pid,@doc,@date, @price, @note);
END;


/*FUNCTIONS:
	1. PRINT STRUK(id consultation) <DONE>
	2. PRINT BUKU(id pasien) <DONE>
*/



CREATE FUNCTION [dbo].cetakResi(@cons VARCHAR(10))
RETURNS VARCHAR(8000)
AS
BEGIN
	DEClARE @patient VARCHAR(100);
	DECLARE @doctor VARCHAR(100);
	DECLARE @unit VARCHAR(50);
	DECLARE @mid INT;
	DECLARE @cp INT;
	DECLARE @mp INT;
	DECLARE @OUT VARCHAR(5000);
	DECLARE @dt DATE;

	SELECT 
		@patient = Patients.PatientName, 
		@doctor = Doctors.DoctorName,
		@unit = Doctors.Unit,
		@mid = MedicationOrders.MedOrder_id,
		@cp = Consultations.ConsultationPrice,
		@mp = MedicationOrders.TotalMedPrice,
		@dt = GETDATE()
	FROM Patients
	INNER JOIN Consultations ON Consultations.Patient_id = Patients.Patient_id
	INNER JOIN Doctors ON Doctors.Doctor_id = Consultations.Doctor_id
	INNER JOIN MedicationOrders ON MedicationOrders.Consultation_id = Consultations.Consultation_id
	WHERE Consultations.Consultation_id = @cons;

	SET @OUT = '                  KLINIKITA
   Jalan Pasirkaliki no.79, Bandung, 40513
            Telp:08190049367
--------------------------------------------
Tanggal     : '+CAST(@dt AS VARCHAR(100))+'
Nama Pasien : ' + @patient+'
Nama Dokter : ' + @doctor+'
Unit        : ' + @unit+'
--------------------------------------------
'; 

	DECLARE @MO TABLE(
		id INT IDENTITY(1,1),
		nama VARCHAR(50),
		qty int
	);
	INSERT INTO @MO(nama, qty) 
	SELECT MedicationLists.MedName, MedicationDetails.Quantity 
	FROM MedicationDetails 
	INNER JOIN MedicationLists ON MedicationLists.Medication_id = MedicationDetails.Medication_id
	WHERE MedicationDetails.MedOrder_id = @mid;

	DECLARE @cnt int = (SELECT COUNT(*) FROM @MO);
	DECLARE @pos INT =0;

	WHILE @pos < @cnt
	BEGIN
		DECLARE @nama VARCHAR(50);
		DECLARE @qty int;
		SELECT @nama = nama, @qty = qty FROM @MO WHERE id = @pos+1;
		SET @OUT = @OUT + @nama +'		'+CAST(@qty as VARCHAR(10))+' 
';
		SET @pos = @pos + 1;
	END;

	SET @OUT = @OUT +' 

Konsultasi      : Rp.'+CAST(@cp AS VARCHAR(10))+'
Obat            : Rp.'+CAST(@mp AS VARCHAR(10))+'
TOTAL           : RP.'+CAST((@cp+@mp) AS VARCHAR(10))+'
--------------------------------------------
      TERIMA KASIH ATAS KUNJUNGAN ANDA
            SEMOGA LEKAS SEMBUH.
--------------------------------------------';
	RETURN @OUT;
END;

CREATE FUNCTION [dbo].cetakBuku(@pats INT)
RETURNS VARCHAR(8000)
AS
BEGIN
	DEClARE @patient VARCHAR(100);
	DECLARE @dob DATE;
	DECLARE @sex CHAR(1);
	DECLARE @berat INT;
	DECLARE @tinggi INT;
	DECLARE @unit VARCHAR(50);
	DECLARE @OUT VARCHAR(5000);
	DECLARE @vdt DATE;
	DECLARE @not VARCHAR(100);

	SELECT 
		@patient = Patients.PatientName, 
		@dob = Patients.DateOfBirth,
		@sex = Patients.Sex,
		@berat = Patients.Weight,
		@tinggi = Patients.Height,
		@unit = Doctors.Unit,
		@vdt = Consultations.VisitDate,
		@not = Consultations.Note

	FROM Patients
	INNER JOIN Consultations ON Consultations.Patient_id = Patients.Patient_id
	INNER JOIN Doctors ON Doctors.Doctor_id = Consultations.Doctor_id
	WHERE Patients.Patient_id = @pats;

	SET @OUT = '                  KLINIKITA
                BUKU PASIEN
--------------------------------------------
Nama          : ' + @patient+'
Tanggal Lahir : ' +CAST(@dob AS VARCHAR(10))+'
Jenis Kelamin : ' +@sex+ '
Berat	      : ' +CAST(@berat AS VARCHAR(3))+ '
Tinggi        : ' +CAST(@tinggi AS VARCHAR(3))+ '
--------------------------------------------
'; 

	DECLARE @MO TABLE(
		id INT IDENTITY(1,1),
		tanggal Date,
		unit VARCHAR(50),
		note VARCHAR(100)
	);
	INSERT INTO @MO(tanggal, unit, note) 
	SELECT Consultations.VisitDate, Doctors.Unit, Consultations.Note
	FROM Consultations
	INNER JOIN Doctors ON Consultations.Doctor_id = Doctors.Doctor_id
	WHERE Consultations.Patient_id = @pats

	DECLARE @cnt int = (SELECT COUNT(*) FROM @MO);
	DECLARE @pos INT =0;

	WHILE @pos < @cnt
	BEGIN
		DECLARE @tgl DATE;
		DECLARE @unt VARCHAR(50);
		DECLARE @notes VARCHAR(100);
		SELECT @tgl = tanggal, @unt = unit, @notes = note FROM @MO WHERE id = @pos+1;
		SET @OUT = @OUT + CAST(@tgl as VARCHAR(10)) +'		'+CAST(@unt as VARCHAR(10))+'		'+@notes+' 
';
		SET @pos = @pos + 1;
	END;

	SET @OUT = @OUT +' 
-------------------------------------------------------------------------
 Apabila anda menemukan buku ini, harap hubungi Klinikita di 081910049367
-------------------------------------------------------------------------';
	RETURN @OUT;
END;


/* INSERT DATA */

INSERT INTO Patients(Patient_id, PatientName, DateOfBirth, Sex, Height, Weight)
VALUES
	(1,'Jaja', '2000-08-24', 'M', 175, 56),
	(2,'Pavel', '2000-07-23', 'M', 175, 58),
	(3,'Max', '2000-06-22', 'M', 178, 69),
	(4,'Adri', '2000-05-21', 'M', 170, 70),
	(5,'Hans', '2000-04-20', 'M', 180, 65);

SELECT * FROM Patients;

INSERT INTO Doctors(Doctor_id,DoctorName, DateOfBirth, Sex, Unit)
VALUES
	(01, 'Bunardi', '1969-06-09','M','Dokter Umum'),
	(02, 'Radya', '1970-07-10','M','Dokter Kulit'),
	(03, 'Jose', '1971-08-11','M','Dokter THT'),
	(04, 'Iggy', '1972-09-12','M','Dokter Mata'),
	(05, 'Dijul', '1973-10-13','M','Dokter Gigi');

INSERT INTO MedicationLists(Medication_id, MedName, MedPrice, MedProducer, MedStock)
VALUES 
	(1, 'Paracetamol Tablet 500mg', 3000, 'Indofarma', 25),
	(2, 'Hydrocortison 2.5%', 12500, 'Kalbe', 8),
	(3, 'Vital Ear Oil 10ml', 19000, 'Medikon', 6),
	(4, 'Insto Tetes Mata 15ml', 22500, 'Sterling', 15),
	(5, 'Panadol Biru', 11000, 'GlaxoSmithKline Indonesia', 20);

SELECT * FROM MedicationLists;

INSERT INTO Consultations(Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note) VALUES (1,1,'2021-01-01',60000,'Perlu minum obat penurun panas selama 3 hari');
INSERT INTO Consultations(Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note) VALUES (2,2,'2021-01-01',75000,'Perlu mengoleskan salep 2x sehari pada kulit yang gatal selama 1 minggu');
INSERT INTO Consultations(Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note) VALUES (3,3,'2021-01-02',115000,'Perlu diperiksa kembali apakah pendengaran sudah membaik atau belum minggu depan');
INSERT INTO Consultations(Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note) VALUES (4, 4, '2021-01-02', 90000, 'Jika mata terasa gatal/kering, tetesi dengan obat tetes mata. Sebisa mungkin hindari kontak tangan dengan mata.');
INSERT INTO Consultations(Patient_id, Doctor_id, VisitDate, ConsultationPrice, Note) VALUES (5,5,'2021-01-02',130000,'Perlu cabut gigi minggu depan sekaligus ganti kawat gigi');


SELECT * FROM Consultations; /*CEK CONST_ID UNTUK ISI MED ORDER*/

INSERT INTO MedicationOrders(Consultation_id, TotalMedPrice) VALUES ('1C01251', 6000);
INSERT INTO MedicationOrders(Consultation_id, TotalMedPrice) VALUES ('2C01251', 12500);
INSERT INTO MedicationOrders(Consultation_id, TotalMedPrice) VALUES ('3C01251', 19000);
INSERT INTO MedicationOrders(Consultation_id, TotalMedPrice) VALUES ('4C01251', 22500);
INSERT INTO MedicationOrders(Consultation_id, TotalMedPrice) VALUES ('5C01251', 11000);


SELECT * FROM MedicationOrders; /* CEK ID ORDER UNTUK INSERT DETAIL*/

INSERT INTO MedicationDetails(MedOrder_id, Medication_id, Quantity)
VALUES
	(1, 1, 2),
	(2, 2, 1),
	(3, 3, 1),
	(5, 5, 1),
	(4, 4, 1);

SELECT * FROM MedicationDetails;

/*EXECUTE PRINT RESI*/
PRINT [dbo].cetakResi('4C01221');
PRINT [dbo].cetakBuku(3); /* Kalo print no 4 error */






