import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o")

# Tools
search_tool = DuckDuckGoSearchRun()

def run_financial_analysis(company: str):
    # 1. Define Agents
    researcher = Agent(
        role="Market Data Researcher",
        goal=f"Gather comprehensive financial data for {company}, including stock price, P/E ratio, and market cap.",
        backstory="You are a seasoned data scientist specializing in financial markets. You find precise data that others miss.",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm
    )

    news_analyst = Agent(
        role="Financial News Analyst",
        goal=f"Analyze the latest news headlines and social sentiment for {company}. Identify key catalysts and risks.",
        backstory="You are a world-class financial journalist. You have a keen eye for sentiment and market-moving news.",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm
    )

    strategist = Agent(
        role="Investment Strategist",
        goal=f"Synthesize the research and news analysis to provide a final investment recommendation for {company}.",
        backstory="You are a senior hedge fund manager with decades of experience. You turn raw data into winning strategies.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    # 2. Define Tasks
    research_task = Task(
        description=f"Collect key financial metrics for {company}. Focus on the last 12 months of performance.",
        agent=researcher,
        expected_output="A structured list of financial metrics including current price, valuation ratios, and growth trends."
    )

    news_task = Task(
        description=f"Summarize the top 5 news stories for {company} from the past week. Highlight sentiment (Bullish/Bearish).",
        agent=news_analyst,
        expected_output="A summary report of news sentiment and its potential impact on the stock price."
    )

    strategy_task = Task(
        description=f"Based on the research and news, write a 3-paragraph investment recommendation for {company}.",
        agent=strategist,
        expected_output="A professional investment report with a 'Buy/Hold/Sell' rating and justification."
    )

    # 3. Form the Crew
    financial_crew = Crew(
        agents=[researcher, news_analyst, strategist],
        tasks=[research_task, news_task, strategy_task],
        process=Process.sequential,
        verbose=True
    )

    # 4. Kickoff
    result = financial_crew.kickoff()
    return result

if __name__ == "__main__":
    print(run_financial_analysis(company="Tesla"))