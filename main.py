from scrappy.models import Store

if __name__ == '__main__':
    value = Store.query.filter_by(name='').value()
    print(value)
