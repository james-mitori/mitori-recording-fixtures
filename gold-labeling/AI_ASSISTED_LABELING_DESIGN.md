# AI-Assisted Labeling Design

This is not enabled in the simple static helper yet.

The current benchmark labels should stay clearly separated into:

- `human_video_observed_gold`: human-only labels, no model suggestion used.
- `human_reviewed_ai_assisted`: model suggested text, human checked and edited it.

This separation matters because we cannot use model-assisted labels as a clean gold benchmark for that same model. They can still be useful for speed, bootstrapping, and operational review.

## Proposed Assist Flow

1. Worker pauses the video at the current step.
2. Worker clicks `Suggest action from screen`.
3. The helper captures the current video frame from the internal player.
4. The helper sends the frame, timestamp, previous step, and current draft text to a backend endpoint.
5. A fast vision model returns suggested text:
   - observed action
   - screen/app context
   - visible evidence
   - uncertainty
6. Worker accepts, edits, or rejects the suggestion.
7. Export records exactly what happened.

## Required Audit Fields

Each step should record:

```json
{
  "assistance": {
    "mode": "none | ai_suggested_human_edited | ai_suggested_human_accepted | ai_suggested_rejected",
    "model": "provider/model-name",
    "prompt_version": "step-suggestion-v0",
    "suggested_observed_label": "raw model suggestion",
    "suggested_evidence": "raw model suggestion",
    "accepted_without_edit": false
  }
}
```

## Backend Shape

The public HTML helper must not contain an API key.

Use a small backend endpoint instead:

```text
POST /suggest-step
```

Request:

```json
{
  "sample_id": "video-001-clean-customer-update",
  "timestamp_sec": 72.5,
  "frame_image_base64": "...",
  "previous_step": "Worker opened the customer record.",
  "current_draft": "",
  "instruction": "Describe only what is visible. Do not infer intent."
}
```

Response:

```json
{
  "observed_label": "Worker typed Priya Shah into the Account Owner field.",
  "screen_context": "Chrome CRM page",
  "evidence": "The Account Owner field shows Priya Shah.",
  "uncertainty": "",
  "confidence": 0.82
}
```

## Recommendation

Keep the next few benchmark videos human-only.

After we have a small human-only gold set, add AI-assisted mode as a separate experiment and measure:

- time saved per video
- edit distance between model suggestion and final human text
- whether suggestions make labels more consistent
- whether suggestions introduce hallucinated actions or evidence

