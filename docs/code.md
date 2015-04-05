# Le code

Tout se déroule à partir du `main.py` :

```python
def main():
    data = DBSelector(DATABASE_PATH).data()
    
    """
    data = {
        ("cow", 1): {
            ("lact", 1): {
                ("crude", "days"): [1, 2, ...],
                ("crude", "prods"): [20.4, 22.0, ...],
                ("crude", "cons"): [11.2, 10.8, ...]
            },
            ("lact", 2): {...}
        },
        ("cow", 4156): {...}
    }
    """
    
    ma = production.MovingAveraging()
    linreg = production.LinearRegression()

    # Views
    crude_data_view = views.CrudeData(join(DATA_PATH, "prod"))
    
    for cow_key in data.get_cow_keys():
        cow = data[cow_key]
        
        ma.analyze(cow, step=2)
        
        """
        data = {
            ("cow", 1): {
                ("lact", 1): {
                    ("crude", "days"): [1, 2, ...],
                    ("crude", "prods"): [20.4, 22.0, ...],
                    ("crude", "cons"): [11.2, 10.8, ...]
                    ("ma", "days", 2): [...],
                    ("ma", "prods", 2): [...]
                },
                ("lact", 2): {...}
            },
            ("cow", 4156): {...}
        }
        """
        
        linreg.analyze(cow, proportion=80)
        
        """
        data = {
            ("cow", 1): {
                ("lact", 1): {
                    ("crude", "days"): [1, 2, ...],
                    ("crude", "prods"): [20.4, 22.0, ...],
                    ("crude", "cons"): [11.2, 10.8, ...]
                    ("ma", "days", 2): [...],
                    ("ma", "prods", 2): [...],
                    ("linreg", "prods", "X", 80): [...],
                    ("linreg", "prods", "error", 80): 9.54
                },
                ("lact", 2): {...}
            },
            ("cow", 4156): {...}
        }
        """
        
        # Views
        crude_data_view.save(cow)
```

## Les tests

Le code est testé avec des tests unitaires, contenus dans le dossier `test`. 
TravisCI est employé comme outil d'intégration continue.
