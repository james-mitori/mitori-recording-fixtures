# Mitori Recording Fixtures

Synthetic worker recording fixtures for testing observed workflow discovery.

All data in this repository is fake. Do not add real customer, company, patient, financial, password, or personal information.

## Fastest Worker Download

Download the ready-made worker pack:

[mitori-recording-fixtures-worker-pack.zip](worker-packages/mitori-recording-fixtures-worker-pack.zip)

After downloading, extract the zip and open:

```text
WORKER_INSTRUCTIONS.txt
```

Workers should complete Videos 1, 2, and 3 unless told otherwise.

## Gold Labeling

After recordings are complete, human labelers can create reference workflow labels from the videos.

Start here:

[gold-labeling/README.md](gold-labeling/README.md)

Gold labels are used to measure whether AI workflow extraction agrees with careful human observation. They are not used to judge worker performance.

## What Is Included

The worker pack contains:

- fake customer update spreadsheet
- fake invoice PDF
- fake support email
- fake credentialing checklist
- fake daily notes
- local browser pages for CRM, invoice intake, support case, and credentialing tasks
- worker recording instructions
- Windows screen-recording instructions

## Windows Extraction

In PowerShell, from the folder containing the zip:

```powershell
Expand-Archive -Path .\mitori-recording-fixtures-worker-pack.zip -DestinationPath . -Force
explorer .\mitori-recording-fixtures
```

## Recording Instructions

Open:

```text
mitori-recording-fixtures/WORKER_INSTRUCTIONS.txt
```

For screen recording help, open:

```text
mitori-recording-fixtures/HOW_TO_RECORD_SCREEN.txt
```

## Regenerate Fixtures

For managers or researchers with Python installed:

```bash
python3 scripts/generate_recording_fixtures.py
```

Then rebuild the worker zip:

```bash
cp WORKER_INSTRUCTIONS.md mitori-recording-fixtures/WORKER_INSTRUCTIONS.md
cp WORKER_INSTRUCTIONS.txt mitori-recording-fixtures/WORKER_INSTRUCTIONS.txt
cp HOW_TO_RECORD_SCREEN.md mitori-recording-fixtures/HOW_TO_RECORD_SCREEN.md
cp HOW_TO_RECORD_SCREEN.txt mitori-recording-fixtures/HOW_TO_RECORD_SCREEN.txt
zip -r worker-packages/mitori-recording-fixtures-worker-pack.zip mitori-recording-fixtures
```
