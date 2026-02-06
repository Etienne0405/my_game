"""
Utility function to get resource paths that work with both development and PyInstaller.
"""
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running in development mode
        base_path = os.path.abspath(".")
    except Exception as e:
        # Fallback to current directory if anything else goes wrong
        base_path = os.path.abspath(".")
    
    # Normalize path separators (convert forward slashes to backslashes on Windows)
    normalized_path = relative_path.replace('/', os.sep).replace('\\', os.sep)
    full_path = os.path.join(base_path, normalized_path)
    
    # Normalize the final path
    full_path = os.path.normpath(full_path)
    
    # Debug: Print path if file doesn't exist (only in dev mode)
    if not os.path.exists(full_path) and not hasattr(sys, '_MEIPASS'):
        print(f"Warning: Resource not found at {full_path}")
    
    return full_path
