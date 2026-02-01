# Device-Personalized Reinforcement Learning for OS Page Replacement

> **Status:** In active development  
> **Focus:** Operating Systems × Reinforcement Learning × Systems Design  
> **Type:** Trace-driven simulator with learning-based eviction policies

---

## 1. Motivation

Modern operating systems rely on **fixed, heuristic-based page replacement algorithms** such as FIFO, LRU, and LFU. While these heuristics work reasonably well on average, they implicitly assume **generic workloads** and fail to adapt to:

- Device-specific usage patterns  
- Phase changes in application behavior  
- Repetitive workloads on the same machine  

### Key Insight
A single device often exhibits *stable and recurring memory access patterns*. Instead of optimizing for an “average workload,” we can **learn a personalized eviction policy per device** using lightweight reinforcement learning.

This project explores whether a **device-specific RL agent**, trained on memory access traces, can outperform classical heuristics **without violating OS constraints**.

---

## 2. Problem Statement

Given a stream of memory page accesses and a fixed-size cache:

> **Which page should be evicted on a cache miss to minimize future page faults?**

Key challenges:
- The future is unknown
- Decisions must be made online
- Overhead must remain minimal
- Policies must remain safe and stable

---

## 3. Approach Overview

This project implements a **trace-driven OS page replacement simulator** and incrementally augments it with a **learning-based eviction policy**.
