import matplotlib
matplotlib.use('Agg')  # Not to use X server. For TravisCI.

from mpf.main import main



def test_main():
    main() # Without cache
    main() # With cache
