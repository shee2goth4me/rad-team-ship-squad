# 📚 How to Apply - Complete Step-by-Step Guide

Welcome to the Ship-Every-Friday Squad application process! This guide will walk you through every step from start to finish.

## 🎯 Before You Start

### Quick Checklist
- [ ] Active GitHub account with public contributions
- [ ] Experience with MERN stack (MongoDB, Express, React, Node.js)
- [ ] Python knowledge for backend services
- [ ] Experience using AI coding tools (Cursor, Claude, Copilot, etc.)
- [ ] Ready to ship code to production every Friday

### What We're Looking For
1. **Open Source Contributions** - Real PRs to real projects
2. **Public Projects** - Your own repos showing your skills
3. **GenAI Tool Usage** - Evidence you code with AI as a teammate
4. **Consistent Activity** - Regular commits showing you ship often
5. **Production Mindset** - Tests, CI/CD, monitoring in your projects

## 📋 Step-by-Step Application Process

### Step 1: Fork the Repository

1. Go to https://github.com/hoichoi-opensource/rad-team-ship-squad
2. Click the "Fork" button in the top-right corner
3. This creates your own copy of the repository

### Step 2: Clone Your Fork Locally


### Step 3: Create Your Application Branch

```bash
# Create a new branch for your application
git checkout -b application/YOUR-GITHUB-USERNAME

# Example: if your username is 'shipcoder123'
git checkout -b application/shipcoder123
```

### Step 4: Create Your Application File

```bash
# Copy the template to create your application
cp applications/template.yml applications/2025/pending/YOUR-GITHUB-USERNAME.yml

# Example:
cp applications/template.yml applications/2025/pending/shipcoder123.yml
```

### Step 5: Fill Out Your Application

Open the file in your favorite editor (bonus points for using Cursor! 🤖):

```bash
# Using Cursor
cursor applications/2025/pending/YOUR-GITHUB-USERNAME.yml

# Or VS Code
code applications/2025/pending/YOUR-GITHUB-USERNAME.yml

# Or any editor
nano applications/2025/pending/YOUR-GITHUB-USERNAME.yml
```

### Step 6: Validate Your Application (Optional but Recommended)

```bash
# Run the validation script locally
python scripts/validate_application.py applications/2025/pending/YOUR-GITHUB-USERNAME.yml
```

### Step 7: Commit Your Application

```bash
# Add your application file
git add applications/2025/pending/YOUR-GITHUB-USERNAME.yml

# Commit with a meaningful message
git commit -m "🚀 Application for Ship-Every-Friday Squad - YOUR-GITHUB-USERNAME"
```

### Step 8: Push to Your Fork

```bash
git push origin application/YOUR-GITHUB-USERNAME
```

### Step 9: Create the Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Ensure base repository is `rad-team/rad-team-ship-squad`
4. Click "Create pull request"

### Step 10: Wait for Automated Analysis

Within minutes, our bot will analyze and score your application!

## 📊 Understanding Your Score

### Scoring Breakdown (Total: 100 points)

1. **GenAI Tool Mastery (50 points) - MOST IMPORTANT!**
   - Cursor usage: 15 points
   - Claude usage: 10 points
   - GitHub Copilot: 10 points
   - Other AI tools: 8 points (Codeium, Tabnine, v0.dev, etc.)
   - AI-powered projects: Up to 7 points

2. **Open Source Contributions (30 points)**
   - Merged PRs to external repos: 2 points each (max 15)
   - Maintained projects with 10+ stars: 2 points each (max 10)
   - Contribution quality: Up to 5 points

3. **Project Portfolio (10 points)**
   - MERN projects: Up to 5 points
   - Python projects: Up to 5 points

4. **GitHub Activity (5 points)**
   - Daily commits get full points

5. **Production Readiness (5 points)**
   - CI/CD setup: 2 points
   - Testing: 2 points
   - Documentation: 1 point

### Score Thresholds

- **80-100**: Ready to ship! Priority review and fast-track process
- **60-79**: Strong potential! Standard review process
- **40-59**: Promising! Focus on areas to improve
- **<40**: Keep building! Specific feedback provided

## 💡 Tips to Maximize Your Score

### GenAI Excellence (50% of score!)
```bash
# Add .cursorrules to your projects
echo "indent_style: space\nindent_size: 2" > .cursorrules
git add .cursorrules
git commit -m "Add Cursor configuration"
```

### Open Source Impact (30% of score!)
- Focus on quality PRs that get merged
- Maintain projects with real users
- Contribute consistently

## 🎯 Ready?

**Let's ship together! Fork the repo and show us what you've got! 🚀**
