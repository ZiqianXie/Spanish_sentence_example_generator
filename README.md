# Spanish_sentence_example_generator
This project query Google translate or spanishdict.com for example Spanish sentences containing a given word.

I am using this to help create an ANKI deck to learn Spanish.

Originally I tried to use BERT-like models to fill up the MASK tokens surround the word and use autoregressive text generation model with different prompts like "aquí es un oración con la palabra [word]:" but the result was not satisfactory.

Note that the Google translation can be very wrong sometimes so manual curation is always needed.