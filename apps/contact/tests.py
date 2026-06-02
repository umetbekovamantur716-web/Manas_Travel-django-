from django.test import TestCase
from apps.contact.models import FooterContact,ContactPage,ContactRequest

class FooterContactTest(TestCase):  
    def test_footer_contact_create(self):
        contact = FooterContact.objects.create(
            about_text="кыскача текст ",
            phone="13",
            address="Картан дон",
            work_hours="Иштөө убактысы",   
            instagram_url="https://instagram.com/manas_travel", 
            whatsapp_url="https://wa.me/123456"

        )
       
        self.assertEqual(
            contact.about_text,
            "кыскача текст "
        )

        self.assertEqual(
            contact.phone,
            "13"
        )

        self.assertEqual(
            contact.address,
            "Картан дон"
        )

        self.assertEqual(
            contact.work_hours,
            "Иштөө убактысы"
        )

        self.assertEqual(
            contact.instagram_url,
            "https://instagram.com/manas_travel"
        )
        
        self.assertEqual(
            contact.whatsapp_url,
            "https://wa.me/123456"
        )

class ContactPageTest(TestCase):
    def test_contactPage_create(self):
        contactpage = ContactPage.objects.create(
            phone = "0553 414 929",
            email = "test@gmail.com",
            address = "Жусупбакиева 7",
            work_hours  = "6:00",
            map_iframe_url = "http://gugle.map"
        )

        self.assertEqual(
            contactpage.phone,
            "0553 414 929",
        )
        self.assertEqual(
            contactpage.email,
            "test@gmail.com",
        )
        self.assertEqual(
            contactpage.address,
            "Жусупбакиева 7",
        )
        self.assertEqual(
            contactpage.work_hours,
            "6:00",
        )

        self.assertEqual(
            contactpage.map_iframe_url,
            "http://gugle.map"
        )



class ContactPageTestCase(TestCase):
    def test_contactpage_create(self):
        contactpage = ContactPage.objects.create(
            phone = "0553414929",
            email = "test@gmail.com",
            address = "Манас шаары ",
            work_hours = "20:00",
            map_iframe_url = "http://gugle.map",

            instagram_url = "http://instagram.com",
            telegram_url = "http://telegram.com",
            facebook_url  = "http://facebook.com",
            vk_url = "http://vk.com"

        )

        self.assertEqual(
            contactpage.phone,
            "0553414929"
        )

        self.assertEqual(
            contactpage. email,
            "test@gmail.com"
        )
        self.assertEqual(
            contactpage.address,
            "Манас шаары ",
        )
        self.assertEqual(
            contactpage.work_hours,
            "20:00",
        )
        self.assertEqual(
            contactpage.map_iframe_url,
            "http://gugle.map",
        )



        self.assertEqual(
            contactpage.instagram_url,
            "http://instagram.com",
        )
        self.assertEqual(
            contactpage.telegram_url,
            "http://telegram.com",
        )
        self.assertEqual(
            contactpage.facebook_url,
            "http://facebook.com",
        )
        self.assertEqual(
            contactpage.vk_url,
            "http://vk.com"
        )



class ContactRequestTestCase(TestCase):
    def test_contactrequest_create(self):
        contactrequest = ContactRequest.objects.create(
            name = "amantur",
            phone = "0900 900 900",
            message = "собшеня",
            created_at = "2026",
            is_processed = True
        )

        
        self.assertEqual(
            contactrequest.name ,
            "amantur",
        )
        self.assertEqual(
            contactrequest.phone,
            "0900 900 900",
        )
        self.assertEqual(
            contactrequest.message,
            "собшеня",
        )
        self.assertEqual(contactrequest.created_at.year, 2026)

        self.assertEqual(
            contactrequest.is_processed,
            True
        )

