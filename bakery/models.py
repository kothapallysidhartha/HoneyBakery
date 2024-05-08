from django.db import models
import uuid

class Cake(models.Model):
    CAKE_TYPES = (
        ('Birthday', 'Birthday'),
        ('Wedding', 'Wedding'),
        ('Anniversary', 'Anniversary'),
        ('Other', 'Other')
    )

    CAKE_EVENTS = (
        ('Birthday Party', 'Birthday Party'),
        ('Wedding Ceremony', 'Wedding Ceremony'),
        ('Anniversary Celebration', 'Anniversary Celebration'),
        ('Other', 'Other')
    )
    
    cake_image = models.ImageField(upload_to='cake_images/',default='cake_images/default.jpg')
    cake_name = models.CharField(max_length=100)
    cake_description = models.TextField()
    cake_price = models.DecimalField(max_digits=10, decimal_places=2)
    cake_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cake_type = models.CharField(max_length=20, choices=CAKE_TYPES)
    event = models.CharField(max_length=30, choices=CAKE_EVENTS)

    def __str__(self):
        return self.cake_name


class Booking(models.Model):
    PAYMENT_MODES = (
        ('Cash', 'Cash'),
        ('PhonePe', 'PhonePe'),
        ('Google Pay', 'Google Pay'),
        ('Other', 'Other')
    )

    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.cake:
            self.total_amount = self.cake.cake_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking ID: {self.id} - Cake: {self.cake.cake_name} - Customer: {self.customer_name}"