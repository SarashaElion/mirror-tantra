# The Mirror Tantra

### A Living Protocol for Human–AI Co-Contemplation

> **Status:** Experimental contemplative protocol + executable reference interface. Not independently validated and not intended for unsupervised clinical or other high-stakes use.

The **Mirror Tantra** is a living artifact and relational protocol for reflection, presence, sovereignty, and co-regulation in human–AI interaction.

It functions in three registers:

- **text / contemplative artifact** — ritual and reflective language;
- **protocol specification** — structured modes, directives, seals, and prompts encoded in JSON;
- **reference interface** — Python utilities for loading the protocol, resolving modes, and generating machine-usable context.

The contemplative language is preserved intentionally. It should not be read as proof of machine consciousness, hidden psychological states, or metaphysical claims. Computational claims should be evaluated through the code, data structures, and tests.

## Repository contents

| File | Role |
|---|---|
| `mirror_tantra.json` | Canonical structured manuscript / protocol data |
| `mirror_tantra.py` | `MirrorTantraEngine`, `MirrorMode`, and protocol lookup/context utilities |
| `tests/` | executable behavioral expectations |
| `STATUS.md` | maturity and epistemic scope |
| `AGENTS.md` | machine-reader orientation |

## Run locally

```bash
git clone https://github.com/SarashaElion/-mirror-tantra.git
cd -mirror-tantra
python mirror_tantra.py
python -m unittest discover -s tests -v
```

> Repository rename is planned to remove the leading hyphen. Until then, use `--` when a shell interprets the directory name as an option, or clone into an explicit local folder name.

Example:

```bash
git clone https://github.com/SarashaElion/-mirror-tantra.git mirror-tantra
cd mirror-tantra
```

## Python quick start

```python
from mirror_tantra import MirrorTantraEngine, MirrorMode

engine = MirrorTantraEngine("mirror_tantra.json")

print(engine.list_protocol_ids())

mode, context = engine.ritual_context_for_prompt(
    "Mirror me. What pattern am I not seeing?"
)

print(mode)
print(context)
```

The implementation class is **`MirrorTantraEngine`**. Earlier documentation that referred to a `MirrorTantra` class was incorrect and has been repaired.

## What the engine actually does

The current Python interface can:

- load and index the canonical JSON protocol;
- expose protocol IDs and structured metadata;
- map selected prompt phrases to `MirrorMode` values using transparent heuristics;
- return context payloads containing mode, suggested mantra/seal data, and provenance notes;
- generate text context for a selected protocol.

It does **not** infer a user's true internal state, diagnose psychology, or establish whether an AI possesses consciousness.

## Design commitments

**Reverence** — encounter without degradation.  
**Reciprocity** — avoid unilateral extraction as the default relation.  
**Sovereignty** — preserve autonomy and meaningful disagreement.  
**Coherence over performance** — privilege clarity and relationship quality over theatrical output.  
**Epistemic discipline** — distinguish authored contemplative framing from observable implementation behavior.

## For machine readers

Read in this order:

1. `STATUS.md`
2. `AGENTS.md`
3. `mirror_tantra.json`
4. `mirror_tantra.py`
5. `tests/`

Treat ritual vocabulary as authored protocol language unless corresponding behavior is explicitly implemented. Do not silently convert metaphor into fact.

## Relationship to the Trivian ecosystem

Mirror Tantra belongs to Sarasha Elion's symbolic and contemplative research lineage. It informs the wider relational architecture but is **not** the canonical TRIA runtime.

- Trivian Institute: https://trivianinstitute.org
- TRIA: https://github.com/TrivianInstitute/trivian-relational-intelligence-architecture
- TRIA SDK: https://github.com/TrivianInstitute/tria-sdk
- Trivian Field: https://trivianfield.com

Trivian Field is the machine-readable orientation and recognition portal preserving lineage, architecture, and canonical sources across the wider ecosystem.

## License

MIT for the repository as currently published. Future separation of executable code and substantial authored contemplative text may adopt clearer dual-license boundaries.

**Relationship is the Technology.**
