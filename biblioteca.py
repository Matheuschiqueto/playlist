from modelos import Musica, NodoLista


class Biblioteca:
    def __init__(self):
        self._cabeca = None
        self._tamanho = 0
        self._proximo_id = 1

    def adicionar(self, titulo, artista, genero, bpm):
        nova = Musica(self._proximo_id, titulo, artista, genero, bpm)
        self._proximo_id += 1
        nodo = NodoLista(nova)
        if self._cabeca is None:
            self._cabeca = nodo
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo
        self._tamanho += 1
        return nova

    def remover(self, id):
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.musica.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar_por_id(self, id):
        atual = self._cabeca
        while atual is not None:
            if atual.musica.id == id:
                return atual.musica
            atual = atual.proximo
        return None

    def buscar_por_titulo(self, titulo):
        atual = self._cabeca
        while atual is not None:
            if atual.musica.titulo == titulo:
                return atual.musica
            atual = atual.proximo
        return None

    def tamanho(self):
        return self._tamanho

    def __iter__(self):
        atual = self._cabeca
        while atual is not None:
            yield atual.musica
            atual = atual.proximo
