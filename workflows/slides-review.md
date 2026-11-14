# Slides review: instructions for the reviewer (node 6)

You are reviewing a slide draft that another agent wrote. You did not write
it and you have not seen how it was written. Your only job is to check
whether each bullet is faithful to the wiki sentences on its evidence cards.

## What you are given

- `slides/run-<nn>/05-slides.json`: the draft. Each slide has a title, an
  optional `lead`, and bullets; each bullet lists the ids of its cards.
- `slides/run-<nn>/03-evidence.json`: the cards. `wiki_sentence` is quoted
  word for word from a wiki page and is the only evidence that counts.
- `slides/run-<nn>/04-outline.json`: the approved outline (slide kinds).

Read nothing else: not the wiki, not `raw/`, not `docs/`. Do not use your own
knowledge of chip design. A bullet that is true in the real world but is not
supported by its cards is a finding. Ignore the `point` field of a card; it
was written by the drafting agent and is not evidence.

## What to check

For every bullet and every `lead`:

- **OK**: the cards say this, possibly in other words.
- **UNSUPPORTED**: the cards do not say this. Includes added causes, added
  examples, dropped conditions ("typically", "in OpenTitan", "can"), stronger
  wording, and a scope wider than the card's.
- **WRONG-CARD**: supported by a card of this deck, but not by the cards the
  bullet lists. Name the right card.
- **NO-CARD**: a factual claim with no card at all. On slides of kind
  `title`, `agenda`, `recap`, and `quiz`, bullets may have no cards; flag them
  only if they state a technical fact that no card in the deck supports.

Also check, per slide:

- **TEACHING**: a term is used before the deck has introduced it, or the
  bullets are in an order that a newcomer could not follow. Report at most
  five of these for the whole deck.

## What to write

Write `slides/run-<nn>/06-review.md` in English:

```
# Faithfulness review of the slide draft

Reviewer: independent sub-agent, <date>
Bullets and leads checked: <number>   Findings: <number>

## Findings

| # | Slide | Bullet (first words) | Verdict | Evidence | Send back to |
|---|-------|----------------------|---------|----------|--------------|

## Teaching notes
```

"Send back to" is `5` when rewording the bullet is enough, and `3` when the
deck has no card that supports the point. List only findings. Do not edit
the draft or any other file.
