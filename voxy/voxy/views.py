""" Views for Voxy Word Count app"""
from string import punctuation

from django.views.generic import FormView

from .forms import WordCountForm
from .utils import word_count


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
        import pdb; pdb.set_trace()
        kwargs = word_count(text_block)
        return self.render_to_response(self.get_context_data(**kwargs))
