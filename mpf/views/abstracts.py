"""Classes to be inherited by any view."""

import os

import matplotlib.pyplot as plt
import pylatex

import mpf.settings as stg


__all__ = ('View')


class View:
    """Provide a basic asbtract interface for views."""

    DATE_LABEL = "Date"
    DAY_LABEL = "Day"
    EXT = 'pdf'
    PROD_LABEL = "Production (L)"

    def __init__(self, relpath):
        """
        :param relpath: The relative path of the view.
        :type relpath: str
        """

        self.path_pattern = os.path.join(stg.VIEWS_DIR, relpath, '{}')
        self.title = ''
        self.cow = -1
        self.doc = None

    def add_plot(self, fig=None):
        """Add a plot to the view."""

        fig = fig or plt

        self.doc.append(pylatex.command.Command('nobreak'))

        with self.doc.create(pylatex.Plt(position="H")) as plot:
            plot.add_plot(fig, width=r'\textwidth')

    def create(self):
        """Create the LaTeX document.

        :return: ``True`` if the document can have been created, else
        ``False``.
        :rtype: bool
        """

        path = self.path_pattern.format(self.cow)
        dirname = os.path.dirname(path)

        if not os.path.isdir(dirname):
            os.makedirs(dirname)

        if (os.path.isfile("{}.{}".format(path, self.EXT)) and
                not stg.FORCE_VIEW):
            return False

        self.doc = pylatex.Document(
            path, 
            title="Cow {} - {}".format(self.cow, self.title), 
            maketitle=True
        )

        self.doc.packages.append(pylatex.Package('geometry', options=[
            'left=1cm', 'right=1cm', 'top=1cm', 'bottom=1cm']))
        self.doc.packages.append(pylatex.Package('float'))
        self.doc.append(pylatex.command.Command('pagenumbering', 'gobble'))

        return True

    def generate(self):
        """Generate the view.

        :raise: NotImplementedError
        """

        raise NotImplementedError('The `generate` method must be overridden.')

    def render(self, *args, **kwargs):
        """Generate and save the view."""

        if self.create():
            self.generate(*args, **kwargs)
            self.save()

    def save(self):
        """Save the document as a PDF file."""

        self.doc.generate_pdf()
