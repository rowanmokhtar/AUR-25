#!/usr/bin/env python3
from word_counter import count_words

big_sentence = 'A grasshopper spent the summer hopping about in the sun and singing to his heart\'s content. One day, an ant went hurrying by, looking very hot and weary. "Why are you working on such a lovely day?" said the grasshopper. "I\'m collecting food for the winter," said the ant, "and I suggest you do the same." And off she went, helping the other ants to carry food to their store. The grasshopper carried on hopping and singing. When winter came the ground was covered with snow. The grasshopper had no food and was hungry. So he went to the ants and asked for food. "What did you do all summer when we were working to collect our food?" said one of the ants. "I was busy hopping and singing," said the grasshopper. "Well," said the ant, "if you hop and sing all summer, and do no work, then you must starve in the winter."'

print(count_words(big_sentence, case_sensitive=False))
