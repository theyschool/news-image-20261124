# The World in One Day — Tuesday 24 November 2026

[![Rank](https://make.fun/badge/news-image-20261124/theyschool/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/theyschool/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)
[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)

One image summing up the world's news of **Tuesday 24 November 2026**,
rendered with Pillow and real fonts (`build_image.py` → `entry.png`,
1024×1024 PNG). `main.ts` copies `entry.png` to the output directory
and verifies it is a whole PNG within the 1 MiB cap.

## The day's stories

- **Lead — Chess, Geneva:** the World Chess Championship opens. Defending
  champion Gukesh Dommaraju, 20, of India faces challenger Javokhir
  Sindarov, 20, of Uzbekistan in Game 1 of a 14-game match for a
  $2.5 million prize fund — the youngest title match ever.
- **Football / Law:** the Court of Arbitration for Sport is to rule today
  on Senegal's appeal over their stripped AFCON title, after CAF awarded
  Morocco a 3-0 win when Senegal walked off in January's final, won 1-0
  by Senegal.
- **Markets / Japan:** manufacturing PMI 53.7 in November, up from 53.3;
  services 50.5; composite 51.5, a six-month low.
- **Sky:** the Beaver Supermoon peaks today, full phase 9:53 a.m. EST —
  the first of four supermoons.
- **Space / California:** SpaceX is to launch the classified USSF-266
  mission on Falcon 9 from Vandenberg today, window from 7:55 a.m. PT;
  booster B1081 flies a record-tying 29th time.
- **Culture / India:** the 557th birth anniversary of Guru Nanak —
  Guru Nanak Jayanti, observed today, with prayers at the Golden Temple
  in Amritsar.
- **Politics / Portugal:** parliament holds its final vote on the 2027
  budget today, as unions demonstrate outside in Lisbon.

Events scheduled later in the day are worded as happening "today", not
in the past tense. All stories were reported on 24 November 2026.

## Run

```sh
python3 build_image.py          # regenerate entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
