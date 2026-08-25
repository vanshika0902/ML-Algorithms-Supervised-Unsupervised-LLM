- RL is a methodology that lets computers **Learn & Adapt Based on Experience**.
- **Examples**: Used to make computers become better at playing "Checkers & Go", self-driving cars, it has also been used to help ChatGPT give more human like response to your prompts.
- Learning Rate control how big or little a change we will make to the probabilities each time we update them.
- Explained using example of fries shop of Norm & Squatch.
- Pick num between 0 & 1 - visit that shop and update probability basis taste of fries using below formula:
- New p(norm) = p(norm) + Learning_Rate * (Fry Score - p(norm)).
- Repeat these steps.


**Terminology**

- *Environment* : Something we want to explore & can interact with.
- *Agent* : One who can explore and interact with the environment.
- *Policy* : Probabilities 
- *Reward* : Something that is used to upate the policy/probability (Fry Score in this case).
