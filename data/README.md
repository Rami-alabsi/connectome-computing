# Data

## Primary dataset

The initial target is FlyWire FAFB v783 (Female Adult Fly Brain).

Codex exposes FAFB v783 as a public static dataset and recommends static downloadable files for bulk analysis rather than scraping the interactive application.

The public FlyWire release is licensed CC BY-NC 4.0. External datasets remain subject to their own terms.

Large biological data files must not be committed to this repository. The ingestion tool will discover resources, download selected files locally, record the dataset/version and support checksum validation.

Initial targets:
- neuron/cell metadata
- consolidated cell types
- connection tables
- synapse counts/weights
- neurotransmitter metadata where available

Every experiment should record dataset, snapshot/version, resource name, download timestamp, file checksum, analysis configuration and software commit.
