# Workflow for Starting and Running a New Theory Research Project

This document describes the standard workflow for creating a new research project from the theory-research template, using VS Code, GitHub, Codex, Zotero, Better BibTeX, and a local Python environment.

The intended use case is an economic theory project with a LaTeX paper, literature notes, proof attempts, numerical or symbolic checks, plots, and local PDFs managed through Zotero.

---

## 1. Core Principle

The project should have one clear source of truth:

```text
GitHub repository + local clone = source of truth
VS Code = main local workspace
Codex = local project agent
Zotero = bibliography and PDF manager
Better BibTeX = automatic references.bib export
LaTeX Workshop = local Overleaf-like compiler
```

Do not let the project become scattered across Overleaf, loose PDFs, notebooks, local folders, and untracked notes. The repository should contain the project structure, LaTeX source, notes, code, and instructions.

PDFs and extracted paper text should usually remain local and should not be pushed to GitHub.

---

## 2. Starting a New Project from the Template

### 2.1 Create the New Repository on GitHub

Go to the template repository on GitHub, for example:

```text
theory-research-template
```

Click:

```text
Use this template
```

Then create a new private repository, for example:

```text
coordinated-learning-in-large-populations
```

or:

```text
relational-investment-paper
```

Use a project-specific name. Avoid generic names such as `paper` or `research`.

---

### 2.2 Clone the New Repository Locally

Open VS Code.

Use:

```text
Ctrl + Shift + P
```

Search for:

```text
Git: Clone
```

Paste the repository URL, for example:

```text
https://github.com/YOUR_USERNAME/NEW-PROJECT.git
```

Choose the local folder where the project should live, for example:

```text
Google Drive/Research/
```

or:

```text
Documents/Research/
```

Then open the cloned folder in VS Code.

Alternatively, from Git Bash:

```bash
cd ~/Documents/Research
git clone https://github.com/YOUR_USERNAME/NEW-PROJECT.git
cd NEW-PROJECT
code .
```

---

## 3. First Pass After Cloning

After opening the project in VS Code, immediately check that the template structure is present.

Expected structure:

```text
NEW-PROJECT/
│
├── AGENTS.md
├── README.md
├── project-log.md
├── notation.md
├── claims-and-results.md
├── references.bib
├── environment.yml
├── .gitignore
├── .gitattributes
│
├── .vscode/
│   ├── settings.json
│   └── extensions.json
│
├── paper/
│   ├── main.tex
│   ├── sections/
│   ├── appendices/
│   └── figures/
│
├── slides/
│
├── notes/
│   ├── literature/
│   ├── proof-attempts/
│   ├── model-variants/
│   └── meeting-notes/
│
├── literature/
│   ├── paper-index.md
│   ├── pdfs/
│   ├── extracted-text/
│   └── manifests/
│
├── code/
│   ├── symbolic/
│   ├── simulations/
│   └── plots/
│
├── outputs/
│   └── figures/
│
└── scripts/
    └── extract_pdfs.py
```

Empty folders should contain `.gitkeep` files so that GitHub keeps the folder structure.

---

## 4. Update Template Files for the New Project

Before using agents heavily, update the project-specific files. These files orient both you and the agents.

---

### 4.1 Update `README.md`

The README should describe the project at a high level.

Suggested structure:

```markdown
# Project Title

## One-sentence description

This project studies ...

## Core question

The main question is ...

## Current status

- Stage: idea / model draft / proof development / writing / revision
- Main file: `paper/main.tex`
- Main notes: `notes/`
- Main literature index: `literature/paper-index.md`

## Repository structure

Brief description of folders.

## Local-only files

PDFs and extracted text are local and ignored by Git.

## How to compile

Open `paper/main.tex` in VS Code and use LaTeX Workshop.
```

Keep the README short. It is a map, not the paper.

---

### 4.2 Update `AGENTS.md`

`AGENTS.md` is the main instruction file for Codex and other project agents.

Update:

```markdown
## Project
```

Replace the template description with a project-specific description.

For example:

```markdown
## Project

This is an economic theory project on coordinated learning in large populations.
The paper studies how information, matching, and strategic complementarities interact in large anonymous populations.
Related themes may include repeated games, random matching, social learning, cheap talk, public reputation, stochastic hidden states, and equilibrium selection.
```

Also update any project-specific rules, such as:

```markdown
## Objects that should not be renamed
```

or:

```markdown
## Equilibrium concept
```

Important: do not make `AGENTS.md` too verbose. It should constrain agents, not duplicate the entire project.

---

### 4.3 Update `paper/main.tex`

Replace the placeholder title, author, abstract, and section names.

Minimum first edit:

```tex
\title{Project Title}
\author{Your Name}
\date{\today}
```

Then confirm the bibliography path is correct.

If `main.tex` is inside `paper/`, the bibliography line should usually be:

```tex
\bibliography{../references}
```

If `main.tex` is in the root folder, it should usually be:

```tex
\bibliography{references}
```

At the top of `main.tex`, keep:

```tex
% !TEX root = main.tex
```

This helps LaTeX Workshop identify the root file.

---

### 4.4 Update `notation.md`

This file records the notation that should remain stable.

At the beginning of the project, it can be incomplete.

Suggested skeleton:

```markdown
# Notation

## Population

- 

## Types

- 

## States

- 

## Actions

- 

## Signals

- 

## Histories

- 

## Matching technology

- 

## Strategies

- 

## Beliefs

- 

## Payoffs

- 

## Equilibrium concept

- 

## Objects that should not be renamed

- 
```

Use this file as soon as notation starts to stabilize. Agents should check this file before rewriting mathematical text.

---

### 4.5 Update `claims-and-results.md`

This file separates proved results from conjectures.

Suggested skeleton:

```markdown
# Claims and Results

## Maintained assumptions

1. 
2. 
3. 

## Proven results

### Proposition 1

Status: draft / checked / proved / needs repair

Statement:

Proof location:

Known gaps:

---

## Conjectures

### Conjecture 1

Statement:

Evidence:

Possible counterexamples:

---

## False starts

- 
```

This file is essential for theory projects. It prevents agents from treating speculative claims as established results.

---

### 4.6 Update `project-log.md`

Start a dated log.

Example:

```markdown
# Project Log

## 2026-05-30

- Created project from theory-research template.
- Added initial LaTeX source.
- Set up Zotero bibliography export.
- Added first central papers to `literature/paper-index.md`.

## Open tasks

- [ ] Confirm paper compiles locally.
- [ ] Fill preliminary notation.
- [ ] Add central papers to Zotero collection.
- [ ] Extract text from selected PDFs.
- [ ] Create first literature notes.
```

The project log is not a diary. It is a lightweight record of research state and open tasks.

---

### 4.7 Update `literature/paper-index.md`

This file is only a map. Do not paste extracted paper text into it.

Use entries like:

```markdown
### Paper short name

Citation key: TBD

PDF: `literature/pdfs/...`

Extracted text: `literature/extracted-text/...`

Status: unread / skimmed / read / central

Use in project: TBD

Difference from my project: TBD

Related note: TBD
```

The fields can be incomplete. The most useful early fields are:

```markdown
PDF:
Extracted text:
Status:
```

The full paper summary belongs in:

```text
notes/literature/
```

not in `literature/paper-index.md`.

---

### 4.8 Update `references.bib`

Do not manually maintain this file unless necessary.

The preferred workflow is:

```text
Zotero collection
    ↓ Better BibTeX automatic export
references.bib
```

For every new project:

1. Create a Zotero collection with the project name.
2. Add relevant papers.
3. Export the collection using Better BibTeX.
4. Export to:

```text
NEW-PROJECT/references.bib
```

5. Enable:

```text
Keep updated
```

Then Zotero updates `references.bib` when the collection changes.

---

## 5. Configure VS Code for the Project

### 5.1 Install Recommended Extensions

VS Code should prompt you to install recommended extensions from:

```text
.vscode/extensions.json
```

At minimum, use:

```text
LaTeX Workshop
Python
```

Optional:

```text
GitHub Pull Requests and Issues
```

---

### 5.2 Select the Python Environment

Use:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Select the project environment, for example:

```text
research-agents
```

If it does not appear, refresh environment managers or restart VS Code.

---

### 5.3 Use Terminal Environments Correctly

A good Windows division of labor is:

```text
Git Bash = Git commands
PowerShell or Anaconda Prompt = conda/Python commands
```

For Git:

```bash
git status
git add .
git commit -m "Message"
git push
```

For Python:

```bash
conda activate research-agents
python scripts/extract_pdfs.py
```

If Git Bash says:

```text
conda: command not found
```

use PowerShell or Anaconda Prompt inside VS Code for Python tasks.

---

## 6. Compile the Paper Locally

Open:

```text
paper/main.tex
```

Use:

```text
Ctrl + S
```

if LaTeX Workshop is set to compile on save.

Manual build:

```text
Ctrl + Alt + B
```

Open PDF preview:

```text
Ctrl + Alt + V
```

Open command palette:

```text
Ctrl + Shift + P
```

Search:

```text
LaTeX Workshop: Build LaTeX project
```

If the project uses `latexmk`, make sure Perl is installed on Windows. With MiKTeX, `latexmk` requires Perl.

---

## 7. Zotero and PDF Workflow

### 7.1 Add Papers to Zotero

For each new paper:

1. Add the paper to Zotero.
2. Put it in the project-specific Zotero collection.
3. Confirm Better BibTeX updates `references.bib`.

---

### 7.2 Add PDFs for Local Agent Access

Agents operating locally can only read files available in the project directory or reachable from it.

Recommended simple workflow:

```text
Copy selected central PDFs into literature/pdfs/
```

Do not put every paper there. Start with central papers only.

The folder is ignored by Git, so PDFs remain local.

---

### 7.3 Extract Text from PDFs

Activate the environment:

```bash
conda activate research-agents
```

Run:

```bash
python scripts/extract_pdfs.py
```

The script reads:

```text
literature/pdfs/
```

and writes:

```text
literature/extracted-text/
```

Run the script again whenever you add new PDFs.

A good extraction script should:

```text
- create one .txt file per PDF;
- overwrite or update the corresponding .txt file;
- avoid duplicate extracted files unless the PDF itself was renamed;
- skip files that are already up to date if that logic is implemented.
```

Do not commit PDFs or extracted text unless there is a specific reason and you have the rights to do so.

---

## 8. Everyday Workflow

### 8.1 Writing Workflow

```text
1. Open `paper/main.tex`.
2. Edit the paper.
3. Save with Ctrl + S.
4. Check the PDF preview.
5. Commit meaningful changes.
```

Suggested commit sequence:

```bash
git status
git add paper/main.tex
git commit -m "Revise model timing section"
git push
```

Use small, meaningful commits. Avoid giant commits with unrelated changes.

---

### 8.2 Literature Workflow

```text
1. Add paper to Zotero collection.
2. Let Better BibTeX update `references.bib`.
3. Copy selected PDF to `literature/pdfs/`.
4. Run `python scripts/extract_pdfs.py`.
5. Add or update entry in `literature/paper-index.md`.
6. Ask an agent to create a literature note in `notes/literature/`.
7. Manually verify important claims before citing.
8. Commit `references.bib`, `paper-index.md`, and the literature note.
```

Suggested commit:

```bash
git add references.bib literature/paper-index.md notes/literature/
git commit -m "Add literature notes on random matching"
git push
```

---

### 8.3 Proof Workflow

```text
1. Write rough proof in `notes/proof-attempts/`.
2. Ask a proof-auditing agent to check it.
3. Repair the argument yourself or with the agent.
4. Once stable, move the cleaned proof into the paper.
5. Update `claims-and-results.md`.
6. Commit.
```

Do not let agents directly convert conjectures into propositions without explicit review.

Suggested commit:

```bash
git add notes/proof-attempts/ claims-and-results.md paper/main.tex
git commit -m "Audit and revise proof of Proposition 1"
git push
```

---

### 8.4 Numerical or Symbolic Check Workflow

```text
1. Put symbolic checks in `code/symbolic/`.
2. Put simulations in `code/simulations/`.
3. Put plotting scripts in `code/plots/`.
4. Save generated figures to `outputs/figures/`.
5. Move only final paper figures into `paper/figures/` if needed.
```

For example:

```bash
python code/symbolic/check_monotonicity.py
python code/plots/plot_example.py
```

Suggested commit:

```bash
git add code/ outputs/figures/ claims-and-results.md
git commit -m "Add numerical check for equilibrium condition"
git push
```

---

### 8.5 Meeting Notes Workflow

After a meeting:

1. Create a file in:

```text
notes/meeting-notes/
```

Example:

```text
notes/meeting-notes/2026-05-30-advisor-meeting.md
```

2. Record:

```markdown
# Meeting Notes: Advisor

Date:

## Main feedback

## Model issues

## Literature suggestions

## To-do items

## Decisions made
```

3. Update `project-log.md` with only the action items and major decisions.

---

## 9. Suggested Agent Roles

For theory research, do not use one generic agent for everything. Use distinct roles through explicit prompts.

---

### 9.1 Project Manager Agent

Purpose:

```text
Organizes tasks, identifies stale files, updates project-log, proposes next steps.
```

Good for:

```text
- creating task lists;
- summarizing project state;
- checking whether documentation files are consistent;
- identifying what needs to be updated before a meeting.
```

Example prompt:

```text
Read README.md, project-log.md, claims-and-results.md, and notation.md.

Do not edit files.

Give me:
1. the current state of the project,
2. the most important unresolved tasks,
3. files that appear stale or incomplete,
4. a recommended work plan for the next two sessions.
```

---

### 9.2 Proof Auditor Agent

Purpose:

```text
Finds logical gaps, hidden assumptions, invalid implications, and ambiguity in equilibrium reasoning.
```

Good for:

```text
- checking propositions;
- finding missing assumptions;
- identifying where compactness, continuity, LLN, fixed-point, or equilibrium-selection arguments are being used;
- separating proof gaps from exposition problems.
```

Example prompt:

```text
Read AGENTS.md, notation.md, claims-and-results.md, and paper/main.tex.

Audit Proposition 1.

Do not rewrite the proof.

Return:
1. the formal claim as stated,
2. the proof strategy,
3. each logical step,
4. any unjustified step,
5. hidden assumptions,
6. whether the result is proved, partially proved, or not yet proved.
```

---

### 9.3 Literature Agent

Purpose:

```text
Reads extracted paper text and creates structured literature notes.
```

Good for:

```text
- summarizing central papers;
- comparing your mechanism with existing papers;
- drafting related-literature notes;
- identifying what needs manual verification.
```

Example prompt:

```text
Read literature/paper-index.md and the extracted text for the paper marked central.

Create a literature note in notes/literature/ using the template.

Do not add claims unsupported by the extracted text.

Include:
1. question,
2. model,
3. main result,
4. mechanism,
5. technical tools,
6. relation to this project,
7. difference from this project,
8. possible citation sentence,
9. things to verify before citing.
```

---

### 9.4 Exposition Editor Agent

Purpose:

```text
Improves clarity while preserving the model, notation, and claims.
```

Good for:

```text
- rewriting introductions;
- making sections clearer;
- improving slide text;
- tightening theorem statements;
- converting rough notes into paper prose.
```

Example prompt:

```text
Read paper/main.tex and notation.md.

Revise only the Introduction section for clarity and flow.

Do not change the model, claims, notation, citations, or theorem statements.

Preserve LaTeX commands and labels.

After editing, report:
1. files changed,
2. substantive claims preserved,
3. any sentences whose meaning you changed.
```

---

### 9.5 Code and Computation Agent

Purpose:

```text
Writes and runs reproducible scripts for symbolic checks, numerical examples, and plots.
```

Good for:

```text
- derivative checks;
- counterexample searches;
- plots;
- parameter grids;
- simulations;
- figure generation.
```

Example prompt:

```text
Create a script in code/symbolic/ to check the sign of the derivative described in notes/proof-attempts/derivative_check.md.

Use sympy where possible.

Do not assume extra parameter restrictions unless explicitly stated.

Print:
1. the symbolic derivative,
2. the conditions under which it has the desired sign,
3. any cases that remain ambiguous.
```

---

## 10. How to Use More Than One Agent for a Task

A good multi-agent workflow means using different prompts or separate Codex/ChatGPT sessions with different roles. The agents do not need to literally talk to each other. You coordinate them through files.

The key principle:

```text
Agent output should become an intermediate artifact that another agent can audit.
```

For example:

```text
Literature Agent → creates note
Proof Auditor → checks whether citation/use is accurate
Exposition Editor → turns verified content into prose
Project Manager → updates project-log and task list
```

---

### Example Task: Add a New Literature Comparison

Goal:

```text
Compare your project to a central paper and add one paragraph to the related literature section.
```

Recommended sequence:

#### Step 1: Literature Agent

```text
Read literature/paper-index.md and the extracted text for [PAPER].

Create or update the literature note in notes/literature/[citekey].md.

Focus on:
1. the model,
2. the main result,
3. the mechanism,
4. the difference from my project.

Do not edit paper/main.tex.
```

Output:

```text
notes/literature/[citekey].md
```

#### Step 2: Researcher Review

Read the note yourself. Verify that the summary is correct.

Mark uncertain parts with:

```markdown
[VERIFY]
```

#### Step 3: Exposition Editor

```text
Using notes/literature/[citekey].md and paper/main.tex, draft one related-literature paragraph.

Do not add new citations beyond the citekey already in references.bib.

Do not overstate novelty.

Return the paragraph first without editing files.
```

#### Step 4: Proof/Logic Auditor

```text
Read the proposed related-literature paragraph and the literature note.

Check whether the comparison is accurate, too strong, or unsupported.

Do not rewrite. Flag risky claims.
```

#### Step 5: Exposition Editor Applies Final Version

```text
Apply the revised paragraph to the related literature section in paper/main.tex.

Preserve citation style and LaTeX formatting.
```

#### Step 6: Project Manager

```text
Update project-log.md and literature/paper-index.md to reflect that [PAPER] has a verified literature note and has been incorporated into the draft.
```

---

### Example Task: Repair a Proof

Goal:

```text
Repair the proof of Proposition 1.
```

Recommended sequence:

#### Step 1: Proof Auditor

```text
Read paper/main.tex, notation.md, and claims-and-results.md.

Audit Proposition 1.

Do not edit files.

Return:
1. proof outline,
2. exact gaps,
3. hidden assumptions,
4. possible repair strategies,
5. whether the statement may need weakening.
```

#### Step 2: Code and Computation Agent, if needed

```text
Create a symbolic or numerical check for the key inequality in the proof of Proposition 1.

Use code/symbolic/ or code/simulations/.

Do not edit the paper.

Report any parameter regions where the inequality fails.
```

#### Step 3: Researcher Decision

Decide whether to:

```text
- add an assumption;
- weaken the proposition;
- change the proof;
- demote the result to a conjecture;
- search for a counterexample.
```

#### Step 4: Exposition Editor

```text
Revise the proof of Proposition 1 according to this decision:

[STATE DECISION]

Preserve notation, labels, and citation style.

After editing, report remaining logical risks.
```

#### Step 5: Proof Auditor Again

```text
Re-audit the revised Proposition 1 proof.

Do not edit files.

State whether the previous gaps were resolved.
```

#### Step 6: Update `claims-and-results.md`

```text
Update claims-and-results.md to reflect the current status of Proposition 1.

Use one of:
- conjecture,
- draft proof,
- checked proof,
- proved subject to assumption,
- false under current assumptions.
```

---

### Example Task: Prepare a Seminar Slide

Goal:

```text
Create a clean Beamer slide explaining the main mechanism.
```

Recommended sequence:

#### Step 1: Project Manager

```text
Read claims-and-results.md and paper/main.tex.

Identify the one mechanism that should be emphasized in a 30-minute talk.

Do not edit files.
```

#### Step 2: Exposition Editor

```text
Draft one Beamer slide explaining the mechanism.

Use concise bullet points.

Avoid dense equations unless essential.

Do not edit files yet.
```

#### Step 3: Proof Auditor

```text
Check the proposed slide for overstatement or imprecise claims.

Flag anything that is not formally established in claims-and-results.md.
```

#### Step 4: Exposition Editor Applies

```text
Add the slide to slides/main.tex.

Preserve the existing Beamer style.
```

---

## 11. Prompt Library

### 11.1 General Diagnostic Prompt

```text
Read AGENTS.md, README.md, project-log.md, notation.md, claims-and-results.md, and paper/main.tex.

Do not edit files.

Give me a diagnostic report on:
1. project structure,
2. missing documentation,
3. notation problems,
4. claims without proof status,
5. citations missing from references.bib,
6. likely next steps.
```

---

### 11.2 LaTeX Compilation Prompt

```text
Try to compile paper/main.tex.

If compilation fails:
1. identify the first meaningful error,
2. explain the cause,
3. propose the minimal fix,
4. do not make broad formatting changes.
```

---

### 11.3 Notation Consistency Prompt

```text
Read notation.md and paper/main.tex.

Check for:
1. variables used but not defined,
2. variables defined but never used,
3. inconsistent notation,
4. overloaded symbols,
5. notation that changes meaning across sections.

Do not edit files.
```

---

### 11.4 Claims Audit Prompt

```text
Read claims-and-results.md and paper/main.tex.

Check whether every proposition, lemma, claim, and conjecture in the paper appears in claims-and-results.md.

Check whether the status in claims-and-results.md matches the paper.

Do not edit files.
```

---

### 11.5 Literature Note Prompt

```text
Read the extracted text for [PAPER] and the entry in literature/paper-index.md.

Create a note in notes/literature/[citekey].md using the literature-note template.

Do not infer missing information from the title alone.

Flag missing or poorly extracted pages.
```

---

### 11.6 Related Literature Paragraph Prompt

```text
Using notes/literature/[citekey].md, draft one paragraph for the related literature section.

Requirements:
- do not overstate novelty;
- distinguish model, mechanism, and result;
- use the existing citation key;
- do not add unsupported claims;
- return the paragraph before editing paper/main.tex.
```

---

### 11.7 Proof Repair Prompt

```text
Repair the proof of [RESULT] using the following decision:

[INSERT DECISION]

Constraints:
- preserve notation from notation.md;
- preserve labels;
- do not change the statement unless explicitly authorized;
- flag any remaining unproved step.
```

---

### 11.8 Counterexample Search Prompt

```text
Create a reproducible script in code/simulations/ to search for counterexamples to [CONJECTURE].

The script should:
1. define all parameters at the top,
2. state parameter restrictions,
3. search over a transparent grid or random seed,
4. print any counterexample,
5. save results to outputs/,
6. not overwrite previous results without warning.
```

---

### 11.9 Plot Prompt

```text
Create a plotting script in code/plots/.

The script should:
1. generate the figure from explicit parameters,
2. save the figure to outputs/figures/,
3. use readable axis labels,
4. avoid hard-coded absolute paths,
5. print the saved file path.
```

---

## 12. Git Workflow

### 12.1 Basic Commands

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Describe the change"
```

Push:

```bash
git push
```

Pull:

```bash
git pull
```

---

### 12.2 Commit Often, But Not Every Save

Good commit messages:

```text
Initialize project from theory template
Add central literature index
Revise timing section
Audit proof of Proposition 1
Add numerical check for learning condition
Update Zotero bibliography export
```

Bad commit messages:

```text
updates
changes
stuff
final
new
```

---

### 12.3 Before a Big Agent Task

Before letting an agent make broad edits:

```bash
git status
git add .
git commit -m "Checkpoint before agent task"
```

Then if the agent makes bad changes, you can inspect or revert.

---

### 12.4 After an Agent Task

Always inspect changes:

```bash
git diff
```

Then compile if relevant.

Then commit:

```bash
git add .
git commit -m "Agent-assisted revision of model section"
git push
```

---

## 13. What Should Be Tracked by Git

Track:

```text
LaTeX source
Markdown notes
Bibliography file
Python scripts
Final generated figures if used in paper/slides
Project documentation
VS Code settings
AGENTS.md
environment.yml
```

Usually do not track:

```text
Raw PDFs
Extracted PDF text
LaTeX auxiliary files
Large temporary outputs
Conda environments
Private credentials
```

The `.gitignore` should enforce this.

---

## 14. What Belongs Where

```text
paper/
    formal LaTeX paper

slides/
    Beamer presentations

notes/literature/
    paper summaries and literature comparisons

notes/proof-attempts/
    informal derivations, failed proofs, partial arguments

notes/model-variants/
    alternative models and abandoned branches

notes/meeting-notes/
    advisor/coauthor/seminar feedback

literature/paper-index.md
    map of papers and paths

literature/pdfs/
    local-only PDFs

literature/extracted-text/
    local-only extracted text

code/symbolic/
    symbolic algebra checks

code/simulations/
    numerical experiments and counterexample searches

code/plots/
    plotting scripts

outputs/figures/
    generated figures

paper/figures/
    figures actually used in the paper
```

---

## 15. Quality-Control Rules for Agent Work

Use these rules consistently:

1. Agents can suggest model changes, but should not silently implement them.
2. Agents can summarize papers, but you must verify important claims.
3. Agents can audit proofs, but you decide whether a result is proved.
4. Agents can generate code, but scripts should be reproducible.
5. Agents should preserve notation unless explicitly told otherwise.
6. Agents should not delete comments, labels, or old proof attempts without permission.
7. Agents should distinguish:
   - proved result,
   - conjecture,
   - numerical evidence,
   - heuristic argument,
   - exposition improvement.
8. Agents should state remaining risks after nontrivial edits.

---

## 16. First-Day Checklist for a New Project

After creating a new project from the template:

```text
[ ] Clone project locally.
[ ] Open project in VS Code.
[ ] Confirm LaTeX Workshop is installed.
[ ] Select Python interpreter.
[ ] Compile `paper/main.tex`.
[ ] Update README.md.
[ ] Update AGENTS.md.
[ ] Update project-log.md.
[ ] Update notation.md skeleton.
[ ] Update claims-and-results.md skeleton.
[ ] Create Zotero collection.
[ ] Export Zotero collection to references.bib using Better BibTeX.
[ ] Add first central PDFs to literature/pdfs/.
[ ] Run scripts/extract_pdfs.py.
[ ] Add entries to literature/paper-index.md.
[ ] Commit and push initial setup.
```

Suggested first commit after edits:

```bash
git add .
git commit -m "Customize template for new project"
git push
```

---

## 17. Standard Weekly Maintenance

Once per week, do the following:

```text
[ ] Compile the paper from a clean save.
[ ] Check `git status`.
[ ] Push all committed changes.
[ ] Update project-log.md.
[ ] Update claims-and-results.md.
[ ] Check whether new citations are in references.bib.
[ ] Check whether central papers have literature notes.
[ ] Remove or archive obsolete proof attempts.
[ ] Make sure important figures are reproducible from scripts.
```

Prompt:

```text
Read project-log.md, claims-and-results.md, notation.md, literature/paper-index.md, and the Git-tracked files.

Give me a weekly maintenance report:
1. stale files,
2. undocumented claims,
3. missing literature notes,
4. likely next tasks,
5. cleanup recommendations.
```

---

## 18. Summary Workflow

The normal research loop is:

```text
Idea
  ↓
notes/proof-attempts/
  ↓
proof audit
  ↓
symbolic/numerical checks if needed
  ↓
claims-and-results.md update
  ↓
paper/main.tex revision
  ↓
compile
  ↓
git commit
  ↓
git push
```

The normal literature loop is:

```text
Zotero collection
  ↓
Better BibTeX export to references.bib
  ↓
selected PDF copied to literature/pdfs/
  ↓
text extraction
  ↓
paper-index.md entry
  ↓
literature note
  ↓
verified related-literature paragraph
  ↓
paper/main.tex
```

The normal agent loop is:

```text
Ask agent to diagnose
  ↓
Review diagnostic
  ↓
Ask agent to make constrained edits
  ↓
Inspect diff
  ↓
Compile/run tests
  ↓
Commit
```

The general rule is:

```text
Agents should help you move faster, but the repository structure should prevent them from making silent, uncontrolled changes to the economics.
```
