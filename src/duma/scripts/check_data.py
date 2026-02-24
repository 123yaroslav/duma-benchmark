#!/usr/bin/env python3
"""
Script to check if the duma data directory is properly configured.
"""

import sys

from duma.utils.utils import DATA_DIR


def main():
    """Main function to check data directory."""
    print("duma Data Directory Checker")
    print("=" * 40)

    print(f"Data directory: {DATA_DIR}")

    if DATA_DIR.exists():
        print("✅ Data directory exists")
        print("You can now run duma commands.")
    else:
        print("❌ Data directory does not exist!")
        print("\nTo fix this, you can:")
        print("1. Set the DUMA_DATA_DIR environment variable:")
        print("   export DUMA_DATA_DIR=/path/to/your/duma-bench/data")
        print("2. (Legacy) TAU2_DATA_DIR is still supported during migration")
        print("3. Or ensure the data directory exists in the expected location")
        sys.exit(1)


if __name__ == "__main__":
    main()
