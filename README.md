### Connor MacMillan's Transcrypt Take-Home Assessment
For this take-home assessment on text generation, I created 3 notebooks and one python file that helps call the MediaStack API.

#### Data Collection Notebook
In this notebook, I collect the recent and popular news articles to be used when I fine-tune the GPT-2 model for text generation.

#### MediaStack File
In the Python file I created helper functions to call the API and ensure that I only use valid parameters. I wanted to validate the parameter before calling the API because I plan on using an LLM to extract relevant details from a user's prompt to retrieve relevent news articles, and while LLMs are great at processing and creating natural language, and can learn fairly well with few-shot prompting, it might provid invalid parameters.

#### News Search Notebook
I took a chat-bot type approach for this notebook. A user can enter a prompt about what news they are interested in reading, an LLM (I used BLOOM because its free to use with a HuggingFace API Token) extracts the relevant categories and keywords (I limited it to English news in the U.S. for the sake of time). After extracting the parameters, I call the news stack API and find the recent news based on those parameters. Once retrieving the articles, I recommend the most similar articles to the user's prompt by calculating the sentence embedding for the prompt and the article's title and description and ranking them by similarity.

##### Example Output:
**Example Input**: "What are new AI and technology achievements?" here are the top results:

1. DeepMind Co-Founder Wants the ‘New Turing Test’ to Be Based on How Good an AI Is at Getting Rich
With artificial intelligence hype leaving venture capitalist firms foaming at the mouth, ready to buy into any new company that sticks an “A” and “I” in its name, we sure as hell need a new way of defining what constitutes an AI. The Turing Test fails to define real intelligence in today’s world of large language…Read more...

Read Full Article by Kyle Barr

2. AI could change the future of yogurt—and turn Danone around
Making the yogurt of the future requires a cast of 21st-century helpers: machine learning, gut science and even a mysterious artificial stomach.

Read Full Article by physorg

3. NTIA Publishes Over 1,400 Comments on Proposed AI Accountability Policy
More than 1,400 written responses were received by the National Telecommunications and Information Administration commenting on its draft artificial intelligence accountability policy. The comments have been published two months after NTIA issued its request for feedback, which will help shape its policy recommendations to ensure earned trust in AI technology. The agency drafted the AI Accountability Policy in an aim to guide the development of assessments, audits, and certifications of AI systems. The document is part of a larger effort by the Biden administration to govern AI-related risks...

Read Full Article by Jamie Bennet

#### Fine Tune GPT
In this notebook I load the pretrained weights and architecture of GPT-2 and then use the ~20k articles I collected in the Data Collection Notebook to finetune the GPT-2 model. After fine-tuning the model I then use the articles I set aside for testing to compare the generated descriptions to the true descriptions. I also generate descriptions using the base GPT-2 model to see how the fine-tuning improved the quality of the generated descriptions.

##### Example Output:

**Input Title**: Sacramento taqueria allegedly used priest to get confessions of workplace ‘sins’

**Original Description**: SACRAMENTO, Calif. - The owners of multiple Sacramento taquerias will have to shell out thousands in damages to former employees and fines after they were busted hiring an alleged priest to spy on workers and extract confessions of workplace "sins." "Federal wage and hour investigators have seen corrupt employers try all kinds of scams to shortchange workers and toThe post Sacramento taqueria allegedly used priest to get confessions of workplace ‘sins’ appeared first on KION546.

**Generated Description**: Sacramento police received two complaints of mass abuses during a hiring process for an Atlanta taqueria after it alleged that two priests...

**Non-Tuned GPT-2 Generated Text**: iced tea is bad for us. There was an incident where a friend of mine and my wife tried to convince the chef to let us buy tea in their cupboards. While they made no effort to conceal their intention to drink tea they were clearly influenced by the situation