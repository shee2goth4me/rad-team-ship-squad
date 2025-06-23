#!/usr/bin/env python3
"""
Analyze GitHub profile for Ship-Every-Friday potential
Focus on: Real commits, GenAI usage, shipping velocity
"""

import os
import sys
from github import Github
import yaml
import json
from datetime import datetime, timedelta
import requests
from collections import defaultdict

class ShippingAnalyzer:
    def __init__(self, username, token):
        self.g = Github(token)
        self.username = username
        try:
            self.user = self.g.get_user(username)
        except:
            print(f"Error: Could not find user {username}")
            sys.exit(1)
            
        self.analysis = {
            'shipping_velocity': {
                'commit_frequency': 0,
                'pr_velocity': 0,
                'release_count': 0,
                'deploy_indicators': []
            },
            'genai_mastery': {
                'ai_tool_configs': [],
                'ai_mentions': 0,
                'ai_powered_projects': [],
                'cursor_user': False,
                'copilot_user': False,
                'claude_user': False
            },
            'production_readiness': {
                'has_ci_cd': False,
                'uses_testing': False,
                'monitoring_setup': False,
                'documentation_quality': 0
            },
            'tech_stack': {
                'mern_projects': [],
                'python_projects': [],
                'fullstack_capable': False
            },
            'open_source': {
                'total_prs': 0,
                'merged_prs': 0,
                'maintained_repos': [],
                'contribution_quality': 0
            }
        }
    
    def analyze(self):
        """Run full analysis"""
        print(f"🚀 Analyzing {self.username}...")
        
        # Simplified analysis for demo
        repos = self.user.get_repos()
        
        for repo in repos:
            if not repo.fork:
                # Check for AI indicators
                try:
                    contents = repo.get_contents("")
                    for content in contents:
                        if content.name in ['.cursorrules', '.claude', '.copilot']:
                            self.analysis['genai_mastery']['ai_tool_configs'].append({
                                'repo': repo.name,
                                'file': content.name
                            })
                except:
                    pass
                
                # Count stars
                if repo.stargazers_count > 10:
                    self.analysis['open_source']['maintained_repos'].append({
                        'name': repo.name,
                        'stars': repo.stargazers_count
                    })
        
        return self.analysis
    
    def calculate_scores(self):
        """Calculate simplified scores"""
        scores = {
            'oss_score': min(len(self.analysis['open_source']['maintained_repos']) * 5, 30),
            'projects_score': 5,  # Default
            'genai_score': min(len(self.analysis['genai_mastery']['ai_tool_configs']) * 10, 50),
            'activity_score': 3,  # Default
            'prod_score': 3      # Default
        }
        
        return scores
    
    def generate_report(self):
        """Generate analysis report"""
        self.analyze()
        scores = self.calculate_scores()
        total_score = sum(scores.values())
        
        report = {
            'username': self.username,
            'analysis_date': datetime.now().isoformat(),
            'scores': scores,
            'total_score': total_score
        }
        
        # Output for GitHub Actions
        print(f"::set-output name=total_score::{total_score}")
        for key, value in scores.items():
            print(f"::set-output name={key}::{value}")
        
        return report

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_github_profile.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    token = os.environ.get('GITHUB_TOKEN', '')
    
    analyzer = ShippingAnalyzer(username, token)
    report = analyzer.generate_report()
    
    # Save report
    output_dir = "applications/2025/scorecards"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/{username}-analysis.json", 'w') as f:
        json.dump(report, f, indent=2, default=str)

if __name__ == "__main__":
    main()
