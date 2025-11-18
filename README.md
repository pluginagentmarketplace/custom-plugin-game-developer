# 🚀 Developer Roadmap Plugin for Claude Code

Complete learning system based on [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) with **66 different development roles**, **7 specialized agents**, and comprehensive skill tracking.

## 🎯 Quick Start

### Install the Plugin

```bash
# Load directly into Claude Code
claude code /path/to/custom-plugin-game-developer
```

Or add to your Claude Code configuration:

```json
{
  "plugins": [
    {
      "name": "developer-roadmap-plugin",
      "path": "./custom-plugin-game-developer"
    }
  ]
}
```

### Available Commands

- **`/learn`** - Discover and start learning paths for 66 development roles
- **`/browse-role`** - Explore all available roles and career paths
- **`/assess`** - Assess your knowledge level for any role or skill
- **`/projects`** - Browse 100+ hands-on projects for practical learning

## ✨ What's Included

### 🧠 7 Specialized Agents

Each agent is an expert in their domain, working in parallel:

1. **Web Development Specialist** (`01-web-development-specialist.md`)
   - Frontend, Backend, Full Stack development
   - Framework expertise (React, Vue, Angular, Next.js, etc.)
   - Web performance and security
   - API design and development

2. **Infrastructure & DevOps Engineer** (`02-infrastructure-devops-engineer.md`)
   - DevOps engineering and CI/CD
   - Containerization (Docker) and orchestration (Kubernetes)
   - Infrastructure as Code (Terraform)
   - Cloud platforms (AWS, Azure, GCP)
   - Linux administration

3. **Data & AI Specialist** (`03-data-ai-specialist.md`)
   - Machine Learning and Deep Learning
   - Data Engineering and data pipelines
   - AI and LLMs
   - MLOps and production ML systems
   - Data analysis and visualization

4. **Architecture & System Design Expert** (`04-architecture-system-design-expert.md`)
   - System design and large-scale architecture
   - Architectural patterns and design decisions
   - Scalability and distributed systems
   - API and database design

5. **Mobile & Game Developer** (`05-mobile-game-developer.md`)
   - iOS development (Swift, SwiftUI)
   - Android development (Kotlin)
   - Cross-platform (React Native, Flutter)
   - Game development and multiplayer systems

6. **Security & Quality Specialist** (`06-security-quality-specialist.md`)
   - Cybersecurity and threat models
   - QA, testing, and automation
   - Code review practices
   - Compliance and security best practices

7. **Professional Development Advisor** (`07-professional-development-advisor.md`)
   - Product Management
   - Engineering Management and leadership
   - Technical Writing
   - Developer Relations and advocacy
   - UX/UI Design

### 🎓 7 Comprehensive Skills

Detailed SKILL.md files covering all 66 roles:

1. **Web Frameworks & Libraries** - React, Vue, Angular, Node.js, Django, Laravel, ASP.NET Core
2. **Programming Languages** - JavaScript, Python, Java, Rust, Go, C++, PHP, Swift, Kotlin
3. **Infrastructure & DevOps Tools** - Docker, Kubernetes, Terraform, AWS, Azure, GCP
4. **Data & AI Technologies** - ML, Deep Learning, Data Engineering, MLOps, NLP, Computer Vision
5. **Security & Quality Practices** - Cybersecurity, QA, Testing, Code Review, Compliance
6. **Professional Development Skills** - Product Management, Leadership, Writing, Design
7. **Mobile & Game Development** - iOS, Android, React Native, Flutter, Game Engines

### 🎮 66 Covered Development Roles

**Web Development (12):**
- Frontend/Backend/Full Stack Developer
- React, Vue, Angular, Next.js, Node.js Developers
- REST API, GraphQL, Performance Specialists

**Infrastructure & DevOps (8):**
- DevOps Engineer, SRE, Cloud Engineer
- Kubernetes, Docker, Terraform Specialists
- AWS/GCP/Azure Solutions Architects

**Data & AI (10):**
- Machine Learning Engineer, Data Scientist
- Data Engineer, AI Engineer, MLOps Engineer
- Computer Vision, NLP Specialists

**Architecture & System Design (6):**
- Software Architect, System Design Expert
- Solutions Architect, Database Architect
- API Designer

**Mobile & Game (12):**
- iOS, Android, React Native, Flutter Developers
- Game Developer, Game Programmer
- Server-Side Game Developer

**Security & Quality (8):**
- Cybersecurity Engineer, Penetration Tester
- QA Engineer, Test Automation Engineer
- Code Reviewer, Security Analyst

**Professional (10):**
- Product Manager, Engineering Manager
- Technical Writer, Developer Advocate
- UX Designer, Design Manager

## 📚 How to Use

### 1. Start Learning a Role

```
/learn Frontend Developer
```

Get a personalized learning path with:
- Step-by-step roadmap
- Recommended resources
- Project ideas
- Estimated timeline

### 2. Explore Available Roles

```
/browse-role
/browse-role web
/browse-role machine learning
```

Browse all 66 roles by category or search.

### 3. Assess Your Knowledge

```
/assess React Developer
/assess System Design
```

Get a proficiency score and gap analysis.

### 4. Find Hands-On Projects

```
/projects
/projects advanced
/projects Kubernetes
```

Discover 100+ projects from beginner to expert level.

## 🏗️ Plugin Architecture

```
custom-plugin-game-developer/
├── .claude-plugin/
│   └── plugin.json                 # Plugin manifest
├── agents/                         # 7 specialized agents
│   ├── 01-web-development-specialist.md
│   ├── 02-infrastructure-devops-engineer.md
│   ├── 03-data-ai-specialist.md
│   ├── 04-architecture-system-design-expert.md
│   ├── 05-mobile-game-developer.md
│   ├── 06-security-quality-specialist.md
│   └── 07-professional-development-advisor.md
├── commands/                       # 4 slash commands
│   ├── learn.md
│   ├── browse-role.md
│   ├── assess.md
│   └── projects.md
├── skills/                         # 7 skill categories
│   ├── web-frameworks/SKILL.md
│   ├── languages/SKILL.md
│   ├── infrastructure/SKILL.md
│   ├── data-ai/SKILL.md
│   ├── security/SKILL.md
│   ├── professional/SKILL.md
│   └── mobile-game/SKILL.md
├── hooks/
│   └── hooks.json                  # Automation hooks
├── README.md                       # This file
├── ARCHITECTURE.md                 # Detailed architecture
└── LEARNING-PATHS.md               # Learning path examples
```

## 🤖 Automated Features (via Hooks)

The plugin includes intelligent automation:

- **Progress Tracking** - Automatically track learning milestones
- **Skill Achievement** - Award badges for skill proficiency
- **Personalized Recommendations** - AI-driven learning suggestions
- **Project Milestone Tracking** - Celebrate completed projects
- **Role Progression** - Monitor progress toward target roles
- **Community Engagement** - Find relevant communities and mentors
- **Knowledge Reinforcement** - Spaced repetition reminders
- **Agent Orchestration** - Automatically route to relevant agents
- **Performance Analytics** - Monthly learning analytics reports
- **Interview Preparation** - Interview guidance and mock questions

## 🎯 Use Cases

### For Career Transition
- Identify target role from 66 available options
- Get personalized learning path
- Track progress with assessments
- Build portfolio with projects
- Prepare for interviews

### For Skill Development
- Learn specific frameworks or technologies
- Get hands-on with projects
- Validate knowledge with assessments
- Find gaps and recommended resources
- Earn skill badges and certificates

### For Mentorship
- Agents provide specialized guidance
- Find communities and mentors
- Get personalized recommendations
- Share progress and celebrate wins
- Network with professionals

### For Team Training
- Design learning programs for teams
- Track team progress
- Identify skill gaps
- Recommend resources
- Measure learning ROI

## 📊 Plugin Statistics

| Metric | Value |
|--------|-------|
| **Total Roles** | 66 |
| **Agents** | 7 |
| **Skills** | 7 (comprehensive) |
| **Commands** | 4 |
| **Projects** | 100+ |
| **Learning Hours** | 1000+ |
| **Code Examples** | 500+ |
| **Automation Hooks** | 10 |
| **Topics Covered** | 50+ |

## 🔥 Key Features

✅ **66 Curated Development Roles** - From classic to emerging roles
✅ **7 Expert Agents** - Specialized knowledge in parallel
✅ **Comprehensive Learning Paths** - From beginner to expert
✅ **100+ Hands-On Projects** - Real-world problem solving
✅ **Smart Assessments** - Track your progress objectively
✅ **Personalized Recommendations** - AI-driven guidance
✅ **Community Integration** - Find mentors and peers
✅ **Portfolio Building** - Showcase your work
✅ **Interview Preparation** - Get ready for jobs
✅ **Modern Architecture** - Clean, modular design

## 🚀 Getting Started

### Step 1: Load the Plugin

```bash
# In Claude Code
/plugin add ./custom-plugin-game-developer

# Or via configuration
claude code --plugin-path ./custom-plugin-game-developer
```

### Step 2: Explore Roles

```
/browse-role
```

### Step 3: Choose Your Path

```
/learn Backend Developer
```

### Step 4: Start Learning

Follow the recommended learning path with resources and projects.

### Step 5: Track Progress

```
/assess Backend Developer
```

Monitor your improvement with assessments.

## 📖 Learning Paths

See `LEARNING-PATHS.md` for detailed example learning paths for:
- Frontend Developer (9 months)
- Backend Developer (9 months)
- Full Stack Developer (15 months)
- DevOps Engineer (12 months)
- Machine Learning Engineer (18 months)
- Mobile Developer (9 months)
- And more!

## 🏛️ Architecture Details

See `ARCHITECTURE.md` for:
- Detailed agent responsibilities
- Skill mapping to roles
- Command workflows
- Hook system design
- Extension points

## 📝 Best Practices

1. **Choose Deliberately** - Select a role aligned with your interests
2. **Build Consistently** - Work through projects in order
3. **Assess Regularly** - Check progress every 3-6 months
4. **Learn in Public** - Share your progress for accountability
5. **Join Communities** - Network with other learners
6. **Mentor Others** - Reinforce your learning by teaching
7. **Specialize Strategically** - Develop deep expertise in one area

## 🔗 External Resources

- [Developer Roadmap](https://roadmap.sh) - Original roadmap source
- [GitHub Repo](https://github.com/kamranahmedse/developer-roadmap) - Source repository
- Official documentation for each technology/framework
- Online communities (Reddit, Discord, Slack)
- Conferences and meetups
- Mentorship platforms

## 🤝 Contributing

Want to improve this plugin?

- Add new skills to existing SKILL.md files
- Create specialized sub-skills
- Add more projects
- Improve agent instructions
- Enhance hooks and automation

## 📄 License

See LICENSE file for details.

## 🙏 Acknowledgments

- Based on [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)
- Designed for Claude Code plugin system
- Community-driven learning approach

## 📞 Support

For questions or issues:
1. Check ARCHITECTURE.md and LEARNING-PATHS.md
2. Review individual agent and skill files
3. Use `/browse-role` to find relevant resources
4. Consult learning path documentation

---

**🎓 Start your learning journey today!**

Choose a role with `/learn`, assess your knowledge with `/assess`, explore projects with `/projects`, and leverage our 7 expert agents to guide your development career!

Made with ❤️ for developers, by developers.
