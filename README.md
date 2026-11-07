## FlareGuard – Research Proof of Concept

**Status:** Pre-project research. This work was done before development of FlareGuard began. It sets out the problem, the evidence and the proposed approach, and no extension or scanner has been built or tested yet.

**Objective:** Illustrate why a Kenyan website identity verification extension is needed, using documented website impersonation cases.

### Evidence

| Suspicious domain | Organisation impersonated | Research finding | Source (date) | Evidence strength |
| ----------------- | ------------------------- | ---------------- | ------------- | ----------------- |
| `ntsca.cc` | NTSA | NTSA stated the site is not affiliated with or operated by the authority. Presented as a traffic-fine payment portal. | K24 Digital (Dec 2025) | Strong: statement from the organisation |
| `kqairways.com` | Kenya Airways | Reported lookalike airline booking website. | Piga Firimbi / Africa Uncensored (Jul 2026) | Moderate: secondary reporting only |
| `moohk.co.ke` | Mookh / CHAN ticketing | Reported ticketing website lookalike; evidence requires further review. | Mozzart Sport Kenya (Aug 2025) | Provisional: needs review |

### Proposed extension demonstration

The extension compares a visited domain against a registry of recognised official domains and a list of reported impersonation domains, then returns one of three states: verified official, reported impersonation, or unknown.

| Domain | Registry status | Verdict shown to user |
| ------ | --------------- | --------------------- |
| `ntsa.go.ke` | Verified official (NTSA) | Verified official |
| `ntsca.cc` | Reported impersonation of NTSA | Reported impersonation |
| `kenya-airways.com` | Verified official (Kenya Airways) | Verified official |
| `kqairways.com` | Reported lookalike of Kenya Airways | Reported lookalike |
| `[confirm Mookh official domain]` | Verified official (Mookh) | Verified official |
| `moohk.co.ke` | Reported lookalike of Mookh; review caveat | Reported lookalike (review caveat) |
| `unlisted-example.co.ke` | Not in registry | Unknown: no verdict, treat with caution |

A domain that is not in the registry is **not** declared safe. It is shown as unknown.

### How the extension detects (proposed signals)

Each check compares the visited site against a reference profile of the organisation's **official main domain** held in the registry:

| Signal | What is compared | Why it helps |
| ------ | ---------------- | ------------ |
| URL | Full address, path and structure against the official site's | Catches lookalike paths and tricks such as extra words or odd extensions |
| Domain | Visited domain against the official domain (exact match, character swaps, added letters, different TLD such as `.cc`) | Catches typosquats such as `ntsca.cc` vs `ntsa.go.ke` |
| Favicon | Favicon of the visited site against the official favicon | Clones often copy the icon exactly, so a matching icon on a non-official domain is a warning sign |
| Logo | Logo image against the official logo | Same logic: official branding on an unregistered domain |
| Colour scheme | Dominant page colours against the official palette | Catches visual imitation even when the logo is altered |
| Broken links | Whether links on the page work, and whether they point to the official domain or nowhere | Cloned pages often have dead links or links that send users back to the real site |

The decision logic is: if the domain is in the registry as official, return verified. If it is a reported impersonation, return reported. Otherwise, if the page looks like a registered organisation (favicon, logo, colours) but the domain does not match, flag it as a suspected lookalike with the reasons listed. If nothing matches, return unknown.

These signals are proposed indicators. None has been tested yet, and their individual usefulness and false-positive rates still need to be evaluated.

### What this demonstrates

1. Kenyan organisations have faced reported website impersonation.
2. Users may encounter websites imitating recognised organisations.
3. Knowing the correct official domain can help users identify potential impersonation.
4. FlareGuard proposes making these checks accessible through a browser extension.

### Proof-of-concept conclusion

> The documented cases illustrate the problem and the proposed check. FlareGuard aims to help users distinguish verified official domains from reported impersonation websites and domains whose identity remains unknown.

The examples demonstrate the problem and proposed functionality, not proven model accuracy.

### Limitations

- Several reported sites were already offline when reviewed, so this proof of concept relies on published reports rather than live page analysis.
- Evidence comes from third-party reporting, and its strength varies by source (see the evidence strength column).
- Registry coverage is currently limited to the domains listed above.
- The detection signals (URL, domain, favicon, logo, colour scheme, broken links) are not yet validated.
- Three cases are not enough to estimate detection performance.
- This is research carried out before the project started, so everything described under the extension is a proposal, not an implemented feature.
