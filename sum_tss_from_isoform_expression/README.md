# sum_tss_from_isoform_expression

This script sums expression for isoforms with the same transcription start site (TSS).

## Inputs

* Expression input
* A transcript to tss positions mapping file in the format "{transcript_ID}\tchr{chr_number}:{position}". The provided version is from GBM_TF_analysis using gencode v27.

## Usage

python sum_tss_from_isoform_expression.py [-h] -i INPUT -t TRANS -e EXP [-s SAMPLES] -m MAPPING -o OUTPUT

  -i INPUT, --input INPUT
                        Expression input file.
  -t TRANS, --trans TRANS
                        Name of column containing transcript IDs.
  -e EXP, --exp EXP     Comma separated list of names of columns containing
                        expression values.
  -s SAMPLES, --samples SAMPLES
                        Optional comma separated list of sample names to
                        overwrite expression column headers.
  -m MAPPING, --mapping MAPPING
                        Mapping file for transcript to tss positions.
  -o OUTPUT, --output OUTPUT
                        Output directory and prefix for file names.

