# Gold Labeling Rubric

Use this rubric to judge whether a human gold label is complete enough for scoring AI outputs.

## Required Qualities

### Observed Only

The label describes what happened on screen. It does not invent missing steps, intent, or ideal business logic.

### Timestamped

Every workflow and step has start and end timestamps.

### Evidence-Backed

Every step includes evidence from the video, such as visible screen text, form fields, buttons, files, pages, or confirmation messages.

### Honest About Mess

The label records:

- interruptions
- mistakes
- rework
- abandoned actions
- unclear starts or ends
- visible discrepancies

### Clear Enough To Score

Another person should be able to compare an AI output to the gold label and decide whether the AI matched the human observation.

## Confidence Guide

Use confidence values from `0.0` to `1.0`.

- `0.95` to `1.0`: directly visible and unambiguous
- `0.80` to `0.94`: strongly supported by visible evidence
- `0.60` to `0.79`: likely, but some detail is unclear
- `0.40` to `0.59`: weak evidence
- below `0.40`: do not treat as a firm label; mark uncertainty

## Common Mistakes To Avoid

- writing what should have happened instead of what happened
- copying the worker script instead of observing the video
- hiding mistakes or interruptions
- using vague steps like "processed the file" without evidence
- leaving out timestamps
- leaving out evidence
- treating a confirmation message as proof of unseen backend state
- marking a discrepancy without visible evidence
