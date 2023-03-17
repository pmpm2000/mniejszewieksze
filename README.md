Prosty solver zagadek typu mniejsze-wieksze, na przyklad takiej:
![](https://pl.forum.grepolis.com/index.php?attachments/plansza_2-png.14990/)

### Input
Do rozwiazania zagadki potrzebne sa 3 pliki tekstowe. 
#### liczby.txt
Wpisuje sie tu wszystkie liczby z planszy, zachowujac jej ksztalt, oddzielajac wszystko srednikami.
#### wiersze.txt
W tym pliku podajemy wszystkie znaki wiekszosci i mniejszosci w poziomie. Jesli znaku nie ma, podajemy srednik.
#### kolumny.txt
Podaje sie tu znaki wiekszosci i mniejszosci w pionie, oznaczajac je literami "g" od "gora" (kiedy znak wskazuje w gore) i "d" od "dol" (kiedy znak wskazuje w dol).\

Pliki stworzone dla powyzszej przykladowej planszy znajduja sie w folderze "2".

### Output
Program zwraca liczby, ktore wpisane po kolei do zagadki w poziomie stanowia jej rozwiazanie. Algorytm nie jest idealny. Moze sie zdarzyc, ze w pojedynczym
kwadratowym nawiasie bedzie kilka liczb. Wowczas jedna z nich jest rozwiazaniem i nalezy samodzielnie ja wybrac.
