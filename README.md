## Flare Guard – Research Proof of Concept

**Objective:** Illustrate why a Kenyan website identity verification extension is needed, using documented website impersonation cases.

### Evidence

| Suspicious domain | Organisation impersonated | Research finding | Source (date) | Evidence strength |
| ----------------- | ------------------------- | ---------------- | ------------- | ----------------- |
| `ntsca.cc` | NTSA | NTSA stated the site is not affiliated with or operated by the authority. Presented as a traffic-fine payment portal. | K24 Digital (Dec 2025) | Strong: statement from the organisation |
| `kqairways.com` | Kenya Airways | Reported lookalike airline booking website. | Piga Firimbi / Africa Uncensored (Jul 2026) | Moderate: secondary reporting only |
| `moohk.co.ke` | Mookh / CHAN ticketing | Reported ticketing website lookalike; evidence requires further review. | Mozzart Sport Kenya (Aug 2025) | Provisional: needs review |

### Proposed extension demonstration

The extension compares a visited domain against a registry of recognised official domains and a list of reported impersonation domains, then returns one of three states.

| Domain | Registry status | Verdict shown to user |
| ------ | --------------- | --------------------- |
| `ntsa.go.ke` | Verified official (NTSA) | Verified official |
| `ntsca.cc` | Reported impersonation of NTSA | Reported impersonation |
| `kenya-airways.com` | Verified official (Kenya Airways) | Verified official |
| `kqairways.com` | Reported lookalike of Kenya Airways | Reported lookalike |
| `[confirm Mookh official domain]` | Verified official (Mookh) | Verified official |
| `moohk.co.ke` | Reported lookalike of Mookh; review caveat | Reported lookalike (review caveat) |
| `unlisted-example.co.ke` | Not in registry | Unknown: no verdict, treat with caution |

The last row matters: a domain that is not in the registry is **not** declared safe. It is shown as unknown.

### What this demonstrates

1. Kenyan organisations have faced reported website impersonation.
2. Users may encounter websites imitating recognised organisations.
3. Knowing the correct official domain can help users identify potential impersonation.
4. FlareGuard proposes making these checks accessible through a browser extension.

### Proof-of-concept conclusion

> The documented cases illustrate the problem and the proposed check. Flare Guard aims to help users distinguish verified official domains from reported impersonation websites and domains whose identity remains unknown.

The examples demonstrate the problem and proposed functionality, not proven model accuracy.

### Limitations

- Several reported sites were already offline when reviewed, so this proof of concept relies on published reports rather than live page analysis.
- Evidence comes from third-party reporting, and its strength varies by source (see the evidence strength column).
- Registry coverage is currently limited to the domains listed above.
- Three cases are not enough to estimate detection performance.
