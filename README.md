# CPPiler
Developed as a project for the Data Structures and Algorithms course  
Department of Mathematics and Computer Science
Iran University of Science and Technology — Fall 2024-2025

---

## About the project
**CPPiler** is a simplified Python-based compiler for a limited subset of C++, developed as the final project for the "Data Structures and Algorithms" course. It performs **lexical analysis**, **token table creation**, **predictive parsing**, and **parse tree generation**.

---

## Phase 1: Lexical Analyzer

This phase involves designing a **DFA (Deterministic Finite Automaton)** to tokenize the input code based on the following token types:

- `reservedword` (e.g., `int`, `float`, `while`, `return`, ...)
- `identifier` (e.g., variable names)
- `number` (e.g., numeric literals)
- `symbol` (e.g., `=`, `+`, `{`, `;`, ...)
- `string` (any text between quotes `"..."`)

**Input:** A restricted C++ code snippet  
**Output:** A list of tokens formatted as `[type, value]`

---

## Phase 2: Token Table & Parse Table

### Token Table

- Uses a custom **Hash Table** to store tokens
- Sorted lexicographically by token name and value (ASCII order)
- Token categories: `string`, `number`, `symbol`, `identifier`, `reservedword`

### Parse Table

- Based on a provided **LL(1) grammar**
- Requires calculation of **FIRST** and **FOLLOW** sets
- Generates a complete predictive **Parse Table**

---

## Phase 3: Non-Recursive Predictive Parser

In this phase, a **Non-Recursive Predictive Parser** is implemented using the Parse Table to:

- Output the production rules used to parse the input
- Construct a **Parse Tree** to represent the code's structure

---

## Bonus Features

- **Tree-based identifier search**: Given an identifier, the parser outputs its first definition in the code.
- **Error handling**: Detects and reports syntax errors such as:
  - Incorrect variable declarations (e.g., `cppiler = x int`)
  - Invalid token sequences or malformed expressions

---
