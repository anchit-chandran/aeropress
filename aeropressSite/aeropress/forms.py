from django import forms


class RecipeForm(forms.Form):

    coffee_g = forms.IntegerField(min_value=0,
                                  step_size=1,
                                  label='Coffee used (g)☕',

                                  widget=forms.NumberInput(
                                      attrs={
                                          'class': 'form-control form-control-sm'}
                                  ))
    water_brew_ml = forms.IntegerField(min_value=0,
                                       step_size=1,
                                       label='Water used for extraction (mL)💧',
                                       widget=forms.NumberInput(
                                           attrs={
                                               'class': 'form-control form-control-sm'}
                                       ))
    brew_time_s = forms.IntegerField(label='Extraction time (s)⌛',
                                     widget=forms.NumberInput(
                                         attrs={
                                             'class': 'form-control form-control-sm'}
                                     ))
    milk_ml = forms.IntegerField(min_value=0,
                                 step_size=1,
                                 label='Milk used (mL)🥛',
                                 widget=forms.NumberInput(
                                     attrs={
                                         'class': 'form-control form-control-sm'}
                                 ))
    extra_water_ml = forms.IntegerField(min_value=0,
                                        step_size=1,
                                        label='Extra water added (mL)💦',
                                        widget=forms.NumberInput(
                                            attrs={
                                                'class': 'form-control form-control-sm'}
                                        ))
    nausea = forms.BooleanField(required=False, label='Experienced nausea🤢',
                                widget=forms.CheckboxInput(
                                    attrs={'class': 'form-check-input',
                                           'role': 'switch'
                                           }
                                ))
    rating = forms.IntegerField(
        min_value=0,
        max_value=10,
        step_size=1,
        label='Rating (/10)🌟',
        widget=forms.NumberInput(
            attrs={'class': 'form-control form-control-sm'}
        ))
