import random
from Othello import Othello
from Stone import Stone
from MLP import MLP_p
import numpy as np

class population():
    def __init__(self,individual):
        self.individual = individual
        self.score = 0
    def printt(self):
        print(self.individual)
        print(self.count)
    def score_reset(self):
        self.score = 0

def select_elite(gas, elite_length):
    sort_individual_list = sorted(gas, key=lambda u: u.score, reverse=True)
    elite, other = sort_individual_list[:elite_length], sort_individual_list[elite_length:]
    return elite, other

def roulette_def(gas, roulette_length):
    total = 0
    roulette_list = []
    for ga in gas:
        total += ga.score
    for i in range(roulette_length):
        Vsum = 0
        arrow = random.randint(0,total-1)
        for j in gas:
            Vsum += j.score
            if Vsum > arrow:
                roulette_list.append(j)
                total = total - j.score
                gas.remove(j)
                break
    return roulette_list

def crossover(ga_one,ga_second):
    genom_list = []
    cross_one = random.randint( 0, len(ga_one.individual) )
    cross_second = random.randint( cross_one, len(ga_one.individual) )
    one = ga_one.individual
    second = ga_second.individual
    progeny_one = np.concatenate([one[:cross_one],second[cross_one:cross_second],one[cross_second:]])
    progeny_second = np.concatenate([second[:cross_one],one[cross_one:cross_second],second[cross_second:]])

    genom_list.append(population(progeny_one))
    genom_list.append(population(progeny_second))
    return genom_list

def mutation(ga,individual_mutation,genom_mutation):
    ga_list = []
    for i in ga:
        if individual_mutation > (random.randint(0, 100) / 100.0):
            genom_list = []
            for i_ in i.individual:
                if genom_mutation > (random.randint(0, 100) / 100.0):
                    genom_list.append(np.random.normal(0.0,1.0))
                else:
                    genom_list.append(i_)
            ga_list.append(population(genom_list))
        else:
            ga_list.append(i)
    return ga_list

def get_player(mode,name,color,bord=None):
    if color == 'black':
        player = MLP_p(Stone("●"),name,bord)
    else:
        player = MLP_p(Stone("○"),name,bord)
    return player

if __name__ == '__main__':
	#  何世代まで
    GENERATIONS = 100
    #  個体数
    POPULATION_LIST = 50
    #  遺伝子の数
    GENE_COUNT = 180
    #  エリート方式で選択される遺伝子の数
    RANKING = 2
    #  ルーレット方式で選択される遺伝子の数
    ROULETTE = 16
    #  エリート同士の数
    SON_ELITE = 2
    #  現世代個体集団とエリート集団を使った子孫
    SON_CURRENT_ALL = 30
    # 個体突然変異確率
    INDIVIDUAL_MUTATION = 0.2
    # 遺伝子突然変異確率
    GENOM_MUTATION = 0.2

    file_name = './result_6.txt'
    f_write = open(file_name,'w')
    count = 0
    individual = []
    current_generation_individual_group = []
    for i in range(POPULATION_LIST):
        current_generation_individual_group.append(population(np.random.normal(0.0,1.0,(GENE_COUNT))))

    for generation in range(GENERATIONS):
        print(count)
        # オセロ盤の評価
        for i in current_generation_individual_group:
            for j in current_generation_individual_group:
                if i == j:
                    continue
                else:
                    player1 = get_player('MLP','P1','black',i.individual)
                    player2 = get_player('MLP','P2','white',j.individual)
                    FirstMove, SecondMove = Othello().play(player1,player2)
                    i.score += FirstMove
                    j.score += SecondMove
        # エリート選択とルーレット選択
        elite, other = select_elite(current_generation_individual_group,RANKING)
        roulette = roulette_def(other,ROULETTE)
        next_list = elite + roulette

        print("\n-----第 "+str(generation+1)+" 世代の結果-----")
        print("   First: "+str(elite[0].score)+"  "+str(elite[0].individual))
        print("  Second: "+str(elite[1].score)+"  "+str(elite[1].individual))
        print("   Third: "+str(other[0].score)+"  "+str(other[0].individual))
        print("     MIN: "+str(other[-1].score)+"  "+str(other[-1].individual))

        print("\n-----第 "+str(generation+1)+" 世代の結果-----",file=f_write)
        print("   First: "+str(elite[0].score)+"  "+str(elite[0].individual),file=f_write)
        print("  Second: "+str(elite[1].score)+"  "+str(elite[1].individual),file=f_write)
        print("   Third: "+str(other[0].score)+"  "+str(other[0].individual),file=f_write)
        print("     MIN: "+str(other[-1].score)+"  "+str(other[-1].individual),file=f_write)

        # エリート同士の交配
        gene_count = [ i for i in range(len(elite))]
        for i in range(int(SON_ELITE/2)):
            select_list = random.sample(gene_count,2)
            next_list.extend(crossover(elite[select_list[0]],elite[select_list[1]]))

        # 引き継がれる個体同士の交配
        gene_count = [ i for i in range(len(next_list))]
        for i in range(int(SON_CURRENT_ALL/2)):
            select_list = random.sample(gene_count,2)
            next_list.extend(crossover(next_list[select_list[0]],next_list[select_list[1]]))

        current_generation_individual_group = mutation(next_list,INDIVIDUAL_MUTATION,GENOM_MUTATION)
        for ga in current_generation_individual_group:
            ga.score_reset()
     
        count += 1













