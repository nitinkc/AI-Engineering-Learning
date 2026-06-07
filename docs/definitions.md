## Tokens

The piece of text (chunk) is a token.

For example, the sentence “I love NY” can be broken into 3 tokens: “I”, “ love”, “ NY”.

The more tokens you send in your message, the more the model has to process, the more tokens it
generates in its reply, the more expensive it gets to run.

A model’s context window is about how many tokens it can hold in memory at once.

Some older models could handle 4,000 tokens. Newer ones can handle over a million.

This is why AI at times forgets earlier parts of a long conversation. Once the conversation fills up
the context window, the oldest tokens are dropped just like when your RAM fills up and your computer
starts lagging.

## Context window

Imagine a system remembers only the last X minutes of a conversation. Everything before that is
Gone & Forgotten.
That’s a context window.

It’s the total amount of text measured in tokens that an AI model can see and consider at one time.

This includes everything: your instructions, the conversation history, any documents you’ve shared,
and the model’s own replies.

Think of it like a whiteboard. The context window is the size of the whiteboard.

A small context window (like 4K tokens) means the AI can only work with a few pages of text at a
time. Give it a long document, and it can only read chunks of it.

A large context window (like 200K tokens) means you can literally paste an entire book and ask
questions about it.

## Temperature

When you ask an AI to write something, there’s a setting known as temperature, that decides how *
*random** or **predictable** the output will be.

Low temperature (closer to 0) = the AI plays it safe. It picks the **most likely**, most expected word
every single time. The output is consistent, accurate, and a little boring.

High temperature (closer to 1 or beyond) = the AI takes risks. It chooses surprising words,
unusual turns, interesting ideas.

Here’s a real example. Ask an AI to “complete the sentence: The cat sat on the…”

At low temperature, it almost always says “mat” or “floor.” Predictable. Safe.

At high temperature, it might say “philosophical dilemma” or “crumbling empire of Tuesday.”
Creative? Yes. Useful for a legal brief? Absolutely not.


If you’re using AI for **factual tasks** such as summarizing, coding, extracting information, you
want low temperature. The AI should be precise, not creative.

If you’re using AI for creative tasks such as writing fiction, brainstorming, generating
marketing ideas, increase the temperature. You want the unexpected.

Most consumer apps like ChatGPT don’t let you touch this dial directly. They’ve set it to a
middle ground. But if you ever use an AI API or a developer tool, you’ll see this setting. And
now you actually know what to do with it.

## Hallucination

Hallucination is when an AI gives out wrong answers with **absolute confidence**. No hesitation. 

Example: You ask an AI about a book. It gives you a title, an author, a year, a plot summary all
made up. The book doesn’t exist. But the AI states it as if it’s reading from Wikipedia.

Why does this happen?

AI language models are not databases. They don’t look up facts. They predict **the next most likely token** based on patterns they learned during training.
They’re autocomplete on a massive scale.

So when an AI doesn’t know something, it doesn’t say “I don’t know.” It generates what sounds
like a correct answer because that’s literally what it was trained to do.

The danger isn’t that AI makes mistakes.  The danger is in the fact AI makes
mistakes with the exact same confidence it uses when it’s right. It just answers.

The practical lesson here is that never blindly trust AI for facts, statistics, medical advice,
legal information, or anything where being wrong has real consequences. 

## RAG - Retrieval-Augmented Generation. 

Here’s the problem it solves.
When you upload a document, the AI system doesn’t feed the whole thing into the AI’s brain. Instead, it
breaks the document into chunks and stores them in a special kind of database called **vector database**
that understands meaning rather than just keywords.

Then, when you ask a question, the system **first searches** this database for the most relevant chunks.
It retrieves those chunks. And **then** it feeds them to the AI along with your question, saying:
“Here’s some relevant context. Now answer the question using this.”

Retrieve relevant stuff -> Feed it to the AI (LLM) -> Generate an answer = RAG.

Why does this matter?

Because it’s the **backbone** of almost every useful AI product built in the last two years. 

Customer support bots that know your company’s policies. AI assistants that can answer questions from your
legal documents. Tools that summarize research papers. All of it is built on RAG.

And knowing this changes how you think about AI products. When an AI knows your documents, it's not
actually learned anything. It's just performing a very smart search and feeding the results to a
language model. The model is still the same. The context just changed.

### How the search actually works — Embeddings

The key mechanism behind this search is **embeddings** — each chunk of text is converted into a list
of numbers that captures its meaning. When you ask a question, it's converted the same way, and the
database finds the chunks whose numbers are mathematically closest.

This is why it can match *meaning*, not just keywords: "car" and "automobile" would land near each
other in this numerical space. A keyword search would miss that. A vector search wouldn't.

### The biggest risk — Retrieval quality

RAG is only as good as what it retrieves. If the wrong chunks are pulled back — because of poor
chunking, weak embeddings, or a vague question — the AI confidently answers using irrelevant context.
**Garbage in, garbage out.**

Common failure modes:

- The answer isn't in any retrieved chunk (the document wasn't indexed, or the question was too vague)
- Too many chunks are retrieved and the relevant part gets buried in noise
- The retrieved chunks fill the context window, leaving no room for the model to reason well

### RAG vs. just having a big context window

You might wonder: if context windows are now 200K+ tokens, why not just paste the whole document?
Sometimes you can. But for large knowledge bases (thousands of documents), retrieval is still
necessary — you can't fit a company's entire policy library into one prompt. RAG scales where brute
force doesn't.


### Document

a "document" means one retrievable text unit in your vector index (often a chunk), not specifically a MongoDB/BSON document.

--8<-- "_abbreviations.md"
