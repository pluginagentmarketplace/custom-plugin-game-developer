<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Game+Developer+Assistant;7+Agents+%7C+21+Skills;Claude+Code+Plugin" alt="Game Developer Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-game-developer/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-7-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-21-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-game-developer)

---

### What is this?

> **Game Developer Assistant** is a Claude Code plugin with **7 agents** and **21 skills** for game developer development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin add marketplace pluginagentmarketplace/custom-plugin-game-developer

# Step 2️⃣ Install the plugin
/plugin install custom-plugin-game-developer@pluginagentmarketplace-game-developer

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-game-developer.git
cd custom-plugin-game-developer

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
custom-plugin-game-developer:05-networking-multiplayer
custom-plugin-game-developer:01-game-designer
custom-plugin-game-developer:03-graphics-rendering
custom-plugin-game-developer:04-audio-sound-design
custom-plugin-game-developer:06-tools-pipeline
... and 2 more
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **7 Agents** | Specialized AI agents for game developer tasks |
| 🛠️ **21 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |

---

## 🤖 Agents

### 7 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **05-networking-multiplayer** | Expert in multiplayer systems, netcode, synchronization algo |
| 2 | **01-game-designer** | Expert in game design, mechanics, level design, player psych |
| 3 | **03-graphics-rendering** | Expert in 3D graphics, shader programming, visual effects, a |
| 4 | **04-audio-sound-design** | Expert in game audio programming, sound design, music compos |
| 5 | **06-tools-pipeline** | Expert in game development tools, asset pipelines, build aut |
| 6 | **02-game-programmer** | Expert game programmer specializing in C# (Unity), C++ (Unre |
| 7 | **07-game-publishing** | Expert in game publishing, platform deployment, monetization |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `asset-optimization` | Asset pipeline optimization, compression, streaming, and res | `Skill("custom-plugin-game-developer:asset-optimization")` |
| `synchronization-algorithms` | Network synchronization, lag compensation, client prediction | `Skill("custom-plugin-game-developer:synchronization-algorithms")` |
| `game-design-theory` | Comprehensive game design theory covering mechanics, dynamic | `Skill("custom-plugin-game-developer:game-design-theory")` |
| `monetization-systems` | Game monetization strategies, in-app purchases, battle passe | `Skill("custom-plugin-game-developer:monetization-systems")` |
| `level-design` | Level design fundamentals, pacing, difficulty progression, e | `Skill("custom-plugin-game-developer:level-design")` |
| `graphics-rendering` | 3D graphics, shaders, VFX, lighting, rendering optimization. | `Skill("custom-plugin-game-developer:graphics-rendering")` |
| `shader-techniques` | Advanced shader programming, visual effects, custom material | `Skill("custom-plugin-game-developer:shader-techniques")` |
| `audio-systems` | Game audio systems, music, spatial audio, sound effects, voi | `Skill("custom-plugin-game-developer:audio-systems")` |
| `publishing-platforms` | Platform submission processes, certification requirements, a | `Skill("custom-plugin-game-developer:publishing-platforms")` |
| `programming-languages` | Game programming languages - C#, C++, GDScript. Learn syntax | `Skill("custom-plugin-game-developer:programming-languages")` |
| ... | +11 more | See skills/ directory |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/explore` | gamedev - Explore Game Development |
| `/learn` | gamedev - Personalized Game Development Learning Paths |
| `/projects` | projects - Game Development Projects |
| `/profile` | profile - Assess Game Development Skills |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-game-developer/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 7 agents
├── 📁 skills/              # 21 skills (Golden Format)
├── 📁 commands/            # 4 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Last Updated** | 2025-12-29 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 7 |
| **Skills** | 21 |
| **Commands** | 4 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
