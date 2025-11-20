# UI Test Scenarios — Employee ID Card Demo

These are simple manual UI test scenarios you can run to verify the interface
behaves as expected. They are intentionally short and readable so you can
perform them in a browser without test automation.

Test 1 — Default render
- Steps:
  1. Open `index.html` in a browser.
  2. Observe the card preview.
- Expected:
  - Front side displays name `Dikshitha`, title `Software Engineer`, ID `S100`.
  - Photo area shows a default avatar.

Test 2 — Edit fields and apply
- Steps:
  1. Change `Name` input to `Alex` and `Title` to `Designer`.
  2. Click `Apply`.
- Expected:
  - The card preview updates to show `Alex` and `Designer`.

Test 3 — Photo upload preview
- Steps:
  1. Click `Photo (optional)` and choose a local image file.
  2. Observe the photo area on the card preview.
- Expected:
  - The selected image appears in the photo area, cropped to fit.

Test 4 — Flip and back content
- Steps:
  1. Click `Flip Card`.
- Expected:
  - The UI shows the back side content (notes, QR placeholder).
  - Clicking `Flip Card` again returns to the front.

Test 5 — Download (optional)
- Steps:
  1. Include `html2canvas` in `index.html` (see `README.md`).
  2. Click `Flip Card` or keep front visible.
  3. Click `Download PNG`.
- Expected:
  - A PNG file is downloaded representing the visible side of the card.

Test 6 — Responsive check
- Steps:
  1. Resize the browser to a narrow width (mobile) or open on a phone.
  2. Observe layout.
- Expected:
  - The controls stack under the card; content remains readable and buttons reachable.
