# SynthSite 🚀

**A Revolutionary Multi-Agent Software Development System for Automated Website Generation**

## 🌟 Overview

SynthSite is an innovative AI-powered platform that leverages multiple specialized agents to automatically generate complete, functional websites from natural language descriptions. Built on cutting-edge language models and multi-agent orchestration, SynthSite transforms ideas into reality through intelligent code generation and project structuring.

## 🤖 Multi-Agent Architecture

SynthSite employs a sophisticated multi-agent system where each agent specializes in different aspects of web development:

### 🎯 **Orchestrator Agent**
- **Role**: Project coordinator and master planner
- **Capabilities**: Analyzes user requirements, coordinates other agents, generates complete project structures
- **Technology**: Google Gemini 1.5 Flash with LangChain integration

### 🎨 **Frontend Agent**
- **Role**: UI/UX specialist and frontend developer
- **Capabilities**: Creates responsive HTML/CSS/JavaScript interfaces, designs user experiences
- **Output**: Complete frontend code with modern styling and interactivity

### ⚙️ **Backend Agent**
- **Role**: Server-side logic and API development
- **Capabilities**: Builds Flask applications, designs APIs, handles data processing
- **Output**: Robust backend services with proper error handling

### 📁 **File Definition Agent**
- **Role**: Project structure architect
- **Capabilities**: Defines file hierarchies, manages dependencies, ensures proper organization
- **Output**: Well-structured project layouts with all necessary configuration files

## 🛠️ Technology Stack

### Backend Technologies
- **Python 3.12+** - Core programming language
- **Flask** - Lightweight web framework
- **LangChain** - AI agent orchestration framework
- **Google Generative AI** - Advanced language model integration
- **Python-dotenv** - Environment configuration management

### Frontend Technologies
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling and responsive design
- **JavaScript (ES6+)** - Interactive functionality
- **Express.js** - Node.js web server (optional)

### AI & Machine Learning
- **Google Gemini 1.5 Flash** - Primary language model
- **LangChain Community** - Extended AI capabilities
- **Multi-Agent Coordination** - Intelligent task distribution

## 🚀 Key Features

### ✨ **Intelligent Code Generation**
- Natural language to code conversion
- Context-aware development decisions
- Best practice implementation
- Cross-platform compatibility

### 🔄 **Automated Project Structuring**
- Complete file hierarchy generation
- Dependency management
- Configuration file creation
- Documentation generation

### 🎯 **Specialized Agent Expertise**
- Domain-specific knowledge application
- Optimized code patterns
- Industry-standard implementations
- Scalable architecture design

### 📦 **Complete Project Delivery**
- Ready-to-deploy applications
- Comprehensive documentation
- Setup and installation guides
- Runtime environment configuration

## 📁 Project Structure

```
SynthSite/
├── SWE/                          # Main application directory
│   ├── agents/                   # AI agent implementations
│   │   ├── orchestrator_agent.py # Project coordination
│   │   ├── frontend_agent.py     # UI/UX development
│   │   ├── backend_agent.py      # Server-side logic
│   │   └── file_definition_agent.py # Project structuring
│   ├── static/                   # Frontend assets
│   │   └── script.js            # Client-side JavaScript
│   ├── server.js                # Node.js server (optional)
│   ├── package.json             # Node.js dependencies
│   └── requirements.txt         # Python dependencies
├── synthsite/                   # Python package
└── generated/                   # Output directory for generated projects
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- Node.js (optional, for Express server)
- Google API key for Gemini integration

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AntoJeffrinG/test-repo.git
   cd test-repo
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r SWE/requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

4. **Run the application**
   ```bash
   cd SWE
   python orchestrator_agent.py
   ```

## 💡 Usage Examples

### Basic Website Generation
```python
# Initialize the orchestrator
orchestrator = OrchestratorAgent()

# Generate a complete website
project = orchestrator.generate_project(
    user_request="Create a portfolio website for a photographer",
    frontend_code="...",
    backend_code="..."
)
```

### Custom Agent Configuration
```python
# Configure specialized agents
frontend_agent = FrontendAgent(style_preference="modern")
backend_agent = BackendAgent(framework="flask")
file_agent = FileDefinitionAgent(structure="mvc")
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Required for Gemini AI integration
- `LANGCHAIN_TRACING`: Optional tracing configuration
- `DEBUG`: Development mode flag

### Agent Customization
- Model selection (Gemini variants)
- Prompt template modification
- Output format configuration
- Error handling preferences

## 🤝 Contributing

We welcome contributions to SynthSite! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Google AI** for providing the Gemini language models
- **LangChain** for the multi-agent orchestration framework
- **Flask** community for the excellent web framework
- **Open Source Community** for inspiration and collaboration

## 🔮 Future Roadmap

- [ ] Support for additional frameworks (Django, FastAPI)
- [ ] Real-time collaboration features
- [ ] Advanced UI/UX design capabilities
- [ ] Database integration and management
- [ ] Deployment automation
- [ ] Multi-language support
- [ ] Plugin architecture for custom agents

## 📞 Support

For questions, issues, or contributions:
- **Issues**: [GitHub Issues](https://github.com/AntoJeffrinG/test-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AntoJeffrinG/test-repo/discussions)
- **Email**: antojeffrin007@gmail.com

---

**Built with ❤️ by the SynthSite Team**

*Transforming ideas into digital reality through intelligent automation.*