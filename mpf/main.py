"""The starting point of the code. Run it to make the analysis work."""

from mpf import analysis
# from mpf import views
from mpf import tools


def main():
    """Launch the analysis."""

    for cow in tools.db.cows():
        analysis.MovingAveraging(step=2).work(cow)


if __name__ == '__main__':
    main()
