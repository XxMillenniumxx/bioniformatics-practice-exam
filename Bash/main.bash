#                             Online Bash Shell.
#                 Code, Compile, Run and Debug Bash script online.
# Write your code in this editor and press "Run" button to execute it.
#ls
#pwd
#ls -F

#echo sequence.fasta
#head -n 1 sequence.fasta | tail -n 1

#grep -n "AAAAA" sequence.fasta

#head -n 1 sequence.fasta
#
#len_string=$(wc -l sequence.fasta | awk '{print $1}')
#echo $len_string
#for string_num in $(seq 1 $len_string)
#do
#    string=$(awk 'NR == $string_num' sequence.fasta)
#    echo $string
#    if [[ $(grep -E "^>" $string) ]]; then
#        echo $(grep -E "^>" sequence.fasta) > result_01.txt
#    else
#        echo $string
#    fi
#done


#$0 — представляет всю строку текста (запись).
#$1 — первое поле.
#$2 — второе поле.
#$n — n-ное поле.
#запись — это строка. Поле — это слово в строк
#FIELDWIDTHS — разделённый пробелами список чисел, определяющий точную ширину каждого поля данных с учётом разделителей полей.
#FS — уже знакомая вам переменная, позволяющая задавать символ-разделитель полей.
#RS — переменная, которая позволяет задавать символ-разделитель записей.
#OFS — разделитель полей на выводе awk-скрипта.
#ORS — разделитель записей на выводе awk-скрипта.


#prev - предыдущая с которой мы работаем(текущая)
#$0 - текущая (Будущая)
awk '{
    if (NR == 1) {
        printf "%s", $0;
    } else if (prev ~ /^>/) {
        print prev;
    } else {
        if ($0 ~ /^>/) {
            print prev;
        } else {
            printf "%s", prev;
            
        }
    }
    prev = $0;
}' sequence.fasta > result.fasta

grep -n -oP '((\w)\2+)' result.fasta > repeat.txt
