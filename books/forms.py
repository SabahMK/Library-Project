from django import forms
from .models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Div,Submit,Field,ButtonHolder

class ReviewForm(forms.ModelForm):
    # comment= forms.CharField( max_length=50, required=False, widget=forms.Textarea(attrs={'cols':80,'rows':2,
    # 'class':'form-control bg-secondary'}))
    # stars = forms.ChoiceField(choices=Review.STAR_CHOICES, required=False, widget=forms.Select
    # (attrs={'class':'form-control bg-secondary'}))
    
    class Meta:
        model = Review
        fields = ('comment', 'stars', )
        exclude = ('book',)

    def __init__(self,*args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class ='form-group my-4'
        self.helper.label_class='col-md-4 col-form-label'
        self.helper.input_class ='col-md-8 form-control'
        self.helper.layout = Layout(
            Div(
                Field('comment'),
                Field('stars'),
                ButtonHolder(Submit('submit','save'))
            )
        )

