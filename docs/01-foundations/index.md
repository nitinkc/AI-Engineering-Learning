# AI Engineer Reference Modules: Build, Debug, Explain

This section is the reusable reference layer for the site. Use these modules when you want the
durable explanation behind the daily plan: how the systems work, what interviewers expect, and how
to connect concepts to execution.

## Who This Is For

Use this if you are targeting AI Engineer, Agent Engineer, GenAI Engineer, or LLMOps roles where
interviewers test build-debug-deploy ownership.

## Module Map

| Module | Focus                                | Use this when you need                                                  | Open                                                                            |
|--------|--------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 01     | RAG debugging and retrieval quality  | Retrieval grounding, chunking, citations, and failure analysis          | [01 RAG Debugging and Quality](01-rag-debugging-quality.md)                     |
| 02     | Agentic workflows                    | Tool calling, state, approval gates, retries, and workflow design       | [02 Agentic Workflows](02-agentic-workflows.md)                                 |
| 03     | Evals, observability, and production | Eval design, tracing, release gates, and readiness reviews              | [03 Evals, Observability, and Production](03-evals-observability-production.md) |
| 04     | STAR story system                    | Role targeting, evidence mapping, story building, and portfolio framing | [04 STAR Story System](04-star-story-system.md)                                 |
| 05     | Interview sprints and mock loops     | Timed drills, scorecards, and mock loop practice                        | [05 Interview Sprints and Mock Loops](05-interview-sprints-and-mock-loops.md)   |

## Suggested Reading Paths

### Build and debug AI systems

01 -> 02 -> 03

### Convert work into interview signal

04 -> 05

### Full reference path

01 -> 02 -> 03 -> 04 -> 05

## Related Sections

| Need                            | Open                                                                |
|---------------------------------|---------------------------------------------------------------------|
| Day-by-day study sequence       | [Learning and Revision Plan](../02-learning-revision-plan/index.md) |
| Week-specific hands-on projects | [Mini Projects](../03-mini-projects/index.md)                       |


1. Tokens
The very first thing that you must register in your brain is that AI models don’t read words. They don’t even read letters. They read tokens.
So what’s a token?
Imagine you’re reading a book, but instead of reading all the words, you’re reading chunks of words. Sometimes a chunk is a complete word like “cat.” Sometimes it’s part of a word like “un” or “tion.” Sometimes it’s punctuation. That piece of text (chunk) is a token.
For example, the sentence “I love pizza” can be broken into 3tokens: “I”, “ love”, “ pizza”.
Why does this matter to you?
Because every AI product you use such as ChatGPT, Claude, Gemini, is counting tokens behind the scenes. The more tokens you send in your message, the more the model has to process. The more tokens it generates in its reply, the more expensive it gets to run.
When you hear people talk about a model’s context window (more on that in a second), they’re talking about how many tokens it can hold in memory at once. Some older models could handle 4,000 tokens. Newer ones can handle over a million.
This is why AI at times forgets earlier parts of a long conversation. Once the conversation fills up the context window, the oldest tokens are dropped just like when your RAM fills up and your computer starts lagging.
Tokens are the atoms of AI language. Once you understand that, you start to see why some prompts work better than others, why AI gets forgets in long chats, and why API pricing is measured in tokens per thousand.


2. Context window
Imagine you’re talking to someone, but they have a very specific kind of memory. They can only remember the last X minutes of a conversation. Everything before that? Gone. Forgotten.
That’s a context window.
It’s the total amount of text measured in tokens that an AI model can see and consider at one time. This includes everything: your instructions, the conversation history, any documents you’ve shared, and the model’s own replies.
Think of it like a whiteboard. The context window is the size of the whiteboard. You can write whatever you want on it. But once it’s full, you have to erase something old to write something new.
You know what is more interesting?
A small context window (like 4K tokens) means the AI can only work with a few pages of text at a time. Give it a long document, and it can only read chunks of it. A large context window (like 200K tokens) means you can literally paste an entire book and ask questions about it.
This is why people got so excited when Claude announced a 200,000-token context window. Or when Gemini pushed towards 1 million. This thing fundamentally changes what you can do with the model.
What is the practical lesson? If you’re working on something important like summarizing a long document or analyzing data, always be aware that your AI might be forgetting earlier parts of your conversation. That’s not a bug. That’s just the whiteboard running out of space.


3. Temperature
This one is my personal favourite to explain, because once people hear it, they never forget it.
When you ask an AI to write something, there’s a setting known as temperature, that decides how random or predictable the output will be.
Low temperature (closer to 0) = the AI plays it safe. It picks the most likely, most expected word every single time. The output is consistent, accurate, and a little boring. Like that one guy who always sends the same email template.
High temperature (closer to 1 or beyond) = the AI takes risks. It chooses surprising words, unusual turns, interesting ideas. Sometimes brilliant. But not always.
Here’s a real example. Ask an AI to “complete the sentence: The cat sat on the…”
At low temperature, it almost always says “mat” or “floor.” Predictable. Safe.
At high temperature, it might say “philosophical dilemma” or “crumbling empire of Tuesday.”
Creative? Yes. Useful for a legal brief? Absolutely not.
So here’s the unwritten rule that most people don’t know:
If you’re using AI for factual tasks such as summarizing, coding, extracting information, you want low temperature. The AI should be precise, not creative.
If you’re using AI for creative tasks such as writing fiction, brainstorming, generating marketing copy, increase the temperature. You want the unexpected.
Most consumer apps like ChatGPT don’t let you touch this dial directly. They’ve set it to a middle ground. But if you ever use an AI API or a developer tool, you’ll see this setting. And now you actually know what to do with it.


4. Hallucination
This is the term everyone has heard, but not everyone understands why it happens and that’s the important part.
Hallucination is when an AI gives out wrong answers with absolute confidence. No hesitation. A wrong, answer stated as fact.
Example: You ask an AI about a book. It gives you a title, an author, a year, a plot summary all made up. The book doesn’t exist. But the AI states it as if it’s reading from Wikipedia.
Why does this happen?
Here’s the thing most people miss. AI language models are not databases. They don’t look up facts. They predict the next most likely token based on patterns they learned during training. They’re autocomplete on a massive scale.
So when an AI doesn’t know something, it doesn’t say “I don’t know.” It generates what sounds like a correct answer because that’s literally what it was trained to do.
The danger isn’t that AI makes mistakes. All tools make mistakes. The danger is that AI makes mistakes with the exact same confidence it uses when it’s right. It just answers.
The practical lesson here is that never blindly trust AI for facts, statistics, medical advice, legal information, or anything where being wrong has real consequences. Use it as a starting point. Then verify.
The people who understand hallucination don’t stop using AI. They just use it smarter.


5. RAG
This is the most misunderstood concept of the five. And honestly? Once you get it, you’ll see it everywhere.
RAG stands for Retrieval-Augmented Generation. It’s actually a very simple idea.
Here’s the problem it solves. A regular AI model was trained on data up to a certain date. It knows nothing about your company’s internal documents. It knows nothing about events from last week. It knows nothing about that PDF you uploaded.
So how does a product like “Chat with your PDF” or “Ask questions about this document” actually work?
This is RAG.
When you upload a document, the system doesn’t feed the whole thing into the AI’s brain. Instead, it breaks the document into chunks and stores them in a special kind of database called vector database that understands meaning rather than just keywords.
Then, when you ask a question, the system first searches this database for the most relevant chunks. It retrieves those chunks. And then it feeds them to the AI along with your question, saying: “Here’s some relevant context. Now answer the question using this.”
That’s it. Retrieve relevant stuff. Feed it to the AI. Generate an answer. RAG.
Why does this matter?
Because it’s the backbone of almost every useful AI product built in the last two years. Customer support bots that know your company’s policies. AI assistants that can answer questions from your legal documents. Tools that summarize research papers. All of it is built on RAG.
And knowing this changes how you think about AI products. When an AI knows your documents, it’s not actually learned anything. It’s just performing a very smart search and feeding the results to a language model. The model is still the same. The context just changed.

--8<-- "_abbreviations.md"


