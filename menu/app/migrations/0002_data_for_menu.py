from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO app_menucategory (id, title, slug) 
                VALUES (1, 'Main menu', 'main_menu');
            
            INSERT INTO app_menuitem (id, title, url, parent_id, category_id) 
                VALUES (1, 'Главная', 'main', null, 1);
            INSERT INTO app_menuitem (id, title, url, parent_id, category_id) 
                VALUES (2, 'Информация', 'information', null, 1);
            INSERT INTO app_menuitem (id, title, url, parent_id, category_id) 
                VALUES (3, 'О нас', 'information/about', 2, 1);
            INSERT INTO app_menuitem (id, title, url, parent_id, category_id) 
                VALUES (4, 'Контакты', 'information/contacts', 2, 1);
            INSERT INTO app_menuitem (id, title, url, parent_id, category_id) 
                VALUES (5, 'Цены', 'information/price', 2, 1);
        """)
    ]
