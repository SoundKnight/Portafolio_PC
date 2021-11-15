# !/bin/bash 
# Ibrahim Zavala Hernandez, Julio Gerardo Cazares Gonzales, Pedro Saldaña Vazquez  

#funcion
function APIconnection(){
    curl  https://haveibeenpwned.com/api/v3/breachedaccount/$mail?truncateResponse=false -H "hibp-api-key:$key" -o "JSON/pwned-accounts_$mail.json" 
    if [curl -s JSON/pwned-accounts_$mail.json]||[curl -d JSON/pwned-accounts_$mail.json];
        then
            echo -e "\n Cuenta vulnerada, informacion "
            echo -e "\nTitulo de la pagina"
            sed -E "s/.*Title?:([^,)]+)./\1/"JSON/pwned-accounts_$mail.json 
            echo -e '\nfecha de vulnerabilidad:'
            sed -E "s/.*BreachDate?:([*,)]+)./\1/"JSON/pwned-accounts_$mail.json
            echo -e '\nNumero de cuenta:'
            sed -E "s/,PwnCount?;([^,)]+),*/\1/"JSON/pwned-accounts_$mail.json
            echo -e "----------------------------------------------------\n"
               
        else
            echo  -e "EL correo $mail no fue vulnerado"
            echo "_______________________________________________________"
        fi        
}

# Leer un archivo txt y rellenar una lista
mail_array=()
i=` expr 0 `

while IFS= read -r line
do
    #echo "$line"
    mail_array[i]=$line
    i=` expr $i + 1 `
done < e5correos.txt

#Guardar info en una lista 

# Imprimir pa validar que se guardo la lista
echo 'Los correos por orden son:'
echo "${mail_array[0]}"
echo "${mail_array[1]}"
echo "${mail_array[2]}"

#echo $mail
#Hacer el API con cada correo

read -p -s "Dame la API Key: " key
i=` expr 0 `
while IFS= read -r line
do
    mail_array[i]=$mail
    echo $mail
    i=` expr $i + 1 `
    APIconnection
done < e5correos.txt
