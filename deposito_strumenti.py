from operator import attrgetter

class Strumento:
    def __init__(self, cod, tipo, marca, anno, valore):
        self.cod=cod
        self.tipo=tipo
        self.marca=marca
        self.anno=anno
        self.valore=valore


class Prestito:
    def __init__(self, cod_prestito, data, cognome_allievo, id_strumento):
        self.cod_prestito=cod_prestito
        self.data=data
        self.id_strumento=id_strumento
        self.cognome_allievo=cognome_allievo


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.resp=responsabile
        self.strumenti=[]
        self.prestati=[]
        self.contatore_prestiti=0

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, mode="r", encoding="utf-8") as fil:
            for riga in fil:
                riga=riga.strip()
                if not riga:
                    continue
                parti=[p.strip() for p in riga.split(",")]
                if len(parti) >= 5:
                    codice = parti[0]
                    tipo = parti[1]
                    marca = parti[2]
                    anno_acquisto = int(parti[3])
                    valore = float(parti[4])

                    nuovoS=Strumento(codice, tipo, marca, anno_acquisto, valore)
                    self.strumenti.append(nuovoS)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):


        max_num = 0
        for s in self.strumenti:
            if s.codice.startswith("S"):
                try:
                    num = int(s.codice[1:])
                    if num > max_num:
                        max_num = num
                except ValueError:
                    pass

        nuovo_codice = f"S{max_num + 1}"
        nuovoStrumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovoStrumento)
        return nuovoStrumento



    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        strumento_trovato = False
        for s in self.strumenti:
            if s.codice==id_strumento:
                strumento_trovato = True
                break
        if not strumento_trovato:

            raise Exception(f"Errore: Lo strumento non esiste")
        for p in self.prestati:
            if p.cod_s == id_strumento:
                raise Exception(f"Errore: Lo strumento è già attualmente in prestito.")

        self.contatore_prestiti += 1
        nuovo_p = Prestito(cod_prestito, data, id_strumento, cognome_allievo)
        self.prestati.append(nuovo_p)
        return nuovo_p

        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for p in self.prestati:
            if p.cod_prestito == id_prestito:
                self.prestati.remove(p)
        raise Exception(f"Errore: Nessun prestito trovato")
        # TODO
