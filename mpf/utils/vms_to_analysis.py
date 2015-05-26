from mpf.settings import mongo, TYPES, LABELS


def main():
    for cow in mongo.cows():
        type_ = TYPES['identity']
        label = LABELS['prods']
        parents = []
        settings = {'cow': cow}

        if mongo.is_analysis(type_, label, parents, settings):
            print('The document must be unique: {}'.format(cow)) 
        else:
            mongo.db.analysis.insert_one({
                'type': type_,
                'label': label,
                'parents': parents,
                'settings': settings,
                'data': mongo.prods(cow),
            })


if __name__ == '__main__':
    main()
