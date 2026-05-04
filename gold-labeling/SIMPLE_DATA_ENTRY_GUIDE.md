# Simple Gold Labeling Guide

This version is for data-entry workers.

You do not need to write JSON by hand. Use the helper tool:

```text
gold-labeling/simple-labeling-tool.html
```

Open it in Chrome or Edge.

## Your Job

Watch the video and write down what you see.

Do not judge whether the person did a good job.

Do not write what should have happened.

Only write what is visible in the video.

## What You Need

- the video file your manager gave you
- this folder
- Chrome or Edge
- headphones are optional

## Step By Step

### 1. Open The Helper Tool

Double-click:

```text
simple-labeling-tool.html
```

If the browser asks permission to open a local video, allow it.

### 2. Load The Video

Click:

```text
Choose File
```

Select the video you are labeling.

Type the video ID exactly, for example:

```text
video-001-clean-customer-update
```

Type your labeler name or worker ID.

### 3. Watch The Video Once

Just watch the whole video.

In the summary box, write a short description of what happened.

Example:

```text
The worker opened a customer update spreadsheet, searched for Acme North in the CRM, changed several fields, and saved the record.
```

### 4. Add Steps

Watch the video again.

Every time the worker does a meaningful action, add a step.

Examples of meaningful actions:

- opens a file
- finds a row in a spreadsheet
- searches in a website
- opens a customer record
- types into a field
- saves a form
- switches to another task
- corrects a mistake

For each step:

1. Pause where the step starts.
2. Click `Use Current Time` in the step start field.
3. Play until the step ends.
4. Click `Use Current Time` in the step end field.
5. Write what happened.
6. Write the evidence you can see.

Good step:

```text
Observed action: Worker typed Priya Shah into the Account Owner field.
Evidence: The Account Owner field shows Priya Shah.
```

Bad step:

```text
Observed action: Worker correctly updated the account.
Evidence: It looks done.
```

The bad example is too vague and judges the work.

### 5. Mark Interruptions

If the worker does something unrelated, write it in the Interruptions box.

Example:

```text
From 42s to 60s, the worker opened a support email before returning to the customer update.
```

If there are no interruptions, write:

```text
None observed.
```

### 6. Mark Rework Or Corrections

If the worker changes something, then fixes or repeats it, write it in the Rework box.

Example:

```text
The worker first typed the wrong invoice amount, then corrected it at 88s.
```

If there is no rework, write:

```text
None observed.
```

### 7. Mark Discrepancies

A discrepancy is when something visible does not match another visible thing.

Example:

```text
The spreadsheet shows status Renewal Review, but the CRM status field still shows Active at the end.
```

If there are no discrepancies, write:

```text
None observed.
```

### 8. Mark Uncertainty

If you are not sure, say so.

Example:

```text
The text in the field is hard to read, so I am not sure whether the email address was typed correctly.
```

Do not guess.

### 9. Export Files

Click:

```text
Export JSON
Export Markdown
```

Send both exported files to your manager.

## Quality Checklist

Before sending your files, check:

- every step has a start time
- every step has an end time
- every step says what was visible
- every step has evidence
- interruptions are listed or say `None observed`
- rework is listed or says `None observed`
- uncertainty is listed if anything was unclear
- you did not include real customer or private data

## If You Get Stuck

Write what you can see and mark the uncertainty.

It is better to write:

```text
I cannot tell what value was entered.
```

than to guess.
