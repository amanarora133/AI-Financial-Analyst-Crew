# AI Financial Analyst Crew 📈🤖

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Autonomous_Agents-red)](https://github.com/joaomdmoura/crewAI)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI Financial Analyst Crew** is an autonomous multi-agent system designed to perform comprehensive stock market research and financial analysis. Powered by **CrewAI**, it orchestrates a team of specialized AI agents that collaborate to analyze market trends, synthesize news, and provide data-driven investment recommendations.

## 🤖 The Crew

The system utilizes three highly specialized agents:

1.  **Market Data Researcher**: Fetches real-time stock prices, historical data, and key financial metrics using APIs.
2.  **Financial News Analyst**: Scours the web for the latest news, sentiment trends, and macro-economic factors affecting the target stock.
3.  **Investment Strategist**: Synthesizes data from the Researcher and Analyst to generate a professional-grade investment report with actionable insights.

## 🌟 Key Features

- **📊 Real-time Data**: Integration with financial APIs for up-to-the-minute market information.
- **📰 Sentiment Analysis**: Deep analysis of news headlines and market sentiment.
- **📑 Autonomous Reporting**: Generates structured Markdown reports ready for professional use.
- **⛓️ Sequential Workflow**: Uses CrewAI's sequential process to ensure logical data flow between agents.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- OpenAI API Key
- Serper API Key (for web search)

### Installation
`ash
git clone https://github.com/amanarora133/AI-Financial-Analyst-Crew.git
cd AI-Financial-Analyst-Crew
pip install -r requirements.txt
`

### Usage
`python
from financial_crew import run_financial_analysis

# Analyze a specific company
result = run_financial_analysis(company="NVIDIA")
print(result)
`

## 🛠️ Tech Stack
- **Agent Orchestration**: CrewAI
- **LLM**: GPT-4o / Claude 3.5 Sonnet
- **Financial Data**: YFinance / Alpha Vantage
- **Web Search**: Serper / DuckDuckGo Search

---
Developed with ❤️ by [Aman Arora](https://github.com/amanarora133)