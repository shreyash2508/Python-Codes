# ⚡ Python for Hardware Engineers

Python practice repo for my work as an **RTL Design / Hardware Engineer**. Small, self-contained exercises that tie Python to real hardware problems.

## 🎯 What's Inside

- **Bit manipulation** – masks, shifts, endianness, Gray code
- **Number formats** – two's complement, fixed-point, Q-format
- **Golden models** – FIFOs, FSMs, arbiters, CRC/LFSR
- **Verification** – cocotb and pytest testbenches

## 🛠️ Tooling & Automation

- Parse synthesis, timing and simulation logs
- Analyze VCD waveforms
- Generate SystemVerilog and register maps from scripts

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
pytest
```

## 📐 Conventions

- One problem per file, with a docstring explaining the hardware motivation
- Every model comes with a pytest
- Bit-accurate: widths are masked explicitly
