from django.db import models
from django.core.validators import RegexValidator

# 1. Валидаторду түзөбүз
phone_validator = RegexValidator(
    regex=r'^\d{13}$', 
    message="Телефон номери так 13 сан болушу керек жана тамга болбошу керек."
)



class FooterContact(models.Model):
    about_text = models.TextField(verbose_name="Компания жөнүндө кыскача текст (футердеги)")
    phone = models.CharField(max_length=13,validators=[phone_validator], verbose_name="Телефон номур (мис: +996 553 414 929)")
    address = models.CharField(max_length=255, verbose_name="Дарек (мис: Жалал-Абад ш., Ленин көчөсү)")
    work_hours = models.CharField(max_length=150, verbose_name="Иштөө убактысы")
    
    # Социалдык тармактардын шилтемелери
    instagram_url = models.URLField(max_length=300, verbose_name="Инстаграм шилтемеси (URL)", blank=True, null=True)
    whatsapp_url = models.URLField(max_length=300, verbose_name="Ватсап шилтемеси (URL)", blank=True, null=True)

    class Meta:
        verbose_name = "Футер маалыматы"
        verbose_name_plural = "Футер маалыматтары"

    def __str__(self):
        return "Контакттар жана Футер маалыматы"


class ContactPage(models.Model):
    """Контакт баракчасынын маалыматтары (админкадан толтурулат)"""
    phone = models.CharField(max_length=13,validators=[phone_validator], verbose_name="Телефон номер")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Дарек")
    work_hours = models.CharField(max_length=150, verbose_name="Иштөө убактысы")
    map_iframe_url = models.URLField(
        max_length=500,
        verbose_name="Google Maps iframe URL",
        blank=True
    )
    # Социалдык тармактар
    instagram_url = models.URLField(max_length=300, verbose_name="Instagram", blank=True, null=True)
    telegram_url = models.URLField(max_length=300, verbose_name="Telegram", blank=True, null=True)
    facebook_url = models.URLField(max_length=300, verbose_name="Facebook", blank=True, null=True)
    vk_url = models.URLField(max_length=300, verbose_name="VK", blank=True, null=True)

    class Meta:
        verbose_name = "Контакт баракчасы"
        verbose_name_plural = "Контакт баракчасы"

    def __str__(self):
        return f"Контакт баракчасы — {self.phone}"
    

class ContactRequest(models.Model):
    """Заявкалар (контакт баракчасынан келген)"""
    name = models.CharField(max_length=100, verbose_name="Аты")
    phone = models.CharField(max_length=13,validators=[phone_validator], verbose_name="Телефон")
    message = models.TextField(verbose_name="Билдирүү", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    is_processed = models.BooleanField(default=False, verbose_name="Иштетилди")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявкалар"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.phone}"
    