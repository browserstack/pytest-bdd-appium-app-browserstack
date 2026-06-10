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
- An application to test. The Android directory is pre-wired to a pre-uploaded
  `WikipediaSample.apk` (`bs://...`); the iOS directory uploads
  `BStackSampleApp.ipa` from a local path.

## Setup

```bash
git clone <this-repo>
cd pytest-bdd-appium/android      # or: cd pytest-bdd-appium/ios

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
browserstack-sdk pytest -s tests/
```

This runs the **Wikipedia search** scenario on a real Samsung Galaxy S22 Ultra:
tap "Search Wikipedia", type "BrowserStack", and assert results are returned.
It also runs the **local** scenario (LocalSample.apk over the BrowserStack Local
tunnel — `browserstackLocal: true`).

To run a single scenario:

```bash
browserstack-sdk pytest -s tests/test_sample.py
```

## Run Sample Test (iOS)

From inside `ios/`:

```bash
browserstack-sdk pytest -s tests/
```

## Run Local Test

The local scenarios (`tests/test_local.py`) exercise BrowserStack Local. With
`browserstackLocal: true` in `browserstack.yml` the SDK starts the Local tunnel
automatically — no separate binary to launch.

## Notes / Dashboard

- View runs and shareable session links at
  [app-automate.browserstack.com](https://app-automate.browserstack.com/).
- Test Observability (`testObservability: true`) reports also appear at
  [observability.browserstack.com](https://observability.browserstack.com/).
- The `app:` value can be a local path (the SDK uploads it and rewrites to
  `bs://<hashed-id>`) or a pre-uploaded `bs://<id>`.
