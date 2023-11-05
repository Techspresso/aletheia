
## Inspiration

In today's hyperconnected world, we are increasingly reliant on online information sources for our news and perspectives. The information sources online are structured to increase the number of clicks. However, this has also led to the rise of echo chambers and provocative content. This can lead to a polarised society and a decline in critical thinking.

The problem not only involves solving multiple nuanced problems on a large corpus of text, like neutral summarisation, extracting topics, and various other metrics like bias, but also using these as context for further transformations. Truly automating this entire pipeline would not be possible without cutting edge AI language models that can operate at scale like Claude.

## The Application

Aletheia integrates with your web browsing experience, by first scanning the current article, identifying the key points, and then scouring the web for articles presenting diverse viewpoints. Once gathered, the application would then meticulously analyze each article, extracting its main arguments and assigning a bias rating based on its tone, language, and sources.

This carefully curated selection of diverse viewpoints is then presented to you in a concise and easy-to-understand format, allowing you to quickly grasp the different perspectives on the issue. It then also prioritizes the least biased articles, guiding you towards reliable and objective sources of information.

## How we built it

![The extension pipeline](https://github.com/Techspresso/aletheia/blob/main/arch.png)

Here is a breakdown of how the application works:

***User Interaction*** : The user encounters an article they wish to analyze and clicks on the browser extension button.

***Article Scraping and Topic Extraction*** : The Python backend scrapes the content of the article and extracts the leading topic using Claude.

***Topic Augmentation***: To ensure diverse viewpoints, the backend performs topic augmentation by identifying related or opposing terms and phrases.

***Web Search with Brave Search API***: The backend utilizes the Brave Search API to conduct a web search for articles related to the original topic and its augmented versions.

***Article Analysis***: Each retrieved article is scraped for its content, and then summarized and analyzed for bias using natural language processing techniques.

***Response Generation and Delivery***: The backend compiles the analysis results, including article summaries, bias ratings, and links to the original articles. This response is sent back to the browser extension.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or later
- make

### Setting Up the Development Environment

To set up your development environment, you'll use a `Makefile` which simplifies the process of creating a virtual environment, installing dependencies, and running tests. Here's how to use it:

1. Create a Virtual Environment:

   Run the following command to create a virtual environment. This will help you manage your Python dependencies separately from your system Python installation.

   ```bash
   make venv
   ```

2. After creating the virtual environment, you need to activate it:

   ```bash
   source venv/bin/activate
   ```

3. To install your project along with all dependencies, needed for development use:

   ```bash
   make install-test-dependencies
   ```

4. You can run tests using:

   ```bash
   make test
   ```

This will execute the pytest tests located in your project.

## Continuous Integration

This template includes a basic GitHub Action located in `.github/workflows/main.yml`. The action will run tests on every push to the remote repository.
