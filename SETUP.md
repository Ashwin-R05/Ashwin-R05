# GitHub Special Repository Setup Guide (`Ashwin-R05`)

This guide explains how to set up and deploy your personalized animated profile README to GitHub.

---

## 🚀 Step 1: Create the GitHub Special Repository

1. Go to [GitHub - Create a New Repository](https://github.com/new).
2. Set the **Repository Name** to exactly: `Ashwin-R05`
   *(GitHub will show a prompt saying: "You found a secret! Ashwin-R05/Ashwin-R05 is a ✨special✨ repository that you can use to add a README.md to your GitHub profile.")*
3. Make sure the repository is **Public**.
4. **Initialize with README**: Leave unchecked (you already have the complete repository files).
5. Click **Create repository**.

---

## 📤 Step 2: Push the Files to GitHub

Unzip the provided `Ashwin-R05.zip` archive or open a terminal inside this directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Initial commit
git commit -m "feat: setup animated special profile README & workflows"

# Set default branch to main
git branch -M main

# Link remote repository
git remote add origin https://github.com/Ashwin-R05/Ashwin-R05.git

# Push to GitHub
git push -u origin main
```

---

## ⚙️ Step 3: Enable GitHub Actions Permissions

For the automated workflows (`projects.yml` and `snake.yml`) to automatically push the generated SVGs (`projects` and `output` branches), you must enable Write permissions:

1. Go to your repository on GitHub: `https://github.com/Ashwin-R05/Ashwin-R05`
2. Click **Settings** ⚙️ at the top right of the repository.
3. In the left sidebar, click **Actions** -> **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Check **"Allow GitHub Actions to create and approve pull requests"**.
7. Click **Save**.

---

## ⚡ Step 4: Trigger the Workflows

1. In your repository, click the **Actions** tab.
2. Select **Generate Projects Panel** on the left, click **Run workflow** -> **Run workflow**.
3. Select **Generate Snake Animation** on the left, click **Run workflow** -> **Run workflow**.
4. Select **Generate Hero Banner** on the left, click **Run workflow** -> **Run workflow**.

Once complete:
- The **snake animation** will automatically be pushed to the `output` branch.
- The **projects panel** SVG will automatically be pushed to the `projects` branch.

Your profile README is now **100% live** and will update automatically every 6 to 12 hours!

---

## 🛠️ Step 5: Editing Featured Projects in the Future

To add, remove, or edit featured projects:
1. Open `projects.json`.
2. Add your repository details (`name`, `repo`, `description`, `tags`, `logo`).
3. Commit & push to `main`.
4. The GitHub Action will automatically re-fetch live stars/languages and regenerate the projects panel SVG without changing the README!
