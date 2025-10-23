import os
import sys
import json
from openai import OpenAI

import os
from openai import OpenAI

class FrontendAgent:
    def __init__(self):
        # Initialize the NVIDIA-integrated OpenAI client
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv('NVIDIA_API_KEY')
        )
        
        # Define the prompt template for generating frontend code
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
        # Format the prompt with the user's request
        prompt = self.prompt_template.format(user_request=user_request)
        
        # Generate the frontend code using the NVIDIA Qwen model
        completion = self.client.chat.completions.create(
            model="deepseek-ai/deepseek-v3.1-terminus",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            top_p=0.8,
            max_tokens=4096,
            stream=True
        )
        
        # Collect the generated code from the streamed response
        code = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                code += chunk.choices[0].delta.content
        
        # Save the generated code to a file
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