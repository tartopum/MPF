from mpf import analysis
# from mpf import views
from mpf import tools


def main():
    for cow in tools.db.cows():
        analysis.MovingAveraging(step=2).work(cow)
        break


if __name__ == '__main__':
    main()
