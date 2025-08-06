# Listas para armazenar os produtos e seus valores
produtos = []
valores = []

# Listas para armazenar os itens da venda
itens_comprados = []
quantidades = []

def cadastrar_produto(): #função para cadastrar novos produtos
    while True: #while loop para permitir múltiplos cadastros
        nome = input("\nDigite o nome do produto (ou 'sair' para encerrar): ") #input do nome do produto
        if nome.lower() == 'sair': #Se o usuário digitar 'sair', encerra o cadastro e sai do loop 
            break
        
        try: # Verifica se o nome do produto é válido
            if nome == "": # Se o nome for vazio, exibe mensagem de erro
                print("❌ Nome do produto não pode ser vazio! Tente novamente.")
                continue
            elif nome in produtos: # Se o produto já estiver cadastrado, exibe mensagem de erro
                # e solicita outro nome
                print(f"❌ Produto '{nome}' já cadastrado! Tente outro nome.")
                continue
            valor = float(input(f"Digite o valor de {nome}: R$ ")) # input do valor do produto
            produtos.append(nome) # Adiciona o nome do produto à lista de produtos
            valores.append(valor) # Adiciona o valor do produto à lista de valores
            print(f"✅ {nome} cadastrado com sucesso por R$ {valor:.2f}!") # Exibe mensagem de sucesso
        except ValueError: # tratamento de erro para valores inválidos
            print("❌ Valor inválido! Digite um número válido.")

def mostrar_produtos(): #função para exibir os produtos cadastrados
    print("\n--- Produtos Cadastrados ---")
    if not produtos:  # Se a lista de produtos estiver vazia, exibe mensagem informando
        print("Nenhum produto cadastrado ainda!")
    else:  # Exibe a lista de produtos e seus valores
        print(f"{'Código':<6} | {'Produto':<20} | {'Valor (R$)':>10}")  # Cabeçalhos da tabela mantendo alinhamento
        print("-" * 45)
        for i, (produto, valor) in enumerate(zip(produtos, valores), 1): #Enumera os produtos e valores
            print(f"{i:<6} | {produto:<20} | {valor:>10.2f}")

def processar_venda(): #função para processar a venda de produtos
    global itens_comprados, quantidades # Importa as listas globais para armazenar itens comprados e quantidades
    itens_comprados = [] # Lista para armazenar os itens comprados
    quantidades = [] # Lista para armazenar as quantidades de cada item comprado
    total_compra = 0.0 # Variável para armazenar o total da compra
    
    print("\n--- Modo de Venda ---")
    print("Digite o código do produto (1 a {}) ou 0 para finalizar".format(len(produtos))) # Informa o usuário sobre os códigos dos produtos
    
    while True: # Loop para processar a venda até que o usuário decida finalizar
        mostrar_produtos()  # Mostra a lista de produtos disponíveis
        
        try:  # Solicita o código do produto ao usuário
            codigo = int(input("\nCódigo do produto: "))
            
            if codigo == 0: # Se o usuário digitar 0, finaliza a venda
                break  # Finaliza a venda   
            
            if codigo < 1 or codigo > len(produtos): # Verifica se o código é válido
                print("❌ Código inválido! Tente novamente.") # Se o código for inválido, exibe mensagem de erro
                continue
            
            # Obtém o produto e valor correspondente
            produto = produtos[codigo-1] # Ajusta o índice para 0
            valor = valores[codigo-1] # Ajusta o índice para 0
            
            # Verifica se o item já está na lista de compras
            if produto in itens_comprados: # Se o produto já foi comprado, incrementa a quantidade
                indice = itens_comprados.index(produto) # Encontra o índice do produto na lista de itens comprados
                quantidades[indice] += 1 # Incrementa a quantidade do produto e atualiza o total da compra
            else: # Se o produto não foi comprado, adiciona à lista de itens comprados e inicializa a quantidade
                itens_comprados.append(produto) # Adiciona o produto à lista de itens comprados
                quantidades.append(1) # Inicializa a quantidade como 1
            
            total_compra += valor # Atualiza o total da compra com o valor do produto
            print(f"✔ {produto} adicionado. Subtotal: R$ {total_compra:.2f}") # Exibe mensagem de sucesso com o subtotal da compra
            
        except ValueError: # Tratamento de erro para valores inválidos
            print("❌ Digite apenas números!") # Se o usuário digitar algo que não seja um número, exibe mensagem de erro

def emitir_nota_fiscal(): #função para emitir a nota fiscal da compra
    print("\n" + "=" * 50) 
    print("NOTA FISCAL".center(50)) #
    print("=" * 50)
    
    if not itens_comprados: 
        print("Nenhum item foi comprado!")
        return
    
    total = 0.0 # Variável para armazenar o total da compra
    print(f"{'Item':<20} | {'Qtd.':>5} | {'Valor Unit.':>12} | {'Total':>12}") # Cabeçalhos da tabela com alinhamento
    print("-" * 55)
    
    for item, qtd in zip(itens_comprados, quantidades): # Itera sobre os itens comprados e suas quantidades, zip combina as listas
        indice = produtos.index(item) # Encontra o índice do item na lista de produtos
        valor_unit = valores[indice] # Obtém o valor unitário do produto
        total_item = valor_unit * qtd # Calcula o total do item (valor unitário * quantidade)
        total += total_item # Atualiza o total da compra
        
        print(f"{item:<20} | {qtd:>5} | R$ {valor_unit:>10.2f} | R$ {total_item:>10.2f}") # Exibe os detalhes do item com alinhamento
    
    print("-" * 55)
    print(f"TOTAL DA COMPRA: R$ {total:>34.2f}") # Exibe o total da compra com alinhamento
    print("=" * 50)

def main(): # função principal que controla o fluxo do programa
    while True: # loop para manter o programa em execução até que o usuário decida sair
        print("\n" + "=" * 50)
        print("SISTEMA DE VENDAS".center(50)) # Exibe o título do sistema centralizado
        print("=" * 50)
        print("\n1. Cadastrar produtos") # Exibe as opções do menu
        print("2. Iniciar venda")
        print("3. Emitir nota fiscal")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ") # Solicita ao usuário que escolha uma opção do menu
        
        if opcao == '1': # Se o usuário escolher a opção 1, chama a função para cadastrar produtos
            cadastrar_produto()
        elif opcao == '2': # Se o usuário escolher a opção 2, chama a função para processar a venda
            processar_venda()
        elif opcao == '3': # Se o usuário escolher a opção 3, chama a função para emitir a nota fiscal
            emitir_nota_fiscal()
        elif opcao == '4': # Se o usuário escolher a opção 4, encerra o programa
            print("Obrigado por usar o sistema!\n\n")
            break
        else: # Se o usuário escolher uma opção inválida, exibe mensagem de erro
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    # Se sim, chama a função principal para iniciar o programa
    main()