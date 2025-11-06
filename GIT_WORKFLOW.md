# Git Workflow for Your Custom FlightTracker

## 🎯 Goal
Keep your customizations in your own GitHub fork while staying connected to the original repository.

---

## 📋 Quick Start (3 Steps)

### Step 1: Fork on GitHub (Manual - Do This First!)

1. Go to https://github.com/ColinWaddell/FlightTracker
2. Click **"Fork"** button (top right)
3. GitHub creates your copy at `https://github.com/YOUR_USERNAME/FlightTracker`

### Step 2: Run the Setup Script

```bash
cd /Users/grzegorzskibinski/workspace/FlightTracker
./setup_my_fork.sh
```

This will:
- ✅ Create a custom branch `poznan-customizations`
- ✅ Commit all your changes
- ✅ Show you the next steps

### Step 3: Connect Your Fork and Push

```bash
# Add your fork as a remote (replace YOUR_USERNAME)
git remote add myfork https://github.com/YOUR_USERNAME/FlightTracker.git

# Push your custom branch
git push myfork poznan-customizations

# Set as default branch (optional)
git push myfork poznan-customizations:main
```

**Done!** 🎉 Your changes are now on your GitHub fork.

---

## 🔄 Repository Structure After Setup

```
origin  → https://github.com/ColinWaddell/FlightTracker (original repo)
myfork  → https://github.com/YOUR_USERNAME/FlightTracker (your fork)

Branches:
├── master (tracks original)
└── poznan-customizations (your changes) ⭐
```

---

## 💡 Common Workflows

### Make More Changes

```bash
# Make sure you're on your custom branch
git checkout poznan-customizations

# Edit files...
# (e.g., add more airports, adjust config)

# Stage and commit
git add utilities/airports.py
git commit -m "Added more airports"

# Push to your fork
git push myfork poznan-customizations
```

### Pull Updates from Original Repository

```bash
# Switch to master branch
git checkout master

# Pull latest from original
git pull origin master

# Switch back to your branch
git checkout poznan-customizations

# Merge updates (if you want them)
git merge master

# Resolve any conflicts, then push
git push myfork poznan-customizations
```

### View Your Changes

```bash
# See what changed from original
git diff master..poznan-customizations

# See commit history
git log --oneline
```

---

## 📦 What's Being Committed

### Modified Files (Existing)
- ✅ `config.py` - Your Poznan location and settings
- ✅ `scenes/weather.py` - Temperature display fixes
- ✅ `scenes/journey.py` - City name support
- ✅ `scenes/planedetails.py` - Route display
- ✅ `utilities/overhead.py` - 10 flight limit
- ✅ `display/__init__.py` - Any display changes
- ✅ `scenes/date.py`, `scenes/day.py` - Any changes

### New Files
- ✅ `utilities/airports.py` - Airport city mapping (150+ airports)
- ✅ `deploy_updates.sh` - Deployment automation
- ✅ `CITY_NAMES_FEATURE.md` - Feature documentation
- ✅ `DISPLAY_EXAMPLE.md` - Visual examples
- ✅ `setup_my_fork.sh` - This setup script
- ✅ `GIT_WORKFLOW.md` - This guide

### Excluded from Git
- ❌ `scenes-old/` - Backup folder (in .gitignore)
- ❌ `__pycache__/` - Python cache
- ❌ `env/` - Virtual environment

---

## 🔐 Authentication

When you push, GitHub will ask for authentication. Use:
- **Username**: Your GitHub username
- **Password**: **Personal Access Token** (not your password!)

### Create a Personal Access Token:
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (full control)
4. Copy the token and use it as your password

---

## 🌐 Viewing Your Fork Online

After pushing, visit:
```
https://github.com/YOUR_USERNAME/FlightTracker/tree/poznan-customizations
```

You'll see:
- All your custom files
- Your commit history
- Easy way to share your setup with others

---

## 🚀 Deploy to Raspberry Pi from Your Fork

On your Raspberry Pi, switch to your fork:

```bash
cd ~/FlightTracker
git remote add myfork https://github.com/YOUR_USERNAME/FlightTracker.git
git fetch myfork
git checkout poznan-customizations
```

Or clone fresh from your fork:
```bash
git clone -b poznan-customizations https://github.com/YOUR_USERNAME/FlightTracker
```

---

## ⚠️ Important Notes

1. **Never commit sensitive data**
   - Your API key is in `config.py` - consider using environment variables
   - Or add `config.py` to `.gitignore` and keep it local

2. **Keep branches separate**
   - `master` = original code (clean)
   - `poznan-customizations` = your changes (custom)

3. **Stay updated** (optional)
   - Periodically merge updates from original repo
   - Only if you want new features from upstream

---

## 🎯 Summary

**Your workflow:**
```bash
# Work on your custom branch
git checkout poznan-customizations

# Make changes, commit, push
git add .
git commit -m "Description"
git push myfork poznan-customizations
```

**Original stays clean:**
- `origin/master` = Original ColinWaddell's code
- Your changes only in `poznan-customizations` branch

**Best of both worlds!** 🎉

---

## 📞 Need Help?

Common issues:

**"Permission denied"**
- Use Personal Access Token, not password

**"Branch already exists"**
- Run: `git checkout poznan-customizations`

**"Conflicts during merge"**
- Resolve conflicts manually in affected files
- Then: `git add .` and `git commit`

**Want to start over?**
```bash
git checkout master
git branch -D poznan-customizations
./setup_my_fork.sh  # Run setup again
```

