"""Provide tools for analysis."""

from mpf.models import mongo
from mpf.settings import FORCE_CACHE


__all__ = ('cache')


def cache(type_):
    """Create a decorator for caching an analysis whose type is ``type_``."""

    def decorator(func):
        """A decorator for caching the analysis ``func``."""

        def wrapper(settings, sources):
            """Prepare the data for the analysis then run it and save it if
             necessary.
            """

            parents = sorted([_id for name, _id in sources.items()])
            created_ids = {}
            data = {name: mongo.data(_id) for name, _id in sources.items()}

            need_analysis = not all([
                mongo.is_analysis(type_, label, parents, stg)
                for label, stg in settings.items()
            ])

            if need_analysis or FORCE_CACHE:
                data = func(data, settings)

            for label, stg in settings.items():
                saved = mongo.is_analysis(type_, label, parents, stg)

                if not saved:
                    _id = mongo.db.analysis.insert_one({
                        'type': type_,
                        'label': label,
                        'parents': parents,
                        'settings': stg,
                        'data': data[label],
                    }).inserted_id
                else:
                    _id = mongo.db.analysis.find_one({
                        'type': type_,
                        'label': label,
                        'parents': parents,
                        'settings': stg,
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
