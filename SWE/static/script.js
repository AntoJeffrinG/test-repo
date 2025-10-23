let currentUserRequest = '';

function showLoading() {
    document.getElementById('loading').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showStep(stepNumber) {
    // Hide all steps
    for (let i = 1; i <= 4; i++) {
        document.getElementById(`step${i}`).style.display = 'none';
    }
    // Show specific step
    document.getElementById(`step${stepNumber}`).style.display = 'block';
}

async function generateFrontend() {
    const userRequest = document.getElementById('userRequest').value;
    if (!userRequest.trim()) {
        alert('Please enter a project description');
        return;
    }
    
    currentUserRequest = userRequest;
    showLoading();
    
    try {
        const response = await fetch('/generate_frontend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ request: userRequest })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('frontendCode').textContent = data.code;
            document.getElementById('previewFrame').src = '/preview_frontend?' + new Date().getTime();

            showStep(2);
        } else {
            alert('Error generating frontend: ' + data.message);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
}

function approveFrontend() {
    generateBackend(true);
}

function regenerateFrontend() {
    showStep(1);
}

async function generateBackend(approved = false) {
    showLoading();
    
    try {
        const response = await fetch('/generate_backend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                request: currentUserRequest,
                approved: approved 
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('backendCode').textContent = data.code;
            showStep(3);
        } else {
            alert('Error generating backend: ' + data.message);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
}

function approveBackend() {
    orchestrateProject(true);
}

function regenerateBackend() {
    generateBackend(true);
}

async function orchestrateProject(approved = false) {
    showLoading();
    
    try {
        const response = await fetch('/orchestrate_project', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                request: currentUserRequest,
                approved: approved 
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            const filesList = document.getElementById('projectFiles');
            filesList.innerHTML = '<h3>Generated Files:</h3><ul>' + 
                data.files.map(file => `<li>📄 ${file}</li>`).join('') +
                '</ul>';
            showStep(4);
        } else {
            alert('Error orchestrating project: ' + data.message);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
}

async function downloadProject() {
    window.location.href = '/download_project';
}

// Initialize the app