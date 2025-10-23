const express = require('express');
const path = require('path');
const { spawn } = require('child_process');
const app = express();

app.use(express.json());
app.use(express.static('templates'));

//frontend generation
app.post('/generate-frontend', (req, res) => {
    const userInput = req.body?.input;

    if (!userInput) {
        return res.status(400).json({ success: false, error: 'No input provided' });
    }
    const pythonScriptPath = path.join(__dirname, 'agents', 'frontend_agent.py');

    const python = spawn('python3', [pythonScriptPath, userInput]);

    let stdoutData = '';
    let stderrData = '';

    python.stdout.on('data', (data) => {
        stdoutData += data.toString();
    });
    python.stderr.on('data', (data) => {
        stderrData += data.toString();
    });

    python.on('close', (code) => {
        if (code === 0) {
            lastUserRequest = userInput;
            lastFrontendCode = stdoutData;
            res.json({ success: true, output: stdoutData });
        } else {
            res.json({ success: false, error: stderrData || 'Python script failed' });
        }
    });
});

//backend generation
app.post('/generate-backend', (req, res) => {
    if (!lastUserRequest || !lastFrontendCode) {
        return res.status(400).json({
            success: false,
            error: 'Frontend must be generated first!'
        });
    }

    const pythonScriptPath = path.join(__dirname, 'agents', 'backend_agent.py');
    const python = spawn('python3', [pythonScriptPath, lastUserRequest, lastFrontendCode]);


    let stdoutData = '';
    let stderrData = '';

    python.stdout.on('data', (data) => { stdoutData += data.toString(); });
    python.stderr.on('data', (data) => { stderrData += data.toString(); });

    python.on('close', (code) => {
        if (code === 0) {
            res.json({ success: true, backendCode: stdoutData });
        } else {
            res.json({ success: false, error: stderrData || 'Backend generation failed' });
        }
    });
});

//streamlit preview
let streamlitProcess = null;
const STREAMLIT_FILE = path.join(__dirname, 'agents', 'generated', 'temp_streamlit_app.py');


app.post('/run-streamlit', (req, res) => {

    if (streamlitProcess) {
        streamlitProcess.kill();
    }

    streamlitProcess = spawn('streamlit', ['run', STREAMLIT_FILE, '--server.port', '8501']);


    streamlitProcess.stdout.on('data', (data) => console.log(`Streamlit: ${data.toString()}`));

    streamlitProcess.stderr.on('data', (data) => console.error(`Streamlit Error: ${data.toString()}`));

    streamlitProcess.on('close', () => { 
        console.log('Streamlit exited'); 
        streamlitProcess = null; 
    });

    res.json({ success: true, url: 'http://localhost:8501' });
});

app.listen(3000, () => console.log('Server running at http://localhost:3000'));