# ENGETO_Python_Project3
My third PY project, it was created during my studyies in Engeto academy in 2025. Topic:  Elections Scraper. Let´s downolad data!

Projekt: 
	Elections Scraper
	Třetí projekt do Engeto Akademie_Python

Autor
	Jméno: Veronika Balková
	Email: veronika.balkova@rohde-schwarz.com

Popis projektu
	Tento projekt je zaměřen na stažení výsledků voleb z webu volby.cz pro konkrétní územní úroveň (například "Most") v České republice. 
	Z vybrané územní úrovně se dostane ke všem příslušným volebním okrskům a získáme některá data o průběhu a výsledku voleb.
	Takto získaná data jsou uložena do formátu csv.

Instalace
	Nejprve aktivujte své virtuální prostředí. Poté nainstalujte potřebné knihovny pomocí následujícího příkazu:
	pip install requirements.txt
		Jedná se konkrétně o tyto knihovny:
			requests
			beautifulsoup4

Spuštění
	Skript spustíte pomocí dvou argumentů: první je odkaz na územní celek, druhý je název výstupního CSV souboru:
	python main.py <URL> <output_filename>
		- <URL>: URL adresa stránky z volby.cz, ze které chcete stáhnout data.
		- <output_filename>: Název souboru, do kterého budou uloženy výsledky.
	Ukázka
		python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205" most.csv
		Tento příkaz stáhne data z daného URL a uloží výsledky do souboru vysledky.csv.
	
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
567043,Bečov,1 286,489,486,29,2,0,42,12,66,2,5,5,1,1,18,0,8,211,0,3,5,0,0,0,1,74,1
567051,Bělušice,626,223,223,24,2,0,15,6,25,3,12,3,1,3,17,0,2,70,1,2,3,0,1,0,6,19,8
567060,Braňany,974,478,474,28,1,0,23,8,75,12,9,2,3,1,26,0,3,201,1,4,0,0,4,0,1,71,1
567078,Brandov,202,120,120,10,0,0,4,2,15,4,1,2,0,1,10,0,2,54,0,1,0,0,0,0,2,12,0
567108,Český Jiřetín,78,57,57,5,0,0,5,6,5,0,0,0,0,0,7,0,2,19,0,0,1,0,0,0,0,7,0
567141,Havraň,480,262,260,7,0,1,46,3,23,1,1,6,0,0,13,0,7,96,0,2,2,0,1,1,2,47,1
567167,Hora Svaté Kateřiny,361,220,219,22,1,0,12,16,17,9,0,1,0,0,22,0,9,83,0,1,2,0,0,0,1,23,0
567175,Horní Jiřetín,1 728,879,873,60,4,1,48,27,79,73,5,11,2,1,47,0,27,365,0,1,6,0,8,0,6,99,3
....

Diagram programu
	main()
	│
	├── download_data(url)
	│
	├── extract_links(raw_data)
	│
	├── process_obec_data(code, location, link)
	│   ├── (volá se pro každou obec)
	│
	└── generate_csv(all_data, output_filename, all_party_names)

Kontakt
	Pokud máte jakékoliv dotazy nebo potřebujete pomoc, neváhejte mě kontaktovat na výše uvedeném emailu.****
