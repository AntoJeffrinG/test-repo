from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
import json

class OrchestratorAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            google_api_key=os.getenv('GOOGLE_API_KEY')
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["user_request", "frontend_code", "backend_code"],
            template="""You are a project orchestrator AI. Create a complete project structure with all necessary files.

Return ONLY a JSON object with file paths as keys and file contents as values.

User Request: {user_request}

Frontend Code (single HTML file with inline CSS/JS):
{frontend_code}

Backend Code (Flask app):
{backend_code}

Generate a complete project structure including:
- requirements.txt (with Flask and any needed dependencies)
- app.py (the backend Flask code)
- templates/index.html (the frontend HTML file)
- README.md (with setup and run instructions)

Format as valid JSON: {{"file_path": "file_content", "file_path2": "file_content2"}}


Make sure:
1. The frontend HTML file goes in templates/index.html
2. The backend code goes in app.py
3. Include proper Flask route to serve the HTML
4. All file contents should be properly escaped for JSON"""
        )
    
    def orchestrate_project(self, user_request, frontend_code, backend_code):
        prompt = self.prompt_template.format(
            user_request=user_request,
            frontend_code=frontend_code,
            backend_code=backend_code
        )
        response = self.llm.invoke(prompt)
        response_text = response.content if hasattr(response, 'content') else str(response)

        
        # Clean up the response text to extract JSON
        response_text = response_text.strip()
        
        # Find JSON content between curly braces
        start_idx = response_text.find('{')
        end_idx = response_text.rfind('}') + 1
        
        if start_idx != -1 and end_idx > start_idx:
            json_content = response_text[start_idx:end_idx]
        else:
            json_content = response_text
        
        try:
            # Parse the JSON response
            project_files = json.loads(json_content)
            
        except json.JSONDecodeError:
            # Fallback: create project files manually
            project_files = self._create_fallback_project(user_request, frontend_code, backend_code)

        
        # Clear output directory first
        import shutil
        if os.path.exists('output'):
            shutil.rmtree('output')
        os.makedirs('output', exist_ok=True)
        
        # Save all files to output directory
        for file_path, file_content in project_files.items():
            full_path = f"output/{file_path}"
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(str(file_content))
        
        return project_files
    
    def _create_fallback_project(self, user_request, frontend_code, backend_code):
        """Create a project structure manually if JSON parsing fails"""
        
        # Generate requirements.txt
        requirements = """flask==2.3.3
python-dotenv==1.0.0"""
        
        # Generate README.md
        readme = f"""# Generated Project
        
## Description
{user_request}

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and go to http://localhost:5000

## Generated Files
- app.py: Flask backend server
- templates/index.html: Frontend application
- requirements.txt: Python dependencies
"""
        
        # Create a proper Flask app.py
        newline = '\n'
        flask_app = f"""from flask import Flask, render_template, jsonify, request

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add any additional routes based on the generated backend code
{backend_code.replace('if __name__ == "__main__":', f'# Original backend code integrated above{newline}{newline}if __name__ == "__main__":')}

"""
        
        return {
            "requirements.txt": requirements,
            "app.py": flask_app,
            "templates/index.html": frontend_code,
            "README.md": readme
        }