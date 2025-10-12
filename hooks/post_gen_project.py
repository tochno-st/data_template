#!/usr/bin/env python3
"""
Post-generation hook for cookiecutter template.
Creates a virtual environment using uv and installs specified packages.
"""
import subprocess
import sys
import os


def create_venv_with_uv():
    """Create virtual environment and install packages using uv."""
    print("Creating virtual environment with uv...")

    # Get the packages from cookiecutter context
    packages = "{{ cookiecutter.python_packages }}".strip()

    try:
        # Check if uv is installed
        result = subprocess.run(
            ["uv", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Error: uv is not installed. Please install uv first.")
            print("Visit: https://github.com/astral-sh/uv")
            sys.exit(1)

        print(f"Found uv version: {result.stdout.strip()}")

        # Create virtual environment
        print("Creating .venv directory...")
        subprocess.run(
            ["uv", "venv", ".venv"],
            check=True
        )
        print("Virtual environment created successfully!")

        # Install packages if any are specified
        if packages:
            package_list = packages.split()
            print(f"Installing packages: {', '.join(package_list)}")

            subprocess.run(
                ["uv", "pip", "install"] + package_list,
                check=True
            )
            print(f"Successfully installed {len(package_list)} package(s)!")
        else:
            print("No packages specified for installation.")

        print("\nSetup complete!")
        print("Activate your virtual environment with:")
        print("  source .venv/bin/activate  (Linux/macOS)")
        print("  .venv\\Scripts\\activate     (Windows)")

    except subprocess.CalledProcessError as e:
        print(f"Error during setup: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_venv_with_uv()
