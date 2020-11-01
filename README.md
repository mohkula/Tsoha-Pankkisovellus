# Tsoha-Pankkisovellus

Pankkisovellukseen voi asiakas luoda oman tunnuksen ja antamalla asiakastunnuksen ja salasanan sovellukseen asiakas pääsee näkemään omat pankkitietonsa:

tilinsä ja niiden tilitapahtumat (näille asiakas ei voi tehdä mitään muuta kuin katsoa)
pankkikorttinsa (asiakas voi muuttaa pankkikorttinsa ominaisuuksia: missä maassa sillä voi maksaa, onko verkkomaksaminen sallittu vai estetty, paljonko käteistä saa nostaa/vrk, paljonko kortilla voi maksaa / vrk)
asiakas voi tilata uuden pankkikortin itselleen
asiakastietonsa (voi muuttaa: puhelinnumero, osoite, kieli, sähköpostiosoite)
 

Jos sovellukseen kirjautuu pääkäyttäjän tunnuksella ja salasanalla, avautuu erilaisia vaihtoehtoja.

Pääkäyttäjä voi valita jonkun tietyn asiakkaan tiedot nähtäväksi / muutettavaksi. Pääkäyttäjä voi päästä myös muuttamaan tietoja, joita asiakas ei itse pääse muuttamaan. Pääkäyttäjä myös näkee luodut uudet tunnukset ja voi joko hyväksyä tai hylätä ne, vasta kun pääkäyttäjä on hyväksynyt uuden tunnuksen, pääsee asiakas kirjautumaan tunnuksellaan.

 

Järjestelmässä olevat taulut:

- Asiakastiedot (asiakkaan perustiedot: nimi, osoite, puhelinnumero, kieli, sähköpostiosoite)

- Tilitiedot (asiakkaan käytössä olevat tilit)

- Tilitapahtumat (tietyn tilin tapahtumat) En tiedä vielä miten tilitapahtumia luodaan, ehkä vain tylsästi lisätään tapahtuman nimi ja rahasumma

- Korttitiedot (käytössä olevat pankkikortit)

- Kortin varoitustiedot (liittyvät kortin katoamiseen)

- Kortin maksutiedot (verkkomaksaminen, maarajaus, käteisnostoraja, maksuraja)

- Tilaustiedot
