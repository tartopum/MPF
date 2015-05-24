"""Test the main module."""

import matplotlib
matplotlib.use('Agg')  # Not to use X server. For TravisCI.

from mpf.main import main


def test_main():
    """Run the analysis."""

    main() # Without cache
    main() # With cache
