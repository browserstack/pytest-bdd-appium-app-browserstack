# pytest-bdd + Appium with BrowserStack App Automate

Run Appium (mobile app) tests written with **pytest-bdd** on real devices on
[BrowserStack App Automate](https://app-automate.browserstack.com/) using the
BrowserStack Python SDK. No capability boilerplate in your tests — the SDK reads
`browserstack.yml` and routes each session to the BrowserStack device cloud.

This repo has two self-contained platform directories:

```
android/   Android sample (WikipediaSample.apk) + local (LocalSample.apk)
ios/       iOS sample (BStackSampleApp.ipa) + local (LocalSample.ipa)
```

Each directory has its own `browserstack.yml`, `conftest.py` (Appium driver
fixture), `features/` (Gherkin), `tests/` (pytest-bdd step definitions), and
`requirements.txt`.

## Prerequisites

- A [BrowserStack](https://www.browserstack.com/) account (username + access key).
- Python 3.8+.
- An application to test. Both directories reference their public sample app by
  **local path** (`app: ./WikipediaSample.apk` / `./BStackSampleApp.ipa`) — the SDK
  uploads it at run time, so the sample works on any account (no pre-uploaded
  `bs://` id required).

## Setup

```bash
git clone <this-repo>
cd pytest-bdd-appium-app-browserstack/android      # or: cd pytest-bdd-appium-app-browserstack/ios

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Configure credentials via env vars (recommended) or by editing `browserstack.yml`:

```bash
export BROWSERSTACK_USERNAME="YOUR_USERNAME"
export BROWSERSTACK_ACCESS_KEY="YOUR_ACCESS_KEY"
```

## Run Sample Test (Android)

From inside `android/`:

```bash
browserstack-sdk pytest -s tests/test_sample.py
```

This runs the **Wikipedia search** scenario on a real Samsung Galaxy S22 Ultra:
tap "Search Wikipedia", type "BrowserStack", and assert matching results are returned.

## Run Sample Test (iOS)

From inside `ios/`:

```bash
browserstack-sdk pytest -s tests/test_sample.py
```

## Run Local Test

The local scenario (`tests/test_local.py`) exercises **BrowserStack Local**. Because
App Automate installs **one app per build**, the local scenario is a *separate* build
that runs against the **local** sample app (`LocalSample.apk` / `LocalSample.ipa`,
committed alongside the main app) — it cannot share a build with the Wikipedia/BStack
sample. To run it, point `app:` at the local build in `browserstack.yml`, then run only
the local test:

```bash
# android/ — set `app: ./LocalSample.apk` in browserstack.yml, then:
browserstack-sdk pytest -s tests/test_local.py
# ios/ — set `app: ./LocalSample.ipa`, then run the same command
```

`browserstackLocal: true` (already set in `browserstack.yml`) starts the Local tunnel
automatically — no separate binary to launch.

## Notes / Dashboard

- View runs and shareable session links at
  [app-automate.browserstack.com](https://app-automate.browserstack.com/).
- Test Observability (`testObservability: true`) reports also appear at
  [observability.browserstack.com](https://observability.browserstack.com/).
- The `app:` value can be a local path (the SDK uploads it and rewrites to
  `bs://<hashed-id>`) or a pre-uploaded `bs://<id>`.
