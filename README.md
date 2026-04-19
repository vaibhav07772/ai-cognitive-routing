# AI Cognitive Routing & RAG System

## Overview
This project implements a cognitive AI system with:
- Vector-based persona matching
- Content generation pipeline
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

---

## How to Run