## Flare gun – Research Proof of Concept

Objective: Demonstrate why a Kenyan website identity verification extension is needed, using documented website impersonation cases.

### Evidence

| Suspicious domain | Organisation impersonated | Research finding                                                        |
| ----------------- | ------------------------- | ----------------------------------------------------------------------- |
| `ntsca.cc`        | NTSA                      | Reported fraudulent traffic-fine payment website.                       |
| `kqairways.com`   | Kenya Airways             | Reported lookalike airline booking website.                             |
| `moohk.co.ke`     | Mookh                     | Reported ticketing website lookalike; evidence requires further review. |

### Proposed extension demonstration

Compare reported domains with recognised official domains:

- `ntsa.go.ke` → Verified official
- `ntsca.cc` → Reported impersonation
- `kenya-airways.com` → Verified official
- `kqairways.com` → Reported lookalike
- `moohk.co.ke` → Reported lookalike; review caveat

### What this demonstrates

1. Kenyan organisations have faced reported website impersonation.
2. Users may encounter websites imitating recognised organisations.
3. Knowing the correct official domain can help users identify potential impersonation.
4. Flare Gun proposes making these checks accessible through a browser extension.

Proof-of-concept conclusion:

> The documented cases demonstrate a real need for accessible website identity verification in Kenya. Flare Gun addresses this gap by helping users distinguish verified official domains from reported impersonation websites and domains whose identity remains unknown.

The examples demonstrate the problem and proposed functionality, not proven model accuracy.
