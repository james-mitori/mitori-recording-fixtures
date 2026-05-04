#!/usr/bin/env python3
"""Generate synthetic worker-recording fixtures for the Mitori workflow benchmark."""

from __future__ import annotations

import csv
import html
import sys
from pathlib import Path


DEFAULT_OUTPUT = Path("mitori-recording-fixtures")


CUSTOMER_ROWS = [
    {
        "customer_id": "C-10017",
        "customer_name": "Acme North",
        "current_owner": "Daniel Park",
        "new_owner": "Priya Shah",
        "current_status": "Active",
        "new_status": "Renewal Review",
        "current_renewal_date": "2026-06-30",
        "new_renewal_date": "2026-07-31",
        "current_billing_email": "billing@acmenorth.example",
        "new_billing_email": "ap-north@example.test",
        "notes": "Update owner, renewal date, and billing email. Verify on summary screen.",
    },
    {
        "customer_id": "C-10022",
        "customer_name": "Brightlane Foods",
        "current_owner": "Priya Shah",
        "new_owner": "Maya Chen",
        "current_status": "Active",
        "new_status": "Active",
        "current_renewal_date": "2026-08-15",
        "new_renewal_date": "2026-08-15",
        "current_billing_email": "finance@brightlane.example",
        "new_billing_email": "finance.ops@brightlane.example",
        "notes": "Billing email only.",
    },
    {
        "customer_id": "C-10039",
        "customer_name": "Northstar Demo Care",
        "current_owner": "Alex Rivera",
        "new_owner": "Alex Rivera",
        "current_status": "Onboarding",
        "new_status": "Active",
        "current_renewal_date": "2026-09-01",
        "new_renewal_date": "2026-09-01",
        "current_billing_email": "ap@northstardemo.example",
        "new_billing_email": "ap@northstardemo.example",
        "notes": "Status update after onboarding checklist complete.",
    },
    {
        "customer_id": "C-10044",
        "customer_name": "Harbor Clinic Group",
        "current_owner": "Maya Chen",
        "new_owner": "Daniel Park",
        "current_status": "Renewal Review",
        "new_status": "Active",
        "current_renewal_date": "2026-05-31",
        "new_renewal_date": "2027-05-31",
        "current_billing_email": "billing@harborclinic.example",
        "new_billing_email": "billing@harborclinic.example",
        "notes": "Renewal completed; update owner and next renewal date.",
    },
    {
        "customer_id": "C-10058",
        "customer_name": "Silverline Parts",
        "current_owner": "Jordan Lee",
        "new_owner": "Jordan Lee",
        "current_status": "Active",
        "new_status": "At Risk",
        "current_renewal_date": "2026-10-10",
        "new_renewal_date": "2026-10-10",
        "current_billing_email": "accounts@silverline.example",
        "new_billing_email": "accounts@silverline.example",
        "notes": "Mark at risk after missed QBR.",
    },
    {
        "customer_id": "C-10063",
        "customer_name": "Cedar Trial Services",
        "current_owner": "Priya Shah",
        "new_owner": "Priya Shah",
        "current_status": "Trial",
        "new_status": "Trial",
        "current_renewal_date": "2026-06-14",
        "new_renewal_date": "2026-06-14",
        "current_billing_email": "trial@cedar.example",
        "new_billing_email": "trial@cedar.example",
        "notes": "No action required; review only.",
    },
]


INVOICE_LINES = [
    "Mitori Fixture Supplies Ltd",
    "Invoice 1048",
    "Issue date: 2026-05-01",
    "Due date: 2026-05-31",
    "PO number: PO-4482",
    "Bill to: Northstar Demo Care",
    "Department: Operations",
    "",
    "Line items",
    "1. Workflow intake support package        1 x 820.00",
    "2. Secure document handling fee           1 x 260.00",
    "3. Admin setup review                     1 x 160.00",
    "",
    "Subtotal: 1,240.00",
    "Tax: 186.00",
    "Total due: 1,426.00",
    "",
    "Payment terms: Net 30",
    "Remit to: payments@mitori-fixtures.example",
]


def write_text(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def write_customer_csv(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(CUSTOMER_ROWS[0].keys()))
        writer.writeheader()
        writer.writerows(CUSTOMER_ROWS)


def pdf_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_simple_pdf(path: Path, lines: list[str]) -> None:
    content_lines = ["BT", "/F1 12 Tf", "72 740 Td", "16 TL"]
    for line in lines:
        content_lines.append(f"({pdf_escape(line)}) Tj")
        content_lines.append("T*")
    content_lines.append("ET")
    stream = "\n".join(content_lines).encode("latin-1")

    objects: list[bytes] = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length "
        + str(len(stream)).encode("ascii")
        + b" >>\nstream\n"
        + stream
        + b"\nendstream",
    ]

    output = bytearray(b"%PDF-1.4\n")
    offsets = []
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{index} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")
    xref_at = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_at}\n%%EOF\n".encode(
            "ascii"
        )
    )
    path.write_bytes(bytes(output))


def html_page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; background: #f5f7fb; color: #172033; }}
    header {{ background: #172033; color: white; padding: 16px 24px; }}
    main {{ padding: 24px; max-width: 1080px; margin: auto; }}
    section {{ background: white; border: 1px solid #d7deea; border-radius: 6px; padding: 18px; margin-bottom: 16px; }}
    label {{ display: block; font-weight: 700; margin-top: 12px; }}
    input, select, textarea {{ width: 100%; box-sizing: border-box; padding: 9px; border: 1px solid #b9c3d3; border-radius: 4px; margin-top: 4px; }}
    button {{ margin-top: 16px; padding: 10px 14px; border: 0; background: #1f6feb; color: white; border-radius: 4px; cursor: pointer; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 12px; }}
    th, td {{ border-bottom: 1px solid #e2e7f0; padding: 8px; text-align: left; }}
    .notice {{ display: none; margin-top: 14px; padding: 12px; background: #e9f8ef; border: 1px solid #98d4aa; color: #165a2f; border-radius: 4px; }}
    .warning {{ background: #fff7df; border-color: #e4c565; color: #6f4c00; }}
    .muted {{ color: #5b6678; font-size: 14px; }}
    .grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}
  </style>
</head>
<body>
  <header><h1>{html.escape(title)}</h1></header>
  <main>
{body}
  </main>
</body>
</html>
"""


def fake_crm_html() -> str:
    rows = "\n".join(
        f"<tr><td>{r['customer_id']}</td><td>{html.escape(r['customer_name'])}</td><td>{html.escape(r['current_owner'])}</td><td>{html.escape(r['current_status'])}</td><td>{r['current_renewal_date']}</td></tr>"
        for r in CUSTOMER_ROWS
    )
    return html_page(
        "Fixture CRM",
        f"""
    <section>
      <p class="muted">Use this local page as the destination system for customer update recordings.</p>
      <label for="search">Search customer</label>
      <input id="search" placeholder="Type Acme North, C-10017, or another customer">
      <button onclick="findCustomer()">Open record</button>
      <div id="searchNotice" class="notice warning">Record opened. Review and update the fields below.</div>
      <table>
        <thead><tr><th>ID</th><th>Customer</th><th>Owner</th><th>Status</th><th>Renewal</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </section>
    <section>
      <h2>Customer Record: Acme North</h2>
      <div class="grid">
        <div><label>Account owner</label><input id="owner" value="Daniel Park"></div>
        <div><label>Status</label><select id="status"><option>Active</option><option>Renewal Review</option><option>At Risk</option></select></div>
        <div><label>Renewal date</label><input id="renewal" value="2026-06-30"></div>
        <div><label>Billing email</label><input id="email" value="billing@acmenorth.example"></div>
      </div>
      <label>Internal note</label>
      <textarea id="note" rows="3">Current record awaiting review.</textarea>
      <button onclick="saveRecord()">Save customer record</button>
      <div id="saveNotice" class="notice">Customer record saved. Summary updated for Acme North.</div>
    </section>
    <script>
      function findCustomer() {{
        document.getElementById('searchNotice').style.display = 'block';
      }}
      function saveRecord() {{
        document.getElementById('saveNotice').style.display = 'block';
      }}
    </script>
""",
    )


def invoice_form_html() -> str:
    return html_page(
        "Invoice Intake",
        """
    <section>
      <p class="muted">Use invoice_1048.pdf as the source document. The correct total due is 1,426.00.</p>
      <div class="grid">
        <div><label>Vendor</label><input id="vendor" placeholder="Vendor name"></div>
        <div><label>Invoice number</label><input id="number" placeholder="Invoice number"></div>
        <div><label>Issue date</label><input id="issue" placeholder="YYYY-MM-DD"></div>
        <div><label>Due date</label><input id="due" placeholder="YYYY-MM-DD"></div>
        <div><label>Department</label><select id="dept"><option></option><option>Operations</option><option>Finance</option><option>Credentialing</option></select></div>
        <div><label>Total amount</label><input id="amount" placeholder="0.00"></div>
      </div>
      <label>Notes</label>
      <textarea rows="3" placeholder="Optional processing notes"></textarea>
      <button onclick="validateInvoice()">Validate invoice</button>
      <button onclick="submitInvoice()">Submit invoice</button>
      <div id="warn" class="notice warning">Validation warning: confirm the total amount and department before submitting.</div>
      <div id="done" class="notice">Invoice 1048 submitted for approval.</div>
    </section>
    <script>
      function validateInvoice() {
        document.getElementById('warn').style.display = 'block';
      }
      function submitInvoice() {
        document.getElementById('done').style.display = 'block';
      }
    </script>
""",
    )


def support_case_html() -> str:
    return html_page(
        "Support Case Console",
        """
    <section>
      <p class="muted">Use support_email.txt as the source message.</p>
      <div class="grid">
        <div><label>Customer</label><input placeholder="Customer name"></div>
        <div><label>Account ID</label><input placeholder="Account ID"></div>
        <div><label>Priority</label><select><option></option><option>Low</option><option>Medium</option><option>High</option></select></div>
        <div><label>Category</label><select><option></option><option>Billing Portal</option><option>Login</option><option>Data Request</option></select></div>
      </div>
      <label>Issue summary</label>
      <input placeholder="Short summary">
      <label>Case notes</label>
      <textarea rows="5" placeholder="Observed issue and requested action"></textarea>
      <button onclick="saveDraft()">Save draft</button>
      <button onclick="submitCase()">Submit case</button>
      <div id="draft" class="notice warning">Draft saved. Case is not submitted yet.</div>
      <div id="done" class="notice">Support case submitted. Case ID: SC-58291.</div>
    </section>
    <script>
      function saveDraft() {
        document.getElementById('draft').style.display = 'block';
      }
      function submitCase() {
        document.getElementById('done').style.display = 'block';
      }
    </script>
""",
    )


def credentialing_html() -> str:
    return html_page(
        "Credentialing Checklist",
        """
    <section>
      <h2>Candidate: Taylor Morgan</h2>
      <p class="muted">Use this page during the messy multi-workflow recording.</p>
      <table>
        <thead><tr><th>Item</th><th>Status</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Identity document received</td><td>Complete</td><td></td></tr>
          <tr><td>License verified</td><td id="licenseStatus">Pending</td><td><button onclick="markLicense()">Mark complete</button></td></tr>
          <tr><td>Reference check</td><td>In review</td><td></td></tr>
          <tr><td>Background check</td><td>Pending vendor response</td><td></td></tr>
          <tr><td>Signed policy acknowledgment</td><td>Complete</td><td></td></tr>
        </tbody>
      </table>
      <div id="done" class="notice">License verification marked complete for Taylor Morgan.</div>
    </section>
    <script>
      function markLicense() {
        document.getElementById('licenseStatus').textContent = 'Complete';
        document.getElementById('done').style.display = 'block';
      }
    </script>
""",
    )


def main() -> int:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    output.mkdir(parents=True, exist_ok=True)

    write_customer_csv(output / "customer_updates.csv")
    write_simple_pdf(output / "invoice_1048.pdf", INVOICE_LINES)
    write_text(output / "invoice_1048.txt", "\n".join(INVOICE_LINES))
    write_text(
        output / "support_email.txt",
        """
From: Casey Nguyen <casey.nguyen@example.test>
To: Operations Queue <ops.queue@example.test>
Subject: Billing portal access issue - Acme North
Date: 2026-05-04 09:18

Hi team,

Acme North says their AP contact cannot access the billing portal after the recent owner update.

Customer: Acme North
Account ID: C-10017
Requested category: Billing Portal
Suggested priority: Medium
Contact: Morgan Ellis, AP Coordinator
Callback: 555-0104

Please create a support case, include the customer/account ID, mark priority Medium, and note that the AP contact needs portal access restored.

Thanks,
Casey
""",
    )
    write_text(
        output / "credentialing_checklist.txt",
        """
Credentialing checklist - Taylor Morgan

Candidate ID: TJC-2048
Role: Agency RN
Facility group: Harbor Clinic Group

Items:
- Identity document received: Complete
- License verified: Pending
- Reference check: In review
- Background check: Pending vendor response
- Signed policy acknowledgment: Complete
- Immunization attestation: Complete

Recording task:
Open the credentialing portal helper page and mark "License verified" complete.
""",
    )
    write_text(
        output / "daily_notes.txt",
        """
Daily notes - synthetic interruption tasks

Unrelated quick task options:
- Rename the draft file "northstar-note-draft.txt" to "northstar-note-final.txt".
- Check whether Brightlane Foods has a billing email update in customer_updates.csv.
- Add this note to a scratch document: "Follow up with Casey after support case is submitted."

Use one of these tasks as an interruption during Video 3 or Video 4.
""",
    )
    write_text(output / "fake_crm.html", fake_crm_html())
    write_text(output / "invoice_intake_form.html", invoice_form_html())
    write_text(output / "support_case_form.html", support_case_html())
    write_text(output / "credentialing_portal.html", credentialing_html())
    write_text(
        output / "README_WORKER.md",
        """
# Mitori Recording Fixtures

This folder contains fake data and local helper pages for workflow-discovery recording sessions.

Use these files with the scripts in `docs/recording-worker-scripts.md`.

Required source files:

- `customer_updates.csv`
- `invoice_1048.pdf`
- `support_email.txt`
- `credentialing_checklist.txt`
- `daily_notes.txt`

Optional helper destination pages:

- `fake_crm.html`
- `invoice_intake_form.html`
- `support_case_form.html`
- `credentialing_portal.html`

All data is synthetic.
""",
    )

    print(f"Generated recording fixtures in {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
