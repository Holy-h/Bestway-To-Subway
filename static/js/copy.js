function copy(val) {
  let dummy = document.createElement("textarea");
  document.body.appendChild(dummy);
  dummy.value = val;
  dummy.select();
  document.execCommand("copy");
  document.body.removeChild(dummy);
}
