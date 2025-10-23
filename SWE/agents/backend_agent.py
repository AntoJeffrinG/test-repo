from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

class BackendAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            google_api_key=os.getenv('GOOGLE_API_KEY')
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["user_request", "frontend_code"],
            template="""You are a backend developer AI. Generate ONLY Python flask backend code.

Do not include any explanations, comments, or text outside the code.

User Request: {user_request}

Frontend Code:
{frontend_code}

Generate a complete Flask backend that:
1. Serves the frontend HTML file
2. Handles any API endpoints needed by the frontend
3. Includes all necessary imports
4. Has proper route handlers
5. Runs on port 5000

Start with imports and end with if __name__ == '__main__': app.run()"""
        )
    
    def generate_backend_code(self, user_request, frontend_code):
        prompt = self.prompt_template.format(
            user_request=user_request, 
            frontend_code=frontend_code
        )
        response = self.llm.invoke(prompt)
        code = response.content if hasattr(response, 'content') else str(response)

        
        # Save the generated code
        os.makedirs('generated/backend', exist_ok=True)
        with open('generated/backend/app.py', 'w') as f:
            f.write(code)
        
        return code
import sys

if __name__ == "__main__":
    # Expect two arguments
    if len(sys.argv) < 3:
        print("Error: Missing arguments")
        sys.exit(1)

    user_request = sys.argv[1]
    frontend_code = sys.argv[2]

    agent = BackendAgent()
    code = agent.generate_backend_code(user_request, frontend_code)