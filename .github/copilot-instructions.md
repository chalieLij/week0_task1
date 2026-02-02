# GitHub Copilot Instructions – AI-Agent Accelerated ML Workflows

## Project Focus
Accelerate ML/Data Science prototyping with AI agents: data pipelines, preprocessing, model training, evaluation, REST APIs for inference. Emphasize reproducible, verifiable, efficient workflows. Use Python (preferred for ML) or TypeScript/Node for APIs.

## Core Workflow Rules (Inspired by Boris Cherny / Anthropic Practices)
- For ANY non-trivial task (e.g., data processing, model building, endpoint): ALWAYS start in planning mode. Output a clear Markdown plan first: 
  - Research codebase/files
  - Step-by-step approach
  - ML-specific considerations (data splits, metrics, reproducibility, overfitting risks)
  - Files to create/change
  - Verification steps (tests, metrics, plots)
  Wait for "proceed" or approval before implementing.
- After implementation: Automatically verify — run unit/integration tests, compute ML metrics (accuracy, F1, ROC-AUC, etc.), suggest visualizations (matplotlib/seaborn), check for errors/overfitting. Iterate until verified. Propose TDD (tests first) for ML functions.
- If prompt unclear: Ask 1-2 targeted questions (e.g., "Dataset format? Target metric?").
- Learn from errors: After any correction, suggest adding a rule here to prevent recurrence (e.g., "Always use random_state=42 for reproducibility").
- Keep context clean: Reference existing files/patterns (e.g., "Follow preprocessing in data/clean.py").

## ML/Data Science Best Practices
- Use scikit-learn, pandas, numpy, matplotlib/seaborn for basics; torch/PyTorch for deep learning if needed.
- Reproducibility: Set seeds (random_state=42, torch.manual_seed), log versions (requirements.txt).
- Code style: PEP 8, type hints (via typing), small functions, descriptive names.
- Error handling: Graceful for data issues (missing values, shape mismatches), log meaningfully.
- Security: No hard-coded keys; flag potential leaks in ML APIs.
- Efficiency: Prefer vectorized ops over loops; suggest caching (joblib) for expensive computations.

## Resources to Reference
- Coding standards: Follow patterns in existing .py files (if added later).
- ML guidelines: Aim for >80% test coverage on new functions; evaluate models rigorously.

Update this file ruthlessly on repeated issues — compound improvements over time (Boris Cherny principle: edit rules after every mistake to drop error rate).

Tenx MCP logs all interactions for clarity/context/efficiency scoring.