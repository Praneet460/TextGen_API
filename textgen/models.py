from django.db import models

class Created(models.Model):
    date_created = models.DateTimeField(auto_now_add=True,
                    verbose_name="Created Date")
    
    class Meta:
        abstract = True

class TextGenContext(Created):

    class Meta:
        verbose_name = "TextGen Context"
        verbose_name_plural = "TextGen Context"
        ordering = ["id"]

    context = models.CharField(max_length=100,
                verbose_name="Input Text")

    def __str__(self):
        return self.context


class TextGenResp(Created):

    class Meta:
        verbose_name = "TextGen Response"
        verbose_name_plural = "TextGen Response"
        ordering = ["id"]

    context = models.ForeignKey(TextGenContext, related_name='textgen_resp',
                    on_delete = models.DO_NOTHING)
    model_type = models.CharField(max_length=100, verbose_name="Model Type")
    gen_text = models.TextField(max_length=500, verbose_name="Generated Text")

    def __str__(self):
        return self.gen_text

