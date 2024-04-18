from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class SchoolTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    

    def research_task(self, agent, subject, skill_level):
       return Task(
           description=dedent(
               f"""
               **Task**: Gather information on the given subject and condsider the skill level

               **Description**:
               1. Use the provided tools (web search, YouTube search, Wikipedia search) to find accurate and up-to-date information on the given subject '{subject}' and skill level '{skill_level}'.
               2. Collect relevant data, including research papers, articles, videos, and other credible sources.
               3. Organize the gathered information in a structured format for further analysis.

               **Parameters**:
               - subject: {subject}
               - skill_level: {skill_level}


               **Note**:
               - Focus on gathering high-quality, reliable information from reputable sources.
               - Ensure the information covers the subject matter comprehensively and aligns with the specified skill level.
               - Be thorough in your research, but also efficient in your approach.
               """
           ),
            expected_output=f"""A comprehensive report containing the gathered information, organized in a structured format, covering the subject '{subject}' at the specified skill level '{skill_level}' """,
           agent=agent,
       )

    def curriculum_design_task(self, agent, research_data):
       return Task(
           description=dedent(
               f"""
               **Task**: Design a curriculum for the given subject from the data while considering the skill level

               **Description**:
               1. Analyze the research data gathered by the Research Agent.
               2. Identify key topics, learning objectives, and proficiency levels relevant to the subject and skill level.
               3. Create a structured curriculum with a logical progression of topics and learning paths.
               4. Define assessment methods and evaluation criteria for each topic and proficiency level.

               **Parameters**:
               - research_data: {research_data}

                """
           ),
            expected_output=f""" 
                Module 1: Basic Arithmetic 
                    1.1 Addition
                        Lesson 1: Introduction to addition
                        Lesson 2: Adding whole numbers
                        Lesson 3: Adding decimals
                        Lesson 4: Word problems involving addition
                    Practice exercises and assessments
                    1.2 Subtraction
                        Lesson 1: Introduction to subtraction
                        Lesson 2: Subtracting whole numbers
                        Lesson 3: Subtracting decimals
                        Lesson 4: Word problems involving subtraction
                    Practice exercises and assessments
                    1.3 Multiplication
                        Lesson 1: Introduction to multiplication
                        Lesson 2: Multiplying whole numbers
                        Lesson 3: Multiplying decimals
                        Lesson 4: Word problems involving multiplication
                    Practice exercises and assessments
                    Module summary and assessment
                    Module 2: Advanced Arithmetic
                    2.1 Division
                        Lesson 1: Introduction to division
                        Lesson 2: Dividing whole numbers
                        Lesson 3: Dividing decimals
                        Lesson 4: Word problems involving division
                    Practice exercises and assessments
                    2.2 Exponents
                        Lesson 1: Introduction to exponents
                        Lesson 2: Evaluating exponents
                        Lesson 3: Laws of exponents
                        Lesson 4: Scientific notation
                    Practice exercises and assessments
                    2.3 Distribution
                        Lesson 1: Introduction to distribution
                        Lesson 2: Distributive property with addition
                        Lesson 3: Distributive property with multiplication
                        Lesson 4: Word problems involving distribution
                    Practice exercises and assessments
            """,

           agent=agent,
       )

    def content_creation_task(self, agent, curriculum):
       return Task(
           description=dedent(
               f"""
               **Task**: Develop engaging and effective learning modules

               **Description**:
               1. Based on the curriculum designed by the Curriculum Designer, create comprehensive learning modules content for each topic and proficiency level.
               2. Utilize multimedia content (text, videos, images, interactive exercises, etc.) to cater to different learning styles.
               3. Incorporate assessments and evaluations to measure learners' progress and understanding.
               4. Ensure the learning modules are engaging, interactive, and aligned with the curriculum objectives.

               **Parameters**:
               - curriculum: {curriculum}


               **Note**:
               - Leverage the provided tools (Claude for text generation) to enhance the learning experience.
               - Focus on creating high-quality, visually appealing, and pedagogically sound learning materials.
               - Collaborate with other agents, such as the Research Agent and Curriculum Designer, to maintain consistency and accuracy.
               """
           ),
           expected_output=f"""A set of comprehensive learning modules, including multimedia content, interactive exercises, assessments, and evaluations, aligned with the provided curriculum and tailored to the specified subject and skill level.""",
           agent=agent,
       )

    def course_integration_task(self, agent, learning_modules, curriculum):
       return Task(
           description=dedent(
               f"""
               **Task**: Integrate the learning modules into a comprehensive course

               **Description**:
               1. Organize and sequence the learning modules developed by the Content Creator according to the curriculum structure.
               2. Ensure a smooth and logical progression between modules, topics, and proficiency levels.
               3. Implement navigation and user experience features to enhance the learning process.
               4. Conduct quality assurance checks and make necessary adjustments to ensure a cohesive and seamless learning experience.

               **Parameters**:
               - learning_modules: {learning_modules}
               - curriculum: {curriculum}

               **Expected Output**:
               A comprehensive and integrated course, including all the learning modules organized and sequenced according to the curriculum structure, with a smooth progression, navigation features, and quality assurance checks.

               **Note**:
               - Collaborate closely with the Curriculum Designer and Content Creator to maintain alignment and consistency.
               - Prioritize usability, accessibility, and an intuitive user interface for the course.
               - Ensure the final course meets industry standards and best practices in online education.
               """
           ),
            expected_output=f"""A comprehensive and integrated course, including all the learning modules organized and sequenced according to the curriculum structure, with a smooth progression, navigation features, and quality assurance checks.""",
           agent=agent,
       )