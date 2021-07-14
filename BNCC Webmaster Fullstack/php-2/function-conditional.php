<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Function</title>
</head>
<body>
    <h1>Berlatih Function PHP</h1>
    <?php 

        echo "<h3> Soal No 1 Greetings </h3>";
        /* 
            Soal No 1
            Greetings
            Buatlah sebuah function greetings() yang menerima satu parameter berupa string. 

            contoh: greetings("andi");
            Output: "Halo Andi, Selamat Datang di BNCC LnT!"
        */

        // Code function di sini
        function greetings($nama){
            echo "Halo ".$nama.", Selamat Datang di BNCC LnT! <br>";
        }

        // Hapus komentar untuk menjalankan code!
         greetings("Bagas");
         greetings("Wahyu");
         greetings("Abdul");

        echo "<br>";
        
        echo "<h3>Soal No 2 Reverse String</h3>";
        /* 
            Soal No 2
            Reverse String
            Buatlah sebuah function reverseString() untuk mengubah string berikut menjadi kebalikannya menggunakan function dan looping (for/while/do while).
            Function reverseString menerima satu parameter berupa string.
            NB: DILARANG menggunakan built-in function PHP sepert strrev(), HANYA gunakan LOOPING!

            reverseString("abdul");
            Output: ludba
            
        */
 
        // Code function di sini 
        function reverseString($kata){
            $reverse = '';
            $length = strlen($kata);
            for ($i = ($length - 1); $i >= 0; $i--){
                $reverse .= $kata[$i];
            }
            return $reverse;
        }

        // Hapus komentar di bawah ini untuk jalankan Code
        echo reverseString("raud");
        echo "<br>";
        echo reverseString("BNCC");
        echo "<br>";
        echo reverseString("Bina Nusantara Computer Club");

        echo "<br>";

        echo "<h3>Soal No 3 Palindrome </h3>";
        /* 
            Soal No 3 
            Palindrome
            Buatlah sebuah function yang menerima parameter berupa string yang mengecek apakah string tersebut sebuah palindrome atau bukan. 
            Palindrome adalah sebuah kata atau kalimat yang jika dibalik akan memberikan kata yang sama contohnya: katak, civic.
            Jika string tersebut palindrome maka akan mengembalikan nilai true, sedangkan jika bukan palindrome akan mengembalikan false.
            NB: 
            Contoh: 
            palindrome("katak") =>  output : true
            palindrome("jambu") => output : false
            NB: DILARANG menggunakan built-in function PHP seperti strrev() dll. Gunakan looping seperti biasa atau gunakan function reverseString dari jawaban no.2!
            
        */


        // Code function di sini
        function palindrome($words){
            $reverse = reverseString($words);
            if ($words == $reverse){
                echo "true <br>";
            }
            else{
                echo "false <br>";
            }
        }
        // Hapus komentar di bawah ini untuk jalankan code
         palindrome("civic") ; // true
         palindrome("nababan") ; // true
         palindrome("jambaban"); // false
         palindrome("racecar"); // true
    ?>
</body>
</html>