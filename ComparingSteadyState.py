#Problem1
import Parameters as P
import CoinModel as Cls
import SupportSteadyState as Support

# create a cohort of patients for when the coin is unfair(when probheads is .45)
cohortUnfair = Cls.SetOfGames(
    id=1,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.MORTALITY_PROB)
# simulate the cohort
UnfairCoin = cohortUnfair.simulation()

# create a cohort of patients for when the coin is fair (when probheads is .5)
cohortFair = Cls.SetOfGames(
    id=2,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.DRUG_EFFECT_RATIO)
# simulate the cohort
FairCoin = cohortFair.simulation()

# print outcomes of each cohort
Support.print_outcomes(UnfairCoin, 'When Coin is Unfair:')
Support.print_outcomes(FairCoin, 'When Coin is Fair:')


# print comparative outcomes
Support.print_comparative_outcomes(UnfairCoin, FairCoin)
