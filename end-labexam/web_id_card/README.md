# Employee ID Card — Demo

This small demo provides a responsive Employee ID card UI (mobile + web) with
live-editable fields and a preview. It is intentionally dependency-free for
core features; an optional `html2canvas` script can be included to enable the
PNG download button.

Files:
- `index.html` — Main UI and controls.
- `styles.css` — Responsive styling (mobile-first).
- `script.js` — Simple interactivity: live preview, photo upload preview,
  flip card, and download hook.
- `UI_TESTS.md` — Manual/simple UI test scenarios.

How to run
1. Open `web_id_card/index.html` in your browser (double-click or `Open File`).
2. On desktop, the edit controls appear to the right; on mobile they appear
   below the card.
3. Edit fields and click `Apply` to update the card preview. Use `Flip Card`
   to view the back side.

Optional: enable download
1. To enable the "Download PNG" button, include `html2canvas` by adding this
   script tag before `script.js` in `index.html`:

```html
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
```

Then pressing "Download PNG" will export the visible side as an image.

Accessibility & notes
- Controls use standard form inputs and simple labels.
- This demo is purposely small — extend with persistence (localStorage) or
  batch printing as needed.
