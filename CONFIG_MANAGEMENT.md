# Config File Management Guide

## 🔑 Understanding config.py

**Important:** `config.py` contains your API key and is **NOT in Git** (it's in `.gitignore`)

---

## 📁 Where config.py Lives

### Your Mac
```
/Users/grzegorzskibinski/workspace/FlightTracker/config.py
✅ Has your API key
✅ Not in Git/GitHub
```

### Raspberry Pi
```
~/FlightTracker/config.py
✅ Has your API key
✅ Not in Git/GitHub
```

### GitHub (Your Fork)
```
config.example.py only (template without API key)
❌ No config.py (safe!)
```

---

## ✅ Safe Workflow

### When Making Changes on Your Mac

**Scenario 1: Changed only code files (scenes, utilities)**
```bash
./deploy_updates.sh
# When asked "Copy config.py?" → Press 'n' (No)
```
✅ Your Pi keeps its existing config.py with API key

**Scenario 2: Changed config.py settings (zone, brightness, etc.)**
```bash
./deploy_updates.sh
# When asked "Copy config.py?" → Press 'y' (Yes)
```
✅ Your updated config.py (with API key) goes to Pi

---

## 🎯 Best Practice

### Keep config.py the Same on Both Machines

**Initial Setup (Do Once):**

1. **On your Mac** - Edit `config.py`:
```python
ZONE_HOME = { ... }  # Your location
OPENWEATHER_API_KEY = "your-key-here"  # Your API key
```

2. **Copy to Pi** (first time):
```bash
scp config.py skibinskig@flightradarpi.local:~/FlightTracker/
```

3. **Done!** Both machines have the same config with API key

**Later Updates:**

When you change settings in config.py (zone, brightness, etc.):
- Edit on Mac
- Run `./deploy_updates.sh`
- Say 'y' when asked to copy config.py
- Both machines stay in sync ✅

---

## ❌ What NOT to Do

**Don't do this:**
```bash
git add config.py  # ❌ NO! Contains API key
git commit
git push
```

**Why?** 
- Your API key would be public on GitHub
- Security risk!
- `.gitignore` prevents this, but don't force it

---

## 🔒 If You Accidentally Committed Your API Key

**If you ever push API key to GitHub by mistake:**

1. **Immediately regenerate** your API key at OpenWeather
2. **Remove from Git history** (harder, ask if needed)
3. Update config.py with new key on both machines

**Prevention:** config.py is in `.gitignore` - Git won't commit it!

---

## 💡 Alternative: Environment Variables

**More secure option (advanced):**

Instead of hardcoding API key in config.py:

```python
import os

# In config.py
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
```

Then set on each machine:
```bash
# On Raspberry Pi
export OPENWEATHER_API_KEY="your-key-here"
```

Add to `~/.bashrc` or the systemd service file.

---

## 📋 Quick Reference

| Action | Copy config.py? | Why |
|--------|----------------|-----|
| Added airports | No | Only code changed |
| Fixed bugs | No | Only code changed |
| Changed ZONE_HOME | Yes | Settings changed |
| Changed BRIGHTNESS | Yes | Settings changed |
| Changed MIN_ALTITUDE | Yes | Settings changed |
| First setup | Yes | Need config on Pi |

---

## ✅ Summary

**Good workflow:**
1. ✅ Edit config.py on Mac (has API key)
2. ✅ Deploy with `./deploy_updates.sh`
3. ✅ Script asks before copying config.py
4. ✅ Both machines have API key
5. ✅ config.py never goes to GitHub (in .gitignore)

**You don't need to worry about:**
- ❌ Removing API key before commit (config.py not in Git)
- ❌ Adding API key back (it stays in config.py locally)
- ❌ API key on GitHub (config.py ignored)

**Simple rule:** Keep config.py the same on Mac and Pi, never commit it to Git! ✨

