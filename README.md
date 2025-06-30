# qd_scan — 2D Scan Controller

A modular Python project to simulate and automate a 2D scanning process with logging, data saving, visualization, and testability.

---

## Features

- Modular device control using `SimStage` and `SimSensor`
- Retry logic with configurable attempts through config.yaml
- Rolling average filter for smoothing measurements, peak detection of sensor values
- Automatic CSV saving and heatmap generation in dedicated measurement folder
- Full logging and error handling
- Unit-tested (retry logic, filtering, peak detection)

---

## Project Structure

```
qdscan/
├── README.md #Breakdown of the project
├── config.py #Loading of config.yaml
├── config.yaml #Parameters for conducting scan
├── devices.py #wrapping interface script with max. retry and retry delay
├── logging_setup.py #handling logging for saving and printing
├── measurements/ #folder data basename_timestamp.csv & basename_timestamp.png is saved
├── plotting.py #for generating the heatmap
├── requirements.txt #required packages to be installed for the venv
├── save_file.py #handles global saving, rolling average and peak detection 
├── scan.log #log file after executing the scan
├── scan_demo.ipynb #demo notebook for interactive inspection of the output
├── scanner.py #main script for executing scan, generating data with analysis
├── sim_devices.py #the script that simulates a scanner and sensor for data read
├── test_scanner.py #automated test script with mocking, analyses control
```

---

## Requirements

Install dependencies:

```bash
python3 -m venv .qdscan
source .qdscan/bin/activate
pip install -r requirements.txt
```

Main packages:

- numpy
- matplotlib
- pyyaml
- pytest
- ipykernel (for notebook support)

---

## Usage

Run a full scan with default config:

```bash
python scanner.py
```

This will:
- Simulate 2D scanning over a grid
- Apply rolling average filtering
- Save raw and filtered data to CSV
- Generate a timestamped heatmap PNG
- Log events to `scan.log`
- Print logged events to terminal

---

## Testing

Run all unit tests (including mocking):

```bash
pytest
```

Test coverage:
- Retry logic on stage failures
- Rolling average filter (basic & edge cases)
- Peak detection from filtered data

---

## Jupyter Notebook

Use `scan_demo.ipynb` to:
- Demonstrate interactive scan execution
- Show raw vs filtered values
- Display 2D heatmap inline

---

## Configuration

Editable via `config.yaml`. Includes:

```yaml
x: [0, 5, 6]                # start, stop, number of points
y: [0, 5, 6]
attempts: 3                # number of retries for stage
failure_rate: 0.1          # simulated stage failure rate
rolling_average_window: 3  # window size for smoothing
output_csv: scan_output	   # csv basename, file extension savepath and timestamp is handled separately
output_plot: heatmap       # heatmap basename, file extension, savepath and timestamp is handled separately
log_level: INFO			   # log level
```

---

## Design Notes

- Wrappers (`stageController`, `sensorController`) isolate failure logic and allow easy mocking
- Results stored as `(x, y, value)` tuples
- Filtering and saving modularized for testability
- Log-first approach to help debug device behavior

---
