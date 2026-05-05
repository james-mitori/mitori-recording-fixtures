# Trainer Script: First-Time Labeler Virtual Onboarding

A structured 75–90 minute walkthrough you run **over a video call with screen share**, using `labeling-workstation.html` and `video-001-clean-customer-update.mp4` as the worked example.

The script alternates between **Say** (verbatim or paraphrased), **Do** (something you ask the trainee to click / hover / type — they drive their own machine), and **Check** (ask the trainee a question to confirm understanding). Italic notes are for you, not the trainee.

> _Trainer note: Read the whole script once before delivering. The trainee shares their screen the entire session — you do not need to share yours except briefly during the tool tour. Most of your job is narrating, prompting, and watching their right pane. If they hit a tough spot, slow down — getting Steps 1–3 right matters more than finishing the whole video in one session._

---

## Before the session (24 hours ahead)

Send the trainee a short prep email or Slack message. Sample below — fill in the bracketed parts.

```
Subject: Mitori labeling onboarding — prep for [DATE]

Hi [name],

Quick prep for our session at [TIME, TIMEZONE]. Plan ~90 minutes
plus 20 minutes optional solo practice at the end.

Before we start, please:

1. Download the labeling tool and example video to your computer
   from [SHARED LINK / FOLDER URL]:
     - labeling-workstation.html
     - video-001-clean-customer-update.mp4

2. Open labeling-workstation.html in Chrome. The topbar should read
   "Mitori · Gold Labeling Workstation". If you see a different
   filename like simple-labeling-tool.html, you have the wrong file.

3. Make sure the video plays locally. Double-click it to confirm.
   If it doesn't play, install VLC.

4. Close other browser tabs and apps that aren't needed. We'll be
   doing keyboard shortcuts and you don't want Slack stealing them.

5. Be on a wired connection or strong wifi. We'll be screen-sharing
   for ~90 minutes.

The session will be recorded for QA review only.

See you at [TIME].
[trainer]
```

---

## At session start (5 min, before the script proper)

1. **Confirm the call works** — both audio directions, screen share visible. Ask: _"Can you hear me clearly? Can you see my cursor when I move it?"_
2. **Ask the trainee to share their screen.** Whole desktop, not just one window — you'll need to see the file picker, browser, and any system dialogs.
3. **Confirm they have the right files open:**
    - `labeling-workstation.html` open in Chrome
    - `video-001-clean-customer-update.mp4` saved locally and findable
4. **Confirm the topbar reads "Mitori · Gold Labeling Workstation".** If they have an older `simple-labeling-tool.html`, send them the right file before continuing.
5. **Ask them to clear any leftover drafts.** Easiest: have them open DevTools (`F12` or `Cmd+Opt+I`), paste this into the Console tab, and reload:
   ```
   Object.keys(localStorage).filter(k => k.startsWith('mitori.')).forEach(k => localStorage.removeItem(k))
   ```
   _If they're not comfortable with DevTools, skip this — the autosave will key by video ID anyway._
6. **State the recording disclaimer if you're recording:** _"I'm recording this session for QA review only. The recording stays internal. Is that OK?"_
7. **Tell them:** _"You drive the keyboard the whole way. I'll narrate and ask you to click or hover specific things. Don't move ahead of me — pause and ask if anything's unclear."_

---

## Section 1 — Why this exists (5 min)

**Say:** "We're building a benchmark to grade an AI system. The AI watches the same screen recordings you'll watch, and tries to figure out what work happened. Your labels are the human reference — the gold answer the AI gets graded against. So your job is not to judge whether the worker did a good job, or to write what should have happened. Your job is to describe **only what was visible on screen**, with timestamps."

**Say:** "If you write a perfect-sounding label that doesn't match what's actually visible, it's worse than no label at all — because the AI might be marked wrong for being right, or right for being wrong. So precision over polish."

**Check:** "What's the difference between 'the worker submitted the form' and 'the worker tried to submit the form'?"

> _Looking for: they recognise that "tried to" describes intent, not what was visible. The first is observable; the second is a guess._

**Say:** "Three things you'll get reminded of throughout: describe what's visible, write the evidence you can quote, and don't hide messy parts — interruptions and mistakes are exactly what the benchmark needs."

---

## Section 2 — Tool tour (10 min)

> _Trainer note: Don't teach them to label yet. Just orient them in the workspace. Since you can't physically point, ask the trainee to **hover their cursor** on each element as you narrate — moving cursors are easy to follow over screen share, static fingers aren't._

### Topbar (the strip at the top)

**Do:** Ask the trainee to hover their cursor on each element left to right as you describe it.

- **Mitori · Gold Labeling Workstation** — branding, no function.
- **Breadcrumb (No video loaded · no labeler · no workflow named · Edit)** — the current session info. Updates as you fill the setup. Click `Edit` to change it later.
- **Step counter** — appears once you have steps, shows `N steps` plus warnings if anything's incomplete or invalid.
- **Saved indicator** — green dot + "Saved Xs ago." Your work is autosaved every 600ms after edits. Hover for details.
- **Guide / ? / Side-by-side / Wrap up & export** — four buttons on the right.

**Say:** "If at any point you forget what something means, hit the Guide button. It's a one-page reference with the same buttons and pills you'll see in the labeling area. Click it now."

**Do:** Trainee clicks **Guide**. Walk through the four cards briefly while they scroll: required step pieces, exception types, reading the timeline, common mistakes. Ask them to close it.

**Say:** "Now click the question mark icon next to Guide."

**Do:** Trainee clicks **?**. Walk through the shortcut overlay briefly. Don't make them memorise — just confirm they see it. Ask them to close it.

**Say:** "You can press `?` anywhere in the tool to bring this overlay back."

### Two-pane workspace

**Say:** "Now sweep your eyes across the workspace from left to right and tell me what the two big columns are for."

> _Looking for: they recognise that the left column is the video + timeline, and the right column is where labels go. If they can't, narrate it yourself: left ≈ 2/3 (video + timeline track), right ≈ 1/3 (active step editor + step list)._

**Say:** "You'll spend most of your time looking at the video on the left and pressing keyboard shortcuts. The right pane is where the labels live and where you'll glance to confirm your work was captured."

### Timeline track (under the video)

**Say:** "Hover your cursor on the empty strip just below the video player — it should say 'Load a video to see the timeline.'"

**Do:** Confirm via screen share that they're hovering on the right thing.

**Say:** "Once a video is loaded, every step you create becomes a coloured block on this strip. You can click a block to jump to it, or drag its edges to nudge times. We'll see this in a few minutes."

### Notes drawer

**Say:** "Look at the right edge of the screen. There should be a vertical 'Notes' tab pinned there."

**Do:** Confirm via screen share that they see it.

**Say:** "This is for things that don't fit a single step — discrepancies between sources, or 'I couldn't tell' notes about the whole video. Press `N` to open it."

**Do:** Trainee presses `N`. Confirm two text areas appear (Observed discrepancies, Whole-video uncertainty). Ask them to press `N` again to close.

> _Trainer note: Do NOT explain exception types yet. We'll cover those when we hit one in the example video. Premature jargon overload is the main reason early labels are inconsistent._

**Check:** "Where do interruptions and rework go — the Notes drawer or on the step itself?"

> _Looking for: on the step itself. The drawer is only for whole-video stuff. Refer back to the Guide if they're unsure. Over a video call you'll often want to repeat what they said back to them — "right, on the step" — to make sure you both heard the same thing._

---

## Section 3 — Set up the example video (5 min)

**Say:** "Let's load video-001."

**Say:** "Click the **Edit** link in the breadcrumb up top — or **Open setup** if you see that big red button. The setup panel will open."

**Do:** Confirm the setup modal is open on their screen.

> _Trainer note: When the file picker dialog opens you may NOT see it over screen share, depending on the conferencing tool — system dialogs are often hidden in privacy modes. Ask the trainee to read out the filename they're picking before they confirm it._

**Do:** Walk through each field in the setup modal as the trainee fills it. Ask them to read the filename aloud when they pick the video file.

| Field | What to type |
|---|---|
| Video file | Choose `video-001-clean-customer-update.mp4` (read aloud to confirm) |
| Telemetry sidecar | Skip (we don't have one for this fixture) |
| Video ID | `video-001-clean-customer-update` (auto-fills from filename — confirm) |
| Your name or worker ID | The trainee's worker ID |
| Workflow name | `Update customer record in CRM` |

**Say:** "Notice that there's no 'completion status' or 'summary' here. Those need the whole video watched first — you'll be prompted at export time."

**Say:** "Now click **Start labeling**."

**Check:** "What does the topbar show now?"

> _Looking for: they see the video ID, their worker ID, and the workflow name in the breadcrumb. The Saved indicator probably reads 'Saved just now'. If you can't read the topbar over screen share, ask them to read it aloud._

---

## Section 4 — First-pass watch (10 min)

**Say:** "Standard practice: watch the whole video once without labeling. You're trying to get the shape of what happened. We'll label on the second pass."

> _Trainer note: Screen share usually drops the framerate of embedded video to 5–10 fps, and small UI text inside the recording can be hard to read on your end. That's fine — the trainee is watching it natively at full quality. You're listening to their reactions, not reading their screen. Tell them so they don't worry about how it looks on your end._

**Say:** "I might not see the video as clearly as you do — screen share blurs it. You're watching it at full quality. If you see something interesting, tell me out loud — name the app, name the field, describe what just changed."

**Say:** "Press **Space** to play. Don't pause unless something is genuinely confusing."

> _Trainer note: While the video plays, narrate what to watch for, but DON'T label yet. Sit on your hands._

**Say (during playback):** "Listen for these phases: opening a source file, opening a destination system, finding the right record, comparing values, updating fields one by one, saving, and reacting to whatever's on screen after save."

When the video ends:

**Say:** "Don't open the right pane yet. Just tell me, in your own words, what happened."

> _Trainer note: Let them recap. Common things they should mention: spreadsheet, CRM, customer name (Acme North), some fields changed (Account Owner, Renewal Date, Billing Email, Internal Note), saved, something didn't quite match at the end. If they miss the post-save discrepancy, ask: "Did anything look off after the save?"_

**Check:** "Is this the kind of workflow that completed cleanly, or did anything go wrong?"

> _Looking for: they recognise that the workflow itself completed (record was saved) but there's a visible discrepancy at the end. We'll capture both._

---

## Section 5 — Labeling walkthrough (30–40 min)

> _Trainer note: This is the meat. Pace yourself. We're going to label the video phase by phase. The keyboard rhythm we want them to internalise is: **scrub to the start of an action → press A → describe it → watch it complete → press S → next action**._

### Step 0: Set the workflow start

**Say:** "Press the Home key or click 0:00 on the timeline. We want to start at the very beginning."

**Do:** Drag the timeline playhead to 0:00 (or click the leftmost edge of the timeline).

**Say:** "We'll let the workflow start get auto-set when you press A on your first step."

### Step 1 — Open the source spreadsheet

**Do:** Press **Space** to play. When the spreadsheet appears on screen, press **Space** again to pause.

**Say:** "We're at the visible start of the first step — opening the spreadsheet. Press **A**."

**Do:** Watch them press A.

**Say:** "What do you see when you press A?"

> _Looking for: A new step appears in the right pane (Step 1 of 1). Cursor lands in the Action field. The timeline shows an amber block (incomplete because end + other fields are missing)._

**Say:** "Now describe what you see. Use a chip if it helps. Press 1 for 'Clicked', 2 for 'Typed', 3 for 'Selected', and so on."

> _Likely answer: "Opened customer-update-data.xlsx in Excel" or similar — depends on what's actually on screen. Trainee picks the chip "Opened" and types the file name they see._

**Say:** "Tab to the next field, or use the action types pills. Click whichever input types you saw — probably just 'click' for opening the file."

**Say:** "Now Screen / app context — what's the visible app or window?"

> _Likely: "Excel" or the workbook title bar text._

**Say:** "Now Visible evidence. Don't repeat the action — quote something on screen. The window title? A cell value? A header?"

> _Likely: "Workbook title shows customer-update-data.xlsx" or the visible header row text._

**Say:** "Confidence — how clearly can you see all of this? If the window title is right there, that's Clear or Strong."

**Do:** Watch them pick a confidence band.

**Say:** "Now press **Space** to keep playing, and press **S** the moment this 'opening the spreadsheet' phase ends — usually when the worker's mouse moves to a different app or starts reading."

> _Trainer note: When they press S, a NEW step is created automatically with start = end of this step. Cursor lands in the new step's Action field. This is the rhythm we want — watch, A, fill, watch, S, fill, repeat._

**Check:** "Look at the timeline — what colour is your first step now?"

> _Looking for: vermillion (complete) if all required fields are filled, amber if anything's still missing. Help them fix any amber dots._

### Steps 2–6 — the body of the workflow

> _Trainer note: For each visible action, repeat the same A/S rhythm. Below is the expected sequence and example labels. The trainee should produce something close to these — exact wording will vary, that's fine. What matters is granularity (one step per logical action) and that evidence quotes something visible._

| # | Phase | Expected step contents |
|---|---|---|
| 2 | Open the CRM in Chrome | Action: "Opened CRM in Chrome" · Screen: "Chrome — CRM login or home page" · Evidence: visible page header or URL · Action types: navigation |
| 3 | Search for the customer | Action: "Typed Acme North into the search box" · Screen: "Chrome — CRM search" · Evidence: search field shows 'Acme North' · Action types: keystroke |
| 4 | Open the Acme North record | Action: "Clicked Acme North in search results" · Screen: "Chrome — CRM search results" · Evidence: visible row text 'Acme North' · Action types: click |
| 5 | Compare spreadsheet to CRM | Action: "Reviewed CRM values against spreadsheet" · Screen: "Chrome — Acme North record (alongside Excel)" · Evidence: visible field values match spreadsheet column X · Action types: wait |
| 6 | Switched between Excel and CRM | _If you see this as a separate observable action, label it. If it's just glance-and-flip during step 5, skip._ |

**Say (after step 4):** "Notice this video has a comparison/reading phase before any field changes. Some labelers skip that because nothing visibly 'changes.' Don't. The reading IS the work — it's a step with action type 'wait' and evidence like 'Spreadsheet column shows X. CRM Account Owner field shows Y.' If it took observable time, it's a step."

### Steps 7–11 — the field updates (one step per field)

> _Trainer note: This is the most important part for the benchmark. The original instructions explicitly call for one step per field change, NOT one broad "updated the data" step._

**Say:** "From here, each field change gets its own step. Don't bundle them. The benchmark needs to know which AI labels matched which specific field updates."

For each of these, repeat the A/S rhythm:

| # | Field | Expected step contents |
|---|---|---|
| 7 | Account Owner | Action: e.g. "Typed Priya Shah into the Account Owner field" · Screen: "Chrome — CRM account record" · Evidence: "Account Owner field shows Priya Shah" · Action types: keystroke + click |
| 8 | Renewal Date | Action: "Changed Renewal Date to {visible date}" · Evidence: "Renewal Date field shows {date}" · Action types: keystroke or click |
| 9 | Billing Email | Action: "Typed {email} into Billing Email" · Evidence: "Billing Email field shows {email}" · Action types: keystroke |
| 10 | Internal Note | Action: "Added internal note: {first words}" · Evidence: "Internal note text shows {first words}" · Action types: keystroke |
| 11 | (Status field check) | _Read carefully — does the worker actually change Status? If not, skip the step but remember this for the discrepancy section._ |

**Check (after step 7):** "Why is each field its own step instead of one big 'updated the record' step?"

> _Looking for: because the benchmark needs field-level granularity. The AI also predicts at the field level; one big human step can't be matched to several AI steps._

### Step 12 — Save

**Say:** "Now the save click."

| # | Phase | Expected step contents |
|---|---|---|
| 12 | Save | Action: "Clicked Save" · Screen: "Chrome — CRM account record" · Evidence: "Save button visibly clicked" or "Toast: 'Record saved'" if visible · Action types: click |

### Step 13 — Post-save observation

> _Trainer note: This is where the discrepancy shows up. Don't tell the trainee yet — see if they notice on their own._

**Say:** "Watch carefully for what happens AFTER the save. Press S when this 'something happens after save' phase ends."

| # | Phase | Expected step contents |
|---|---|---|
| 13 | Reviewed save state | Action: "Reviewed customer list and save confirmation" · Screen: "Chrome — CRM customer list (or save toast)" · Evidence: e.g. "Save toast says 'Summary updated' / customer list row shows old values" · Action types: wait |

**Check:** "Did anything look inconsistent on screen after the save?"

> _Looking for: they spot that the save message says one thing but the list shows another, OR they notice the Status field shows 'Active' even though the spreadsheet had something different. If they miss it, scrub back and watch the post-save segment again together._

---

## Section 6 — Discrepancies and uncertainty (5 min)

**Say:** "There are two known discrepancies in this video that we need to capture. One belongs on a step, the other belongs in the Notes drawer."

### The Status field discrepancy → Notes drawer

**Say:** "If the spreadsheet has a 'new_status' value but the CRM Status field never changed, that's a discrepancy between sources. It's about the data, not the worker. Press **N** to open the Notes drawer."

**Do:** Press **N**.

**Say:** "Type one line under 'Observed discrepancies.' Something like: 'The spreadsheet new_status column shows Renewal Review, but the CRM Status field still shows Active at the end of the video.'"

**Check:** "Why is this not on a step?"

> _Looking for: it doesn't fit any single labelled action. It's a comparison across the whole workflow. The drawer's purpose._

### The save-message vs customer-list discrepancy → also Notes drawer

**Say:** "Same drawer, second line: 'The save toast text says the summary was updated, but the visible customer list still shows the old Account Owner value.'"

> _Trainer note: Both go in the drawer because both are mismatches between visible sources, not actions taken by the worker. If the worker had visibly DONE something wrong (e.g. typed the wrong email), that would be a Mistake exception on the step itself._

**Say:** "Press **N** again to close the drawer."

### What about uncertainty?

**Say:** "If anything in the video was hard to see — say a field value was blurry, or a tooltip blocked something — write it under 'Whole-video uncertainty.' For per-step things you couldn't quite tell, use the Step-level uncertainty field on the step itself."

**Check:** "Was anything in this video hard to read?"

> _Looking for: if yes, capture it in either the per-step or whole-video uncertainty depending on scope. If no, leave both blank._

---

## Section 7 — Wrap-up and export (5 min)

**Say:** "We've labelled every visible action and captured the discrepancies. Now wrap up and export."

**Do:** Click **Wrap up & export** (top right).

**Say:** "This modal has three jobs. Top — show you any errors that block export. Middle — collect the wrap-up fields you couldn't fill at the start because you hadn't watched the video yet. Bottom — get your sign-off."

### Wrap-up fields

| Field | What to pick |
|---|---|
| Workflow outcome | Most likely **Completed** (the worker did save the record). If you saw the worker abandon or close without saving, pick **Abandoned** instead. |
| Workflow confidence | **Strong** if the action and evidence were clearly visible across the whole video. **Likely** if some stretches were unclear. Don't pick **Doubtful** unless you genuinely can't tell what happened. |
| Short summary | Two to four plain sentences. Example: "Worker opened a customer update spreadsheet, opened the CRM, searched for Acme North, and updated the Account Owner, Renewal Date, Billing Email, and Internal Note fields against the spreadsheet values. The record saved successfully but the customer list and Status field appeared inconsistent with the new spreadsheet values." |

> _Trainer note: Watch the validation banner at the top of the modal. If it shows red errors (e.g. "Step 7: visible evidence is missing"), close the modal, fix the step, come back. Validation re-runs every time you open the modal._

### Sign-off

**Say:** "Read this declaration. By signing, you're saying you only described what you saw, you didn't use AI, and you didn't peek at anyone else's labels of this video. Type your full name."

**Do:** Watch the trainee type their name. Date is auto-filled.

### Download

**Say:** "Click **Sign & download all**. Three files come down: a JSON, a Markdown, and a BPMN XML. The JSON is what the benchmark uses. The Markdown is for human reviewers. The BPMN is for process modelling tools downstream."

**Do:** Watch them export. Save the files into `gold-labels/` next to the `templates/` folder.

**Check:** "Where would you find this draft if you closed the browser tomorrow?"

> _Looking for: they understand that drafts autosave per video ID. Refresh the page → setup modal pre-fills → click Load draft → labels reappear (video file needs re-loading)._

---

## Section 8 — Common mistakes (5 min)

> _Trainer note: This is also in the in-tool Guide, but say it out loud at least once._

Read these in order. Pause for the trainee's reaction or example after each.

1. **Writing intent.** _"Tried to save the record." "Wanted to update the email."_ — describe what was visible, not what they meant to do.
2. **Action equals evidence.** Action: "Clicked Save." Evidence: "Clicked Save." — that's not evidence. Evidence is what's on screen — a toast, a state change, a quoted value.
3. **Hiding messy parts.** If the worker fumbled, retried, got interrupted, or made a visible mistake — capture it. The benchmark cares more about messy reality than tidy stories.
4. **Confirmation as proof.** A "Saved successfully" toast tells you the toast appeared, not that the back-end actually saved correctly. Describe the visible toast.
5. **Steps with `—` for start or end.** Every step needs both timestamps. The export blocks until they're there.
6. **One broad step instead of several.** "Updated the record" → split into one step per field change.
7. **Vague evidence.** "Yes." "Done." "OK." — quote what's actually on screen.

---

## Section 9 — First solo (20 min, optional)

**Say:** "Now you'll do video 002 on your own. Two ways we can run this — your choice. Either keep me on the call and I'll stay muted while you work, or end the call and you do it asynchronously and send me the JSON when you're done. The async option is more realistic — that's how real labeling will work."

> _Trainer note: For virtual training, async is usually better — labelers will work without a trainer on the line, so practice that. If they choose live, mute yourself and turn off your camera. Resist the urge to coach mid-video. Note the start time so you have a baseline for future labeling speed._

**Say:** "Either way, after you finish: paste the contents of the .gold.json file into Slack [or whatever channel you use], or attach the file. I'll review it within [X hours] and we'll either book a 15-min review call or I'll send written feedback."

**Do:** Trainee loads `video-002-invoice-rework.mp4`. Set up the same way.

> _Trainer note: Video 002 is named "invoice-rework," so it likely contains rework — that's a good test of the exception type picker. Don't tell the trainee that; let them notice on the first watch._

When you review the trainee's label, check:

- Did they hit one step per visible action?
- Did they fill all required fields on every step?
- Did they use the exception toggle for the rework steps with the correct exception type?
- Did they capture any whole-video discrepancies in the drawer?
- Did the wrap-up summary describe what was visible without intent verbs?
- Did they sign off?

---

## If something goes wrong (virtual troubleshooting)

Quick fixes for the most common in-session issues. Bookmark this section so you can find it fast.

### "I can't see the video file in the file picker"

Trainee's download didn't complete or it landed somewhere unexpected. Have them check Downloads folder, search for `video-001` in Finder/Explorer, or re-share the file via your conferencing tool's file transfer.

### "The video won't play in the labeling tool"

The browser may be blocking local file access (rare on Chrome but happens). Have them:
1. Confirm the file plays when double-clicked outside the browser.
2. Drag the video file directly onto the Chrome window — sometimes that works around the file picker.
3. As a last resort, click **Side-by-side** in the topbar and play the video in VLC or their OS player. They type timestamps into the Manual timestamp field.

### "Screen share is too laggy / I can't read your right pane"

Ask the trainee to share **only the browser window**, not the whole desktop — most platforms allocate more bandwidth to single-window shares. If still bad, ask them to read aloud the text you can't see. Cmd/Ctrl+Plus to zoom the browser if needed.

### "My audio cut out / I missed what you said"

Stop. Don't let them keep labeling without context — wrong labels stick. Repeat the last instruction, then ask the trainee to recap what they're about to do before they do it. Consider re-recording with better audio for the QA file.

### "I accidentally pressed the wrong key and lost my step"

The Saved indicator should say "Saved Xs ago" — their work is in localStorage. Tell them to refresh the page; the setup modal pre-fills, they click **Load draft**, and the labels reappear (they will need to re-pick the video file). If they pressed Space repeatedly during a typing field, the field captured spaces, not playback toggles — they can just delete the spaces.

### "The shortcut overlay opened in Slack instead of the tool"

Conferencing tools and chat apps sometimes capture single-letter shortcuts globally. Ask them to click into the labeling-workstation browser window first, then try the shortcut. Or close the chat app for the rest of the session.

### "I lost track of where in the video we are"

Click the timeline empty space to jump there visually, or click any existing step block to seek back to its start.

### "The export modal validation says my step is invalid but I can't tell which one"

Open the topbar step counter — click the red "X invalid" badge to jump to the first invalid step. The amber dot next to a field name tells you what's missing.

### Trainee finishes 30 min ahead of schedule

Either start them on Section 9 solo immediately, or do an extra exercise: have them re-label the spreadsheet-comparison phase (step 5) with deliberately bad evidence ("done", "yes") and watch the linter / validation flag it. Builds intuition for what the tool catches.

### Trainee is 30 min behind schedule

Cut Section 9 (solo). Cut Section 8 (common mistakes — link to the in-tool Guide instead). Get them through wrap-up + export so they finish a complete label. They can read the rest async after the session.

---

## Trainee sign-off checklist

Have the trainee tick each box at the end of training and send it back to you (paste in Slack, copy into a doc, whatever your team uses). Don't proceed to unsupervised labeling unless every box is ticked.

```
[ ] I can load a video and fill setup without help.
[ ] I know that A starts a step, S ends-and-advances.
[ ] I know that I describe what is visible, never intent.
[ ] I know evidence is something quoted from the screen, not the action.
[ ] I know to split field updates into one step per field.
[ ] I know the five exception types and when to use each.
[ ] I know that interruption / rework / mistake / abandoned goes ON the step, not in the drawer.
[ ] I know that whole-video discrepancies and uncertainty go IN the drawer.
[ ] I know to wrap up before export (outcome, summary, confidence).
[ ] I know I have to sign off before downloading.
[ ] I know my work autosaves but the video file won't reload by itself after refresh.
```

If anything is unticked, run that section again with the trainer.

---

## Trainer notes for future videos

- **video-002-invoice-rework** — expected to contain visible rework. Use it for solo practice.
- **video-003-support-interruption** — expected to contain interruption. Practice the Interruption exception type.
- **video-004-messy-multi-workflow** — multi-workflow recordings. Discuss whether to split into multiple labels or label as one with exception steps. (Tool currently supports one workflow per export — get manager guidance.)
- **video-005-same-role-variant** — repeat workflow type. Useful for consistency testing across labelers.

After three supervised videos, a labeler typically transitions to independent work with adjudication review. Track them in `labeling-tracker.csv`.

For virtual delivery, the natural cadence is:

- **Session 1** (this script) — onboarding + video-001 walkthrough + video-002 solo
- **Session 2** (45 min, async-first) — review their video-002 label live, then a guided pass through video-003 (interruption)
- **Session 3** (30 min, async-first) — review video-003 + agree on adjudication cadence going forward

After session 3 they label independently; their work goes through the adjudication pipeline tracked in `labeling-tracker.csv`.

---

_End of script. Total run time: 75–90 minutes for the supervised walkthrough over video call; +20 minutes if the solo is done live._
