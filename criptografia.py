# Função que realiza a Cifra de César
def cifra_de_cesar(mensagem, deslocamento):
    resultado = ""
    # Percorre cada letra da mensagem
    for letra in mensagem:
        if letra.isalpha():  # Verifica se é uma letra
            ascii_offset = 65 if letra.isupper() else 97  # Define o offset para maiúsculas ou minúsculas
            nova_letra = chr((ord(letra) - ascii_offset + deslocamento) % 26 + ascii_offset)
            resultado += nova_letra  # Adiciona a nova letra ao resultado
        else:
            resultado += letra  # Mantém espaços e pontuação
    return resultado  # Retorna a mensagem criptografada

# Função que realiza a Cifra de Vigenère
def cifra_de_vigenere(mensagem, chave):
    resultado = ""
    # Repete a chave para que tenha o mesmo tamanho que a mensagem
    chave_repetida = (chave * (len(mensagem) // len(chave))) + chave[:len(mensagem) % len(chave)]
    for i in range(len(mensagem)):
        letra_mensagem = mensagem[i]
        if letra_mensagem.isalpha():  # Verifica se é uma letra
            ascii_offset = 65 if letra_mensagem.isupper() else 97
            deslocamento = ord(chave_repetida[i].upper()) - 65  # Calcula o deslocamento baseado na chave
            nova_letra = chr((ord(letra_mensagem) - ascii_offset + deslocamento) % 26 + ascii_offset)
            resultado += nova_letra  # Adiciona a nova letra ao resultado
        else:
            resultado += letra_mensagem  # Mantém espaços e pontuação
    return resultado  # Retorna a mensagem criptografada

# Função para descriptografar usando a Cifra de César
def decifra_de_cesar(mensagem, deslocamento):
    return cifra_de_cesar(mensagem, -deslocamento)  # Inverte o deslocamento

# Função para descriptografar usando a Cifra de Vigenère
def decifra_de_vigenere(mensagem, chave):
    resultado = ""
    # Repete a chave para que tenha o mesmo tamanho que a mensagem
    chave_repetida = (chave * (len(mensagem) // len(chave))) + chave[:len(mensagem) % len(chave)]
    for i in range(len(mensagem)):
        letra_mensagem = mensagem[i]
        if letra_mensagem.isalpha():  # Verifica se é uma letra
            ascii_offset = 65 if letra_mensagem.isupper() else 97
            deslocamento = ord(chave_repetida[i].upper()) - 65  # Calcula o deslocamento baseado na chave
            nova_letra = chr((ord(letra_mensagem) - ascii_offset - deslocamento) % 26 + ascii_offset)
            resultado += nova_letra  # Adiciona a nova letra ao resultado
        else:
            resultado += letra_mensagem  # Mantém espaços e pontuação
    return resultado  # Retorna a mensagem descriptografada

# Função para criptografar um arquivo
def criptografar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, algoritmo, chave=None, deslocamento=None):
    with open(nome_arquivo_entrada, 'r') as arquivo:  # Abre o arquivo de entrada
        mensagem = arquivo.read()  # Lê a mensagem do arquivo
    
    # Verifica qual algoritmo usar para criptografar
    if algoritmo == 'cesar':
        mensagem_criptografada = cifra_de_cesar(mensagem, deslocamento)
    elif algoritmo == 'vigenere':
        mensagem_criptografada = cifra_de_vigenere(mensagem, chave)

    # Salva a mensagem criptografada em um novo arquivo
    with open(nome_arquivo_saida, 'w') as arquivo:
        arquivo.write(mensagem_criptografada)

# Função para descriptografar um arquivo
def descriptografar_arquivo(nome_arquivo_entrada, nome_arquivo_saida, algoritmo, chave=None, deslocamento=None):
    with open(nome_arquivo_entrada, 'r') as arquivo:  # Abre o arquivo de entrada
        mensagem_criptografada = arquivo.read()  # Lê a mensagem criptografada do arquivo
    
    # Verifica qual algoritmo usar para descriptografar
    if algoritmo == 'cesar':
        mensagem_descriptografada = decifra_de_cesar(mensagem_criptografada, deslocamento)
    elif algoritmo == 'vigenere':
        mensagem_descriptografada = decifra_de_vigenere(mensagem_criptografada, chave)

    print(f"\n🔍 Mensagem descriptografada: {mensagem_descriptografada}")  # Exibe a mensagem descriptografada
    
    # Salva a mensagem descriptografada em um novo arquivo
    with open(nome_arquivo_saida, 'w') as arquivo:
        arquivo.write(mensagem_descriptografada)

# Função principal que gerencia o menu
def main():
    print("======================================================================")
    print("    🌟 BEM-VINDO AO SISTEMA DE CRIPTOGRAFIA 🌟")
    print("       🔐 Protegendo Suas Mensagens com Estilo 🔐")
    print("======================================================================")
    
    while True:  # Loop para manter o menu ativo
        print("Escolha uma opção:")
        print("  [1] 🌍 Criptografar uma Mensagem")
        print("  [2] 🔓 Descriptografar uma Mensagem")
        print("  [3] 📂 Criptografar um Arquivo")
        print("  [4] 📁 Descriptografar um Arquivo")
        print("  [5] ❌ Sair")
        print("======================================================================")
        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            mensagem = input("Digite a mensagem a ser criptografada: ")
            print("Escolha o algoritmo:")
            print("  [1] Cifra de César")
            print("  [2] Cifra de Vigenère")
            algoritmo = input("Digite o número do algoritmo: ")

            if algoritmo == '1':
                deslocamento = int(input("Digite o deslocamento para a Cifra de César: "))
                resultado = cifra_de_cesar(mensagem, deslocamento)
                print(f"\n🔒 Mensagem criptografada (César): {resultado}")
            elif algoritmo == '2':
                chave = input("Digite a chave para a Cifra de Vigenère: ")
                resultado = cifra_de_vigenere(mensagem, chave)
                print(f"\n🔑 Mensagem criptografada (Vigenère): {resultado}")
            else:
                print("Opção inválida!")  # Se a opção não for válida

        elif opcao == '2':
            mensagem = input("Digite a mensagem a ser descriptografada: ")
            print("Escolha o algoritmo:")
            print("  [1] Cifra de César")
            print("  [2] Cifra de Vigenère")
            algoritmo = input("Digite o número do algoritmo: ")

            if algoritmo == '1':
                deslocamento = int(input("Digite o deslocamento para a Cifra de César: "))
                resultado = decifra_de_cesar(mensagem, deslocamento)
                print(f"\n🔓 Mensagem descriptografada (César): {resultado}")
            elif algoritmo == '2':
                chave = input("Digite a chave para a Cifra de Vigenère: ")
                resultado = decifra_de_vigenere(mensagem, chave)
                print(f"\n🔍 Mensagem descriptografada (Vigenère): {resultado}")
            else:
                print("Opção inválida!")  # Se a opção não for válida

        elif opcao == '3':
            nome_arquivo = input("Digite o nome do arquivo de entrada (com .txt): ")
            print("Escolha o algoritmo:")
            print("  [1] Cifra de César")
            print("  [2] Cifra de Vigenère")
            algoritmo = input("Digite o número do algoritmo: ")

            if algoritmo == '1':
                deslocamento = int(input("Digite o deslocamento para a Cifra de César: "))
                nome_arquivo_saida = input("Digite o nome do arquivo de saída (com .txt): ")
                criptografar_arquivo(nome_arquivo, nome_arquivo_saida, 'cesar', deslocamento=deslocamento)
                print("Mensagem criptografada e salva no arquivo com sucesso!")
            elif algoritmo == '2':
                chave = input("Digite a chave para a Cifra de Vigenère: ")
                nome_arquivo_saida = input("Digite o nome do arquivo de saída (com .txt): ")
                criptografar_arquivo(nome_arquivo, nome_arquivo_saida, 'vigenere', chave=chave)
                print("Mensagem criptografada e salva no arquivo com sucesso!")
            else:
                print("Opção inválida!")  # Se a opção não for válida

        elif opcao == '4':
            nome_arquivo = input("Digite o nome do arquivo de entrada (com .txt): ")
            print("Escolha o algoritmo:")
            print("  [1] Cifra de César")
            print("  [2] Cifra de Vigenère")
            algoritmo = input("Digite o número do algoritmo: ")

            if algoritmo == '1':
                deslocamento = int(input("Digite o deslocamento para a Cifra de César: "))
                nome_arquivo_saida = input("Digite o nome do arquivo de saída (com .txt): ")
                descriptografar_arquivo(nome_arquivo, nome_arquivo_saida, 'cesar', deslocamento=deslocamento)
                print("Mensagem descriptografada e salva no arquivo com sucesso!")
            elif algoritmo == '2':
                chave = input("Digite a chave para a Cifra de Vigenère: ")
                nome_arquivo_saida = input("Digite o nome do arquivo de saída (com .txt): ")
                descriptografar_arquivo(nome_arquivo, nome_arquivo_saida, 'vigenere', chave=chave)
                print("Mensagem descriptografada e salva no arquivo com sucesso!")
            else:
                print("Opção inválida!")  # Se a opção não for válida

        elif opcao == '5':
            print("Saindo do programa... Até logo! 👋")  # Mensagem de despedida
            break  # Sai do loop e encerra o programa

        else:
            print("Opção inválida!")  # Se a opção não for válida

# Chamada da função principal
if __name__ == "__main__":
    main()  # Inicia o programa
