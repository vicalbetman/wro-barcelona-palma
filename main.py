import yaml
import xarray as xr

def main():
    with open("config.yaml", "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    waves_path = cfg["data"]["waves_file"]
    ds = xr.open_dataset(waves_path)

    hs_var = cfg["data"]["waves_vars"]["hs"]
    dir_var = cfg["data"]["waves_vars"]["wave_dir"]

    print("✅ Config cargado")
    print("✅ Dataset abierto:", waves_path)
    print("Variables disponibles:", list(ds.data_vars))
    print("Hs var:", hs_var, "shape:", ds[hs_var].shape)
    print("Dir var:", dir_var, "shape:", ds[dir_var].shape)
    print("Tiempo:", ds["time"].values[0], "→", ds["time"].values[-1])

if __name__ == "__main__":
    main()
