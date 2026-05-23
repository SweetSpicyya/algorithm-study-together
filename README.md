# 📚 Algorithm Study Group

A collaborative repository for our weekly algorithm study group.  
We follow the **[Grind 75](https://www.techinterviewhandbook.org/grind75/?weeks=6&hours=5&difficulty=Easy&difficulty=Medium&order=all_rounded&mode=preferences&grouping=weeks)** problem list (6 weeks · Easy + Medium · All Rounded).

---

## 📅 Schedule

- **Frequency:** 4 problems per week
- **Problem source:** Grind 75 — worked through in order, week by week

---

## 📁 Repository Structure

```
leetcode-study/
├── problems/
│   ├── week01-01-two-sum/
│   │   ├── jane.py
│   │   ├── daniel.ts
│   │   └── README.md
│   ├── week01-02-Valid Parentheses/
│   │   ├── ...
│   │   └── README.md
│   └── ...
└── README.md
```

Each problem lives in its own folder under `problems/`.  
The folder name follows the format: `{week}-{order}-{problem-slug}` (e.g. `week1-01-two-sum`).

---

## 📝 Per-Problem README Format

Each `problems/{slug}/README.md` should include:

```markdown
# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/{slug}/  
**Difficulty:** Easy | Medium  
**Topic:** Array, Hash Table, ...

## Problem Summary
Brief description of the problem in your own words.

## Approaches & Discussion
### {Your Name}
- Approach: ...
- Time Complexity: O(...)
- Space Complexity: O(...)
- Notes: ...
```

---

## 🔀 PR Rules

| Rule                  | Detail                                                          |
|-----------------------|-----------------------------------------------------------------|
| **Branch name**       | `{your name}` (e.g. `Jane`)                                     |
| **Commit & PR title** | `[{week}-{order}] {Problem Title} - {Your Name}`  <br/> (e.g. `[week01-01] Two Sum - Alice`) |
| **PR per problem**    | One PR per person per problem                                   |
| **Deadline**          | Submit PR before the next session                               |

---

## 💻 Solution File Naming

Name your solution file after yourself, using your preferred language extension.

| Member | File        |
|--------|-------------|
| Jane   | `jane.py`   |
| Daniel | `daniel.ts` |
| ...    | ...         |

---

## 🗓️ Grind 75 — Weekly Problem List

> Study 4 problems per week.
> Full list: [techinterviewhandbook.org/grind75](https://www.techinterviewhandbook.org/grind75/?weeks=6&hours=5&difficulty=Easy&difficulty=Medium&order=all_rounded&mode=preferences&grouping=weeks)

| Week | Problems |
|------|----------|
| Week 1 | Two Sum, Valid Parentheses, Merge Two Sorted Lists, Best Time to Buy and Sell Stock |
| Week 2 | Valid Palindrome, Invert Binary Tree, Valid Anagram, Binary Search |
| Week 3 | Flood Fill, Lowest Common Ancestor of BST, Balanced Binary Tree, Linked List Cycle |
| Week 4 | Implement Queue Using Stacks, First Bad Version, Ransom Note, Climbing Stairs |
| Week 5 | Longest Palindrome, Reverse Linked List, Majority Element, Add Binary |
| Week 6 | Diameter of Binary Tree, Middle of Linked List, Maximum Depth of Binary Tree, Contains Duplicate |

---

## ✅ Getting Started

```bash
git clone https://github.com/SweetSpicyya/algorithm-study-together.git
cd algorithm-study/problems

# Create your branch
git checkout -b alice

# Add your solution
mkdir -p ./week01-01-two-sum
touch ./week01-01-two-sum/alice.py

# Commit and push
git add .
git commit -m "[week01-01] Two Sum - Alice"
git push origin alice

# Open a PR on GitHub
create PR on GitHub
PR title "[week01-01] Two Sum - Alice"
```

---

## 👥 Members

| Name   | GitHub                              |
|--------|-------------------------------------|
| Yourim | [@yourim](https://github.com/SweetSpicyya) |
| Rachel | [@rachel](https://github.com/rachelcylee)   |
| Angela | [@angela](https://github.com/YOONSEO99)   |

---
