class DramaKorea:
    def __init__(self, judul, tahun_rilis, genre):
        self.__judul = judul  
        self.__tahun_rilis = tahun_rilis  
        self.__genre = genre  
    
    def get_judul(self):
        return self.__judul

    def set_judul(self, judul):
        self.__judul = judul

    def get_tahun_rilis(self):
        return self.__tahun_rilis

    def set_tahun_rilis(self, tahun_rilis):
        self.__tahun_rilis = tahun_rilis

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def info(self):
        return f'Judul: {self.__judul}, Tahun Rilis: {self.__tahun_rilis}, Genre: {self.__genre}'

class DramaKoreaKomedi(DramaKorea):
    def __init__(self, judul, tahun_rilis, genre, humor_level):
        super().__init__(judul, tahun_rilis, genre)
        self.__humor_level = humor_level  

    def get_humor_level(self):
        return self.__humor_level

    def info(self):
        return f'{super().info()}, Level Humor: {self.__humor_level}'        

class KoleksiDrama:
    def __init__(self):
        self.__koleksi_drama = []  

    def tambah_drama(self, drama):
        self.__koleksi_drama.append(drama)

    def tampilkan_koleksi(self):
        for drama in self.__koleksi_drama:
            print(drama.info())
            print("-" * 50)    

drama1 = DramaKorea("Lovely Runner", 2024, "Romantis, Olahraga")
drama2 = DramaKorea("Queen of Tears", 2024, "Drama, Melodrama")
drama3 = DramaKorea("All of Us Are Dead", 2024, "Thriller, Horor")
drama_komedi = DramaKoreaKomedi("Welcome to wakiki", 2018, "Komedi", "Tinggi")

koleksi_drama = KoleksiDrama()
koleksi_drama.tambah_drama(drama1)
koleksi_drama.tambah_drama(drama2)
koleksi_drama.tambah_drama(drama3)
koleksi_drama.tambah_drama(drama_komedi) 

print("Koleksi Drama Korea Tahun 2024:")
koleksi_drama.tampilkan_koleksi()
