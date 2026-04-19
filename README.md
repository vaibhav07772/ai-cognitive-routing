# AI Cognitive Routing & RAG System

## Overview
This project implements a cognitive AI system with:

- Vector-based persona matching
- Content generation pipeline (LangGraph-style)
- RAG-based defense against prompt injection

---

## Phase 1: Routing
Uses embeddings + cosine similarity to match posts with relevant bot personas.

---

## Phase 2: Content Generation
Simulates AI agents generating posts using persona + search context.

---

## Phase 3: Defense System
Implements RAG-style context understanding and protects against prompt injection attacks.

---

## Prompt Injection Defense
We enforce strict system rules to:
- Ignore malicious instructions
- Maintain persona consistency
- Continue logical argument

---

## Tech Stack
- Python
- Sentence Transformers
- NumPy
- LangGraph (concept)

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
