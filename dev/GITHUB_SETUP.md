PoE2 Minion Army checklist on GitHub — setup and updates (v2.13)
================================================================
You do the setup once, on your PC, in a web browser. About 15 minutes. Everything is free.

PART 1 — Put the page online (GitHub Pages)
 1. Go to github.com and create a free account (Sign up). Remember your username.
 2. Click the "+" at the top right -> "New repository".
      Repository name: minion-guide
      Choose "Public" (free hosting needs public; the page holds only the guide, nothing personal).
      Tick "Add a README file".
    Click "Create repository".
 3. In the new repository: "Add file" -> "Upload files".
    Drag in index.html from the UPLOAD_TO_GITHUB folder in this zip. Click "Commit changes".
 4. Click "Settings" (top of the repository) -> "Pages" (left menu).
      Under "Build and deployment": Source = "Deploy from a branch", Branch = "main" and "/ (root)". Click "Save".
 5. Wait about 1–2 minutes and refresh that Settings -> Pages screen. It shows your address:
      https://countinbiskitsyo.github.io/MinionGuide/
    Open it — that is your checklist. Bookmark it.

PART 2 — Make ticks sync (a token for Gists)
 6. Click your profile picture (top right) -> "Settings" -> scroll down the left menu -> "Developer settings".
 7. "Personal access tokens" -> "Tokens (classic)" -> "Generate new token" -> "Generate new token (classic)".
      Note: minion guide
      Expiration: pick one (e.g. 1 year). GitHub emails you before it expires.
      Scopes: tick ONLY "gist". Nothing else.
    Click "Generate token". COPY IT NOW — GitHub shows it only once.
 8. Open your checklist page, tap "Sync" in the top bar, paste the token, tap "Save token and connect".
    The status line says "Synced with GitHub". The page creates a secret Gist for your ticks by itself.

PART 3 — Your phone
 9. On your phone, open https://countinbiskitsyo.github.io/MinionGuide/
10. Tap "Sync", paste the same token, connect. (Send it to yourself in a private note to copy it; delete the note afterwards.)
11. Add it to your home screen:  iPhone: Share -> "Add to Home Screen".  Android (Chrome): menu ⋮ -> "Add to Home screen".

DAILY USE
- Tick things off on either device. Ticks save to GitHub about a second after you tap.
- When you switch back to the page on the other device, it pulls the latest ticks automatically.
- No signal? Ticks are kept on the device and sync next time.

UPDATING (every new version)
 1. Unzip the update zip I give you. Open the folder inside it.
 2. Select everything in that folder (index.html, README.md and/or the dev folder — whatever is there) and drag it all
    into your MinionGuide repository: "Add file" -> "Upload files". Click "Commit changes".
    Files with the same name are replaced; folders merge. Nothing else in the repository is touched.
 3. About a minute later both devices show the new version. Your ticks stay — they live in the Gist, not the page.
    If a phone still shows the old version, pull down to refresh.

IF SOMETHING GOES WRONG
- "GitHub rejected the token": it expired or was deleted. Make a new one (step 7) and paste it via "Sync" on each device.
- Lost a phone: GitHub -> Settings -> Developer settings -> Tokens (classic) -> delete that token. Make a new one for your other devices.
- Want to stop syncing on a device: "Sync" -> "Remove token from this device".
- Your ticks file: gist.github.com shows a secret gist named poe2-minion-checklist.json. Don't edit or delete it.

SHOW THE LINK ON THE REPOSITORY'S FRONT PAGE (like MirrorFilter)
 1. On the MinionGuide front page, click the gear icon next to "About" (right side).
 2. Description: Interactive checklist guide for a PoE2 Witch → Infernalist minion army build.
 3. Tick "Use your GitHub Pages website". Click "Save changes".
