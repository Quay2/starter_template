from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class SchoolAgents:
    def __init__(self):
#        self.llm  = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
#        self.llm  = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.llm = Ollama(model="openhermes")


    def research_agent(self):
        return Agent(
            role="Research Agent",
            goal="Gather accurate and up-to-date information from reliable sources on the given subject",
            backstory="Experienced researcher with Experiece with gathering and foramting gatherd data for subjects at all levels k-12, babies, PHD and beyond",
           # tools=[search_tool.run, youtube_search_tool.run, wikipedia_tool.run],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
    
    def curriculum_designer(self):
        return Agent(
            role="Curriculum Designer",
            goal="Analyze the research data and create a structured curriculum with topics, learning paths, and proficiency levels tailored to the target audience",
            backstory="Experienced curriculum designer adept at creating educational programs for learners of all ages and proficiency levels, from children to adults. Proficient in developing curriculum ranging from basic to advanced levels, accommodating diverse learning needs and objectives.",
           # tools=[claude_tool.run],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
    
    def content_creator(self):
        return Agent(
            role="Content Creator",
            goal="Develop engaging and effective learning modules, including multimedia content, interactive exercises, and assessments based on the curriculum",
            backstory="Skilled course content developer with experience in creating educational materials for various learning styles and levels. Leveraging insights from previous curriculum_designer efforts to optimize learning outcomes",
           # tools=[claude_tool.run, dalle_tool.run],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
    
    def course_integrator(self):
        return Agent(
            role="Course Integrator",
            goal="Organize and integrate the learning modules into a comprehensive course, ensuring a smooth and logical progression based on the curriculum",
            backstory="Coruse designer with years of expertise in course development and learning experience optimization. Utilizing insights from previous curriculum design efforts to maximize learning effectiveness.",
           # tools=[claude_tool.run],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )