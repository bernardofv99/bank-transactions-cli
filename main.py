import argparse
from pathlib import Path
from app.processor import TransactionProcessor

def main():
    parser = argparse.ArgumentParser(description="Procesador de transacciones bancarias (CSV)")
    parser.add_argument(
        "--csvfile",
        type=str,
        default=str(Path(__file__).resolve().parent / "data" / "data.csv"),
        help="Ruta del archivo CSV con transacciones"
    )

    args = parser.parse_args()
    processor = TransactionProcessor(args.csvfile)
    processor.load()
    print(processor.generate_report())

if __name__ == "__main__":
    main()
