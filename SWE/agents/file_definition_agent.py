import os
import sys
import json
from openai import OpenAI


class FrontendAgent:
    def __init__(self):
        # Initialize NVIDIA-integrated OpenAI client
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv('NVIDIA_API_KEY')
        )

        # Define the prompt template for frontend generation
        self.prompt_template = """You are a frontend developer AI. Generate ONLY a complete HTML file with inline CSS and JavaScript.

Do not include any explanations, comments, or text outside the code.
Do not use external files or links - everything must be inline.
Develop the frontend alone, no need to generate backend.

User Request: {user_request}

Generate a complete HTML file with:
1. HTML structure
2. CSS styles inside <style> tags in the <head>
3. JavaScript code inside <script> tags before closing </body>
4. Make it responsive and modern
5. Use only inline styles and scripts - no external files

Start with <!DOCTYPE html> and end with </html>."""

    def generate_frontend_code(self, user_request):
        # Format prompt
        prompt = self.prompt_template.format(user_request=user_request)

        # Generate frontend using the NVIDIA OpenAI client
        completion = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            top_p=1,
            max_tokens=4096,
            stream=True
        )

        # Stream and collect the code
        code = ""
        for chunk in completion:
            reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)

            if reasoning:
                print(reasoning, end="")  # Optional: to view reasoning if available

            if chunk.choices[0].delta.content is not None:
                piece = chunk.choices[0].delta.content
                print(piece, end="")  # Stream output in real time
                code += piece

        # Save the generated code to file
        os.makedirs('generated/frontend', exist_ok=True)
        with open('generated/frontend/index.html', 'w') as f:
            f.write(code)

        return code


if __name__ == "__main__":
    # Get the user request from command-line arguments
    user_request = " ".join(sys.argv[1:])  # Get text passed from Node
    agent = FrontendAgent()
    code = agent.generate_frontend_code(user_request)
    print(code)