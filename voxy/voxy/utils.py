"""utils for Voxy app"""
from string import punctuation

def word_count(text_block):
    total_tokens = len(text_block.split())
    for piece in punctuation:
        text_block = text_block.replace(piece, '')
    word_count = len(text_block.split())
    return {
        'extra_tokens': total_tokens - word_count,
        'word_count': word_count,
        'text_block': text_block
    }
