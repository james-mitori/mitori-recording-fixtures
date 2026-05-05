# Redo Instructions For Video 001

Video:

```text
video-001-clean-customer-update.mp4
```

Thank you for the first label. The main workflow was captured correctly: the worker opened the customer update spreadsheet, opened the CRM, searched for Acme North, compared the spreadsheet to the CRM, updated the CRM fields, saved the record, and noticed a post-save discrepancy.

We need one revised version so the label can be used for AI benchmarking.

## Why We Need A Revised Version

The first export included one empty step. The updated helper tool now checks for missing fields before export.

The first export also grouped several form updates into one broad step. For benchmarking, we need those split into separate field-level steps.

## Use The Updated Helper Tool

Use:

```text
gold-labeling/simple-labeling-tool.html
```

The top of the page should say:

```text
Version 0.4.0
```

If you already had the helper open:

1. Close the old browser tab.
2. Open `simple-labeling-tool.html` again.
3. Check that it says `Version 0.4.0`.
4. If it still shows an older version, press `Ctrl` + `F5`.

## What To Do Again

1. Open the updated helper tool.
2. Load `video-001-clean-customer-update.mp4` into the helper tool video player.
3. Enter the same video ID:

```text
video-001-clean-customer-update
```

4. Use the helper tool video player for timestamps, or use Windows Media Player side by side.
5. If the internal video feels too small, click `Hide internal video for side-by-side` and type the Windows Media Player timestamp into `Manual timestamp from Windows Media Player`.
6. Click inside the step you are editing, then use `Set start from video time` and `Set end from video time`, or use the manual timestamp `Set start` and `Set end` buttons.
7. Watch the video again.
8. Recreate the steps.
9. Use `Finish step + add next` or `Finish + add next` when you want to end the current step and create the next action.
10. Use `Add next step below` at the bottom of a step when you only want to create a blank next step.
11. Use the `Quick starters` buttons, such as `Clicked`, `Typed`, `Changed`, `Copied`, `Pasted`, and `Saved`, to start common action sentences.
12. Click `Check Label Before Export`.
13. Fix any red error messages.
14. Export both files:

```text
video-001-clean-customer-update.gold.json
video-001-clean-customer-update.gold.md
```

## Important Changes For This Redo

Do not leave any blank step cards in the tool.

Make one step for each important field update instead of one broad "changed the data" step.

For the customer update section, please try to capture separate steps for:

- changing the Account Owner field
- changing the Renewal Date field
- changing the Billing Email field
- adding or changing the Internal Note
- saving the customer record

Also check whether the Status field was changed. If the spreadsheet shows a new status but the CRM still shows a different status, write that in `Observed discrepancies`.

For example:

```text
The spreadsheet shows new_status as Renewal Review, but the CRM Status field still shows Active at the end.
```

Also keep the discrepancy you already noticed if it is visible:

```text
The save message says the summary was updated, but the visible customer list still shows old values.
```

## Good Step Example

```text
Observed action: Worker typed Priya Shah into the Account Owner field.
Screen/app context: Chrome CRM page
Evidence: Account Owner field shows Priya Shah.
```

## Less Useful Step Example

```text
Observed action: Worker changed the data in the fields.
Evidence: The worker copied data from the spreadsheet.
```

That is too broad for this benchmark.

## Confidence

Use `0.9` or `1` only when the action and field value are clear.

Use a lower confidence, such as `0.6` or `0.7`, if the field is hard to read or the action is uncertain.

## Optional

If your manager asks, record your screen while you do the labeling. This helps us improve the instructions and the helper tool. It is okay if you do not record unless asked.
