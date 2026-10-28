Technical Proposal: Personalized Email Drafts Using LLMs

1. Problem

Businesses send emails to customers for follow-ups, appointment reminders, product updates, and support responses. Writing each email manually takes time, while generic templates may not feel personal. The goal is to generate personalised email drafts using customer information and approved communication guidelines, while maintaining accuracy, privacy, and a consistent brand voice.

2. Recommended Approach

Recommend a Large Language Model (LLM) with a structured prompt and authorised Customer Relationship Management (CRM) data. The system retrieves relevant customer fields and uses a predefined prompt containing the email purpose, customer context, tone, length, and required format. It generates a draft for a human to review.

For example, the prompt can instruct the LLM to write a polite follow-up email using the customer's name, last interaction, and agreed next step. Missing information must not be invented.

A human must approve the draft before sending because the LLM may generate incorrect facts, unsuitable wording, or unintended commitments. Human approval also provides accountability and helps prevent privacy breaches or inappropriate customer communication.

3. Data Requirements

The client must provide:

- Customer fields: Customer name, email address, company, relationship status, previous interactions, product or service details, and relevant follow-up dates.
- Tone guidelines: Approved brand voice, formality level, greeting and closing style, prohibited phrases, and email-length preferences.
- 20 approved sample emails: Examples covering different scenarios, such as follow-ups, thank-you messages, reminders, and support responses.
- Business rules: Email templates, required disclaimers, communication permissions, and rules for handling sensitive information.

Only necessary, authorised CRM data should be used. Access controls and data-retention rules must be defined before implementation.

4. Evaluation Metric

Evaluate generated drafts using the following methods:

- Human rating: Reviewers score relevance, clarity, correctness, and usefulness on a 1–5 scale, targeting an average score of at least 4.2/5.
- Edit distance: Compare generated drafts with approved reference emails to measure the amount of editing required. Use this as a supporting metric, with a target of a normalised edit distance of ≤ 0.30 where reference emails are available.
- Tone checklist: Target at least 95% compliance with the approved tone and brand guidelines.

Also verify factual correctness, privacy compliance, and whether the draft meets the intended email purpose. Evaluation targets should be validated using real business scenarios.

5. Estimated Build Time

Estimated duration: 7–10 working days, assuming CRM access and approved examples are available.

- Days 1–2: Gather requirements, CRM fields, tone guidelines, and sample emails.
- Days 3–4: Design structured prompts and connect authorised CRM data.
- Days 5–6: Generate drafts for representative email scenarios.
- Days 7–8: Evaluate quality, improve prompts, and test privacy safeguards.
- Days 9–10: Add human approval workflow, conduct user testing, and document the solution.

Complex CRM integrations or additional security requirements may increase the timeline.

6. Key Trade-offs

Personalisation can improve customer engagement, but using more customer information increases privacy risks. The solution should use only relevant data and apply appropriate access controls.

LLM costs depend on model choice, prompt length, and email volume; a smaller model may reduce cost but could affect quality. Generated drafts may also contain incorrect facts or unsuitable promises. Therefore, the system should generate drafts rather than send emails automatically. A human must verify customer details, tone, accuracy, and business commitments before approving each email for sending.