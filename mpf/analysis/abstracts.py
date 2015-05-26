"""Provide tools for analysis."""

from mpf.models import mongo
from mpf.settings import FORCE_CACHE


__all__ = ('cache')


def cache(type_):
    """Create a decorator for caching an analysis whose type is ``type_``."""

    def decorator(func):
        """A decorator for caching the analysis ``func``."""

        def wrapper(labels, sources, settings):
            """Prepare the data for the analysis then run it and save it if
             necessary.
            """

            parents = sorted([_id for name, _id in sources.items()])
            created_ids = {}
            data = {name: mongo.data(_id) for name, _id in sources.items()}

            need_analysis = not all([
                mongo.is_analysis(type_, label, parents, settings)
                for label in labels
            ])

            if need_analysis or FORCE_CACHE:
                data = func(data, settings)

            for label in labels:
                saved = mongo.is_analysis(type_, label, parents, settings)

                if not saved:
                    _id = mongo.db.analysis.insert_one({
                        'type': type_,
                        'label': label,
                        'parents': parents,
                        'settings': settings,
                        'data': data[label],
                    }).inserted_id
                else:
                    _id = mongo.db.analysis.find_one({
                        'type': type_,
                        'label': label,
                        'parents': parents,
                        'settings': settings,
                    })['_id']

                    if FORCE_CACHE:
                        mongo.db.analysis.update({
                            '_id': _id,
                        }, {
                            '$set': {
                                'data': data[label]
                            }
                        }, upsert=False)

                created_ids[label] = _id

            return created_ids

        return wrapper
    return decorator
