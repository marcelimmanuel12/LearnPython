class MyClass:
    def _init_(self) -> None:
        pass

    def myFunction(self) -> None:
        pass

    def otherFunction(self) -> str:
        return "test"
    
    def chekNilai(self, grade: str) -> int:
        nilai = -1

        match (grade): 
            case "A":
                nilai = 4

            case "B":
                nilai = 3

            case "C":
                nilai = 2

            case "D":
                nilai = 1

            case "E":
                nilai = 0

        return nilai
    
    # def nomor 2
    def chekhuruf(self, huruf: float) -> int:

        if (huruf >= 90.0 and huruf <= 100):
                keterangan = "A"

        elif (huruf >= 80.0 and huruf <= 89.9):
                keterangan = "B"
                
        elif (huruf > 70.0 and huruf < 79.9):
                keterangan = "C"
        
        elif (huruf > 60.0 and huruf < 69.9):
                keterangan = "D"

        elif (huruf > 50.0 and huruf < 59.9):
                keterangan = "E"

        elif (huruf < 50.0):
            keterangan = "F"

        return keterangan
    
    # Def nomor 3
    def hitungluastrapesium(s: float, t: float) -> float:
        LS = 1 / 2 * (s+ s) * t
        return LS
    
    # Def nomor 4
    def hitung_pajak(penghasilan):
        if penghasilan <= 54000000:
             pajak = 0
        elif penghasilan <= 150000000:
             pajak = (penghasilan - 54000000) * 3/100 + 100000 
        else:
             pajak = (penghasilan - 72000000) * 4/100 + 0.1/100 * penghasilan
             return pajak
        
    # Def nomor 5
    def kali(a, b):
        hasil = 0
        for _ in range(b):
            hasil += a
            return hasil