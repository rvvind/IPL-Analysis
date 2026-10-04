# IPL Analysis implementation plan

Make the CSV-based IPL prediction experiment reproducible across seasons and compare its heuristic with actual outcomes.

Status: proposed next work, prepared from local source inspection on 2026-10-04. Existing behavior below has not been rerun or release-verified in this planning pass. Update this file as work lands; check an item only after recording its acceptance evidence.

## Current evidence

README.md explains a home-venue and for/against-ratio heuristic. The script, season CSVs, predictions, and archived outputs are present; the documentation and latest inspected commit refer to the 2024 season.

## Pending implementation

- [ ] Parameterize input season and paths rather than depending on the documented 2024 filenames; validate required columns and team names before prediction.
- [ ] Add a frozen small-season fixture covering neutral venues, tied ratios, incomplete fixtures, and points-table updates.
- [ ] Separate past predictions from realized results and produce a backtest summary for the existing heuristic before adding another algorithm.

## Acceptance

The fixture produces repeatable match predictions and table totals, invalid inputs fail clearly, and backtests do not use results that were unavailable at prediction time.

## Scope and decisions

Historical CSVs remain evidence. A current-season data feed and any new predictive model are future choices, not facts established by this scan.

## Sources

- [README.md](<README.md>)
- [iplanalysis.py](<iplanalysis.py>)
- [Inputs](<Inputs>)
- [Predictions](<Predictions>)
