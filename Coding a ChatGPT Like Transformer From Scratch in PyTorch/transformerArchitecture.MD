**Transformer Decoder Model**

- The architecture behind models like **GPT**

**Problem Statement**: 

- Imagine input sentence to model as : "What is StatQuest awesome"
- Task of model is to predict the next word
- Input to model is : What is StatQuest awesome <EOS>
- EOS means End of Sentence

**Solution**


Steps:

***STEP 1***

- *Word Embedding*

   - The computer can not understand words - only numbers
   - Each word is converted in numbers

      - "is" : [1.1, -0.8, 0.7, ....]
      - "awesome" : [0.6, 2.4, 0.1, ...]

***STEP 2***

- *Positional Encoding*
   - Useful to understand which place the words comes on 
   - Word embedding + Position embedding
   - Embedding : [0.3,1.2,-0.5]; Position 1 : [0.1,0.1,0.1]; Final : [0.4,1.3,-0.4]

***STEP 3***

- *Masked Self Attention*
  - Which earlier words are important?
  - awesome
     ↑
   looks at 
 
    What ✔ (10%)

    is ✔   (15%)

    StatQuest ✔ (70%)


***STEP 4***

- *Query, Key, Value*
  - The Query asks "Which other words should I pay attention to?". The Keys help compare. The Values contain the information to use.







