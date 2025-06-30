# qd_scan — 2D Scan Controller

A modular Python package to simulate and automate a 2D scanning process with logging, data saving, visualization, and testability.

---

## ✨ Features

- Modular device control using `SimStage` and `SimSensor`
- Retry logic with configurable attempts
- Rolling average filter for smoothing measurements
- Automatic CSV saving and heatmap generation
- Full logging and error handling
- Unit-tested (retry logic, filtering, peak detection)

---

## 🗂️ Project Structure

```
qd_scan/
├── scanner.py           # Main scan logic
├── sim_devices.py       # Simulated hardware
├── device_wrappers.py   # Controller wrappers
├── save_file.py         # CSV + filtered data
├── plotting.py          # Heatmap generation
├── logging_setup.py     # Logging config
├── tests/
│   └── test_scanner.py  # Unit tests (pytest + mocking)
├── config.yaml          # Scan configuration
└── scan_demo.ipynb      # Jupyter notebook demo
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Main packages:

- numpy
- matplotlib
- pyyaml
- pytest
- ipykernel (for notebook support)

---

## 🚀 Usage

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

---

## 🧪 Testing

Run all unit tests (including mocking):

```bash
pytest
```

Test coverage:
- Retry logic on stage failures
- Rolling average filter (basic & edge cases)
- Peak detection from filtered data

---

## 📓 Jupyter Notebook

Use `scan_demo.ipynb` to:
- Demonstrate interactive scan execution
- Show raw vs filtered values
- Display 2D heatmap inline

---

## 🔧 Configuration

Editable via `config.yaml`. Includes:

```yaml
x: [0, 5, 6]                # start, stop, number of points
y: [0, 5, 6]
attempts: 3                # number of retries for stage
failure_rate: 0.1          # simulated stage failure rate
rolling_average_window: 3  # window size for smoothing
output_csv: scan_output.csv
output_plot: heatmap.png
log_level: INFO
```

---

## 🧠 Design Notes

- Wrappers (`stageController`, `sensorController`) isolate failure logic and allow easy mocking
- Results stored as `(x, y, value)` tuples
- Filtering and saving modularized for testability
- Log-first approach to help debug device behavior

---