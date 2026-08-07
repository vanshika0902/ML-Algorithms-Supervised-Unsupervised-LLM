**Transformer Decoder Model**

- The architecture behind models like **GPT**
- GPT uses decoder-only because it is autoregressive task : Next-Word Prediction: It focuses entirely on guessing the next token based on previous tokens.
- **Primary uses** : Text Generation, Open ended chat, Code completion.
- Encoder-Decoder required for Sequence-2-Sequence tasks such as Machine Translation (Changing English to French)

**Features**
- Uni-directional
- Auto-regressive
- Masked self-attention & cross attention

**Model**
- GPT (OpenAI)
- Gemini (Google)
- LLAMA (Meta)
- Gemma (Google)
- Mistral

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
   - Using sine & cosine curves
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

 - *Query, Key, Value*
   - The Query asks "Which other words should I pay attention to?". The Keys help compare. The Values contain the information to use.

***STEP 4***

- *Residual Connection*
   - Old information


***STEP 5***

- *Fully Connected Layer*
   - Old information + New information = Better information

***STEP 6***

- *Softmax*
  - Now the model picks the most likely word (or samples one based on these probabilities)
