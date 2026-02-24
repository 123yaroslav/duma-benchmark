# ACL Rolling Review Submission Form

This document contains the information needed for submitting to ACL Rolling Review (ARR). Fill in all required fields before submission.

## Paper Information

### Title
**DUMA-bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security**

### Authors
List all authors with their affiliations and email addresses. For anonymous submission, this will be hidden during review.

1. **Ivan Aleksandrov**
   - Affiliation: ITMO Security Lab
   - Email: 

2. **German Kochnev**
   - Affiliation: ITMO Security Lab
   - Email: 

3. **Yaroslav Rogoza**
   - Affiliation: ITMO Security Lab
   - Email: 

*Note: Search for author profiles by first, middle, and last name or email address in the ARR system. If profile is not found, add the author by completing all name fields and email address.*

---

## Abstract

LLM-based agent systems are increasingly deployed for automating complex tasks, yet their security in realistic interaction scenarios remains understudied. Existing benchmarks evaluate either isolated agent capabilities or prompt injection resistance in simplified settings, without accounting for the dynamics of active user interaction. We present DUMA-bench (Dual-control User Multi-Agent benchmark), which extends the τ²-bench framework with three new security domains: mail_rag_phishing (RAG system poisoning attacks), collab (inter-agent attacks), and output_handling (improper output processing). The domains cover threat levels 1-5 of the AI-SAFE framework and align with OWASP LLM Top 10 and AI Agents Top 15 classifications.

We evaluate five models (Claude Sonnet 4.5, GPT-4.1, GPT-4o, GPT-4o-mini, GPT-3.5-turbo) while varying user model temperature (T_user ∈ {0.0, 0.5, 1.0}) and report both pass@1 and pass@4 metrics. Results show that: (1) GPT-4o demonstrates superior robustness in RAG poisoning scenarios compared to larger models like GPT-4.1 and Claude Sonnet 4.5, though exhibits instability when evaluating pass@k with higher k; (2) GPT-3.5-turbo shows the most stable performance across temperature variations; (3) model size does not consistently correlate with security robustness. Even the best-performing configurations maintain non-zero Attack Success Rate (ASR), indicating the need for specialized defense mechanisms for agent architectures.

---

## TL;DR
**"Too Long; Didn't Read"**: A short sentence describing your paper (max 100 words)

DUMA-bench evaluates LLM agent security in dual-control environments across five models, revealing that model size doesn't predict security robustness and that mid-sized GPT-4o outperforms larger models in RAG poisoning scenarios.

---

## Paper Files

### PDF
- **Main submission PDF**: `paper.pdf`
- The PDF should include: paper content, references, and any appendices
- Ensure the paper follows ACL formatting guidelines

### Paper Type
Select one:
- [ ] **Long paper** (8 pages + unlimited references)
- [x] **Short paper** (4 pages + unlimited references)

*Note: See the CFP for detailed requirements for short and long papers*

---

## Research Area

### Primary Area
Select the most relevant research area/track:
- [x] **Security and Safety**
- [ ] Machine Learning for NLP
- [ ] Natural Language Generation
- [ ] Question Answering
- [ ] Dialogue and Interactive Systems
- [ ] Other: _______________

---

## Resubmission Information

### Is this a resubmission to ARR?
- [ ] Yes
- [x] No (skip the sections below if No)

### Previous URL
If resubmission, provide the OpenReview URL of your previous submission:
- URL: `https://openreview.net/forum?id=XXXXXXXXXX`

### Previous PDF
- Upload the PDF of your previous ARR submission

### Response PDF
- Upload a PDF containing your responses to previous reviews
- Address each reviewer comment systematically
- Highlight what changes were made

### Reviewer/Editor Reassignment Request
If you believe a previous reviewer or action editor was not qualified:
- Reviewer IDs to reassign (comma-separated): `_______________`
- Add 'AE' for action editor reassignment
- **Use this option sparingly** - only in clear circumstances

### Reassignment Justification
Provide specific reasons for reassignment requests:
- Clear lack of expertise in the area
- Dismissing work without concrete comments
- Other valid criticisms related to review quality

Example justification:
```
Reviewer 2 (ID: XXXX) appeared to lack expertise in agent security,
as evidenced by their comment "I am not familiar with LLM agents"
and subsequent generic criticisms without technical substance.
```

---

## Supplementary Materials

### Software
- Upload one `.tgz` or `.zip` archive (max 200MB)
- Include: source code, scripts, agent implementations
- File: `_______________`

### Data
- Upload one `.tgz` or `.zip` archive (max 200MB)
- Include: datasets, evaluation results, logs
- File: `_______________`

---

## Preprints and Publication

### Anonymous Preprint
Would you like ARR to publish an anonymous preprint of your submission?
- [ ] Yes
- [x] No

### Existing Non-Anonymous Preprints
List any publicly available non-anonymous preprints (provide URLs):
- arXiv: `_______________`
- Other: `_______________`

*Note: Having a non-anonymous preprint does not violate anonymity requirements, but must be disclosed*

---

## Venue Preferences

### Preferred Venue
Enter the designated acronym for your target venue (first choice only):
- Preferred venue: `ACL` (or `EMNLP`, `NAACL`, `EACL`, etc.)

*Note: This is not a firm commitment but helps with planning. You must use the official acronym from the ARR venue list.*

### Potential Venues
Other venues you might consider (for your planning):
1. ACL 2026
2. EMNLP 2026
3. NAACL 2026

---

## Data Sharing and Review Consent

### Consent to Share Anonymized Metadata
**I agree for the anonymized metadata associated with my submission to be included in a publicly available dataset.**

- [x] Yes, I consent
- [ ] No, I do not consent

This dataset **WILL include**:
- Scores and anonymized paper/reviewer IDs
- Acceptance decisions
- Numerical and categorical metadata

This dataset **WILL NOT include**:
- Names, submission titles, or text
- Review texts or author responses
- Any uniquely attributable data

*Your decision does not affect the review of your submission*

### Consent to Review
**By submitting this paper, all authors agree to serve as reviewers for ACL Rolling Review if eligible and invited.**

- [x] Yes, all authors agree
- [ ] No (submission may be rejected)

---

## Responsible NLP Research Checklist

### Research Questions
Answer the following questions from the responsible NLP research checklist:

#### 1. Limitations
- [x] Does your paper discuss the limitations of your work?
- Section: 7 (Limitations)

#### 2. Data
- [x] Does your paper use existing datasets? If yes, provide citations and discuss data collection process.
- We extend τ²-bench with new security domains

#### 3. Human Subjects
- [ ] Does your work involve human subjects?
- N/A - we use LLM simulators

#### 4. Environmental Impact
- [x] Have you considered the computational costs and environmental impact?
- We report API costs and discuss computational requirements

#### 5. Reproducibility
- [x] Do you provide sufficient details to reproduce your work?
- Yes - we provide domain descriptions, hyperparameters, and evaluation protocols

#### 6. Statistical Significance
- [x] Do you report statistical significance and confidence intervals?
- Yes - we use Fisher's exact test and Wilson confidence intervals

#### 7. Ethics Statement
- [x] Have you considered ethical implications?
- We focus on defensive security evaluation to improve LLM agent safety

---

## Submission Checklist

Before submitting, ensure you have:

- [ ] Compiled the final PDF using ACL style files
- [ ] Checked that the paper is properly anonymized (for review)
- [ ] Verified all figures and tables are referenced in text
- [ ] Proofread for grammar and formatting errors
- [ ] Prepared bibliography in ACL format
- [ ] Included all required sections (abstract, introduction, related work, method, experiments, results, conclusion, limitations)
- [ ] Prepared supplementary materials (if any)
- [ ] Completed all fields in this submission form
- [ ] Obtained co-author approval for submission

---

## Additional Notes

### Contact Information (for internal use)
- Corresponding author: `_______________`
- Email: `_______________`
- Alternative contact: `_______________`

### Internal Deadline Tracking
- Paper draft completion: `_______________`
- Internal review deadline: `_______________`
- ARR submission deadline: `_______________`
- Target venue deadline: `_______________`

---

## Submission URLs

### ACL Rolling Review
- Main submission portal: https://openreview.net/group?id=aclweb.org/ACL/ARR
- ARR website: https://aclrollingreview.org/
- Guidelines: https://aclrollingreview.org/cfp

### Style Files and Resources
- ACL style files: https://github.com/acl-org/acl-style-files
- Formatting guidelines: https://acl-org.github.io/ACLPUB/formatting.html

---

**Document last updated**: 2026-02-23
