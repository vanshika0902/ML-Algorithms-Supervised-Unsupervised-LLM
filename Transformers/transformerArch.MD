*ARCHITECTURE*

Input sentence

↓

Word Embedding
(Convert words into numbers)

↓

Position Encoding
(Add word order)

↓

Masked Self Attention
(Each word looks at previous words and decides which ones matter using Q, K and V.)

↓

Residual Connection
(Add old information + new information)

↓

Feed Forward Network
(Process and improve the information)

↓

Residual Connection
(Keep both old and refined information)

↓

Linear Layer
(Give every word in the vocabulary a score)

↓

Softmax
(Convert scores into probabilities)

↓

Choose the next word

↓

Repeat










