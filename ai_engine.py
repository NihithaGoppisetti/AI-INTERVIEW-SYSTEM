class AIEngine:

    def __init__(self):
        pass

    def generate_questions(
        self,
        job_role,
        experience,
        question_type,
        number_of_questions
    ):

        questions = []

        if question_type in ["Technical", "Mixed"]:

            technical_questions = [
                f"What are the important skills required for a {job_role}?",
                f"Explain the main responsibilities of a {job_role}.",
                f"What technical concepts should a {experience} candidate know for {job_role}?",
                f"Describe a project related to {job_role} that you have worked on.",
                f"What are common challenges faced by a {job_role}?"
            ]

            questions.extend(technical_questions)

        if question_type in ["HR", "Mixed"]:

            hr_questions = [
                "Tell me about yourself.",
                "What are your strengths and weaknesses?",
                "Why should we hire you?",
                "Where do you see yourself in five years?",
                "Why do you want this job?"
            ]

            questions.extend(hr_questions)

        if question_type == "Behavioral":

            questions = [
                "Tell me about a difficult situation you faced.",
                "Describe a time when you worked in a team.",
                "Tell me about a mistake you made and what you learned.",
                "Describe a situation where you solved a problem.",
                "Tell me about a time when you demonstrated leadership."
            ]

        return questions[:number_of_questions]

    def generate_response(self, prompt):

        prompt_lower = prompt.lower()

        if "evaluate" in prompt_lower:

            return """
Score: 8/10

Strengths:
- The answer is relevant to the question.
- The response is understandable.
- The candidate demonstrates confidence.

Weaknesses:
- The answer could include a specific example.
- Some points could be explained in more detail.

Suggestions:
- Use the STAR method: Situation, Task, Action and Result.
- Give specific examples from projects or experience.
- Keep the answer structured and concise.
"""

        return "AI response generated successfully."