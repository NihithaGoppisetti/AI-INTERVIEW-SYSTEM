class AnswerEvaluator:

    def __init__(self, ai_engine):

        self.ai_engine = ai_engine

    def evaluate(self, question, answer):

        prompt = f"""
        Evaluate the candidate's interview answer.

        Interview Question:
        {question}

        Candidate Answer:
        {answer}

        Provide:
        1. Score out of 10
        2. Strengths
        3. Weaknesses
        4. Suggestions for improvement
        """

        result = self.ai_engine.generate_response(prompt)

        return result