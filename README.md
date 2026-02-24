# da-instaseis

Data assimilation of global wavefields using [instaseis](https://instaseis.net/).

## Repository layout

```
da-instaseis/
├── notebooks/          # Jupyter notebooks (examples, tutorials)
│   ├── getting_started.ipynb      # Introduction and basic usage
│   └── generate_wavefields.ipynb  # Synthetic & real data workflows
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

This opens JupyterLab in your browser. Navigate to the `notebooks/` directory to access:

- **`getting_started.ipynb`** - Introduction and basic usage examples
- **`generate_wavefields.ipynb`** - Complete workflow for:
  - Generating synthetic wavefields using Instaseis/Syngine
  - Downloading real seismic data from FDSN networks (II, IU)
  - Querying earthquake catalogs (M≥7.0 in 2023)
  - Processing and visualizing multi-component waveforms
  - Saving data in NPZ format for machine learning applications

### Run individual notebooks from command line

```bash
# Execute all cells in a notebook
pixi run jupyter nbconvert --to notebook --execute notebooks/getting_started.ipynb

# Or use papermill for parameterized execution
pixi run pip install papermill
pixi run papermill notebooks/generate_wavefields.ipynb output.ipynb
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
| [obspy](https://docs.obspy.org/) | conda-forge | Seismological data handling & FDSN access |
| [instaseis](https://instaseis.net/) | pip | Green's function database access |
| [matplotlib](https://matplotlib.org/) | conda-forge | Visualization |
| [numpy](https://numpy.org/) | conda-forge | Numerical computing |
| [scipy](https://scipy.org/) | conda-forge | Scientific algorithms |
| [pandas](https://pandas.pydata.org/) | conda-forge | Data manipulation & analysis |
| [cartopy](https://scitools.org.uk/cartopy/) | conda-forge | Geographic map visualizations |
| [pillow](https://python-pillow.org/) | conda-forge | Image processing |
| [h5py](https://www.h5py.org/) | conda-forge | HDF5 file I/O |
| [torch](https://pytorch.org/) | pip | Deep learning / data assimilation |
| [jupyterlab](https://jupyter.org/) | conda-forge | Interactive notebooks |

### Optional dependencies

- **longboard** (install separately): `pip install longboard` - Interactive seismic waveform visualization (if available in your Python environment)

## Working with Real Seismic Data

The `generate_wavefields.ipynb` notebook includes functionality to download real seismic data from FDSN web services:

1. **Earthquake catalog queries** - Query global earthquake catalogs (e.g., M≥7.0 events in 2023)
2. **Waveform downloads** - Download 3-component long-period data (LHZ, LHN, LHE) from networks II, IU
3. **Automatic preprocessing** - Remove instrument response, filter, and organize by station
4. **Multiple visualization approaches**:
   - Traditional matplotlib record sections
   - Interactive longboard explorer (optional)
   - Geographic maps with Cartopy
5. **Data export** - Save processed data as NumPy NPZ arrays for machine learning workflows

**Note**: Internet connection required for FDSN data downloads. Downloads may take several minutes depending on the number of earthquakes and stations.

## Quick Start

```bash
# Clone and set up the environment
git clone https://github.com/Denolle-Lab/da-instaseis.git
cd da-instaseis
pixi install

# Launch JupyterLab
pixi run lab

# Or run tests
pixi run test
```

Then open `notebooks/generate_wavefields.ipynb` or `notebooks/getting_started.ipynb` in JupyterLab.

## License

See [LICENSE](LICENSE).
