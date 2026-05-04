# Gold Labeling Pack

This folder is for creating human reference labels for the five Mitori workflow recordings.

The goal is to produce an evidence-backed "gold" version of what happened in each video so AI outputs can be scored against human observation.

Important: the gold label is not an ideal process and not a performance review. It should describe only what is visible or otherwise evidenced.

## Videos To Label

- `video-001-clean-customer-update.mp4`
- `video-002-invoice-rework.mp4`
- `video-003-support-interruption.mp4`
- `video-004-messy-multi-workflow.mp4`
- `video-005-same-role-variant.mp4`

The videos are not stored in this public repository. Your manager will provide them separately.

## What To Produce For Each Video

Create two files per video:

- `gold-labels/<video-id>.gold.json`
- `gold-labels/<video-id>.gold.md`

Use these templates:

- `templates/workflow_gold_label.template.json`
- `templates/workflow_gold_label.template.md`

## Labeling Method

Use a video player that shows timestamps. Watch each video at least twice.

First pass:

- identify workflow starts and ends
- list visible steps in order
- write down timestamps
- note mistakes, rework, interruptions, and uncertainty

Second pass:

- tighten start/end times
- add evidence citations
- confirm whether each step is actually visible
- remove guesses

Optional reconciliation pass:

- after the video-only label is complete, review the fake source files in the fixture folder
- mark discrepancies between what the source data says and what was done on screen
- do not rewrite observations to match the source files if the video shows something different

## Main Rule

Describe observed work, not ideal work.

Good:

```text
At 75s, the worker typed 2026-07-31 into the renewal date field.
```

Bad:

```text
The worker correctly completed the renewal workflow.
```

The second statement judges the process. The gold label should record what happened.

## Adjudication

Best practice is:

1. Labeler A creates an independent label.
2. Labeler B creates an independent label.
3. Reviewer compares both labels and creates the final adjudicated gold label.

Use `templates/adjudication_notes.template.md` for reviewer notes.
