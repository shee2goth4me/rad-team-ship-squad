#!/usr/bin/env python3
"""
Extract GitHub username from application files
"""

import os
import yaml
import sys

def find_application_files():
    """Find all application files in pending directory"""
    app_files = []
    pending_dir = 'applications/2025/pending'
    
    if os.path.exists(pending_dir):
        for file in os.listdir(pending_dir):
            if file.endswith('.yml') and file != 'template.yml':
                app_files.append(os.path.join(pending_dir, file))
    
    return app_files

def extract_username(file_path):
    """Extract username from application file"""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            return data.get('essentials', {}).get('github_username', '')
    except:
        return None

def main():
    app_files = find_application_files()
    
    if not app_files:
        print("No application files found")
        sys.exit(1)
    
    # Get the most recent application file
    latest_file = max(app_files, key=os.path.getctime)
    username = extract_username(latest_file)
    
    if username:
        print(f"::set-output name=username::{username}")
    else:
        print("Failed to extract username")
        sys.exit(1)

if __name__ == "__main__":
    main()
