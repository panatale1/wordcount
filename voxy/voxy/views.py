from string import punctuation

from django.views.generic import FormView, TemplateView

from .forms import WordCountForm


class WordCountView(FormView):
    form_class = WordCountForm
    template_name = 'counting/text_entry.html'

    def form_valid(self, form):
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


class WordCountResultsView(TemplateView):
    template_name = 'counting/results.html'
