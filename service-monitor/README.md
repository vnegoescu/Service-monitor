# service-monitor
```
                +--------------+          +-------------+
                |              +<---------+             |
       +------->+    Monitor   +<-----+   |   MongoDB   |
       |        |              |      |   |             |
       |        +--------------+      |   +-------------+
       |                              |                  
       |                              |                  
       |                              |                  
+------+-----+                 +------+-----+            
|            |                 |            |            
|  Service1  |                 |  Service2  |            
|            |                 |            |            
+------------+                 +------------+            
```


Service-monitor- monitor de servicii:
	1. Un serviciu master care monitorizeaza alte servicii slave
	2. Masterul(Monitor) stocheaza intr o DB(mongo DB) ultima data cand a primit semnal de la restul serviciilor( slaves).Fiecar serviciu trimitea catre master un pinc(ca e activ) -> masterul updata in 
	baza de date faptul ca serviciul e activ.
	3. In baza de date se stoca ID-ul serviciului si timestampul
	4. Se va imlementa un serviciu writer. Serviciul primeste ca parametru pe metoda post un JSON. Daca primeste "exit" serviciul se oprese, altfel scrie in fiesier continutul primit pe me
	metoda post.( face append, nu suprascrie continutul)
	5. MONGO DB- serviciu de baze de date nonrelationala, optimizata pentru operatii de write
	5.Monitor-2 metode
		POST:(upd) se posteaza un json(se stocheaza numele si timestampul in DB) si se suprascrie in cazul in care serviciul exista deja in baza de date( e deja monitorizat), altfel il creeaza
		GET:(info) verifica daca serviciul este in DB. IN cazul in care este se face diferenta intre timestampul curent si timpul la care serviciul a trimis ultimul ping. Daca diferenta este 
		mai mare de 5 secunde se considera ca serviciul nu mai este activ. In caz contrar (dif<5) se returneaza ce este in baza de date
