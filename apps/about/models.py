from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name=" Биз жөнүндө")
    description = models.TextField(verbose_name="Компания жөнүндө толук текст")
    
    # Статистика бөлүмү
    stat_clients = models.CharField(max_length=50, default="500+", verbose_name="Кардарлардын саны")
    stat_tours = models.CharField(max_length=50, default="50+", verbose_name="Турлардын саны")
    stat_experience = models.CharField(max_length=50, default="5+", verbose_name="Жылдык тажрыйба")
    
    # Fun Facts (Фактылар)
    fact_1_icon = models.CharField(max_length=50, verbose_name="Факт 1 иконка")
    fact_1_number = models.CharField(max_length=50,  verbose_name="Факт 1 сан")
    fact_1_text = models.TextField(verbose_name="Факт 1 текст")

    fact_2_icon = models.CharField(max_length=50,  verbose_name="Факт 2 иконка")
    fact_2_number = models.CharField(max_length=50, verbose_name="Факт 2 сан")
    fact_2_text = models.TextField(verbose_name="Факт 2 текст")

    fact_3_icon = models.CharField(max_length=50, verbose_name="Факт 3 иконка")
    fact_3_number = models.CharField(max_length=50, verbose_name="Факт 3 сан")
    fact_3_text = models.TextField(verbose_name="Факт 3 текст")

    fact_4_icon = models.CharField(max_length=50, verbose_name="Факт 4 иконка")
    fact_4_number = models.CharField(max_length=50, verbose_name="Факт 4 сан")
    fact_4_text = models.TextField(verbose_name="Факт 4 текст")

    # Принцибы
    principle_1_title = models.CharField(max_length=100, verbose_name="Принцип 1 аталышы")
    principle_1_desc = models.TextField(verbose_name="Принцип 1 текст")

    principle_2_title = models.CharField(max_length=100, default="Надежность")
    principle_2_desc = models.TextField(verbose_name="Принцип 2 текст")

    # Карта
    map_iframe_url = models.TextField(verbose_name="Гугл картанын iframe шилтемеси (src ичиндеги гана)",
                                       default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2924.1234567890123!2d73.00000000000001!3d42.00000000000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1234567890abcdef%3A0xabcdef1234567890!2sManas%20Travel%20Office!5e0!3m2!1sen!2skg!4v1700000000000")

    class Meta:
        verbose_name = "Биз жөнүндө маалымат"
        verbose_name_plural = "Биз жөнүндө маалыматтар"

    def __str__(self):
        return self.title