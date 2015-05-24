"""The starting point of the code. Run it to make the analysis work."""

from mpf import analysis
from mpf import views
from mpf import settings as stg 


def main():
    """Launch the analysis."""

    for cow in stg.model.cows():
        analysis.MovingAveraging(step=2).work(cow)
        views.Crude().render(cow)


if __name__ == '__main__':
    main()
