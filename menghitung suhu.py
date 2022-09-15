# program untuk menghitung suhu
 
# convert celcius to reamur
def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur
 
 
# convert celcius to kelvin
def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin

# convert celcius to farenheit
def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit
 
# create main menu
def main():
    print('selamat datang di Program tri ayuningtyas')
    print('=========================================')
    print('selamat datang di Program Konversi Suhu')
 
    # create input

    print('=========================================')
    temperature = int(input('Masukan Skala Celcius: '))
 
    # cetak hasil
    print('=================================================')
    print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_kelvin(temperature)} Kelvin')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_farenheit(temperature)} farenheit')
  
    print('=================================================')
 
if __name__=='__main__':
    main()