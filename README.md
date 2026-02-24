# da-instaseis

Data assimilation of global wavefields using [instaseis](https://instaseis.net/).

## Repository layout

```
da-instaseis/
├── notebooks/          # Jupyter notebooks (examples, tutorials)
│   └── getting_started.ipynb
├── src/
│   └── da_instaseis/   # Main Python package
│       ├── __init__.py
│       ├── waveforms.py
│       └── plotting.py
├── tests/              # pytest unit tests
├── pixi.toml           # Pixi environment & task definitions
├── pyproject.toml      # Python package metadata (PEP 517/518)
└── README.md
```

## Installation

This project uses [Pixi](https://prefix.dev/docs/pixi/overview) to manage the
conda + pip environment.

### 1 – Install Pixi (once per machine)

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

### 2 – Clone and install the environment

```bash
git clone https://github.com/Denolle-Lab/da-instaseis.git
cd da-instaseis
pixi install
```

Pixi reads `pixi.toml` and installs all dependencies (obspy, matplotlib,
scipy, numpy, jupyterlab, … from **conda-forge**; torch and instaseis via
**pip**) into an isolated environment under `.pixi/`.

### 3 – Activate the environment

```bash
pixi shell
```

Or prefix individual commands with `pixi run`:

```bash
pixi run python -c "import obspy; print(obspy.__version__)"
```

## Usage

### Launch JupyterLab

```bash
pixi run lab
```

### Run the tests

```bash
pixi run test
```

### Install the package in editable mode (optional)

Inside `pixi shell`:

```bash
pip install -e .
```

## Key dependencies

| Package | Source | Purpose |
|---------|--------|---------|
| [obspy](https://docs.obspy.org/) | conda-forge | Seismological data handling |
| [instaseis](https://instaseis.net/) | pip | Green's function database access |
| [matplotlib](https://matplotlib.org/) | conda-forge | Visualisation |
| [numpy](https://numpy.org/) | conda-forge | Numerical computing |
| [scipy](https://scipy.org/) | conda-forge | Scientific algorithms |
| [torch](https://pytorch.org/) | pip | Deep learning / data assimilation |
| [jupyterlab](https://jupyter.org/) | conda-forge | Interactive notebooks |

## License

See [LICENSE](LICENSE).
