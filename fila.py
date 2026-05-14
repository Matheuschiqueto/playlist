from modelos import NodoFila


class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def enqueue(self, musica):
        nodo = NodoFila(musica)
        if self._fim is None:
            self._inicio = nodo
            self._fim = nodo
        else:
            self._fim.proximo = nodo
            self._fim = nodo
        self._tamanho += 1

    def dequeue(self):
        if self._inicio is None:
            return None
        musica = self._inicio.musica
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return musica

    def tamanho(self):
        return self._tamanho

    def __iter__(self):
        atual = self._inicio
        while atual is not None:
            yield atual.musica
            atual = atual.proximo
