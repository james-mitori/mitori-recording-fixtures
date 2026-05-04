# Worker Instructions: Mitori Test Recordings

## What You Are Doing

You will record your screen while completing simple fake office tasks.

These recordings help test software that watches normal computer work and identifies the steps in a workflow.

All data is fake. Do not use any real customer, company, patient, financial, password, or personal information.

## Before You Start

If you received a zip file, extract it first.

On Windows PowerShell:

```text
Expand-Archive -Path .\mitori-recording-fixtures-worker-pack.zip -DestinationPath . -Force
```

Then open the extracted folder.

You should now have a folder named:

```text
mitori-recording-fixtures
```

Inside the folder, you should see files like:

- `customer_updates.csv`
- `invoice_1048.pdf`
- `support_email.txt`
- `daily_notes.txt`
- `credentialing_checklist.txt`
- `fake_crm.html`
- `invoice_intake_form.html`
- `support_case_form.html`
- `credentialing_portal.html`

If any of these files are missing, stop and ask for help.

You do not need Python. You do not need to generate any files yourself.

## Recording Rules

Follow these rules for every recording:

1. Record your full screen.
2. Keep your mouse cursor visible.
3. Do not talk during the recording.
4. Do not explain what you are doing out loud.
5. Do not pause or edit the recording.
6. Work at a normal pace.
7. If you make a mistake, correct it normally. Do not restart.
8. Use only the fake files provided.
9. Do not open real email, real work systems, password managers, banking websites, private chats, or personal files.
10. Stop the recording only after the task is finished.

## How To Record Your Screen

Use the separate file:

```text
HOW_TO_RECORD_SCREEN.md
```

Recommended method:

1. Open Windows `Snipping Tool`.
2. Choose the video/record option.
3. Select the full screen.
4. Start recording.
5. Complete the task.
6. Stop and save the video with the required filename.

If Snipping Tool does not have a record option, check `HOW_TO_RECORD_SCREEN.md` for other options.

## Recommended Screen Setup

Before recording:

1. Close private or unrelated windows.
2. Open the `mitori-recording-fixtures` folder.
3. Make sure the browser is available.
4. Make sure the screen recorder is ready.
5. Start with a clean desktop or the fixtures folder visible.

## File Naming

Name the videos exactly like this:

```text
video-001-clean-customer-update.mp4
video-002-invoice-rework.mp4
video-003-support-interruption.mp4
video-004-messy-multi-workflow.mp4
video-005-same-role-variant.mp4
```

If your recorder saves in another format like `.mov` or `.mkv`, keep the same name and use that extension.

## Required Recordings

Please complete Videos 1, 2, and 3.

Videos 4 and 5 may be requested if more recordings are needed.

---

# Video 1: Clean Customer Update

## Goal

Update the fake customer record for `Acme North` using information from the spreadsheet.

## Files To Use

- `customer_updates.csv`
- `fake_crm.html`

## Steps

1. Start screen recording.
2. Open `customer_updates.csv`.
3. Find the row for `Acme North`.
4. Open `fake_crm.html` in the browser.
5. In the CRM page, search for `Acme North` or `C-10017`.
6. Click `Open record`.
7. Compare the spreadsheet row with the CRM record.
8. Update the CRM fields using the spreadsheet:
   - Account owner: `Priya Shah`
   - Status: `Renewal Review`
   - Renewal date: `2026-07-31`
   - Billing email: `ap-north@example.test`
9. Click `Save customer record`.
10. Make sure the success message is visible.
11. Stop recording.
12. Save the video as:

```text
video-001-clean-customer-update.mp4
```

---

# Video 2: Invoice With Mistake And Correction

## Goal

Enter a fake invoice into the invoice intake form. Make one mistake first, then correct it.

## Files To Use

- `invoice_1048.pdf`
- `invoice_intake_form.html`

## Correct Invoice Details

Use these correct values:

- Vendor: `Mitori Fixture Supplies Ltd`
- Invoice number: `1048`
- Issue date: `2026-05-01`
- Due date: `2026-05-31`
- Department: `Operations`
- Total amount: `1426.00`

## Steps

1. Start screen recording.
2. Open `invoice_1048.pdf`.
3. Open `invoice_intake_form.html` in the browser.
4. Start entering the invoice details into the form.
5. Make one intentional mistake:
   - Enter the total amount as `1246.00` instead of `1426.00`.
6. Continue filling the form for about 20 to 40 seconds.
7. Go back to the invoice PDF.
8. Check the total amount again.
9. Return to the invoice form.
10. Correct the total amount to `1426.00`.
11. Click `Validate invoice`.
12. If a warning appears, review the fields.
13. Click `Submit invoice`.
14. Make sure the success message is visible.
15. Stop recording.
16. Save the video as:

```text
video-002-invoice-rework.mp4
```

---

# Video 3: Support Case With Interruption

## Goal

Create a fake support case, interrupt yourself with an unrelated notes task, then return and finish the support case.

## Files To Use

- `support_email.txt`
- `support_case_form.html`
- `daily_notes.txt`

## Support Case Details

Use the information in `support_email.txt`.

Important values:

- Customer: `Acme North`
- Account ID: `C-10017`
- Priority: `Medium`
- Category: `Billing Portal`
- Issue: AP contact cannot access the billing portal

## Steps

1. Start screen recording.
2. Open `support_email.txt`.
3. Open `support_case_form.html` in the browser.
4. Begin filling in the support case form.
5. Enter the customer, account ID, priority, category, and issue summary.
6. Before submitting the case, switch away to an unrelated task.
7. Open `daily_notes.txt`.
8. Read the note.
9. Do one small interruption task, such as typing this into a scratch note or document:

```text
Follow up with Casey after support case is submitted.
```

10. Spend about 1 to 2 minutes on this interruption.
11. Return to the support case form.
12. Finish any missing fields.
13. Click `Submit case`.
14. Make sure the success message is visible.
15. Stop recording.
16. Save the video as:

```text
video-003-support-interruption.mp4
```

---

# Video 4: Messy Multi-Workflow Session

Only complete this video if requested.

## Goal

Complete several small office tasks in one recording, with context switching.

## Files To Use

- `customer_updates.csv`
- `fake_crm.html`
- `invoice_1048.pdf`
- `invoice_intake_form.html`
- `credentialing_checklist.txt`
- `credentialing_portal.html`

## Steps

1. Start screen recording.
2. Open `customer_updates.csv`.
3. Open `fake_crm.html`.
4. Update the `Acme North` customer record and save it.
5. Open `invoice_1048.pdf`.
6. Open `invoice_intake_form.html`.
7. Start entering the invoice details.
8. Stop halfway through the invoice task.
9. Open `credentialing_checklist.txt`.
10. Open `credentialing_portal.html`.
11. Mark `License verified` as complete.
12. Return to the invoice form.
13. Finish entering the invoice details.
14. Submit the invoice.
15. Open `customer_updates.csv` again and check another row.
16. Do not update anything else.
17. Stop recording.
18. Save the video as:

```text
video-004-messy-multi-workflow.mp4
```

---

# Video 5: Same Role, Different Path

Only complete this video if requested.

## Goal

Update a fake customer record, but do the steps in a different order than Video 1.

## Files To Use

- `customer_updates.csv`
- `fake_crm.html`

## Steps

1. Start screen recording.
2. Open `fake_crm.html` first.
3. Search for `Acme North` or `C-10017`.
4. Open the record.
5. Look at the fields and pause briefly as if you realize you need the source data.
6. Open `customer_updates.csv`.
7. Find the row for `Acme North`.
8. Return to the CRM page.
9. Update the fields:
   - Account owner: `Priya Shah`
   - Status: `Renewal Review`
   - Renewal date: `2026-07-31`
   - Billing email: `ap-north@example.test`
10. Save the record.
11. Use the search/list area to verify the record is complete.
12. Stop recording.
13. Save the video as:

```text
video-005-same-role-variant.mp4
```

## Final Checklist Before Sending Files

For each video, check:

- The screen is visible.
- The cursor is visible.
- The recording includes the full task.
- There is no real private information.
- There is no voice narration.
- The file name is correct.
- The video opens and plays.

Send back the completed video files using the upload method provided by the project manager.
