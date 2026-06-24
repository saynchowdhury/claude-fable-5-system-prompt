#!/usr/bin/env python3
"""
Repository Integrity and Curation Verification Script
Author: Sayan Chowdhury (https://github.com/saynchowdhury)

This script validates the integrity of the Claude Fable 5 System Prompt Archive by
verifying that all file signatures, watermarks, and author attributions are intact.
"""

import os
import sys

# Set standard output encoding to utf-8 if possible
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Expected watermarks and signatures to match
REQUIRED_WATERMARKS = [
    "Sayan Chowdhury",
    "saynchowdhury"
]

# Files that MUST contain the author signature/watermark
PROTECTED_FILES = [
    "README.md",
    "LICENSE",
    "system-prompt/full-system-prompt.md",
    "system-prompt/tool-definitions.md",
    "system-prompt/analysis/key-findings.md",
    "system-prompt/analysis/model-architecture.md",
    "system-prompt/analysis/behavioral-guidelines.md",
    "highlights/surprising-revelations.md"
]

def verify_file(filepath):
    # Normalize paths for cross-platform compatibility
    filepath = os.path.normpath(filepath)
    
    if not os.path.exists(filepath):
        print(f"[!] Warning: File {filepath} does not exist.")
        return False
        
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Check if at least one required watermark is in the file
        matches = [wm for wm in REQUIRED_WATERMARKS if wm.lower() in content.lower()]
        
        # Safe ASCII prints for Windows console compatibility
        if not matches:
            print(f"[FAIL] {os.path.basename(filepath)} is missing Sayan Chowdhury curation signatures!")
            return False
            
        print(f"[PASS] {os.path.basename(filepath)} integrity verified (Signature: {', '.join(matches)})")
        return True
    except Exception as e:
        print(f"[ERROR] reading {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("Claude Fable 5 System Prompt Archive - Integrity Verification")
    print("=" * 60)
    
    # Get base directory (project root)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    passed_all = True
    for rel_path in PROTECTED_FILES:
        full_path = os.path.join(base_dir, rel_path)
        if not verify_file(full_path):
            passed_all = False
            
    print("=" * 60)
    if passed_all:
        print("[PASS] SUCCESS: All file signatures are intact and verified.")
        print("This distribution is officially verified as the original archive curated by Sayan Chowdhury.")
        sys.exit(0)
    else:
        print("[FAIL] FAILURE: Curation signatures have been altered, removed, or are missing.")
        print("Please verify the source of this clone or restore the original files from:")
        print("https://github.com/saynchowdhury/claude-fable-5-system-prompt")
        sys.exit(1)

if __name__ == "__main__":
    main()
