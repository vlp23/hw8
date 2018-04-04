#Problem2

import Parameters as P
import CoinModel as Cls
import SupportTransientState as Support

# create multiple cohorts for when the coin is unfair
multiCohortUnfair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.MORTALITY_PROB]*P.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortUnfair.simulation()

# create multiple cohorts for when the Coin is fair
multiCohortFair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.DRUG_EFFECT_RATIO]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortFair.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiCohortUnfair, 'When coin is unfair:')
Support.print_outcomes(multiCohortFair, 'When coin is fair:')

# print comparative outcomes
Support.print_comparative_outcomes(multiCohortUnfair, multiCohortFair)
