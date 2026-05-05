# Simple Gold Labeling Guide

This version is for data-entry workers.

You do not need to write JSON by hand. Use the helper tool:

```text
gold-labeling/simple-labeling-tool.html
```

Open it in Chrome or Edge.

The current helper tool version is shown at the top of the page. Use version `0.3.0` or newer.

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

### 1. Put The Files Somewhere Easy

Create one folder on your Desktop called:

```text
Mitori Gold Labeling
```

Put these files/folders inside it:

- the video file or files your manager gave you
- this `gold-labeling` folder

Example:

```text
Desktop
└── Mitori Gold Labeling
    ├── video-001-clean-customer-update.mp4
    └── gold-labeling
        ├── SIMPLE_DATA_ENTRY_GUIDE.md
        └── simple-labeling-tool.html
```

### 2. Open The Helper Tool

Double-click:

```text
simple-labeling-tool.html
```

It should open in Chrome or Edge.

If you already had the helper tool open from an earlier attempt:

1. Close that browser tab.
2. Open `simple-labeling-tool.html` again from the folder.
3. Check that the top of the page says `Version 0.3.0` or newer.
4. If it still shows an older version, press `Ctrl` + `F5` to refresh the page.

If Windows asks how to open it:

1. Choose `Chrome` or `Edge`.
2. If you do not see either option, choose `Open with`.
3. Select `Google Chrome` or `Microsoft Edge`.

### 3. Load The Video In The Helper Tool

Click:

```text
Choose File
```

Select the video you are labeling.

This loads the video inside the helper tool.

Use the helper tool video player for timestamps. Do not open the video in another player unless the helper tool cannot load the video.

The tool will fill in the video ID from the file name when possible. Check that it is correct.

Type your labeler name or worker ID.

### 4. Use The Video Workstation

The video stays visible on the left while you fill out steps on the right.

Use these controls:

- `Play/Pause` starts or stops the video.
- `Back 5s`, `Back 1s`, `Forward 1s`, and `Forward 5s` move around the video.
- `Set Step Start` fills the start time for the active step.
- `Set Step End` fills the end time for the active step.
- `Set Workflow Start` and `Set Workflow End` fill the whole workflow times.
- `Bigger Video` gives the video more space.
- `Speed` slows down or speeds up playback.

Click inside a step to make it the active step. The active step is highlighted.

Keyboard shortcuts work when you are not typing in a field:

- `Space`: play or pause
- `A`: set active step start time
- `S`: set active step end time
- `Left Arrow`: back 1 second
- `Right Arrow`: forward 1 second
- `Shift` + `Left Arrow`: back 5 seconds
- `Shift` + `Right Arrow`: forward 5 seconds

The Step Review box shows all steps and helps you jump back to a step.

### 5. Watch The Video Once

Just watch the whole video.

In the summary box, write a short description of what happened.

Example:

```text
The worker opened a customer update spreadsheet, searched for Acme North in the CRM, changed several fields, and saved the record.
```

Do not worry about exact steps during the first watch.

### 6. Add Steps

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
2. Click inside the step so it is highlighted.
3. Click `Set Step Start`, or click `Use Current Time` under the step start field.
4. Play until the step ends.
5. Click `Set Step End`, or click `Use Current Time` under the step end field.
6. Write what happened.
7. Write the evidence you can see.

Use short, clear step labels.

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

### 7. How Detailed Should Steps Be?

Use one step for each meaningful action.

Too broad:

```text
The worker updated the customer.
```

Better:

```text
The worker opened the customer spreadsheet.
The worker found the Acme North row.
The worker searched for Acme North in the CRM.
The worker changed the Account Owner field to Priya Shah.
The worker changed the Renewal Date field to 2026-07-31.
The worker changed the Billing Email field to ap-north@example.test.
The worker added the internal note.
The worker saved the record.
```

Do not create a separate step for every tiny mouse movement.

When the worker changes several fields on one form, split them into separate steps. This helps us compare the human label to the AI label.

### 8. Mark Interruptions

If the worker does something unrelated, write it in the Interruptions box.

Example:

```text
From 42s to 60s, the worker opened a support email before returning to the customer update.
```

If there are no interruptions, write:

```text
None observed.
```

### 9. Mark Rework Or Corrections

If the worker changes something, then fixes or repeats it, write it in the Rework box.

Example:

```text
The worker first typed the wrong invoice amount, then corrected it at 88s.
```

If there is no rework, write:

```text
None observed.
```

### 10. Mark Discrepancies

A discrepancy is when something visible does not match another visible thing.

Example:

```text
The spreadsheet shows status Renewal Review, but the CRM status field still shows Active at the end.
```

If there are no discrepancies, write:

```text
None observed.
```

### 11. Mark Uncertainty

If you are not sure, say so.

Example:

```text
The text in the field is hard to read, so I am not sure whether the email address was typed correctly.
```

Do not guess.

### 12. Save A Draft If You Need A Break

If you need to stop before finishing:

1. Click `Save Draft In Browser`.
2. Leave the browser installed and do not clear browser data.
3. When you come back, open the same helper tool.
4. Click `Load Draft`.

Important: the draft is only saved on that computer and in that browser.

### 13. Export Files

Before exporting, click:

```text
Check Label Before Export
```

If the tool shows a red error message, fix the listed problems before exporting.

The tool will not export if required fields are missing.

Click:

```text
Export JSON
Export Markdown
```

This downloads two files.

They should look like this:

```text
video-001-clean-customer-update.gold.json
video-001-clean-customer-update.gold.md
```

Send both exported files to your manager.

Do not rename them unless your manager asks you to.

## Worked Example Of One Step

Imagine the video shows the worker typing an email address into a Billing Email field.

You might enter:

```text
Start time: 85
End time: 95
Observed action: Worker entered ap-north@example.test into the Billing Email field.
Screen/app context: Chrome CRM page
Evidence: Billing Email field shows ap-north@example.test.
Confidence: 0.9
Uncertainty: blank
```

If the email is hard to read:

```text
Observed action: Worker entered a billing email address.
Evidence: Billing Email field contains an email address, but it is hard to read.
Confidence: 0.6
Uncertainty: Exact email address is not clear.
```

## Quality Checklist

Before sending your files, check:

- every step has a start time
- every step has an end time
- every step end time is after the start time
- every step says what was visible
- every step says which app/screen was visible
- every step has evidence
- there are no empty step cards
- if several fields were changed, each important field change has its own step
- interruptions are listed or say `None observed`
- rework is listed or says `None observed`
- discrepancies are listed if something visible does not match
- uncertainty is listed if anything was unclear
- you did not include real customer or private data

## Common Problems

### I cannot see the timestamp

Move your mouse over the video player. The playback bar and time usually appear at the bottom.

### I cannot get the exact second

Pause as close as you can. A few seconds difference is okay.

### The helper tool timestamp button does not work

Check that the video is loaded in the helper tool and that you clicked inside the step you are editing.

If the helper video still will not play, tell your manager:

```text
The helper tool video player is not working for this video.
```

Only use another video player if your manager tells you to.

### I do not understand what the worker is doing

Write what you can see. Example:

```text
The worker opened a form page and typed into a field. The exact purpose of the form is unclear.
```

### The video is blurry

Write that in uncertainty:

```text
Some field values are blurry and hard to read.
```

## If You Get Stuck

Write what you can see and mark the uncertainty.

It is better to write:

```text
I cannot tell what value was entered.
```

than to guess.
