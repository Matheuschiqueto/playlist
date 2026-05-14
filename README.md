# Sistema de Playlist

Projeto 2 — Estrutura de Dados

Sistema de gerenciamento de músicas com biblioteca pessoal e filas de reprodução por humor, implementado com estruturas de dados próprias (lista encadeada e fila FIFO) sem uso de `list`, `deque` ou similares do Python.

---

## Estrutura do projeto

| Arquivo | Responsabilidade |
|---|---|
| `modelos.py` | Classes `Musica`, `NodoLista` e `NodoFila` |
| `biblioteca.py` | `Biblioteca` — lista encadeada simples |
| `fila.py` | `Fila` — fila FIFO com nós encadeados |
| `playlist.py` | `GerenciadorPlaylist` — filas de humor e histórico |
| `main.py` | Menu interativo com validações de entrada |

---

## Estruturas de dados utilizadas

### Lista Encadeada — `Biblioteca`

Armazena todas as músicas cadastradas. Cada nó (`NodoLista`) guarda uma `Musica` e uma referência para o próximo nó. Operações: inserção no fim, remoção por ID e busca por ID ou título.

### Fila FIFO — `Fila`

Usada tanto para as filas de humor quanto para o histórico de reproduções. Cada nó (`NodoFila`) aponta para o próximo. Operações: `enqueue` (insere no fim) e `dequeue` (remove do início).

---

## Filas de humor

As músicas são distribuídas nas filas conforme o BPM:

| Fila | BPM |
|---|---|
| Relaxar | até 80 |
| Focar | 81 a 120 |
| Animar | 121 a 160 |
| Treinar | acima de 160 |

A operação **Montar filas** pode ser chamada a qualquer momento; ela limpa as filas anteriores e reconstrói do zero com base na biblioteca atual.

---

## Como executar

```bash
python main.py
```

## Menu de opções

```
1. Adicionar música
2. Remover música
3. Buscar música
4. Listar biblioteca
5. Montar filas de humor
6. Reproduzir próxima
7. Exibir fila de humor
8. Exibir histórico
9. Estatísticas
10. Sair
```
