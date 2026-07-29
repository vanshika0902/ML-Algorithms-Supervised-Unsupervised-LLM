**Transformer Decoder Model**

- The architecture behind models like **GPT**

**Problem Statement**: 

- Imagine input sentence to model as : "What is StatQuest awesome"
- Task of model is to predict the next word
- Input to model is : What is StatQuest awesome <EOS>
- EOS means End of Sentence


Steps:

**STEP 1**

- **Word Embedding**

The computer can not understand words - only numbers

- Each word is converted in numbers
  -"What" : [0.3, 1.2, -0.5, ...]
  - "is" : [1.1, -0.8, 0.7, ....]
  - "awesome" : [0.6, 2.4, 0.1, ...]
