import random
from collections import deque

# Gera as peças (0-6)
def gerar_pecas():
    pecas = [(i, j) for i in range(7) for j in range(i, 7)]
    random.shuffle(pecas)
    return pecas

# Distribui 7 peças para cada jogador (2 jogadores)
def distribuir(pecas):
    mao1 = [pecas.pop() for _ in range(7)]
    mao2 = [pecas.pop() for _ in range(7)]
    monte = pecas  # restante é o monte (boneyard)
    return mao1, mao2, monte

# calcula soma pips de uma peça
def soma_peca(peca):
    return peca[0] + peca[1]

# encontra a peça inicial (maior duplo; se não houver duplos, maior soma)
def escolher_inicial(mao1, mao2):
    todas = [(p, 'p1') for p in mao1] + [(p, 'p2') for p in mao2]
    # prioridade: maior duplo
    duplos = [(p, who) for p, who in todas if p[0] == p[1]]
    if duplos:
        duplos.sort(key=lambda x: (x[0][0], x[0][1]), reverse=True)
        return duplos[0]  # (peca, 'p1'/'p2')
    # senão maior soma
    todas.sort(key=lambda x: soma_peca(x[0]), reverse=True)
    return todas[0]

# checa se peça é jogável nos dois lados
def jogavel(peca, mesa):
    if not mesa:
        return True
    left = mesa[0][0]
    right = mesa[-1][1]
    a, b = peca
    return a == left or b == left or a == right or b == right

# retorna lista de movimentos possíveis do jogador: (indice_na_mao, lado, peça_orientada)
# lado: 'L' ou 'R' (left/right)
def movimentos_possiveis(mao, mesa):
    moves = []
    if not mesa:
        for i, p in enumerate(mao):
            moves.append((i, 'R', p))  # quando mesa vazia, colocar como base (direita)
        return moves
    left = mesa[0][0]
    right = mesa[-1][1]
    for i, p in enumerate(mao):
        a, b = p
        # encaixa esquerda?
        if a == left:
            moves.append((i, 'L', (b, a)))  # precisa girar: colocar (b,a) pra casar
        elif b == left:
            moves.append((i, 'L', (a, b)))
        # encaixa direita?
        if a == right:
            moves.append((i, 'R', (a, b)))
        elif b == right:
            moves.append((i, 'R', (b, a)))
    return moves

# imprime estado da mesa e mão
def imprimir_estado(mao_jogador, mesa, monte, turno):
    print("\n" + "="*40)
    print(f"Monte: {len(monte)} peças | Turno: {turno}")
    print("Mesa: ", end='')
    if not mesa:
        print(" (vazia)")
    else:
        # mostra apenas extremidades e comprimento para evitar poluição
        if len(mesa) <= 7:
            print(' '.join([f"[{a}|{b}]" for a,b in mesa]))
        else:
            left_part = ' '.join([f"[{a}|{b}]" for a,b in mesa[:3]])
            right_part = ' '.join([f"[{a}|{b}]" for a,b in mesa[-3:]])
            print(f"{left_part} ... ({len(mesa)} peças) ... {right_part}")
    print("\nSua mão:")
    for i, p in enumerate(mao_jogador):
        print(f"{i}: [{p[0]}|{p[1]}]", end='   ')
    print("\n" + "="*40)

# jogada do jogador humano — recebe movimentos_possiveis para validação
def jogada_humana(mao, mesa, monte):
    moves = movimentos_possiveis(mao, mesa)
    if not moves:
        # tenta comprar até poder jogar ou monte acabar
        while True:
            if not monte:
                print("Sem movimentos e monte vazio. Você passa.")
                return False  # passou
            comprado = monte.pop()
            print(f"Você comprou: [{comprado[0]}|{comprado[1]}]")
            mao.append(comprado)
            moves = movimentos_possiveis(mao, mesa)
            if moves:
                break
        # agora há movimentos
    imprimir_estado(mao, mesa, monte, "Jogador")
    moves = movimentos_possiveis(mao, mesa)
    # mostra movimentos enumerados
    print("Movimentos possíveis:")
    mov_map = []
    for idx, (i, side, oriented) in enumerate(moves):
        mov_map.append((i, side, oriented))
        print(f"{idx}: jogar peça {i} -> lado {side} como [{oriented[0]}|{oriented[1]}]")
    print("d: comprar (se quiser) / p: passar (se não puder e monte vazio)")
    while True:
        escolha = input("Escolha o número do movimento (ou 'd' para comprar): ").strip()
        if escolha.lower() == 'd':
            if not monte:
                print("Monte vazio. Não é possível comprar.")
                continue
            comprado = monte.pop()
            print(f"Você comprou: [{comprado[0]}|{comprado[1]}]")
            mao.append(comprado)
            # atualizar lista de movimentos; se ainda não houver movimento, permite passar mais tarde
            moves = movimentos_possiveis(mao, mesa)
            if not moves:
                print("Ainda sem movimentos. Se monte vazio posteriormente, você passa.")
            else:
                return jogada_humana(mao, mesa, monte)  # reentrar para escolher
        else:
            try:
                num = int(escolha)
                if num < 0 or num >= len(mov_map):
                    print("Número inválido.")
                    continue
                i, side, oriented = mov_map[num]
                # executar jogada
                pecas_idx = i
                p_oriented = oriented
                # remover da mão: remover pela posição original i — cuidado: mao pode ter mudado se comprou
                # portanto encontrar peça p_oriented (ou a equivalente sem orientação) na mão
                # melhor: usamos index i salvo (pode falhar se a mão mudou), mas estamos em branch sem compras recentes.
                # Vamos remover a peça por valor (sem orientação) para segurança:
                # procurar peça compatível na mão (mesmo com ordem trocada)
                for j, pv in enumerate(mao):
                    if (pv == (p_oriented[0], p_oriented[1])) or (pv == (p_oriented[1], p_oriented[0])):
                        removido = mao.pop(j)
                        break
                else:
                    # fallback: pop pelo i informado se existir
                    removido = mao.pop(i)
                if side == 'L':
                    mesa.appendleft(p_oriented)
                else:
                    mesa.append(p_oriented)
                return True
            except ValueError:
                print("Entrada inválida. Digite um número ou 'd'.")

# jogada simples do CPU: escolhe movimento jogável com maior soma de pips; se não, compra até poderou passa
def jogada_cpu(mao, mesa, monte):
    moves = movimentos_possiveis(mao, mesa)
    if not moves:
        # tenta comprar até encontrar ou monte acabar
        while True:
            if not monte:
                print("CPU não tem movimentos e monte vazio. CPU passa.")
                return False
            comprado = monte.pop()
            mao.append(comprado)
            moves = movimentos_possiveis(mao, mesa)
            if moves:
                break
    # escolhe melhor movimento: maior soma peca (heurística)
    best = None
    best_score = -1
    for i, side, oriented in moves:
        score = soma_peca(oriented)
        if score > best_score:
            best_score = score
            best = (i, side, oriented)
    if best is None:
        return False
    i, side, oriented = best
    # remover peça correspondente na mão (buscar peça independente da orientação)
    for j, pv in enumerate(mao):
        if (pv == (oriented[0], oriented[1])) or (pv == (oriented[1], oriented[0])):
            removido = mao.pop(j)
            break
    else:
        removido = mao.pop(i)
    if side == 'L':
        mesa.appendleft(oriented)
    else:
        mesa.append(oriented)
    print(f"CPU jogou [{oriented[0]}|{oriented[1]}] no lado {side}")
    return True

# calcula soma de pips da mão
def soma_mao(mao):
    return sum(soma_peca(p) for p in mao)

# checa se o jogo está bloqueado: nenhum jogador tem movimento e monte vazio
def bloqueado(mao1, mao2, mesa, monte):
    if monte:
        return False
    m1 = movimentos_possiveis(mao1, mesa)
    m2 = movimentos_possiveis(mao2, mesa)
    return (not m1) and (not m2)

# função principal do jogo
def jogar_domino():
    pecas = gerar_pecas()
    mao_jogador, mao_cpu, monte = distribuir(pecas)

    # escolher inicial
    inicial, dono = escolher_inicial(mao_jogador, mao_cpu)
    peca_inicial = inicial
    print(f"Peça inicial selecionada: [{peca_inicial[0]}|{peca_inicial[1]}] do {dono}")
    # remover da mão do dono a peça inicial
    if dono == 'p1':
        for i, p in enumerate(mao_jogador):
            if p == peca_inicial:
                mao_jogador.pop(i); break
        mesa = deque([peca_inicial])
        turno = 'cpu'  # o outro joga depois
    else:
        for i, p in enumerate(mao_cpu):
            if p == peca_inicial:
                mao_cpu.pop(i); break
        mesa = deque([peca_inicial])
        turno = 'jogador'

    # loop principal
    while True:
        # verificar vitória por esvaziamento
        if not mao_jogador:
            print("Você esvaziou a mão — você venceu!")
            return
        if not mao_cpu:
            print("CPU esvaziou a mão — CPU venceu!")
            return

        # verificar bloqueio
        if bloqueado(mao_jogador, mao_cpu, mesa, monte):
            print("Jogo bloqueado! Calculando vencedor por soma de pips...")
            s1 = soma_mao(mao_jogador)
            s2 = soma_mao(mao_cpu)
            print(f"Soma suas peças: {s1} | Soma CPU: {s2}")
            if s1 < s2:
                print("Você venceu por menor soma de pips!")
            elif s2 < s1:
                print("CPU venceu por menor soma de pips!")
            else:
                print("Empate técnico!")
            return

        if turno == 'jogador':
            imprimir_estado(mao_jogador, mesa, monte, "Jogador")
            played = jogada_humana(mao_jogador, mesa, monte)
            turno = 'cpu'
        else:
            print("\nTurno da CPU...")
            played = jogada_cpu(mao_cpu, mesa, monte)
            turno = 'jogador'

# inicia jogo
if __name__ == "__main__":
    print("Bem-vindo ao Dominó (versão console) — Você vs CPU")
    print("Regras básicas implementadas: compra do monte, bloqueio, vitória por esvaziamento ou menor soma de pips.")
    jogar_domino()
