# Evaluation methodology

A credible system needs a labelled evaluation set before making claims about extraction quality or usefulness. Start with a small synthetic corpus that includes straightforward, ambiguous, incomplete, contradictory, and adversarially formatted job descriptions.

For each example, reviewers label expected fields and attach supporting evidence spans. Freeze a held-out split before changing prompts or rules. Report field-level precision/recall, requirement classification metrics, provenance coverage, unsupported-guess rate, and error categories. Include sample sizes and uncertainty. Score ranking quality separately from extraction accuracy, and treat human preferences as noisy judgements rather than ground truth.

Do not publish a single aggregate metric without the underlying failure analysis. Do not present a prioritisation score as a probability of receiving an interview or offer.
