/* script.js

   Minimal interactive JS for the Employee ID Card demo.
   - Updates the preview when the user edits form inputs
   - Handles photo preview upload
   - Flips the card (toggle front/back)
   - Provides a simple Download PNG action using html2canvas if available
     (if html2canvas is not included, the button will still be present but
      the download will be a no-op with a helpful message in the console).
*/

// Helper to safely query elements
const $ = (sel) => document.querySelector(sel);

// Map inputs to card elements
const inputName = $('#inputName');
const inputTitle = $('#inputTitle');
const inputDept = $('#inputDept');
const inputId = $('#inputId');
const inputPhoto = $('#inputPhoto');

const cardName = $('#cardName');
const cardTitle = $('#cardTitle');
const cardDept = $('#cardDept');
const cardId = $('#cardId');
const photoPreview = $('#photoPreview img');

const flipBtn = $('#flipBtn');
const downloadBtn = $('#downloadBtn');
const applyBtn = $('#applyBtn');
const resetBtn = $('#resetBtn');

let showingBack = false;

function applyChanges(){
  cardName.textContent = inputName.value || '—';
  cardTitle.textContent = inputTitle.value || '—';
  cardDept.textContent = 'Dept: ' + (inputDept.value || '—');
  cardId.textContent = 'ID: ' + (inputId.value || '—');
}

function resetForm(){
  inputName.value = 'Dikshitha';
  inputTitle.value = 'Software Engineer';
  inputDept.value = 'R&D';
  inputId.value = 'S100';
  // reset photo to default svg (reload page image by setting src to same)
  photoPreview.src = photoPreview.src; // leaves default
  applyChanges();
}

// Photo upload preview
inputPhoto.addEventListener('change', (e)=>{
  const f = e.target.files && e.target.files[0];
  if(!f) return;
  const reader = new FileReader();
  reader.onload = (ev)=>{
    photoPreview.src = ev.target.result;
  };
  reader.readAsDataURL(f);
});

// Apply button updates the card immediately
applyBtn.addEventListener('click', ()=>{
  applyChanges();
});

resetBtn.addEventListener('click', ()=>{
  resetForm();
});

// flip functionality: toggles a CSS class which can be used to show back
flipBtn.addEventListener('click', ()=>{
  const idCard = $('#idCard');
  showingBack = !showingBack;
  if(showingBack){
    idCard.classList.add('show-back');
  } else {
    idCard.classList.remove('show-back');
  }
});

// Download action: use html2canvas if provided on the page. If not available,
// fallback to notifying in the console. This keeps the UI simple while still
// being friendly if the consumer wants to include the library.
downloadBtn.addEventListener('click', async ()=>{
  const idCard = $('#idCard');
  // pick the visible side to capture
  const side = showingBack ? $('#cardBack') : $('#cardFront');
  if(window.html2canvas){
    try{
      const canvas = await window.html2canvas(side, {backgroundColor:null});
      const dataUrl = canvas.toDataURL('image/png');
      const a = document.createElement('a');
      a.href = dataUrl;
      a.download = `${inputName.value || 'employee'}-id.png`;
      a.click();
    }catch(err){
      console.error('Download failed', err);
    }
  } else {
    console.info('html2canvas not found. Include html2canvas to enable download.');
    alert('Download not available: include html2canvas to enable PNG export.');
  }
});

// Initialize with defaults on load
document.addEventListener('DOMContentLoaded', ()=>{
  applyChanges();
});
