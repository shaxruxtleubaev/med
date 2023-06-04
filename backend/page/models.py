from django.db.models import *

class Specializations(Model):

    name = CharField(
        'Name',
        max_length=100
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'specialization'
        verbose_name_plural = 'specializations'

class Doctors(Model):

    first_name = CharField(
        'First Name',
        max_length=100
    )

    last_name = CharField(
        'Last Name',
        max_length=100
    )

    email = EmailField(
        'Email'
    )

    contact_number = CharField(
        'Contact Number (optional)',
        max_length=13,
        blank=True,
        null=True
    )

    password = CharField(
        'Password',
        max_length=20
    )

    confirm_password = CharField(
        'Confirm Password',
        max_length=20
    )

    dob = DateField(
        'Date of birth (optional)',
        blank=True,
        null=True
    )

    specialization = ForeignKey(
        Specializations,
        on_delete=CASCADE
    )

    experience_in_year = IntegerField(
        'Experience in Year (optional)',
        blank=True,
        null=True
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    gender = CharField(
        'Gender',
        max_length=50,
        choices = GENDER_CHOICES
    )

    profile_picture = ImageField(
        'Profile picture',
        upload_to='doctors-profile-pictures'
    )

    monday = BooleanField(
        'Monday',
        default=False
    )

    tuesday = BooleanField(
        'Tuesday',
        default=False
    )

    wednesday = BooleanField(
        'Wednesday',
        default=False
    )

    thursday = BooleanField(
        'Thursday',
        default=False
    )

    friday = BooleanField(
        'Friday',
        default=False
    )

    saturday = BooleanField(
        'Saturday',
        default=False
    )

    sunday = BooleanField(
        'Sunday',
        default=False
    )

    status = BooleanField(
        'Status',
        default=False
    )

    address1 = CharField(
        'Address 1 (optional)',
        max_length=150,
        blank=True,
        null=True
    )

    address2 = CharField(
        'Address 2 (optional)',
        max_length=150,
        blank=True,
        null=True
    )

    COUNTRIES = (
        ('UZ', 'Uzbekistan'),
        ('KR', 'Karakalpakistan'),
        ('KZ', 'Kazakhstan'),
        ('RU', 'Russia')
    )

    country = CharField(
        'Country (optional)',
        max_length=50,
        choices=COUNTRIES,
        blank=True,
        null=True
    )

    state = CharField(
        'State (optional)',
        max_length=50,
        blank=True,
        null=True
    )

    city = CharField(
        'City (optional)',
        max_length=50,
        blank=True,
        null=True
    )

    postal_code = IntegerField(
        'Postal Code (optional)',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

class ServicesCategories(Model):

    name = CharField(
        'Name of the category of the service',
        max_length=100
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'services category'
        verbose_name_plural = 'services categories'

class Services(Model):

    name = CharField(
        'Name of the service',
        max_length=50
    )

    category = ForeignKey(
        ServicesCategories,
        on_delete=CASCADE
    )

    doctors = ForeignKey(
        Doctors,
        on_delete=CASCADE
    )

    short_description = TextField(
        'Short Description'
    )

    icon = ImageField(
        'Icon',
        upload_to='services-icons'
    )

    status = BooleanField(
        'Status',
        default=False
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:

        verbose_name = 'service'
        verbose_name_plural = 'services'
