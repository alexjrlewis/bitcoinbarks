
function copyToClipboard(id) {
  const copyText = document.getElementById(id);
  // copyText.select();
  copyText.setSelectionRange(0, 99999); // For mobile devices
  navigator.clipboard.writeText(copyText.value);
}
