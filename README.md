# wake-on-lan

Skript naslouchá na zařízení v subnetu a jakmile přijde HTTP request zvenčí, pošle magic packet na zadanou MAC adresu - v témže subnetu. Vhodné pro rasberi, ale pro testovací účely lze spustit i na androidu pod Termuxem.

<img width="420" height="180" alt="obrazek" src="https://github.com/user-attachments/assets/1d9819c7-ff69-48b2-ac46-82a06a22450c" />

Kontrola síťového portu:
- curl sklep.chochrun.eu:8081 

P.S. Prosím, zacpyte si oči, zapomněl jsem zamaskovat MAC adresu svého PC... dík

## Požadavky a Setup na androidu (jestli si chudý jak já a nemáš peníze na Rasberi)
- Samozřejmostí je mít povolený wake on lan na základní desce.
- Další samozřejmostí je mít aktualizovaný síťový ovladač s požadovanou konfigurací v síťových zařízeních
# Teď to hlavní!
- Nainstaluješ mamce Termux emulátor přes F-droid
- Nainstaluješ python
- Zapneš skript a naforwarduješ přes router
- Když je proces zamražen správcem android baterie, tak mamku prozvoň a spamuj: `curl http://Tvoja.IP:8080`
- ... Jo a mamka musí být doma
