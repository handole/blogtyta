from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget) # widget untuk form date publish
	
	class Meta:
		model = Post
		fields = [
 			"title",
			"content",
			"image",
			"draft",
			"publish",
			]