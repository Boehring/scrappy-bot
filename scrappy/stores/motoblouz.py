from scrappy import db
from scrappy.models import Article, Store, Price
from scrappy.stores.request_service import get_product_detail, get_product_prices, get_road_articles, \
    get_helmets

STORE = 'Motoblouz'


def process_articles():
    print('Getting articles...')
    road_articles_lst = get_road_articles()
    counter = 0
    for product_id in road_articles_lst:
        counter += 1
        process_article(product_id['id'])

        commit_needed(counter)
    db.session.commit()

    print('Getting helmets...')
    counter = 0
    helmets_lst = get_helmets()
    for helmet in helmets_lst:
        counter += 1
        process_article(helmet['id'])

        commit_needed(counter)
    db.session.commit()

    read_all_prices()


def commit_needed(counter):
    if counter % 500 == 0:
        db.session.commit()


def process_article(article_id):
    existing_article = Article.query.filter(Article.oid == article_id).first()

    if existing_article is None:
        detail = get_product_detail(article_id)
        store = Store.query.filter(Store.name == STORE).first()

        db.session.add(new_article(detail, store))


def new_article(detail, store):
    return Article(
        detail['id'],
        detail['brand']['name'],
        '{} {} {}'.format(detail['categoryName'], detail['brand']['name'], detail['name']),
        detail['url'],
        detail['categoryName'],
        None,
        detail['shortDescription'],
        store.id
    )


def read_all_prices():
    print('Checking prices...')
    store = Store.query.filter(Store.name == STORE).one()
    articles = Article.query.filter(Article.store_id == store.id)

    counter = 0
    for article in articles:
        counter += 1
        print('Checking price for article {}'.format(article.oid))
        price = get_product_prices(article.oid)

        if price is not None and len(price) > 0:
            db.session.add(
                Price(price['skus'][0]['sellPrice']['inclTax'], price['skus'][0]['discountPercent'], None, None,
                      None, article.id))

        commit_needed(counter)
    db.session.commit()
