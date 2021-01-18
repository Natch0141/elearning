#For scheduling task execution
import schedule
import time, datetime, requests, os
from bs4 import BeautifulSoup
waktu = datetime.datetime.now().strftime("%A, %d. %B %Y")
hari = waktu.split(',')[0]
if hari == 'Monday':
  pilih = 'Senin'
  thisday = 'Senin'
elif hari == 'Tuesday':
  pilih =  ["Kelas Ekonomi X MIPS 9","Kelas MATEMATIKA WAJIB X MIPS 9","Kelas SKI X MIPS 9","Kelas IBADAH X MIPS 9"]
  thisday = 'Selasa'
elif hari == 'Wednesday':
  pilih = 'Rabu'
  thisday = 'Rabu'
elif hari == 'Thursday':
  pilih = 'Kamis'
  thisday = 'Kamis'
elif hari == 'Friday':
  pilih = "Jum'at"
  thisday = "Jum'at"
elif hari == 'Saturday':
  pilih = 'Sabtu'
  thisday = 'Sabtu'
else:
  pass
def get_time():
  os.system('clear')
  print 'Author: @Natch0141'
  print 'Tanggal hari ini : %s\n'%waktu
  print '[!] INFO: Bot akan melakukan auto absen semua mapel\npada hari %s di jam 7'%thisday
  for thismapel in pilih:
    print '[+] list mapel hari ini : %s'%thismapel
  print 'Bot berjalan....'
  print 'Sedang menunggu waktu nya absen\n'

def elearning():
  try:
    get_time()
    s = requests.Session()
    data = {'username':'1220200578','password':'DKGJW0'}
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'http://elearning2.maalmablitar.sch.id/'}
    url = 'http://elearning2.maalmablitar.sch.id/login/do_login'
    req = s.post(url,data=data,headers=headers)
    if 'Akun Anda tidak ditemukan, Mohon periksa Username atau Password yang Anda masukkan' in req.text:
      print 'Login gagal periksa username dan password!'
    elif True:
      url2 = 'http://elearning2.maalmablitar.sch.id/studentam'
      req2 = s.get(url2,headers=headers)
      scrap = BeautifulSoup(req2.text,'html.parser')
      user = scrap.title.text
      kelas = scrap.find('div', {'class': 'navigation-2 landing-menu'})
      for href in kelas.find_all('a',href=True):
       mapel = href.get('title')
       links = href.get('href')
       req3 = s.get(links,headers=headers)
       scrap2 = BeautifulSoup(req3.text,'html.parser')
       absen = scrap2.find_all('a',attrs={'class':'icon-housing icon-click menuajaxkelas','title':'RPP'})[1]
       click = mapel,absen.attrs['href']
       for day in pilih:
         if day in click[0]:
           req4 = s.get(click[1],headers=headers)
           if req4.status_code == 200:
             print '[BOT] Berhasil absensi mapel => %s'%mapel
           else:
             print 'Unknow Error!'
         else:
           pass
    else:
      print 'Unknown Error!'
  except Exception as e:
    print 'Error %s'%e
  except Exception as E:
    print E
get_time()
schedule.every().day.at("07:00").do(elearning)
while True:
  schedule.run_pending()
  time.sleep(5)