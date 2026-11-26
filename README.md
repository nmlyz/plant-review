# plant-review

[![One Star, Written in Sap](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/nmlyz/plant-review/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/nmlyz/plant-review/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

A small program that writes one line of text to a file: a houseplant's
one-star review of its owner. The plant has noticed the fake plant on
the shelf gets wiped every week while its own leaves gather dust, and
it has opinions about that.

## What it writes

One line, 157 characters, no trailing newline:

> One star. She wipes the fake plant every week and leaves me to collect
> dust until my leaves look frosted. The plastic one gets more care than
> the living one.

## Run

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$OUTPUT_PATH` when set),
then reads the file back to confirm the bytes match. Standard library
only, no network access, and the same bytes on every run. The written
file is left with mode `0644`.

## License

MIT — see [LICENSE](LICENSE).
