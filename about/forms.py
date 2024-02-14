from .models import Reviews
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 40})