from playlist import GerenciadorPlaylist

FILAS = {"1": "relaxar", "2": "focar", "3": "animar", "4": "treinar"}


def escolher_fila():
    print("1-Relaxar  2-Focar  3-Animar  4-Treinar")
    return FILAS.get(input("Escolha a fila: ").strip())


def main():
    gp = GerenciadorPlaylist()

    while True:
        print("\n=== SISTEMA DE PLAYLIST ===")
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Buscar música")
        print("4. Listar biblioteca")
        print("5. Montar filas de humor")
        print("6. Reproduzir próxima")
        print("7. Exibir fila de humor")
        print("8. Exibir histórico")
        print("9. Estatísticas")
        print("10. Sair")

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            genero = input("Gênero: ").strip()
            try:
                bpm = int(input("BPM: ").strip())
            except ValueError:
                print("BPM inválido — informe um número inteiro.")
                continue
            if bpm <= 0:
                print("BPM deve ser maior que zero.")
                continue
            musica = gp.biblioteca.adicionar(titulo, artista, genero, bpm)
            print(f"Adicionada: {musica}")

        elif opcao == "2":
            try:
                id_buscado = int(input("ID da música: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            if gp.biblioteca.remover(id_buscado):
                print("Música removida.")
            else:
                print("ID não encontrado na biblioteca.")

        elif opcao == "3":
            print("Buscar por: 1-ID  2-Título")
            modo = input("Opção: ").strip()
            if modo == "1":
                try:
                    id_buscado = int(input("ID: ").strip())
                except ValueError:
                    print("ID inválido.")
                    continue
                musica = gp.biblioteca.buscar_por_id(id_buscado)
            elif modo == "2":
                titulo = input("Título: ").strip()
                musica = gp.biblioteca.buscar_por_titulo(titulo)
            else:
                print("Opção inválida.")
                continue
            print(musica if musica else "Música não encontrada.")

        elif opcao == "4":
            if gp.biblioteca.tamanho() == 0:
                print("Biblioteca vazia.")
            else:
                for musica in gp.biblioteca:
                    print(musica)

        elif opcao == "5":
            gp.montar_filas()
            print("Filas de humor montadas com sucesso.")

        elif opcao == "6":
            nome = escolher_fila()
            if nome is None:
                print("Opção inválida.")
                continue
            musica = gp.reproduzir(nome)
            if musica:
                print(f"Reproduzindo: {musica}")
            else:
                print(f"A fila '{nome}' está vazia.")

        elif opcao == "7":
            nome = escolher_fila()
            if nome is None:
                print("Opção inválida.")
                continue
            if gp.filas[nome].tamanho() == 0:
                print(f"A fila '{nome}' está vazia.")
            else:
                for musica in gp.filas[nome]:
                    print(musica)

        elif opcao == "8":
            if gp.historico.tamanho() == 0:
                print("Histórico vazio.")
            else:
                for musica in gp.historico:
                    print(musica)

        elif opcao == "9":
            print(f"Biblioteca: {gp.biblioteca.tamanho()} música(s)")
            for nome in FILAS.values():
                print(f"  Fila {nome}: {gp.filas[nome].tamanho()} música(s)")
            print(f"Histórico:  {gp.historico.tamanho()} reprodução(ões)")

        elif opcao == "10":
            print("Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
