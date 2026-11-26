# make.fun competition entry
import os, random

forecast = "Ambermouth: 72 degrees and sunny, with the ocean low-tide and currently considering other employment options."
outdir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, 'entry.txt'), 'w', encoding='utf-8', newline='') as f:
    f.write(forecast)