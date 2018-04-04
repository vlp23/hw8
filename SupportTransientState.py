import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of Return from the games
    return_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward (dollars) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          return_mean_PI_text)


def draw_histograms(multi_cohort_UnfairCoin, multi_cohort_FairCoin):
    """ draws the histograms of average survival time
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # histograms of average survival times
    set_of_survival_times = [
        multi_cohort_UnfairCoin.get_mean_total_reward(),
        multi_cohort_FairCoin.get_mean_total_reward()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of average patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=1,
        legend=['No Drug', 'With Drug'],
        transparency=0.5,
        x_range=[6, 20]
    )


def print_comparative_outcomes(multi_cohort_UnfairCoin, multi_cohort_FairCoin):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean survival time',
        x=multi_cohort_UnfairCoin.get_mean_total_reward(),
        y_ref=multi_cohort_FairCoin.get_mean_total_reward()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean survival time (years) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

