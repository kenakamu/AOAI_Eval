## Simulator

To create evaluation test dataset.
https://learn.microsoft.com/azure/ai-studio/how-to/develop/simulator-interaction-data
[sample code](./simulate_data.py)

## Manual Evaluation
https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-prompts-playground
https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-generative-ai-app

There are a set of pre-defined categories.

|AI quality (AI assisted)|	AI quality (NLP)|	Risk and safety metrics|
|---|---|---|
|Groundedness, Relevance, Coherence, Fluency, GPT similarity|	F1 score, ROUGE, score, BLEU score, GLEU score, METEOR score|	Self-harm-related content, Hateful and unfair content, Violent content, Sexual content, Protected material, Indirect attack|

### Create evaluation from Evaluation menu
Upload or manually create input/desired output, then use LLM to generate the answers.
Finally, people will evaluate the result by thumbs up and down.

### Create evaluation from model benchmark page
Select a model and click benchmark, then you can use your own data to evaluate the model.

### From Prompt Flow
You can also start evaluation from prompt flow.

## See the result
https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-results

## Evaluation SDK

https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk
Successor of prompt flow evaluation

OOB evaluators

|Category	|Evaluator class|
|---|---|
|Performance and quality (AI-assisted)	|GroundednessEvaluator, GroundednessProEvaluator, RetrievalEvaluator, RelevanceEvaluator, CoherenceEvaluator, FluencyEvaluator, SimilarityEvaluator|
|Performance and quality (NLP)|	F1ScoreEvaluator, RougeScoreEvaluator, GleuScoreEvaluator, BleuScoreEvaluator, MeteorScoreEvaluator|
|Risk and safety (AI-assisted)|	ViolenceEvaluator, SexualEvaluator, SelfHarmEvaluator, HateUnfairnessEvaluator, IndirectAttackEvaluator, ProtectedMaterialEvaluator|
|Composite	|QAEvaluator, ContentSafetyEvaluator|

Each evaluator has different input data requirements.

