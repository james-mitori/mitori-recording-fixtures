# Gold Labeling Instructions

Follow these instructions exactly.

## Purpose

You are helping create reference answers for testing an AI workflow discovery system.

Your job is to watch a screen recording and write down what work happened, when it happened, and what evidence supports it.

You are not judging whether the worker did a good job. You are not writing the ideal process. You are only recording what was observed.

## Before You Start

You need:

- the video file
- this `gold-labeling` folder
- a video player with visible timestamps
- a text editor

Do not use the worker recording script while doing your first pass. The first pass should be based on the video itself.

## Step 1: Create Your Output Files

For each video, copy:

```text
templates/workflow_gold_label.template.json
templates/workflow_gold_label.template.md
```

Rename them using the video ID.

Example:

```text
gold-labels/video-001-clean-customer-update.gold.json
gold-labels/video-001-clean-customer-update.gold.md
```

If the `gold-labels` folder does not exist, create it.

## Step 2: Watch The Whole Video Once

Do not pause too much during the first watch.

Write down:

- what apps or websites are used
- what main work appears to be happening
- any obvious workflow starts and ends
- interruptions
- mistakes or corrections
- anything confusing

## Step 3: Watch Again And Mark Timestamps

For each observed workflow, record:

- start time
- end time
- short workflow name
- completion status
- confidence

Completion status examples:

- `completed`
- `partially_completed`
- `abandoned`
- `interrupted_then_completed`
- `unclear`

## Step 4: Record Steps

For each workflow step, record:

- step number
- start time
- end time
- what happened
- screen/app context
- evidence
- confidence
- uncertainty, if any

Every step must have evidence.

Evidence examples:

```json
{
  "timestamp_sec": 75,
  "visible_evidence": "Renewal date field shows 2026-07-31"
}
```

## Step 5: Mark Rework, Interruptions, And Discrepancies

Rework means the user repeats or corrects something.

Interruption means unrelated work appears inside the workflow.

Discrepancy means something visible does not line up with another visible source.

Only mark a discrepancy if the evidence supports it.

## Step 6: Mark Uncertainty

Use uncertainty when something is not clear.

Good uncertainty note:

```text
The user appears to save the record at 100s, but only the confirmation message is visible; exact backend persistence is not observable.
```

Do not guess to make the label look complete.

## Step 7: Final Check

Before submitting, confirm:

- every workflow has a start and end time
- every step has evidence
- guesses are marked as uncertainty
- interruptions and rework are not hidden
- the Markdown summary matches the JSON
- no private or real customer data was added

## File Naming

Use these exact names:

```text
video-001-clean-customer-update.gold.json
video-001-clean-customer-update.gold.md
video-002-invoice-rework.gold.json
video-002-invoice-rework.gold.md
video-003-support-interruption.gold.json
video-003-support-interruption.gold.md
video-004-messy-multi-workflow.gold.json
video-004-messy-multi-workflow.gold.md
video-005-same-role-variant.gold.json
video-005-same-role-variant.gold.md
```
