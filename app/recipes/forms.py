from django import forms
from .models import Recipe
from ckeditor.widgets import CKEditorWidget
from .categories import MEALTYPES_SETS, CATLIST_SETS
class SearchForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'source', 'mealtype', 'mealcat', 'ingredients', 'instructions', 'image']
        labels = {
            'title':'',
            #'mealcat':'קטגוריות',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'שם המתכון'}),
        }

    title = forms.CharField(
        label='',
        required=False)
    mealcat = forms.MultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple,
        choices=CATLIST_SETS)
    mealtype = forms.MultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple,
        choices=MEALTYPES_SETS)



class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'source', 'mealtype', 'mealcat', 'ingredients', 'instructions', 'image']
        error_messages = {
            'title': {
                'required': 'שדה חובה!',
                'unique': 'שיגאה!! מתכון עם שם זהה כבר קיים במערכת!!'
            },
            'mealtype': {
                'required': 'שדה חובה!'
            },
            'ingredients': {
                'required': 'שכחת לכתוב את רשימת המרכיבים!'
            },
            'instructions': {
                'required': 'שכחת לכתוב את הוראות ההכנה!'
            },
        }
        labels = {
            'title':'',
            'source':'',
            'mealtype':'',
            #'mealcat':'קטגוריות',
            'ingredients':'',
            'instructions':'',
            'image':'תמונה (לא חובה)'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'שם המתכון'}),
            'source': forms.TextInput(attrs={'placeholder': 'מקור המתכון'}),
            'ingredients': forms.Textarea(attrs={'placeholder': 'רשימת מצרכים'}),
            # 'instructions': forms.Textarea(attrs={'placeholder': 'אופן ההרכנה','rows':10, 'cols':80}),
            'instructions': CKEditorWidget(),
        }

    mealcat = forms.MultipleChoiceField(
        required=True,
        label='',
        widget=forms.CheckboxSelectMultiple,
        choices=CATLIST_SETS,
        error_messages={
            'required': 'שכחת לסמן קטגוריות חיפוש!'
        })
    
    mealtype = forms.MultipleChoiceField(
        required=True,
        label='',
        widget=forms.CheckboxSelectMultiple,
        choices=MEALTYPES_SETS,
        error_messages={
            'required': 'שכחת לסמן את סוג המנה!'
        })
