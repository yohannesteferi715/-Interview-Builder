from django import forms

from .models import Interview


class InterviewGenerationForm(forms.ModelForm):

    class Meta:
        model = Interview

        fields = [
            "title",
            "topic",
            "difficulty",
            "question_type",
            "number_of_questions",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Backend Engineering Interview",
                }
            ),

            "topic": forms.TextInput(
                attrs={
                    "placeholder": "Python, Django, APIs",
                }
            ),

            "number_of_questions": forms.NumberInput(
                attrs={
                    "min": 1,
                    "max": 50,
                }
            ),
        }

    def clean_number_of_questions(self):

        value = self.cleaned_data[
            "number_of_questions"
        ]

        if value < 1 or value > 50:
            raise forms.ValidationError(
                "Number of questions must be between 1 and 50."
            )

        return value