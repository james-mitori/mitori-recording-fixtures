function showStatus(id) {
  var element = document.getElementById(id);
  if (element) {
    element.classList.add('is-visible');
  }
}

function hideStatus(id) {
  var element = document.getElementById(id);
  if (element) {
    element.classList.remove('is-visible');
  }
}

function setText(id, value) {
  var element = document.getElementById(id);
  if (element) {
    element.textContent = value;
  }
}

function markActiveRecord(rowId) {
  var rows = document.querySelectorAll('[data-record-row]');
  rows.forEach(function(row) {
    row.classList.toggle('selected', row.id === rowId);
  });
}

function findCustomerRecord() {
  markActiveRecord('customer-row-c-10017');
  showStatus('searchNotice');
  document.getElementById('owner').focus();
}

function saveCustomerRecord() {
  var owner = document.getElementById('owner').value;
  var status = document.getElementById('status').value;
  var renewal = document.getElementById('renewal').value;
  var email = document.getElementById('email').value;

  setText('summaryOwner', owner);
  setText('summaryStatus', status);
  setText('summaryRenewal', renewal);
  setText('summaryEmail', email);
  showStatus('saveNotice');
}

function validateInvoice() {
  var amount = document.getElementById('amount').value.trim();
  if (amount && amount !== '1426.00' && amount !== '1,426.00') {
    setText('invoiceWarningText', 'Validation warning: total amount does not match invoice 1048. Confirm and correct before submitting.');
  } else {
    setText('invoiceWarningText', 'Validation warning: confirm the total amount and department before submitting.');
  }
  showStatus('warn');
}

function submitInvoice() {
  hideStatus('warn');
  showStatus('done');
}

function saveSupportDraft() {
  showStatus('draft');
}

function submitSupportCase() {
  hideStatus('draft');
  showStatus('caseDone');
}

function markLicenseComplete() {
  var status = document.getElementById('licenseStatus');
  if (status) {
    status.textContent = 'Complete';
    status.classList.remove('pending');
    status.classList.add('complete');
  }
  showStatus('credentialingDone');
}
