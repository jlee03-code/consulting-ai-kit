# Windows Setup — Mode A (Claude Code)

Step-by-step guide for a fresh Windows laptop with nothing pre-installed.
Only one thing needs to be downloaded: **Node.js**.

---

## Step 1 — Open PowerShell

PowerShell is the terminal built into every Windows machine.

**How to open it:**
1. Press the **Windows key** (bottom-left of keyboard, looks like ⊞)
2. Type `powershell`
3. Click **Windows PowerShell** in the search results

You should see a blue window with a `PS C:\Users\YourName>` prompt.
Keep this window open — all commands below are typed here.

> **Tip:** Right-click the taskbar icon and choose "Pin to taskbar" so you can find it easily later.

---

## Step 2 — Install Node.js

Node.js is the only software you need to download.

1. Open a browser and go to **https://nodejs.org**
2. Click the big green **"LTS" download button** (the left one — LTS means stable)
3. Open the downloaded `.msi` file and click **Next** through every screen — all defaults are fine
4. Click **Finish** when done

**Verify it worked.** Back in PowerShell, type this and press Enter:

```powershell
node --version
```

You should see something like `v20.18.0`. If you see an error, close and reopen PowerShell and try again.

```powershell
npm --version
```

You should see something like `10.8.0`.

---

## Step 3 — Install Claude Code

In PowerShell, run:

```powershell
npm install -g @anthropic-ai/claude-code
```

This takes about 30 seconds. When it finishes, verify:

```powershell
claude --version
```

**Log in to your Anthropic account (one-time only):**

```powershell
claude
```

A browser window will open asking you to log in. Complete the login, then return to PowerShell. You will see a `>` prompt — type `/exit` and press Enter to close for now.

---

## Step 4 — Download the kit

No Git required — download as a ZIP file.

1. Open a browser and go to **https://github.com/jlee03-code/consulting-ai-kit**
2. Click the green **Code** button near the top right
3. Click **Download ZIP**
4. Open File Explorer (Win + E), go to **Downloads**, right-click the ZIP file, choose **Extract All**
5. In the dialog, change the destination to `C:\Users\YourName\consulting-ai-kit` (replace YourName with your actual Windows username)
6. Click **Extract**

---

## Step 5 — Install the skills

This copies the kit's skills and rules into Claude Code's config folder.

In PowerShell, run these commands **one at a time**, pressing Enter after each:

```powershell
cd "$env:USERPROFILE\consulting-ai-kit"
```

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\rules"
```

```powershell
Copy-Item -Recurse -Force skills\house-style         "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse -Force skills\consult-research    "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse -Force skills\finance-model       "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse -Force skills\karpathy-guidelines "$env:USERPROFILE\.claude\skills\"
```

```powershell
Copy-Item -Recurse -Force rules\common "$env:USERPROFILE\.claude\rules\"
```

**Verify the skills were copied:**

```powershell
ls "$env:USERPROFILE\.claude\skills"
```

You should see four folders: `house-style`, `consult-research`, `finance-model`, `karpathy-guidelines`.

---

## Step 6 — Start a working session

Every time you want to use Mode A, follow this pattern:

**1. Create or navigate to your project folder.** Example — create a new one:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\my-project"
cd "$env:USERPROFILE\my-project"
```

**2. Copy `CLAUDE.md` into the project folder** (this activates BCG register directives):

```powershell
Copy-Item "$env:USERPROFILE\consulting-ai-kit\CLAUDE.md" .
```

**3. Launch Claude Code:**

```powershell
claude
```

**4. Confirm skills are loaded.** Inside Claude, type:

```
/skills
```

You should see `house-style`, `consult-research`, `finance-model`, `karpathy-guidelines` listed. You are ready.

---

## Optional: Word and Excel export

If you want to generate `.docx` research outputs and `.xlsx` finance models:

**Install Python (one-time):**
1. Go to **https://python.org/downloads**
2. Click **Download Python 3.x** (latest)
3. Run the installer — **check the box "Add Python to PATH"** before clicking Install Now
4. Click Install Now

**Verify:**
```powershell
python --version
```

**Install export libraries:**
```powershell
python -m pip install python-docx openpyxl
```

**Test the scripts:**
```powershell
cd "$env:USERPROFILE\consulting-ai-kit"
python skills\finance-model\templates\word_export.py
python skills\finance-model\templates\excel_export.py
```

Output files are saved to your system's temp folder. To save them to the Desktop instead, open each script in Notepad and change the last line:

```python
# Change this:
'/tmp/bcg_research_output.docx'

# To this (replace YourName):
'C:/Users/YourName/Desktop/bcg_research_output.docx'
```

---

## Updating the kit later

When the kit is updated on GitHub:

1. Go to **https://github.com/jlee03-code/consulting-ai-kit**, download the ZIP again
2. Extract it, overwriting the existing `consulting-ai-kit` folder
3. In PowerShell, re-run the Copy-Item block from Step 5

---

## Quick reference

| Task | Where | Command |
|------|-------|---------|
| Open terminal | Start menu | Win key → type `powershell` → Enter |
| Start a session | PowerShell | `cd your-project-folder` then `claude` |
| Confirm skills loaded | Inside Claude | `/skills` |
| Exit Claude | Inside Claude | `/exit` |
| Update kit | PowerShell | Re-download ZIP, re-run Step 5 |
