# TRP 1 - MCP Setup Challenge  
Task 3: Documentation Report

**Project Title**  
AI-Agent Accelerated Machine Learning Workflows with Tenx MCP

**Author**: Chalie  
**Location**: Addis Ababa, Ethiopia  
**Date**: February 2026  
**IDE & Agent**: VS Code + GitHub Copilot  
**MCP Status**: Tenx MCP Analysis server connected and active throughout all interactions (clarity, context, turn count, efficiency logged automatically).

## 1. What I Did – Changes Made to the Rules File

I created and iteratively refined `.github/copilot-instructions.md` to guide GitHub Copilot toward efficient, reliable Machine Learning & Data Science workflows.

**Major changes & iterations**:
- **v1** (initial): Basic structure with project overview and simple style rules.
- **v2**: Added mandatory **plan-first** rule for all non-trivial tasks (especially ML-related: data prep, modeling, evaluation).
- **v3**: Enforced **automatic verification loop** — run tests, check metrics, suggest visualizations, iterate on failures (inspired by Boris Cherny’s emphasis on verification loops to 2–3× quality).
- **v4 (final)**: 
  - ML-specific guidance: reproducibility (random_state=42), type hints, pandas/sklearn conventions, handling missing values/scaling.
  - Error-learning clause: “After correction, suggest updating these instructions to prevent recurrence.”
  - Kept file concise (~90 lines) to avoid context overload.
  - Tailored toward data science: reference patterns in preprocessing/modeling code, prefer vectorized operations, evaluate rigorously.
- Tested rules on real tasks: e.g., “Plan and implement a data preprocessing function”, “Create ML inference endpoint”, “Fix failing pytest import”.

All changes were committed with clear messages showing progression.  
Final file: `.github/copilot-instructions.md`

## 2. What Worked – Successful Configurations & Approaches

- **Plan-first rule** → Copilot consistently produced structured Markdown plans before coding (steps, assumptions, verification ideas). Reduced wrong-first-attempt code and improved alignment with deliberate ML thinking.
- **Verification loop** → Agent started suggesting/mentioning tests, shape checks, no-NaN asserts, metric computation, before/after comparisons — caught bugs early (especially valuable in data pipelines).
- **Concise ML-focused rules** → Kept agent focused without token bloat. Rules like “set random_state=42” and “prefer vectorized ops” appeared naturally in generated code.
- **Error-learning mechanism** → When I corrected the agent (e.g., wrong scaler or missing import), it sometimes suggested rule additions — showed emerging self-improvement.
- **Overall interaction quality** → Fewer back-and-forth turns, higher clarity/context scores (visible in Tenx MCP logs), no major stalls after rules stabilized.

## 3. What Didn’t Work – Challenges & How I Troubleshot

- **Challenge 1**: Early verbose rules caused partial ignoring or inconsistent behavior.  
  **Fix**: Trimmed to essentials + used “reference patterns in existing files” instead of long lists → much better focus.

- **Challenge 2**: Copilot sometimes skipped planning on “small” tasks despite rule.  
  **Fix**: Clarified wording to “ANY non-trivial task (data processing, modeling, pipelines…)” → planning became consistent.

- **Challenge 3**: Pytest import error (`ModuleNotFoundError: No module named 'src'`) when testing preprocessing function.  
  **Troubleshooting steps**:
  - Confirmed folder structure: `src/preprocessing.py` and `tests/test_preprocessing.py`
  - Tried running `python -m pytest` (sometimes works)
  - Added `pytest.ini` with `pythonpath = src` → tests collected and ran successfully
  - Verified fix by re-running `pytest` from project root

- **Challenge 4**: Occasional MCP connection drops (likely network in Addis Ababa).  
  **Fix**: Restarted VS Code + Copilot extension → reconnected quickly. Kept active for all final tests.

## 4. Insights Gained – How Rules Change Agent Behavior

Rules act like a **persistent system prompt** that shapes the agent’s personality and reasoning:

- **Planning first** mirrors my own workflow: think → outline → verify → execute. This prevents drift, especially critical in ML where wrong preprocessing can ruin downstream modeling.
- **Verification emphasis** turns the agent from “code generator” to “reliable collaborator” — it now proactively suggests tests/metrics/plots, aligning with my expectation of production-grade, reproducible ML code.
- **Reproducibility & ML conventions** baked into rules (seeds, type hints, vectorization) make outputs immediately usable and trustworthy — huge time-saver.
- **Conciseness + update-on-error** creates compounding improvement: each mistake becomes a permanent fix → error rate drops over time (core Boris Cherny insight).
- **Tenx MCP perspective**: Rules lead to clearer prompts from me, better context provision, fewer stalled/inefficient turns → higher-quality logged interactions.

In short: Without rules → helpful but unpredictable assistant.  
With rules → thoughtful pair programmer who anticipates ML needs, self-corrects, and accelerates prototyping.

**Artifacts in this repo**:
- `.github/copilot-instructions.md` (final rules)
- `src/preprocessing.py` (example function created with agent)
- `tests/test_preprocessing.py` (pytest file + fixed import issue)
- `pytest.ini` (solution to src import problem)
- This REPORT.md

Tenx MCP was active throughout → full trace of planning, clarification, implementation, troubleshooting, and verification steps is logged.

Thank you for the opportunity.