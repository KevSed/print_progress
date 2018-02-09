import sys


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(iteration=0)
def print_progress(total, prefix='', suffix='', decimals=1, bar_length=50,
                   fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent
        bar_length  - Optional  : character length of bar (Int)
    """

    print_progress.iteration += 1
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (print_progress.iteration /
                                        float(total)))
    filled_length = int(round(bar_length * print_progress.iteration /
                              float(total)))
    bar = fill * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%',
                                            suffix)),

    if print_progress.iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

    return
