#!/usr/bin/env python3
"""
Post-generation hook for cookiecutter template.
Creates a virtual environment and installs specified packages.
Supports multiple package managers: uv (preferred) or pip (fallback).
"""
import subprocess
import sys
import os


def is_tool_available(tool_name):
    """Check if a command-line tool is available."""
    try:
        result = subprocess.run(
            [tool_name, "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, None


def create_with_uv(packages):
    """Create virtual environment and install packages using uv."""
    print("Using uv (fast package manager)...")

    try:
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

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error during uv setup: {e}")
        return False


def create_with_pip(packages):
    """Create virtual environment using standard venv and install packages with pip."""
    print("Using standard Python venv + pip...")

    try:
        # Create virtual environment using python -m venv
        print("Creating .venv directory...")
        subprocess.run(
            [sys.executable, "-m", "venv", ".venv"],
            check=True
        )
        print("Virtual environment created successfully!")

        # Determine pip executable path based on OS
        if os.name == 'nt':  # Windows
            pip_executable = os.path.join(".venv", "Scripts", "pip")
        else:  # Linux/macOS
            pip_executable = os.path.join(".venv", "bin", "pip")

        # Install packages if any are specified
        if packages:
            package_list = packages.split()
            print(f"Installing packages: {', '.join(package_list)}")

            subprocess.run(
                [pip_executable, "install"] + package_list,
                check=True
            )
            print(f"Successfully installed {len(package_list)} package(s)!")
        else:
            print("No packages specified for installation.")

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error during pip setup: {e}")
        return False


def setup_environment():
    """Set up virtual environment using available package manager."""
    # Get the packages from cookiecutter context
    packages = "{{ cookiecutter.python_packages }}".strip()

    print("Setting up virtual environment...")
    print("-" * 50)

    # Check for uv (preferred)
    uv_available, uv_version = is_tool_available("uv")

    if uv_available:
        print(f"Found uv: {uv_version}")
        success = create_with_uv(packages)
        if success:
            print("\nSetup complete!")
            print("Activate your virtual environment with:")
            print("  source .venv/bin/activate  (Linux/macOS)")
            print("  .venv\\Scripts\\activate     (Windows)")
            return
        else:
            print("\nFalling back to pip...")

    # Fallback to standard pip
    print("uv not found, using standard Python venv + pip")
    success = create_with_pip(packages)

    if success:
        print("\nSetup complete!")
        print("Activate your virtual environment with:")
        print("  source .venv/bin/activate  (Linux/macOS)")
        print("  .venv\\Scripts\\activate     (Windows)")
        print("\nTip: Install uv for faster package management:")
        print("  https://github.com/astral-sh/uv")
    else:
        print("\nError: Failed to set up virtual environment")
        print("Please set up your environment manually")
        sys.exit(1)


if __name__ == "__main__":
    setup_environment()
