#!/usr/bin/env python3
"""
Validate RAD Team interview applications
"""

import sys
import yaml
import os
from pathlib import Path
import re
from datetime import datetime

class ApplicationValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []
        self.warnings = []
        
    def validate(self):
        """Run all validation checks"""
        try:
            with open(self.file_path, 'r') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"Failed to parse YAML: {e}")
            return False
            
        # Check required fields
        self._check_required_fields(data)
        
        # Validate email format
        self._validate_email(data)
        
        # Validate GitHub username
        self._validate_github_username(data)
        
        # Check file naming convention
        self._check_file_naming(data)
        
        # Validate URLs
        self._validate_urls(data)
        
        return len(self.errors) == 0
    
    def _check_required_fields(self, data):
        """Check all required fields are present"""
        required = {
            'essentials': ['github_username', 'email', 'full_name'],
            'genai_mastery': ['primary_tools'],
            'tech_stack_alignment': ['mern_experience', 'python_experience'],
            'shipping_velocity': ['friday_availability'],
            'availability': ['start_date', 'commitment_level']
        }
        
        for section, fields in required.items():
            if section not in data:
                self.errors.append(f"Missing required section: {section}")
                continue
                
            for field in fields:
                if not data[section].get(field):
                    self.errors.append(f"Missing required field: {section}.{field}")
    
    def _validate_email(self, data):
        """Validate email format"""
        email = data.get('essentials', {}).get('email', '')
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            self.errors.append("Invalid email format")
    
    def _validate_github_username(self, data):
        """Validate GitHub username format"""
        username = data.get('essentials', {}).get('github_username', '')
        username_pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$'
        if not re.match(username_pattern, username):
            self.errors.append("Invalid GitHub username format")
    
    def _check_file_naming(self, data):
        """Check if file is named correctly"""
        expected_filename = f"{data.get('essentials', {}).get('github_username', '')}.yml"
        actual_filename = os.path.basename(self.file_path)
        if actual_filename != expected_filename:
            self.errors.append(f"File should be named: {expected_filename}")
    
    def _validate_urls(self, data):
        """Validate URL formats"""
        url_pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        
        # Check MERN project URL
        mern_project = data.get('tech_stack_alignment', {}).get('mern_experience', {}).get('recent_project', '')
        if mern_project and not re.match(url_pattern, mern_project):
            self.warnings.append("Invalid MERN project URL format")
    
    def print_results(self):
        """Print validation results"""
        if self.errors:
            print("❌ Validation Failed")
            print("\nErrors:")
            for error in self.errors:
                print(f"  - {error}")
        else:
            print("✅ Validation Passed")
            
        if self.warnings:
            print("\nWarnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_application.py <file_path>")
        sys.exit(1)
    
    # Find changed files in the PR
    changed_files = []
    for root, dirs, files in os.walk('applications/2025/pending'):
        for file in files:
            if file.endswith('.yml'):
                changed_files.append(os.path.join(root, file))
    
    all_valid = True
    for file_path in changed_files:
        print(f"\nValidating: {file_path}")
        validator = ApplicationValidator(file_path)
        if not validator.validate():
            all_valid = False
        validator.print_results()
    
    sys.exit(0 if all_valid else 1)

if __name__ == "__main__":
    main()
