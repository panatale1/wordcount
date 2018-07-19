""" Views for Voxy Word Count app"""
from string import punctuation

from django.views.generic import FormView

from .forms import WordCountForm


class WordCountView(FormView):
    # FormView handles a lot of the heavy lifting
    # The following are class features required to use FormView
    form_class = WordCountForm
    template_name = 'counting/text_entry.html'

    def form_valid(self, form):
        # Here we get the input text block.
        # We get total number of character groups, discard non-alphanumeric characters,
        # and get total word count.
        text_block = form.cleaned_data['text_block']
        total_tokens = len(text_block.split())
        for piece in punctuation:
            text_block = text_block.replace(piece, '')
        word_count = len(text_block.split())
        kwargs = {
            'text_block': form.cleaned_data['text_block'],
            'word_count': word_count,
            'extra_tokens': total_tokens - word_count,
        }
        return self.render_to_response(self.get_context_data(**kwargs))
