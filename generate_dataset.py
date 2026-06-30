from pathlib import Path
import runpy

script_path = Path(__file__).resolve().parent / "AI_Predictive_Maintenance" / "dataset" / "generate_dataset.py"
runpy.run_path(str(script_path), run_name="__main__")
