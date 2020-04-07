import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ebook_mall.settings")

    import django
    django.setup()

    from Book.models import Book, Author

    au1_list = []
    for i in range(10):
        i = str(i)
        au1_list.append(Book(title=i,course_img=i, brief=i, pub_date='2020-04-04',isbn=i,bpan_code=i, bpan_link=i,language=0, order=i,first_category=3,book_tag=1))

    Book.objects.bulk_create(au1_list)


