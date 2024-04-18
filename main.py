import os
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
from agents import SchoolAgents
from tasks import SchoolTasks

class CustomCrew:
    def __init__(self, subject, skill_level):
        self.subject = subject
        self.skill_level = skill_level

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = SchoolAgents()
        tasks = SchoolTasks()

        # Define your custom agents and tasks here
        research_agent_instance = agents.research_agent()
        curriculum_designer_instance = agents.curriculum_designer()
        content_creator_instance = agents.content_creator()
        course_integrator_instance = agents.course_integrator()

        # Custom tasks include agent name and variables as input
        research_task = tasks.research_task(
            research_agent_instance,
            self.subject,
            self.skill_level,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[research_agent_instance, curriculum_designer_instance, content_creator_instance, course_integrator_instance],
            tasks=[research_task],
            verbose=True,
        )

        # Pass the output of research_task to curriculum_design_task
        research_data = crew.run(research_task)

        curriculum_design_task = tasks.curriculum_design_task(
            curriculum_designer_instance,
            research_data,
        )

        # Update the crew with the new task
        crew.tasks.append(curriculum_design_task)

        # Continue with the remaining tasks
        curriculum = crew.run(curriculum_design_task)

        content_creation_task = tasks.content_creation_task(
            content_creator_instance,
            curriculum,
        )

        crew.tasks.append(content_creation_task)

        learning_modules = crew.run(content_creation_task)

        course_integration_task = tasks.course_integration_task(
            course_integrator_instance,
            learning_modules,
            curriculum,
        )

        crew.tasks.append(course_integration_task)

        result = crew.kickoff()
        return result

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to NewAge Course Creator")
    print("-------------------------------")
    subject = "Science" #input("Enter subject: ")
    skill_level = "intermediate" #input("Enter skill level: ")

    custom_crew = CustomCrew(subject, skill_level)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom Course:")
    print("########################\n")
    print(result)