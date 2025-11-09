A text-based horror adventure game where you and your friend Hannah explore haunted locations. Features multiple branching paths, different endings, and an AI-powered conversation with a mysterious severed head using a local LLM.

## How to Play

Navigate the story by entering the number of your choice when prompted. In the special AI conversation route, you can ask the severed head questions about the factory and its dark past.

**Exit words during AI chat:** `quit`, `exit`, `leave`, `run`, `goodbye`, `bye`

## Prerequisites

Before you can play the game, you need to install:

1. **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
2. **Ollama** - Local AI model runner

##  Installation Instructions

### Step 1: Install Ollama

1. Go to [https://ollama.com](https://ollama.com)
2. Download Ollama for your operating system (Windows, Mac, or Linux)
3. Install Ollama following the installer instructions
4. Ollama should start automatically after installation

### Step 2: Pull an AI Model

Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
ollama pull gemma3
```

This will download the AI model needed for the game (~4GB download).

**Alternative models you can use:**
- `ollama pull llama3.2:1b` - Smaller and faster (1GB)
- `ollama pull mistral` - Higher quality responses (4GB)
- `ollama pull gemma2:2b` - Good balance (1.6GB)

> **Note:** If you use a different model, you'll need to change the model name in the code (see Configuration section below).

### Step 3: Set Up the Python Environment

1. **Clone or download this repository** to your computer

2. **Open a terminal** in the game folder

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv ENVIRONMENTNAME
   ```

4. **Activate the virtual environment:**
   
   **Windows (Command Prompt):**
   ```bash
   ENVIRONMENTNAME\Scripts\activate
   ```
   
   **Windows (PowerShell):**
   ```bash
   ENVIRONMENTNAME\Scripts\Activate.ps1
   ```
   
   **Mac/Linux:**
   ```bash
   source ENVIRONMENTNAME/bin/activate
   ```

5. **Install required Python libraries:**
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Run the Game

```bash
python ghost_game.py
```

## Configuration

### Using a Different AI Model

If you want to use a different Ollama model, open `ghost_game.py` and find this line in the `chat_with_head()` function:

```python
model='gemma3',  # Change this to your preferred model
```

Change it to match the model you pulled, for example:
```python
model='mistral',  # or 'llama3.2:1b', 'gemma2:2b', etc.
```

##  Troubleshooting

### "Cannot connect to Ollama"
- Make sure Ollama is running: `ollama serve`
- Verify Ollama is installed: `ollama list`

### "Model not found"
- Pull the model first: `ollama pull gemma3`
- Check you're using the correct model name in the code

### "Module not found: ollama"
- Make sure you activated your virtual environment
- Install requirements: `pip install -r requirements.txt`

### AI responses are slow
- Try a smaller model like `llama3.2:1b`
- Close other applications to free up RAM
- The first response is always slower (model loading)

##  Requirements

- Python 3.8+
- Ollama
- ollama Python library (installed via requirements.txt)
- ~2-4GB free disk space (for AI model)
- ~4-8GB RAM recommended
