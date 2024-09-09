# Artificial-Intelligence

# Lab12 - Recunoastere emotii in imagini



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. 

## :book:  Aspecte teoretice

Tehnici de pre-procesare a imaginilor.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 




## :bulb: Probleme

Job-ul de la Facebook se consolideaza. Utilizatorii sunt foarte incantati de noul algoritm de detectie a filtrelor in poze si a emotilor in texte, asadar poti sa te ocupi de o noua functionalitate care ar face platforma si mai atractiva.

Echipa de analisti ar dori sa evalueze starea emotionala a utilizatorilor si pe baza imaginilor (daca ei au poze de profil sau posteaza imagini vesele sau triste). De aceea, noul tau task este sa implementezi un algoritm de clasificare a pozelor care care sa indice daca o poza este vesela sau trista. 

Team leaderul echipei de ML iti propune un plan de lucru in 3 iteratii:
- Iteratia 1: clasificarea emotiilor in imagini continand emoticoane (de exemplu Happy faces   versus Sad faces ). Pentru aceasta va trebui:
    - creata o baza cu imagini cu emoticoane si etichetele corespunzatoare (please check this one[link](https://github.com/iamcal/emoji-data))
    - antrenarea unui clasificator de emotii in imagini cu emoticoane
    - testarea clasificatorului
- Iteratia 2: clasificarea emotiilor in imagini cu fete reale folosind un clasificator pre-antrenat. Pentru aceasta va trebui:
    - Preluarea unei baze cu imagini faciale (de ex [FER](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview))
    - Preluarea unui clasificator (model) de emotii in imagini pre-antrenat (de ex [EmoPy](https://github.com/thoughtworksarts/EmoPy))
    - Testarea clasificatorului 
- Iteratia 3: clasificarea emotiilor in imagini cu fete reale folosind un clasificator antrenat de la 0. Pentru aceasta se vor efectua urmatorii pasi:
    - Preluarea unei baze cu imagini faciale (de ex [FER](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview))
    - Antrenarea unui clasificator (model) de emotii in imagini folosind caracteristici ale imaginilor extrase
        - manual - descriptori precum [Haar](https://www.merl.com/publications/docs/TR2004-043.pdf), [HOG](https://hal.inria.fr/file/index/docid/548512/filename/hog_cvpr2005.pdf), etc. Se pot folosi descriptorii implementati in biblioteci specifice de Computer Vision precum [OpenCV](https://opencv.org/), [SciKit-Image](https://scikit-image.org/).
        - automat - modele de extragere preantrenate (precum Facenet) sau antrenate de la 0.
    - Testarea clasificatorului 

Clasificarea imaginilor poate fi:
- Multi-class – fiecare imagine apartine unei anumite emotii
- Multi-label – o imagine poate avea associate mai multe emotii  (de ex baza cu imagini [EmoReact](https://www.behnaznojavan.com/emoreact) descrie imaginile prin mai multe etichete emotionale)


## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati algoritmi de Machine Learning pentru problema de mai sus.

🏵️ Cerinte opționale

Feel free to add!


## :hourglass: Termen de predare 
Laborator 13

## :moneybag: Evaluarea

Punctajele acordate 

- Clasificare emoticoane – 100 puncte
- Clasificare imagini faciale folosind model pre-antrenat – 200 puncte
- Clasificare imagini faciale folosind model antrenat (from scratch) si 
    - Caracteristici „extrase manual”  – 200 puncte
    - Caracteristici „extrase automat” – 300 puncte
- Clasificarea multi-label a imaginilor – 200 puncte (bonus)
 


Notă: 
- punctajul maxim acumulat pentru acest laborator este 1000 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  









# Lab11 - Rezolvarea unor probleme de clustering prin metode de învățare automată 


## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clustering din domeniul text-mining
rezolvate cu ajutorul algoritmilor de tip k-means. Evaluareaa performanței acestor metode.


## :book:  Aspecte teoretice

Algoritmul k-means. Tehnici de pre-procesare a textelor.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță.

 



## :bulb: Probleme

1. **Ce fel de mesaje primesti in Inbox?**
Se doreste clusterizarea unor mesaje in doua categorii (spam si ham). Pentru fiecare mesaj se cunoaste textul aferent lui. Să se rezolve problema, implementându-se rutine pentru clusterizare cu k-means a mesajelor.

2. **Retea sociala: ce fel de mesaje ai postat?**
Mai tii minte ca tocmai ti-ai inceput munca ca si software developer la Facebook si ca faci parte din echipa care se ocupa cu partea de continut a platformei? 
Utilizatorii sunt foarte incantati de noul algoritm de detectie a filtrelor in poze, asadar poti sa te ocupi de o noua functionalitate care ar face platforma mai atractiva. Utilizatorii posteaza o gama larga de mesaje, iar in feed-urile lor apar de multe ori prea multe mesaje negative si prea putine pozitive. Facebook incearca o noua functionalitate prin care sa detecteze sentimentele dintr-un mesaj si sa filtreze feed-urile utilizatorilor. 
Task-ul tau este sa implementezi un algoritm care poate recunoaste sentimentele dintr-un text (pozitiv, negativ, ura, rasism, etc.). 
Team leaderul echipei de ML iti propune urmatorul plan de lucru 
- devoltarea, antrenarea si testarea unui algoritm de tip k-means folosind data de tip numeric (de ex datele cu irisi) 
- devoltarea, antrenarea si testarea unui algoritm de tip k-means folosind data de tip text
    - Considerarea unei baze cu texte etichetate cu emotii (de ex. textele din data/review_mixed.csv sau https://github.com/sarnthil/unify-emotion-datasets/tree/master/datasets)
    - Extragerea de caracteristici din texte folosind diferite reprezentari precum:
        - Bag of Words
        - TF-IDF
        - Word2Vec
        - N-grams, etc.
    - pe baza caracteristicilor extrase, clasificarea textelor si etichetarea lor cu emotii folosind
        - un algoritm de invatare supervizat (folosind etichetele pt emotiile asociate fiecarui text)
        - un algoritm de invatare nesupervizat bazat pe k-means (fara a folosi etichetele pt emotiile asociate fiecarui text)
        - un algoritm hibrid care combina tehncile de invare cu reguli ajutatoare, de ex prin folosirea unor reguli care verifica/numara aparitiile unor cuvinte - polarized words - (e.g. negative words such as bad, worst, ugly, etc and positive words such as good, best, beautiful, etc.)


## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare nesupervizata bazat pe k-means.


🏵️ Cerinte opționale

Feel free to add!


## :hourglass: Termen de predare 
Laborator 12

## :moneybag: Evaluarea

Punctajele acordate
- Implementare kMeans pt clusterizare – 100 puncte
- Extragere caracteristici din texte –
    - Bag of Words / TF-IDF / Wrd2Vec - 50 puncte
    - Alte caracteristici – 100 puncte
- Etichetare emotii
    - supervizat – 50 puncte
    - nesupervizat  – 100 puncte
    - hibrid – 100 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  






# Lab10 - Rezolvarea unor probleme de clasificare prin metode de învățare automată  <img src="images/ann.jpeg" width="150">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clasificare rezolvate cu ajutorul rețeleleor neuronale artificiale (Artificial Neural Networks - ANN). Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Rețele neuronale artificiale pentru rezolvarea problemelor de clasificare.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 
 



## :bulb: Probleme

1. **Ce fel de floare preferi?** 
Se consideră problema clasificării florilor de iris în diferite specii precum: setosa, versicolor și virginica. Pentru fiecare floare se cunosc caracteristici precum: lungimea și lățimea sepalei, lungimea și lățimea petalei. Mai multe detalii despre acest set se pot găsi [aici](https://archive.ics.uci.edu/ml/datasets/Iris). Folosindu-se aceste informații, să se decidă din ce specie aparține o anumită floare. 

2. **Ce cifră am scris?**
Se consideră un set de imagini care conțin cifre scrise de mână. Sa se decida ce cifra apare intr-o imagine.

3. **Retea sociala: ce fel de poze ai postat?**
Tocmai ti-ai inceput prima ta zi de munca ca si software developer la Facebook in echipa care se ocupa cu partea de continut a platformei. 
Echipa de analisti a observat ca foarte multe persoane folosesc filtre peste pozele lor, asadar in speranta de a promova continut mai putin editat, si poze cat mai reale, doresc sa implementeze o noua functionalite in care sa arate utilizatorilor daca o poza a fost sau nu editata. Pentru a testa aceasta idee, si pentru a vedea daca utlizatorilor li s-ar parea folositoare o astfel de functionalitate, au decis sa testeze ideea pe pozele care au filtre sepia. 
Primul task al tau este sa implementezi un algoritm de clasificare a pozelor care sa ne spuna daca o poza are sau nu adaugat filtru sepia. 
Team leaderul echipei de ML iti propune urmatorul plan de lucru 
- devoltarea, antrenarea si testarea unui clasificator bazat pe retele neuronale folosind date mai simple, de tip caracteristici numerice - de ex datele cu irisi) 
- devoltarea, antrenarea si testarea unui clasificator bazat pe retele neuronale folosind date mai complexe, de tip imagine - de ex baza de date cu cifre, pentru fiecare exmplu considerandu-se matricea de pixeli) 
- crearea unei baze cu imagini (cu si fara filtru sepia) si etichetele corespunzatoare 
- antrenarea si testarea clasificatorului (bazat pe retele neuronale artificiale – tool sau ANN-ul dezvoltat la pasul 2) pentru clasificarea imaginilor cu si fara filtru



## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe retele neuronale artificiale (ANN). 


🏵️ Cerinte opționale

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe retele neuronale artificiale convolutive (CNN). 


## :hourglass: Termen de predare 
Laborator 11

## :moneybag: Evaluarea

Punctajele acordate:
- Implementare ANN pt clasificare (cod propriu):
    - antrenare si testare pt datele cu irisi - 200 puncte
    - antrenare si testare pt imagini (de ex cifre) - 300 puncte
- Clasificare (antrenare si testare) imagini cu si fara filtru cu o ANN (cod propriu sau tool) – 250 puncte
- Clasificare (antrenare si testare) imagini cu si fara filtru cu o CNN (cod propriu sau tool) – 250 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 1000 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  









# Lab09 - Rezolvarea unor probleme de clasificare prin metode de învățare automată  <img src="images/binClassification.png" width="150">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clasificare rezolvate cu metoda regresiei logistice. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Metoda gradientului descrescător pentru rezolvarea problemelor de clasificare.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 



## :bulb: Probleme

1. **Clasificarea țesuturilor cancerigene** 
Se consideră informații despre cancerul de sân la femei, informații extrase din ecografii mamare (detalii [aici](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))) precum:
    -	Tipul malformației identificate (țesut benign sau țesut malign)
    -	Caracteristici numerice ale nucleului celulelor din aceste țesuturi:
        - raza (media distanțelor între centru si punctele de pe contur)
        - textura (măsurată prin deviația standard a nivelelor de gri din imaginea asociată țesutului analizat)
Folosindu-se aceste date, să se decidă dacă țesutul dintr-o nouă ecografie (pentru care se cunosc cele 2 caracteristici numerice – raza și textura –) va fi etichetat ca fiind malign sau benign. 


2. **Ce fel de floare preferi?** 
Se consideră problema clasificării florilor de iris în diferite specii precum: setosa, versicolor și virginica. Pentru fiecare floare se cunosc caracteristici precum: lungimea și lățimea sepalei, lungimea și lățimea petalei. Mai multe detalii despre acest set se pot găsi [aici](https://archive.ics.uci.edu/ml/datasets/Iris). Folosindu-se aceste informații, să se decidă din ce specie aparține o anumită floare. 




## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe metoda regresiei logistice. 


🏵️ Cerinte opționale

- folosirea batch-urilor în procesul de antrenament și validarea încrucișată 
- investigarea diferitelor funcții de loss 
- ce se întîmplă în cazul clasificarii binare daca se modifică pragul de decizie din 0.5 în alte valori. Cum se poate aprecia calitatea clasificatorului pentru diferite valori ale pragului?


## :hourglass: Termen de predare 
Laborator 10

## :moneybag: Evaluarea

Punctajele acordate:
- Rezolvarea problemei cu tool – 100 puncte
- Rezolvarea problemei cu cod propriu – 150 puncte + 50 puncte (daca acuratetea clasificarii > 90%)
- Rezolvarea cerințelor opționale – 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  







# Lab08 - Rezolvarea unor probleme de regresie prin metode de învățare automată  <img src="images/regression.png" width="200">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip regresie rezolvate cu metoda gradientului descrescator. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Metoda gradientului descrescător pentru rezolvarea problemelor de regresie.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 



## :bulb: Probleme

**Ce îi poate face pe oameni fericiți?** 
Se consideră problema predicției gradului de fericire a populației globului folosind informații despre diferite caracteristici a bunăstării respectivei populații precum Produsul intern brut al țării în care locuiesc (gross domestic product – GBP), gradul de fericire, etc. 

Folsind datele aferente anului 2017 [link](https://www.kaggle.com/unsdsn/world-happiness#2017.csv), să se realizeze o predicție a gradului de fericire în funcție:
-	doar de Produsul intern brut
-	de Produsul intern brut si de gradul de libertate. 




## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de predicție bazat pe:
- metoda gradientului descrescator stocastic (demo)
- metoda gradientului descrescator bazat pe batch-uri, cu tool/API si/sau cod propriu (tema).

Se vor normaliza datele de antrenament si test. 
 


🏵️ Cerinte opționale

Rezolvarea unei probleme de regresie prin:
- implementare regresie multi-target (cu mai multe output-uri) – sugestii:
    -	outputurile sa fie independente (de ex pe setul de date din sklearn.datasets pot folosi datele psyho din linnerud)
    - outputurile sa fie dependente (aici s-ar putea folosi un regressor gata antrenat – gen yolo (https://pjreddie.com/darknet/yolo/) – pentru a prezice coordonatele bounding box-urilor care încadrează obiectele recunoscute în imagini; trebuie studiat cum se evaluează dacă acele BBs sunt bune sau nu; focusul este de fapt pe interpretarea outputului dat de regressor, nu pe modul în care se antrenează regressorul)


## :hourglass: Termen de predare 

Laborator 9

## :moneybag: Evaluarea

Punctajele acordate:

- Rezolvarea problemei cu tool – 50 puncte

- Rezolvarea problemei cu cod propriu, cazul regresiei univariate – 100 puncte

- Rezolvarea problemei cu cod propriu, cazul regresiei multi-variate – 50 puncte

- Normalizarea datelor – cod propriu 100 puncte

- Rezolvarea cerințelor opționale – maxim 200 puncte

Notă: 

- punctajul maxim acumulat pentru acest laborator este 500 puncte.

- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  








# Lab07 - Rezolvarea unor probleme de regresie prin metode de învățare automată  <img src="images/regression.png" width="200">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip regresie rezolvate cu metoda celor mai mici pătrate. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Metoda celor mai mici pătrate pentru rezolvarea problemelor de regresie.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 



## :bulb: Probleme

**Ce îi poate face pe oameni fericiți?** 
Se consideră problema predicției gradului de fericire a populației globului folosind informații despre diferite caracteristici a bunăstării respectivei populații precum Produsul intern brut al țării în care locuiesc (gross domestic product – GBP), gradul de fericire, etc. 

Folsind datele aferente anului 2017 (fisierul v1_world-happiness-report-2017.csv), să se realizeze o predicție a gradului de fericire în funcție:
-	doar de Produsul intern brut (exemplu detaliat live - demo)
-	de Produsul intern brut si de gradul de libertate (temă). 

Rezolvati problema pentru cazurile in care datele sunt preluate din fisierul:
- v2_world-happiness-report-2017.csv
- v3_world-happiness-report-2017.csv



## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati un algoritm de predicție bazat pe metoda celor mai mici pătrate. 
 


🏵️ Cerinte opționale

Studiul comportamentului algoritmului de predictie pentru date corelate sau incomplete.

## :hourglass: Termen de predare 
Laborator 8

## :moneybag: Evaluarea

Punctajele acordate ...
 
- Rezolvarea problemei (pt datele v1) cu tool – 100 puncte
- Rezolvarea problemei (pt datele v1) cu cod propriu (fara biblioteci specializate – e.g. sklearn, numpy, skit, opencv, etc) – 200 puncte
- Rezolvarea problemei (pt datele v2) - 100 puncte
- Rezolvarea problemei (pt datele v3) - 100 puncte

 Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  








# Lab06 - Invatare automata - metode de evaluare  :+1: or :-1:



## :microscope: Obiective 

Introducere în dezvoltarea sistemelor care învaţă singure. Tipuri de probleme rezolvabile cu metode de învățare automată (regresie și clasificare). Măsuri de evaluare a performanței acestor metode.

## :book:  Aspecte teoretice

Clasificarea problemelor care necesită metode de învățare automată.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță:
- Eroare
- Acuratețe, Precizie, Rapel,
- Funcție de cost 


## :bulb: Probleme

**Problema de regresie**: predictia bunastarii sociale pe baza PIB-ului si a altor factori economici: Se consideră problema predicției gradului de fericire a populației globului folosind informații despre diferite caracteristici a bunăstării respectivei populații precum Produsul intern brut al țării în care locuiesc (gross domestic product – GBP), gradul de fericire, etc. 

**Problema de clasificare**: clasificarea emailurilor (spam si ham) sau a unor persoane (infectate sau sanatoase) sau a unor imagini cu fructe si alte obiecte (fruit vs. non-fruit) sau a unor imagini cu fructe (apple vs. pear vs grappes). 



## :memo:  Cerinte 

Specificaţi, proiectaţi şi implementaţi rutine de evaluare a performanței unui algoritm de ML:
- performanța predicției în cazul unei probleme de regresie
- performanța clasificării (acuratețe, precizie, rapel) în cazul unei probleme de clasificare


Demo:
- **demo1**: performanța predicției în cazul unei probleme de regresie (cu un singur output)
- **demo2**: performanța clasificării (acuratețe, precizie, rapel) în cazul unei clasificări binare (cu output-uri de tip etichetă) - cazul unui set de date echilibrat si cazul unui set de date ne-echilibrat
- **demo3**: performanța clasificării (acuratețe, precizie, rapel) în cazul unei clasificări binare (cu output-uri de tip probabilități - matrice cu $noSamples \times noClasses$ elemente)

Temă:
- sa se specifice procedura de evaluare a unui algoritm de ML care a rezolvat o problema de regresie multi-target si sa se determine eroarea de predictie: pe baza unor date de intrare (precum numarul de ridicari, sarituri, etc.) se doreste predicatia greutatii, taliei si pulsului persoanei care a realizat exrcitiile. Un algoritm de ML a prezis aceste valori. Se doreste calcularea calitatii acestor predictii. A se consulta datele din fisierul "sport.csv".

- sa se specifice procedura de evaluare a unui algoritm de ML care a rezolvat o problema de clasificare multi-clasa si sa se determine acuratetea, precizia, rapelul: pe baza unor masuratori ale petalelor si sepalelor, se doreste predictia tipului de floare intr-un din clasele Daisy, Tulip, Rose. Se doreste calcularea calitatii acestor predictii. A se consulta datele din fisierul "flowers.csv". 

🏵️ Cerinte opționale
- Determinarea loss-ului (funcție de cost) în cazul problemelor de regresie 
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare binară (outputul clasificatorului este reprezentat ca o matrice cu noSamples x 2 valori reale subunitare, fiecare linie având suma 1)
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare multi-clasă (outputul clasificatorului este reprezentat ca o matrice cu noSamples x noClasses valori reale)
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare multi-label (outputul clasificatorului este reprezentat ca o matrice cu noSamples x noClasses valori reale) 


## :hourglass: Termen de predare 
Laborator 7

## :moneybag: Evaluarea

Punctajele acordate:
•	Determinarea erorii de predictie - regresie multi-target – 150 puncte
•	Determinarea acurateții, preciziei, rapelului - clasificare multi-class – 150 puncte
•	Determinarea loss-ului - probleme de regresie și clasificare multi-class și multi-label – 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  











# Lab05 - Algoritmi inspirati de furnici  <img src="ants.jpg" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi inspirati de furnici. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi inspirati de furnici.

## :book:  Aspecte teoretice

- Rezolvarea problemelor ca proces de optimizare
- Tipuri de probleme de optimizare.
- Modalităţi de rezolvare a problemelor de căutare -> Identificarea soluţiei potenţiale optime:
    - Stabilirea componentelor problemei 
        - Condiţii (constrângeri) pe care trebuie să le satisfacă (parţial sau total) soluţia  
        - Funcţie de evaluare a unei soluţii potenţiale -> identificareaa optimului
    - Definirea spaţiul de căutare 
    - Stabilirea strategiei de identificare a soluţiei optime în spaţiul de căutare 

## :bulb: Problema celui mai scurt drum

A se consulta descrierea de la laboratorul 4.



## :memo:  Cerinte 

Să se identifice cel mai scurt drum care pleacă dintr-un nod, vizitează toate nodurile (fiecare nod este vizitat o singură dată) și revine în locația de start folosind un algoritm inspirat de furnici. 


Materiale utile:
- Articolele lui Marco Dorigo [link](https://scholar.google.com/citations?user=PwYT6EMAAAAJ&hl=en), precum
    - M. Dorigo, C. Blum, Ant colony optimization theory: A survey, Theoretical computer science 344 (2-3), 243-278 [link](http://www.mat.uab.cat/~alseda/MasterOpt/DorBlu2005tcs.pdf)
    - M Dorigo, M Birattari, T Stützle, Ant Colony Optimization - Artificial Ants as a Computational Intelligence Technique, IEEE Computational Intelligence Magazine 1 (4), 28-39  [link](https://courses.cs.ut.ee/all/MTAT.03.238/2011K/uploads/Main/04129846.pdf)
    - M. Dorigo, T. Ztutzle, Ant Colony Optimisation, MIT Press [link](http://www.mat.uab.cat/~alseda/MasterOpt/DorBlu2005tcs.pdf)
- Articolele lui C. Blum [link](https://scholar.google.com/citations?user=4e-ykx0AAAAJ&hl=en&oi=sra)
    - Blum, Christian. "Ant colony optimization: Introduction and recent trends." Physics of Life reviews 2, no. 4 (2005): 353-373. 
- Articole pentru grafe dinamice 
    - Chowdhury, Sudipta, Mohammad Marufuzzaman, Huseyin Tunc, Linkan Bian, and William Bullington. "A modified ant colony optimization algorithm to solve a dynamic traveling salesman problem: a case study with drones for wildlife surveillance." Journal of Computational Design and Engineering 6, no. 3 (2019): 368-386. [link](https://academic.oup.com/jcde/article/6/3/368/5732351)
    - Articolele amintite in lucrarea precedenta (in finalul sectiunii Introduction)

Seturi de date utile pot fi gasite [aici](http://www.math.uwaterloo.ca/tsp/data/index.html)
Pentru grafe dinamice se pot folosi:
-	grafurile statice asupra carora se aplica diferite perturbari random
-	grafuri dinamice precum cele de [aici](http://networkrepository.com/dynamic.php)


Aplicaţia (specificata, proiectata si implementata) trebuie să permită:
-	Încărcarea datelor problemei 
-	Alegerea şi parametrizarea metodei de rezolvare a problemei
-	Afişarea soluţiei identificate
-	Precizarea performanţelor metodei de rezolvare alese

Aplicația trebuie să respecte specificațiile privind datele de intrare și datele de ieșire.

Aplicația va fi testată folosind date de difcultăți diferite (fiecare test validat având asociat un anumit punctaj).

Datele de intrare sunt reprezentate de:
-	graful retelei
-	parametrii algoritmului

Datele de iesire sunt reprezentate de:
-	ordinea in care trebuie vizitate nodurile pentru a obtine cel mai bun drum


## :hourglass: Termen de predare 
Laborator 6

## :moneybag: Evaluarea

Punctajele acordate (în funcție de seturile de date folosite) sunt:
-	Seturi de date cu grafe statice 300 puncte
-	Seturi de date cu grafe dinamice 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  








# Lab04 - Algoritmi evolutivi  <img src="evolComp.gif" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi evolutivi. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi evolutivi.

## :book:  Aspecte teoretice

- Rezolvarea problemelor ca proces de optimizare
- Tipuri de probleme de optimizare.
- Modalităţi de rezolvare a problemelor de căutare -> Identificarea soluţiei potenţiale optime:
    - Stabilirea componentelor problemei 
        - Condiţii (constrângeri) pe care trebuie să le satisfacă (parţial sau total) soluţia  
        - Funcţie de evaluare a unei soluţii potenţiale -> identificareaa optimului
    - Definirea spaţiul de căutare 
    - Stabilirea strategiei de identificare a soluţiei optime în spaţiul de căutare 

## :bulb: Problema celui mai scurt drum

In contextul problemei de la laboratoarele 2 si 3, se doreste propagarea unui mesaj in retea intre doua noduri pe drumul cel mai bun posibil (e.g. drumul cel mai scurt, drumul cel mai ieftin, drumul cel mai putin periculos, etc.).



## :memo:  Cerinte 

Să se identifice cel mai scurt drum care pleacă dintr-un nod, vizitează toate nodurile (fiecare nod este vizitat o singură dată) și revine în locația de start folosind un algoritm evolutiv. Se vor folosi:
- informatii din lucrarea Gonen, B., & Louis, S. J. (2006). Genetic Algorithm finding the shortest path in Networks. Reno: University of Nevada [link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.712.8445&rep=rep1&type=pdf)
- reteaua sociala dezvoltata semestrul trecut la MAP (cu construirea in prealabil a grafului corespunzator ei)
- exemplele din arhiva TSP.zip

Aplicaţia (specificata, proiectata si implementata) trebuie să permită:
-	Încărcarea datelor problemei 
-	Alegerea şi parametrizarea metodei de rezolvare a problemei
-	Afişarea soluţiei identificate
-	Precizarea performanţelor metodei de rezolvare alese

Aplicația trebuie să respecte specificațiile privind datele de intrare și datele de ieșire.

Aplicația va fi testată folosind date de difcultăți diferite (fiecare test validat având asociat un anumit punctaj).

Datele de intrare sunt reprezentate de:
-	graful retelei
-	parametrii algoritmului

Datele de iesire sunt reprezentate de:
-	ordinea in care trebuie vizitate nodurile pentru a obtine cel mai bun drum

## 🏵️Cerinte optionale

1. In cazul existentei mai multor solutii, precizati toate solutiile. Analizati diversitatea populatiei de potentiale solutii.

2. Cum impacteaza metoda de rezolvare si solutia/solutiile identificate modificarea cerintei astfel: *Să se identifice cel mai scurt drum care pleacă dintr-un nod și revine în locația de start folosind un algoritm evolutiv.*


## :hourglass: Termen de predare 
Laborator 5

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
- date de dificultate redusa - 50 puncte
- date de dificultate medie - 100 puncte
- date de dificultate mare - 150 puncte
- cerinte optionale - 2 * 100 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  






# Lab03 - Algoritmi evolutivi  <img src="evolComp.gif" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi evolutivi. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi evolutivi.

## :book:  Aspecte teoretice

- Rezolvarea problemelor ca proces de optimizare
- Tipuri de probleme de optimizare.
- Modalităţi de rezolvare a problemelor de căutare -> Identificarea soluţiei potenţiale optime:
    - Stabilirea componentelor problemei 
        - Condiţii (constrângeri) pe care trebuie să le satisfacă (parţial sau total) soluţia  
        - Funcţie de evaluare a unei soluţii potenţiale -> identificareaa optimului
    - Definirea spaţiul de căutare 
    - Stabilirea strategiei de identificare a soluţiei optime în spaţiul de căutare 

## :bulb: Probleme

1. Identificarea punctului de optim a unei functii reale - Demo1


2. Problema identificării comunităților într-o rețea complexă. A se consulta descrierea de la laboratorul 2 - Tema


## :memo:  Cerinte 

Se cere identificarea comunităților existente într-o rețea folosind un algoritm evolutiv. Se vor folosi 
-	informații privind reprezentarea cromozomilor și operatorii genetici din lucrarea: Pizzuti, Clara. "Evolutionary computation for community detection in networks: a review." IEEE Transactions on Evolutionary Computation 22.3 (2017): 464-483. [link](http://staff.icar.cnr.it/pizzuti/pubblicazioni/IEEETEC2017.pdf)
- reteaua sociala dezvoltata semestrul trecut la MAP (cu construirea in prealabil a grafului corespunzator ei)
-	cele 4 rețele / seturi de date din folderul asociat laboratorului current (in format GML – more details [here](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/rutter/abschlussarbeiten/ba-goetz.pdf))
-	rețele / seturi de date identificate de student 

Aplicaţia (specificata, proiectata si implementata) trebuie să permită:
-	Încărcarea datelor problemei 
-	Alegerea şi parametrizarea metodei de rezolvare a problemei
-	Afişarea soluţiei identificate
-	Precizarea performanţelor metodei de rezolvare alese

Aplicația trebuie să respecte specificațiile privind datele de intrare și datele de ieșire.

Aplicația va fi testată folosind date de difcultăți diferite (fiecare test validat având asociat un anumit punctaj).

Datele de intrare sunt reprezentate de:
-	graful retelei
-	parametrii algoritmului

Datele de iesire sunt reprezentate de:
-	numarul de comunitati identificate in graf
-	apartenenta la o anumita comunitate pentru fiecare nod al grafului/retelei


## :hourglass: Termen de predare 
Laborator 4 

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
-	Seturi de date indicate in documentatie - maxim 200 puncte (50 puncte / retea – sunt 4 retele in arhiva real-networks.zip) 
-	Seturi de date identificate de student – maxim 200 puncte (50 puncte / retea)
- functii de fitnes diferite de modularitate - maxim 100 puncte (50 puncte / functie)


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  





# Lab02 - Metoda Greedy <img src="greedy.png" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi de tip greedy. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi de tip greedy.

## :book:  Aspecte teoretice 

- Rezolvarea problemelor ca proces de optimizare
- Tipuri de probleme de optimizare.
- Modalităţi de rezolvare a problemelor de căutare -> Identificarea soluţiei potenţiale optime:
    - Stabilirea componentelor problemei 
        - Condiţii (constrângeri) pe care trebuie să le satisfacă (parţial sau total) soluţia  
        - Funcţie de evaluare a unei soluţii potenţiale -> identificareaa optimului
    - Definirea spaţiul de căutare 
    - Stabilirea strategiei de identificare a soluţiei optime în spaţiul de căutare 

## :bulb: Probleme

**Problema identificării comunităților într-o rețea complexă**

Descoperirea și analiza comunităților în rețele este o temă larg dezbătută în sociologie, biologie și informatică. Rețelele complexe reprezintă suportul pentru diferite sisteme reale (facebook, sistemul imun, creierul, infrastrcutura de transport, etc.). O comunitate în aceste rețele este definită ca un grup de noduri dens conectate unele cu altele, dar puțin conectate cu noduri din alte comunități. 

<details><summary>La ce ajută identificarea acestor comunități? Click pentru câteva exemple</summary>

1.	cum influenteaza tipul relatiilor dintre studenti definirea comunitatilor ce pot aparea in reteaua pe care o formeaza? (Exista mai mult tipuri de relatii in datasetul furnizat, comunitatile create au o diveristate in tipurile de relatii? Sau “cine se aseamana se aduna”?)
    - [dataset](http://networkrepository.com/soc-student-coop.php)
    - [lucrare]http://www.ise.bgu.ac.il/faculty/fire/pdf/fire2012predicting.pdf)

2.	cum tind sa formeze comunitati persoanele populare aka influencers pe tweeter (aici se poate discuta definitia popularitatii prin diferite metrici ca si degree centrality, betweeness centrality, articulation point) - principiul "cine se aseamana se aduna")
    - [dataset](http://networkrepository.com/soc-twitter-follows.php)
    - [lucrare](https://arxiv.org/pdf/1211.4266.pdf)

3.	comportamentul social al furnicilor (retea dinamica) - sunt furnicile insecte sociale? isi schimba des comunitatile din care fac parte, sau tind sa ramana in aceleasi comunitati? Exista vreun pattern in comportamentul furnicilor in acest sens?
    - [dataset](https://github.com/bansallab/asnr/tree/master/Networks/Insecta/)ants_proximity_weighted)
    - [lucrare](https://www.nature.com/articles/s41597-019-0056-z)
</details>


<img src="complexNetworks.png" width="400">


## :memo:  Cerinte 

Se cere identificarea comunităților existente într-o rețea folosind un algoritm Greedy. Se vor folosi:
- informații privind metoda Greedy propusa de Newman - Newman, M. E. (2004). Fast algorithm for detecting community structure in networks. Physical review E, 69(6), 066133. [link](https://arxiv.org/pdf/cond-mat/0309508.pdf)
- reteaua sociala dezvoltata semestrul trecut la MAP (cu construirea in prealabil a grafului corespunzator ei)
- cele 4 rețele / seturi de date din folderul asociat laboratorului current (in format GML – more details [here](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/rutter/abschlussarbeiten/ba-goetz.pdf))
-	rețele / seturi de date identificate de student 

Aplicaţia (specificata, proiectata si implementata) trebuie să permită:
-	Încărcarea datelor problemei 
-	Alegerea şi parametrizarea metodei de rezolvare a problemei
-	Afişarea soluţiei identificate
-	Precizarea performanţelor metodei de rezolvare alese

Aplicația trebuie să respecte specificațiile privind datele de intrare și datele de ieșire.

Aplicația va fi testată folosind date de difcultăți diferite (fiecare test validat având asociat un anumit punctaj).

Datele de intrare sunt reprezentate de:
-	graful retelei
-	parametrii algoritmului

Datele de iesire sunt reprezentate de:
-	numarul de comunitati identificate in graf
-	apartenenta la o anumita comunitate pentru fiecare nod al grafului/retelei


## :hourglass: Termen de predare 
Laborator 3 

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
-	Seturi de date indicate in documentatie - maxim 200 puncte (50 puncte / retea – sunt 4 retele in arhiva real-networks.zip) 
-	Seturi de date identificate de student – maxim 300 puncte (50 puncte / retea)|



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  




# Lab01 - Algoritmi simpli <img src="algorithm.png" width="100">


## :microscope: Obiective 

Rezolvarea problemelor folosind metode diferite din punct de vedere al complexității (temporale și spațiale). 

## :book:  Aspecte teoretice 

Rezolvarea problemelor. Analiza complexității procesului de rezolvare.


## :bulb: Probleme simple, dar cu dichis :blossom:

1.	Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care conține mai multe cuvinte separate prin ” ” (spațiu). *De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".*

2.	Să se determine distanța Euclideană între două locații identificate prin perechi de numere. 
*De ex. distanța între (1,5) și (4,1) este 5.0*

3.	Să se determine produsul scalar a doi vectori rari care conțin numere reale. Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
*De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.*

4.	Să se determine cuvintele unui text care apar exact o singură dată în acel text. 
*De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.*

5.	Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
*De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.*

6.	Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar (care apare de mai mult de n / 2 ori).
*De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].*

7.	Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
*De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.*

8.	Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. 
*De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.*

9.	Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile identificate de fieare pereche. 
    > *De ex, pt matricea*\
    > [[0, 2, 5, 4, 1], \
    >  [4, 8, 2, 3, 7], \
    >  [6, 3, 4, 6, 2], \
    >  [7, 3, 1, 8, 3], \
    >  [1, 5, 7, 9, 4]] \
    > *și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.*

10.	Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice indexul liniei care conține cele mai multe elemente de 1. 
    > *De ex. în matricea* \
    > [[0,0,0,1,1], \
    > [0,1,1,1,1], \
    > [0,0,1,1,1]] \
    > *a doua linie conține cele mai multe elemente 1.*

11.	Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1. 
    > *De ex. matricea* \ 
    > [[1,1,1,1,0,0,1,1,0,1],\
    > [1,0,0,1,1,0,1,1,1,1],\
    > [1,0,0,1,1,1,1,1,1,1],\
    > [1,1,1,1,0,0,1,1,0,1],\
    > [1,0,0,1,1,0,1,1,0,0],\
    > [1,1,0,1,1,0,0,1,0,1],\
    > [1,1,1,0,1,0,1,0,0,1],\
    > [1,1,1,0,1,1,1,1,1,1]]\
	> *devine * \
    > [[1,1,1,1,0,0,1,1,0,1],\
    > [1,1,1,1,1,0,1,1,1,1],\
    > [1,1,1,1,1,1,1,1,1,1],\
    > [1,1,1,1,1,1,1,1,0,1],\
    > [1,1,1,1,1,1,1,1,0,0],\
    > [1,1,1,1,1,1,1,1,0,1],\
    > [1,1,1,0,1,1,1,0,0,1],\
    > [1,1,1,0,1,1,1,1,1,1]]\



## :memo:  Cerinte 

Specificaţi, implementaţi și testați subalgoritmi pentru problemele enuntate. Încercați să rezolvați fiecare cerința cât mai eficient (ca număr de pași și / sau ca resurse de memorie folosite).

## :hourglass: Termen de predare 

Laborator 1 (tema live): minim doua probleme

Laborator 2: restul de probleme

## :moneybag: Evaluarea

**Obligatoriu** 5 probleme la alegere, pentru fiecare problemă se va prezenta o soluție cat mai eficienta. Fiecare rezolvare corectă va primi maxim 20 puncte. 

**\[Opțional\]**
Rezolvarea prin alte metode a problemelor alese la punctul precedent sau rezolvarea unor noi probleme. Fiecare rezolvare corectă va primi maxim 20 puncte. 

Notă: 
- punctajul maxim acumulat pentru acest laborator este 200 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  

