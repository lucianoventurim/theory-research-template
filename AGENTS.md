# AGENTS.md

## Project

This is an economic theory project on coordinated learning in large populations.

The paper studies learning, coordination, and equilibrium behavior in large-population or random-matching environments. Related themes may include repeated games, anonymous random matching, social learning, cheap talk, public reputation, stochastic hidden states, and equilibrium selection.

## Source of truth

- The main paper is in `paper/main.tex`.
- Notation is tracked in `notation.md`.
- Claims, propositions, conjectures, and proof status are tracked in `claims-and-results.md`.
- Literature notes are in `notes/literature/`.
- Raw or extracted paper text may exist locally in `literature/extracted-text/`, but this folder is not tracked by Git.

## Core rules

- Do not invent assumptions, theorem statements, citations, or references.
- Do not cite a paper unless it appears in `references.bib`, `literature/paper-index.md`, or a literature note.
- Do not infer a paper's content from its title alone.
- Do not rename variables without updating `notation.md`.
- Do not change the economic model unless explicitly asked.
- Do not delete commented LaTeX unless explicitly asked.
- Preserve equation labels, theorem labels, citation keys, and cross-references.

## Proof-auditing rules

When checking a proof, distinguish between:

1. algebraic mistakes,
2. missing assumptions,
3. unjustified inequalities,
4. continuity/compactness issues,
5. equilibrium-concept issues,
6. exposition problems.

Flag any use of:

- law of large numbers,
- large-population approximation,
- fixed-point theorem,
- martingale convergence,
- continuity of payoff correspondences,
- upper hemicontinuity,
- equilibrium selection,
- public/private belief consistency,
- one-shot deviation principle,
- purification or limiting arguments.

Never say a proposition is proved unless every step is accounted for.

## Literature rules

When summarizing a paper, use this structure:

1. Question.
2. Model.
3. Main result.
4. Mechanism.
5. Technical tool.
6. Relation to this project.
7. Difference from this project.
8. Possible citation sentence.
9. Things to verify.

If the extracted text is incomplete, say so.

## LaTeX rules

- Keep the project compilable.
- Use the existing citation style.
- Do not add packages without checking the preamble.
- Avoid changing notation for stylistic reasons.
- Preserve all comments unless explicitly asked to clean them.

## Code rules

- Put symbolic checks in `code/symbolic/`.
- Put simulations in `code/simulations/`.
- Put plotting scripts in `code/plots/`.
- Save generated figures to `outputs/figures/`.
- Save parameter values used in counterexamples.