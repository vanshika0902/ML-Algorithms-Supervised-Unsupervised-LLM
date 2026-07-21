**RLFH**

- RLHF stands for Reinforcement Learning with Human Feedback

How to train a Large Language Model from scratch?

- it is untrained means all the weights & biases are random initialization values.
- **Step 1** : Train it to predict next token in a very large body of text, like the entire Wikipedia. It is called Pre-Training.
- **Step 2** : Align the pre-trained model which has two steps :
     - Supervised Fine-Tuning : Uses a dataset with pairs of human created prompts & human created responses. This dataset is relatively smaller as compared to pre-                                  training dataset. It can cause overfitting - model does not respond well to new prompts. Thats why we use RLHF.
     - RLHF: We create preference dataset & create a reward model - which is then used to train fine-tuned model.
- After this we have an aligned model.

--------------------------------------------------------------------------------------------------------------------------------------
**Example**

End-to-End Example

Suppose the prompt is:

"Write a polite email asking for an interview."

** Stage 1 (Pretraining) **

The model learns English and email structure from large text corpora.

** Stage 2 (SFT) **

It sees examples like:

Dear Hiring Manager,

I hope you're doing well...

and learns to imitate them.

** Stage 3 (Human Preferences) **

Three responses are generated.

A

Give me interview.

B

Dear Hiring Manager...

C

Hello
Need interview ASAP

Humans rank:

B > C > A


** Stage 4 (Reward Model) **

The reward model learns to assign the highest score to responses similar to B.

** Stage 5 (RL) **

The chat model is updated so future responses are more likely to resemble highly rated ones.


