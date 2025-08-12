import random
import time
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass

class ArcanoTier(Enum):
    FUNDAMENTAL = 1
    INTERMEDIARIO = 2
    SUPREMO = 3

@dataclass
class ArcanoCard:
    name: str
    japanese_name: str
    number: int
    tier: ArcanoTier
    energy_cost: int
    cooldown: int
    duration: int
    description: str
    effect_power: int
    risk_level: int  # 0-10, onde 10 é muito arriscado

class ArcanoRuina:
    def __init__(self, user_name: str = "Akira Yamamoto"):
        self.user_name = user_name
        self.max_energy = 1000
        self.current_energy = 1000
        self.health = 100
        self.cards_on_cooldown = {}
        self.active_effects = {}
        self.battle_log = []
        self.cards_destroyed = []  # Para sacrifícios
        
        # Inicializar baralho
        self.deck = self._create_deck()
        
        # Status do usuário
        self.level = 1  # 1=Iniciante, 2=Experiente, 3=Mestre
        self.can_combine = False
        self.max_combinations = 1
        
    def _create_deck(self) -> Dict[int, ArcanoCard]:
        """Cria o baralho completo com os 22 Arcanos Maiores"""
        cards = {
            0: ArcanoCard("O Louco", "愚者", 0, ArcanoTier.FUNDAMENTAL, 50, 120, 30, 
                         "Campo aleatório onde leis físicas são distorcidas", 60, 8),
            
            1: ArcanoCard("O Mago", "魔術師", 1, ArcanoTier.FUNDAMENTAL, 40, 60, 10, 
                         "Amplifica próxima técnica em 200%", 70, 2),
            
            2: ArcanoCard("A Sacerdotisa", "女教皇", 2, ArcanoTier.FUNDAMENTAL, 45, 90, 15, 
                         "Barreira que bloqueia técnicas amaldiçoadas", 65, 1),
            
            3: ArcanoCard("A Imperatriz", "女帝", 3, ArcanoTier.FUNDAMENTAL, 50, 180, 10, 
                         "Regenera ferimentos do usuário e aliados", 55, 0),
            
            4: ArcanoCard("O Imperador", "皇帝", 4, ArcanoTier.FUNDAMENTAL, 55, 120, 20, 
                         "Cria decretos que inimigos devem obedecer", 60, 3),
            
            5: ArcanoCard("O Hierofante", "法王", 5, ArcanoTier.FUNDAMENTAL, 35, 0, 0, 
                         "Revela técnica e fraquezas do oponente", 40, 0),
            
            6: ArcanoCard("Os Amantes", "恋人", 6, ArcanoTier.FUNDAMENTAL, 50, 150, 60, 
                         "Conecta dois alvos, dividindo dano igualmente", 45, 4),
            
            7: ArcanoCard("A Carruagem", "戦車", 7, ArcanoTier.FUNDAMENTAL, 60, 180, 45, 
                         "Aumenta velocidade 300% e imunidade a controle", 75, 1),
            
            8: ArcanoCard("A Força", "力", 8, ArcanoTier.INTERMEDIARIO, 80, 240, 60, 
                         "Multiplica força física por 5x", 85, 2),
            
            9: ArcanoCard("O Eremita", "隠者", 9, ArcanoTier.INTERMEDIARIO, 75, 300, 120, 
                         "Invisibilidade e indetectabilidade completa", 70, 3),
            
            10: ArcanoCard("Roda da Fortuna", "運命の輪", 10, ArcanoTier.INTERMEDIARIO, 100, 600, 30, 
                          "Efeito aleatório extremamente poderoso", 95, 9),
            
            11: ArcanoCard("A Justiça", "正義", 11, ArcanoTier.INTERMEDIARIO, 90, 360, 60, 
                          "Reflete 150% do dano recebido", 80, 5),
            
            12: ArcanoCard("O Enforcado", "吊られた男", 12, ArcanoTier.INTERMEDIARIO, 70, 240, 60, 
                          "Inverte todos os sentidos do inimigo", 75, 2),
            
            13: ArcanoCard("A Morte", "死神", 13, ArcanoTier.INTERMEDIARIO, 120, 480, 45, 
                          "Acelera o fim das coisas em área", 90, 4),
            
            14: ArcanoCard("A Temperança", "節制", 14, ArcanoTier.INTERMEDIARIO, 100, 420, 0, 
                          "Cancela técnicas extremas e equilibra energias", 85, 1),
            
            15: ArcanoCard("O Diabo", "悪魔", 15, ArcanoTier.SUPREMO, 150, 720, 120, 
                          "Corrompe energia amaldiçoada dos inimigos", 95, 6),
            
            16: ArcanoCard("A Torre", "塔", 16, ArcanoTier.SUPREMO, 160, 900, 0, 
                          "Colapso total em 15 metros de raio", 100, 7),
            
            17: ArcanoCard("A Estrela", "星", 17, ArcanoTier.SUPREMO, 200, 1440, 60, 
                          "Sorte absoluta por 1 minuto", 100, 0),
            
            18: ArcanoCard("A Lua", "月", 18, ArcanoTier.SUPREMO, 180, 1200, 180, 
                          "Ilusões que se tornam temporariamente reais", 90, 5),
            
            19: ArcanoCard("O Sol", "太陽", 19, ArcanoTier.SUPREMO, 190, 1800, 120, 
                          "Purifica área e revela inimigos ocultos", 95, 0),
            
            20: ArcanoCard("O Julgamento", "審判", 20, ArcanoTier.SUPREMO, 250, 0, 0, 
                          "Julga inimigo baseado em ações passadas", 100, 3),
            
            21: ArcanoCard("O Mundo", "世界", 21, ArcanoTier.SUPREMO, 300, 10080, 30, 
                          "Reescreve regras da realidade local", 100, 2)
        }
        return cards
    
    def get_available_cards(self) -> List[ArcanoCard]:
        """Retorna cartas disponíveis baseado no nível do usuário"""
        available = []
        max_number = 7 if self.level == 1 else (14 if self.level == 2 else 21)
        
        for num, card in self.deck.items():
            if (num <= max_number and 
                num not in self.cards_on_cooldown and 
                num not in self.cards_destroyed and
                self.current_energy >= card.energy_cost):
                available.append(card)
        
        return available
    
    def use_card(self, card_number: int, target: str = "enemy") -> Tuple[bool, str]:
        """Usa uma carta específica"""
        if card_number not in self.deck:
            return False, "Carta não existe no baralho!"
        
        card = self.deck[card_number]
        
        # Verificações
        if card_number in self.cards_destroyed:
            return False, f"A carta {card.name} foi sacrificada e não pode ser usada!"
        
        if card_number in self.cards_on_cooldown:
            remaining = self.cards_on_cooldown[card_number]
            return False, f"Carta {card.name} ainda em cooldown por {remaining} segundos!"
        
        if self.current_energy < card.energy_cost:
            return False, f"Energia insuficiente! Necessário: {card.energy_cost}, Atual: {self.current_energy}"
        
        # Verificar nível de acesso
        max_number = 7 if self.level == 1 else (14 if self.level == 2 else 21)
        if card_number > max_number:
            return False, f"Nível insuficiente para usar {card.name}!"
        
        # Usar carta
        self.current_energy -= card.energy_cost
        if card.cooldown > 0:
            self.cards_on_cooldown[card_number] = card.cooldown
        
        # Efeito especial da carta
        result = self._apply_card_effect(card, target)
        
        # Log da batalha
        self.battle_log.append(f"🃏 {self.user_name} usou {card.name} ({card.japanese_name})")
        self.battle_log.append(f"   {result}")
        
        return True, result
    
    def _apply_card_effect(self, card: ArcanoCard, target: str) -> str:
        """Aplica o efeito específico de cada carta"""
        effects = {
            0: self._effect_louco,
            1: self._effect_mago,
            2: self._effect_sacerdotisa,
            3: self._effect_imperatriz,
            4: self._effect_imperador,
            5: self._effect_hierofante,
            6: self._effect_amantes,
            7: self._effect_carruagem,
            8: self._effect_forca,
            9: self._effect_eremita,
            10: self._effect_roda_fortuna,
            11: self._effect_justica,
            12: self._effect_enforcado,
            13: self._effect_morte,
            14: self._effect_temperanca,
            15: self._effect_diabo,
            16: self._effect_torre,
            17: self._effect_estrela,
            18: self._effect_lua,
            19: self._effect_sol,
            20: self._effect_julgamento,
            21: self._effect_mundo
        }
        
        if card.duration > 0:
            self.active_effects[card.number] = {
                'duration': card.duration,
                'power': card.effect_power,
                'name': card.name
            }
        
        return effects[card.number](target)
    
    def _effect_louco(self, target: str) -> str:
        chaos_events = [
            "Gravidade se inverte aleatoriamente!",
            "Tempo flui em câmera lenta por alguns segundos!",
            "Ataques ricocheteiam em direções impossíveis!",
            "O ar se torna sólido temporariamente!",
            "Cores começam a fazer barulho!"
        ]
        event = random.choice(chaos_events)
        # Risco: 30% de chance de afetar o usuário também
        if random.random() < 0.3:
            damage = random.randint(5, 15)
            self.health -= damage
            return f"CAOS ATIVADO: {event} (Você também foi afetado! -{damage} HP)"
        return f"CAOS ATIVADO: {event}"
    
    def _effect_mago(self, target: str) -> str:
        return "✨ Próxima técnica terá poder amplificado em 200%! Energia mágica flui intensamente!"
    
    def _effect_sacerdotisa(self, target: str) -> str:
        return "🛡️ Barreira espiritual ativa! Técnicas amaldiçoadas bloqueadas por 15 segundos!"
    
    def _effect_imperatriz(self, target: str) -> str:
        heal_amount = random.randint(15, 30)
        self.health = min(100, self.health + heal_amount)
        return f"💚 Energia curativa restaura {heal_amount} HP! Ferimentos se fecham rapidamente!"
    
    def _effect_imperador(self, target: str) -> str:
        commands = [
            "PARE DE SE MOVER!",
            "LARGUE SUA ARMA!",
            "RECUE 10 PASSOS!",
            "FECHE OS OLHOS!",
            "NÃO USE TÉCNICAS POR 10 SEGUNDOS!"
        ]
        command = random.choice(commands)
        return f"👑 DECRETO IMPERIAL: '{command}' - O inimigo deve obedecer!"
    
    def _effect_hierofante(self, target: str) -> str:
        revelations = [
            "Técnica principal: Manipulação Sombria",
            "Fraqueza: Ataques de luz",
            "Próximo movimento: Ataque pela esquerda",
            "Ponto fraco: Articulação do joelho direito",
            "Reserva de energia: 60% restante"
        ]
        revelation = random.choice(revelations)
        return f"👁️ REVELAÇÃO MÍSTICA: {revelation}"
    
    def _effect_amantes(self, target: str) -> str:
        return f"💕 CONEXÃO ESTABELECIDA: Dano será dividido igualmente entre os alvos conectados!"
    
    def _effect_carruagem(self, target: str) -> str:
        return "🏃‍♂️ VELOCIDADE SUPREMA: Movimento 300% mais rápido! Imune a efeitos de controle!"
    
    def _effect_forca(self, target: str) -> str:
        return "💪 FORÇA TITÂNICA: Poder físico multiplicado por 5x! Pode quebrar barreiras de energia!"
    
    def _effect_eremita(self, target: str) -> str:
        return "👻 INVISIBILIDADE TOTAL: Completamente indetectável por 2 minutos!"
    
    def _effect_roda_fortuna(self, target: str) -> str:
        outcomes = [
            ("🎰 JACKPOT! Energia infinita por 30 segundos!", 100),
            ("🎰 SORTE EXTREMA! Próximos 3 ataques são críticos!", 90),
            ("🎰 TELETRANSPORTE! Pode se mover instantaneamente!", 85),
            ("🎰 ESCUDO MÁGICO! Invencível por 15 segundos!", 95),
            ("🎰 REGENERAÇÃO! HP restaurado completamente!", 80),
            ("💥 AZAR! Você tropeça e perde o turno!", -20),  # 10% chance de azar
        ]
        
        # 90% chance de efeito positivo, 10% negativo
        if random.random() < 0.9:
            outcome = random.choice([o for o in outcomes if o[1] > 0])
        else:
            outcome = outcomes[-1]  # Efeito de azar
        
        if outcome[1] < 0:
            self.health += outcome[1]
        
        return outcome[0]
    
    def _effect_justica(self, target: str) -> str:
        return "⚖️ JUSTIÇA ATIVA: Todo dano recebido será refletido como 150% de volta!"
    
    def _effect_enforcado(self, target: str) -> str:
        return "🔄 INVERSÃO TOTAL: Todos os sentidos do inimigo estão invertidos! Confusão máxima!"
    
    def _effect_morte(self, target: str) -> str:
        decay_effects = [
            "Armas do inimigo começam a enferrujar rapidamente!",
            "O chão sob os pés do inimigo começa a rachar!",
            "Ferimentos do inimigo se agravam e não cicatrizam!",
            "Energia amaldiçoada do inimigo se dissipa lentamente!"
        ]
        return f"💀 DECADÊNCIA ACELERADA: {random.choice(decay_effects)}"
    
    def _effect_temperanca(self, target: str) -> str:
        return "⚖️ EQUILÍBRIO RESTAURADO: Todas as técnicas extremas são canceladas! Harmonia no campo!"
    
    def _effect_diabo(self, target: str) -> str:
        return "😈 CORRUPÇÃO SOMBRIA: Energia amaldiçoada do inimigo corrompida! Técnicas podem falhar!"
    
    def _effect_torre(self, target: str) -> str:
        destruction = [
            "Edifícios ao redor desmoronam completamente!",
            "O chão racha formando crateras profundas!",
            "Estruturas metálicas se dobram e quebram!",
            "Até o ar parece pesado e opressor!"
        ]
        return f"🏗️ COLAPSO TOTAL: {random.choice(destruction)}"
    
    def _effect_estrela(self, target: str) -> str:
        return "⭐ SORTE ABSOLUTA: Todos os seus ataques acertarão pontos vitais! Esquivas perfeitas!"
    
    def _effect_lua(self, target: str) -> str:
        illusions = [
            "Criou 5 clones perfeitos de si mesmo!",
            "O campo de batalha parece um labirinto infinito!",
            "Inimigos veem seus piores medos materializados!",
            "A realidade e ilusão se misturam completamente!"
        ]
        return f"🌙 ILUSÃO SUPREMA: {random.choice(illusions)}"
    
    def _effect_sol(self, target: str) -> str:
        self.health = min(100, self.health + 25)
        return "☀️ PURIFICAÇÃO SOLAR: Área purificada! +25 HP! Inimigos ocultos revelados!"
    
    def _effect_julgamento(self, target: str) -> str:
        judgments = [
            "CULPADO de assassinato! Maldição da dor eterna!",
            "CULPADO de traição! Técnicas falham por 2 minutos!",
            "CULPADO de ganância! Energia constantemente drenada!",
            "INOCENTE! Nenhum efeito negativo aplicado."
        ]
        judgment = random.choice(judgments)
        return f"⚖️ JULGAMENTO FINAL: {judgment}"
    
    def _effect_mundo(self, target: str) -> str:
        reality_changes = [
            "Gravidade agora é 0.5x para todos, incluindo você!",
            "Tempo desacelera para todos, exceto você!",
            "Regras da física se alteram: magias têm dano dobrado!",
            "Terreno muda constantemente durante a luta!"
        ]
        return f"🌍 MUNDO REESCRITO: {random.choice(reality_changes)}"
    
    def sacrifice_card(self, card1: int, card2: int) -> Tuple[bool, str]:
        """Sacrifica duas cartas para destruição e benefício de outras cartas"""
        if card1 not in self.deck or card2 not in self.deck:
            return False, "Uma ou ambas as cartas não existem!"
        if card1 == card2:
            return False, "Você precisa escolher duas cartas diferentes para sacrificar!"
        if card1 in self.cards_destroyed or card2 in self.cards_destroyed:
            return False, "Uma das cartas já foi sacrificada!"
        # Remove as cartas sacrificadas do baralho
        self.cards_destroyed.extend([card1, card2])
        # Aumenta energia máxima e atual como benefício
        self.max_energy += 200
        self.current_energy += 200
        # Talvez libere combos
        self.can_combine = True
        self.max_combinations += 1
        
        return True, (f"Cartas {self.deck[card1].name} e {self.deck[card2].name} sacrificadas! "
                      f"Energia máxima aumentada! Combinações liberadas.")
    
    def update_cooldowns(self, seconds: int) -> List[str]:
        """Atualiza o cooldown das cartas usadas"""
        ready_cards = []
        for card_num in list(self.cards_on_cooldown.keys()):
            self.cards_on_cooldown[card_num] -= seconds
            if self.cards_on_cooldown[card_num] <= 0:
                ready_cards.append(self.deck[card_num].name)
                del self.cards_on_cooldown[card_num]
        return ready_cards
    
    def level_up(self) -> str:
        """Sobe o nível do usuário para liberar cartas"""
        if self.level < 3:
            self.level += 1
            return f"🔺 Nível aumentado para {self.level}! Mais cartas liberadas!"
        else:
            return "⭐ Você já atingiu o nível máximo!"
    
    def activate_domain_expansion(self) -> Tuple[bool, str]:
        """Ativa a Expansão de Domínio, carta final do baralho"""
        if self.level < 3:
            return False, "Nível insuficiente para ativar a Expansão de Domínio!"
        if 21 in self.cards_on_cooldown:
            return False, "Expansão de Domínio está em cooldown!"
        if self.current_energy < self.deck[21].energy_cost:
            return False, "Energia insuficiente para ativar a Expansão de Domínio!"
        
        self.current_energy -= self.deck[21].energy_cost
        self.cards_on_cooldown[21] = self.deck[21].cooldown
        # Efeito especial e destrutivo
        self.battle_log.append(f"🌌 {self.user_name} ativou a Expansão de Domínio: {self.deck[21].name}!")
        return True, ("🌌 Expansão de Domínio ativada! As regras da realidade local foram reescritas. "
                      "Inimigos enfraquecidos e aliados fortalecidos!")
    
def simulate_battle():
    print("=== Simulação de batalha iniciada ===")
    akira = ArcanoRuina()
    turn = 1
    
    while akira.health > 0 and turn <= 10:
        print(f"\n--- Turno {turn} ---")
        available = akira.get_available_cards()
        if not available:
            print("Sem cartas disponíveis para usar no momento...")
            akira.update_cooldowns(10)
            akira.current_energy = min(akira.max_energy, akira.current_energy + 100)
            print(f"Energia restaurada para {akira.current_energy}/{akira.max_energy}")
            turn += 1
            continue
        
        card = random.choice(available)
        success, message = akira.use_card(card.number)
        if success:
            print(f"Usando carta: {card.name} ({card.japanese_name})")
            print(message)
        else:
            print(f"Falha ao usar carta: {message}")
        
        # Atualizar cooldown e energia por turno
        ready = akira.update_cooldowns(10)
        if ready:
            print(f"Cartas saíram do cooldown: {', '.join(ready)}")
        
        akira.current_energy = min(akira.max_energy, akira.current_energy + 150)
        print(f"Energia atual: {akira.current_energy}/{akira.max_energy}")
        print(f"Vida atual: {akira.health}")
        
        turn += 1
    
    print("\n=== Simulação de batalha finalizada ===")
    print("Logs da batalha:")
    for log in akira.battle_log:
        print(log)
    
def interactive_mode():
    akira = ArcanoRuina()
    
    print("Modo interativo de uso de cartas iniciado.")
    print("Digite 'help' para ver os comandos disponíveis.")
    
    while True:
        try:
            command = input("\nDigite comando: ").strip().lower()
            if command == 'help':
                print("""
Comandos disponíveis:
- use <número da carta> : usa a carta pelo número
- sacrifice <número1> <número2> : sacrifica duas cartas
- domain : ativa a Expansão de Domínio
- levelup : sobe o nível do usuário
- cooldown <segundos> : avança o tempo para reduzir cooldowns
- status : mostra energia, vida, nível e cartas destruídas
- deck : lista cartas disponíveis para uso
- exit : sai do modo interativo
                """)
            elif command == 'exit':
                print("Saindo do modo interativo...")
                break
            elif command == 'status':
                print(f"Nome: {akira.user_name}")
                print(f"Nível: {akira.level}")
                print(f"Vida: {akira.health}")
                print(f"Energia: {akira.current_energy}/{akira.max_energy}")
                print(f"Cartas sacrificadas: {[akira.deck[n].name for n in akira.cards_destroyed]}")
                print(f"Cartas em cooldown: {[akira.deck[n].name for n in akira.cards_on_cooldown.keys()]}")
                print(f"Cartas disponíveis para uso: {[c.name for c in akira.get_available_cards()]}")
            elif command == 'deck':
                print("Cartas disponíveis para uso:")
                for card in akira.get_available_cards():
                    print(f"{card.number}: {card.name} ({card.japanese_name}) - Custo: {card.energy_cost} Energia")
            elif command.startswith('use '):
                try:
                    card_number = int(command.split()[1])
                    success, result = akira.use_card(card_number)
                    if success:
                        print(f"✅ {result}")
                    else:
                        print(f"❌ {result}")
                except ValueError:
                    print("⚠️ Número de carta inválido!")
            elif command.startswith('sacrifice '):
                try:
                    parts = command.split()
                    card1 = int(parts[1])
                    card2 = int(parts[2])
                    success, result = akira.sacrifice_card(card1, card2)
                    if success:
                        print(f"✅ {result}")
                    else:
                        print(f"❌ {result}")
                except (ValueError, IndexError):
                    print("⚠️ Uso correto: sacrifice <carta1> <carta2>")
            elif command == 'domain':
                success, result = akira.activate_domain_expansion()
                if success:
                    print(f"✅ {result}")
                else:
                    print(f"❌ {result}")
            elif command == 'levelup':
                print(akira.level_up())
            elif command.startswith('cooldown '):
                try:
                    seconds = int(command.split()[1])
                    ready_cards = akira.update_cooldowns(seconds)
                    if ready_cards:
                        print(f"⏰ Cartas prontas: {', '.join(ready_cards)}")
                    else:
                        print("⏱️ Nenhuma carta ficou pronta ainda.")
                except ValueError:
                    print("⚠️ Uso correto: cooldown <segundos>")
            elif command == 'battle':
                simulate_battle()
            else:
                print("❌ Comando não reconhecido! Digite 'help' para ver as opções.")
        except KeyboardInterrupt:
            print("\n👋 Saindo do modo interativo...")
            break

if __name__ == "__main__":
    print("Escolha o modo de execução:")
    print("1 - Simulação de batalha")
    print("2 - Modo interativo")
    choice = input("Digite 1 ou 2: ").strip()
    if choice == "1":
        simulate_battle()
    else:
        interactive_mode()
