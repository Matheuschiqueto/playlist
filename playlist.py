from biblioteca import Biblioteca
from fila import Fila


class GerenciadorPlaylist:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.filas = {
            "relaxar": Fila(),
            "focar":   Fila(),
            "animar":  Fila(),
            "treinar": Fila(),
        }
        self.historico = Fila()

    def _nome_fila(self, bpm):
        if bpm <= 80:
            return "relaxar"
        elif bpm <= 120:
            return "focar"
        elif bpm <= 160:
            return "animar"
        else:
            return "treinar"

    def montar_filas(self):
        for nome in self.filas:
            self.filas[nome] = Fila()
        for musica in self.biblioteca:
            self.filas[self._nome_fila(musica.bpm)].enqueue(musica)

    def reproduzir(self, nome_fila):
        musica = self.filas[nome_fila].dequeue()
        if musica is not None:
            self.historico.enqueue(musica)
        return musica
