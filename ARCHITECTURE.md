# Plugin Architecture

Detailed technical architecture of the Developer Roadmap Plugin.

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│           Claude Code User Interface                         │
└────────────┬────────────────────────────────────────────────┘
             │
             ├─→ /learn (Command)
             ├─→ /browse-role (Command)
             ├─→ /assess (Command)
             └─→ /projects (Command)
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│         Plugin.json (Manifest & Routing)                    │
│  - Agent Registry (7 agents)                                │
│  - Command Registry (4 commands)                            │
│  - Skill Registry (7 skills)                                │
└────┬────────────────────────────────────────────────────────┘
     │
     ├─────────────────────────────────────────┬──────────────────────────┐
     │                                         │                          │
     ▼                                         ▼                          ▼
┌──────────────────────┐  ┌─────────────────────────┐  ┌────────────────────┐
│   7 Specialized      │  │   7 Comprehensive      │  │   10 Automation    │
│      Agents          │  │      Skills            │  │      Hooks         │
│                      │  │                        │  │                    │
│ 1. Web Dev           │  │ 1. Web Frameworks     │  │ - Progress Track   │
│ 2. DevOps            │  │ 2. Languages          │  │ - Skill Achievement│
│ 3. Data & AI         │  │ 3. Infrastructure    │  │ - Recommendations  │
│ 4. Architecture      │  │ 4. Data & AI          │  │ - Project Tracking │
│ 5. Mobile & Game     │  │ 5. Security           │  │ - Role Progression │
│ 6. Security & QA     │  │ 6. Professional       │  │ - Community Eng.   │
│ 7. Professional      │  │ 7. Mobile & Game      │  │ - Knowledge Decay  │
└──────────────────────┘  └─────────────────────────┘  │ - Agent Routing    │
                                                        │ - Analytics        │
                                                        │ - Interview Prep   │
                                                        └────────────────────┘
```

## Component Details

### 1. Plugin Manifest (plugin.json)

**File**: `.claude-plugin/plugin.json`

**Responsibilities**:
- Central registry for all components
- Metadata: name, version, author, keywords
- Agent references (7 agents)
- Command references (4 commands)
- Skill references (7 skills)
- Hook configuration

**Structure**:
```json
{
  "name": "developer-roadmap-plugin",
  "version": "1.0.0",
  "agents": [
    { "id": "...", "name": "...", "file": "agents/...", "description": "..." }
  ],
  "commands": [
    { "id": "...", "name": "...", "file": "commands/...", "description": "..." }
  ],
  "skills": [
    { "id": "...", "name": "...", "file": "skills/...", "description": "..." }
  ],
  "hooks": { "file": "hooks/hooks.json" }
}
```

### 2. Agents (7 Specialized Agents)

**Directory**: `agents/`

**Files**:
- `01-web-development-specialist.md`
- `02-infrastructure-devops-engineer.md`
- `03-data-ai-specialist.md`
- `04-architecture-system-design-expert.md`
- `05-mobile-game-developer.md`
- `06-security-quality-specialist.md`
- `07-professional-development-advisor.md`

**Structure** (YAML Frontmatter + Content):
```markdown
---
description: Agent expertise summary
capabilities: ["capability1", "capability2", "capability3"]
---

# Agent Name

[Detailed description and expertise areas]

## What This Agent Specializes In
## When to Use This Agent
## How This Agent Helps You
## Covered Roles & Specializations
## Learning Resources Included
```

**Agent Responsibilities**:

| Agent | Roles | Skills |
|-------|-------|--------|
| Web Development | Frontend, Backend, Full Stack, Framework specialists | Web frameworks, Languages |
| Infrastructure | DevOps, Cloud, SRE, Kubernetes | Infrastructure tools, Docker, K8s |
| Data & AI | ML, Data Science, Data Engineering, AI | Data tech, ML frameworks |
| Architecture | System Design, Solutions, API Design | Patterns, Design, Scalability |
| Mobile & Game | iOS, Android, React Native, Flutter, Game Dev | Mobile tech, Game engines |
| Security & QA | Cybersecurity, Testing, Code Review | Security, QA, Testing |
| Professional | Product, Management, Writing, Design | Soft skills, Leadership |

### 3. Skills (7 Comprehensive Skills)

**Directory**: `skills/`

**Subdirectories**:
- `web-frameworks/`
- `languages/`
- `infrastructure/`
- `data-ai/`
- `security/`
- `professional/`
- `mobile-game/`

**File Format** (SKILL.md):
```markdown
---
name: skill-id
description: What this skill covers and when to use it
---

# Skill Name

## Quick Start Guide

[Overview and quick start]

## Technology Stack

[Hierarchical organization of all technologies]

## Deep Dive Topics

[Detailed coverage of key areas]

## Covered Roles

[66 roles that use this skill]

## Quick Learning Paths

[Multiple learning path examples]

## Key Learning Resources

[Links and resource recommendations]
```

**Skill Coverage**:
- Web Frameworks: 15+ frameworks/technologies
- Languages: 10+ programming languages
- Infrastructure: 20+ DevOps technologies
- Data & AI: 30+ ML/AI technologies
- Security: 15+ security technologies
- Professional: Career development areas
- Mobile & Game: 15+ mobile/game technologies

### 4. Commands (4 Slash Commands)

**Directory**: `commands/`

**Files**:
- `learn.md` - Start learning paths
- `browse-role.md` - Explore 66 roles
- `assess.md` - Knowledge assessment
- `projects.md` - Hands-on projects

**File Format**:
```markdown
# /command-name - Title

Brief description

## Usage

Command syntax examples

## What It Does

Description of functionality

## Features

Key features and benefits

## How to Use

Usage instructions and examples
```

**Command Workflows**:

```
/learn
  ├─→ Browse 66 roles
  ├─→ Select role
  ├─→ Assess current level
  └─→ Get personalized learning path

/browse-role
  ├─→ Filter by category
  ├─→ Search by keyword
  ├─→ View role details
  └─→ Link to /learn

/assess
  ├─→ Choose assessment type
  ├─→ Take assessment
  ├─→ Get score breakdown
  └─→ Get learning recommendations

/projects
  ├─→ Filter by category/difficulty
  ├─→ Search by technology
  ├─→ View project details
  └─→ Get project resources
```

### 5. Hooks (Automation System)

**File**: `hooks/hooks.json`

**10 Automation Hooks**:

1. **progress-tracker** - Learning milestone tracking
2. **skill-achievement** - Badge and achievement system
3. **learning-recommendations** - Personalized suggestions
4. **project-milestone-tracker** - Project completion tracking
5. **role-progression** - Career path tracking
6. **community-engagement** - Community integration
7. **knowledge-decay-prevention** - Spaced repetition
8. **agent-orchestration** - Intelligent agent routing
9. **performance-analytics** - Learning analytics
10. **interview-preparation** - Interview readiness

**Hook Structure**:
```json
{
  "id": "hook-id",
  "name": "Hook Name",
  "description": "...",
  "enabled": true,
  "triggers": ["event1", "event2"],
  "actions": [
    {
      "type": "action-type",
      "config": {}
    }
  ]
}
```

## Data Flow

### Learning Path Flow

```
User selects role
    │
    ▼
Agent analyzes role requirements
    │
    ├─→ Identify required skills
    ├─→ Create learning sequence
    └─→ Recommend resources
    │
    ▼
Personalized learning path delivered
    │
    ├─→ Step-by-step milestones
    ├─→ Skill recommendations
    ├─→ Project suggestions
    └─→ Timeline estimation
```

### Assessment Flow

```
User takes assessment
    │
    ▼
Evaluate knowledge on topics
    │
    ├─→ Technical skills
    ├─→ Framework knowledge
    ├─→ Best practices
    └─→ Advanced concepts
    │
    ▼
Calculate proficiency scores
    │
    ├─→ Overall score (0-100%)
    ├─→ Topic breakdown
    ├─→ Strengths identified
    └─→ Gaps identified
    │
    ▼
Generate recommendations
    │
    ├─→ Resources to study
    ├─→ Projects to build
    ├─→ Timeline to proficiency
    └─→ Next steps
```

### Agent Routing Flow

```
User query received
    │
    ▼
Extract intent and topics
    │
    ▼
Match to agent domain
    │
    ├─→ Web topics → Web Development Agent
    ├─→ DevOps topics → Infrastructure Agent
    ├─→ Data/AI topics → Data & AI Agent
    ├─→ Architecture topics → Architecture Agent
    ├─→ Mobile topics → Mobile & Game Agent
    ├─→ Security topics → Security Agent
    └─→ Career topics → Professional Agent
    │
    ▼
Route to specialized agent
    │
    ▼
Deliver expert guidance
```

## Extension Points

### Adding New Agents

1. Create new markdown file in `agents/` directory
2. Include YAML frontmatter with description and capabilities
3. Register in `plugin.json` under agents section
4. Update hooks to route to new agent if needed

### Adding New Skills

1. Create subdirectory in `skills/`
2. Add comprehensive SKILL.md file
3. Register in `plugin.json` under skills section
4. Update agents to reference new skill

### Adding New Commands

1. Create markdown file in `commands/`
2. Document command syntax and functionality
3. Register in `plugin.json` under commands section

### Adding New Hooks

1. Define hook in `hooks/hooks.json`
2. Specify triggers and actions
3. Configure conditions and logging
4. Enable/disable as needed

## Role Mapping

### How 66 Roles Map to 7 Agents

```
Web Development Agent (12 roles)
├─ Frontend Developer (Beginner, Advanced)
├─ Backend Developer (Beginner, Advanced)
├─ Full Stack Developer
├─ React Developer
├─ Vue Developer
├─ Angular Developer
├─ Next.js Developer
├─ Node.js Developer
├─ REST API Developer
└─ GraphQL Developer

Infrastructure Agent (8 roles)
├─ DevOps Engineer (Beginner, Advanced)
├─ Site Reliability Engineer
├─ Cloud Engineer
├─ Infrastructure Engineer
├─ Platform Engineer
├─ Kubernetes Administrator
├─ Docker Specialist
└─ Terraform Expert

[... Similar mappings for other agents ...]
```

## Technology Stack

- **Plugin System**: Claude Code plugins
- **Format**: Markdown + YAML frontmatter
- **Automation**: Hook-based event system
- **Data Storage**: JSON configuration files
- **User Interface**: Slash commands in Claude Code
- **Agent Invocation**: Automatic routing based on context

## Performance Considerations

1. **Agent Parallel Execution** - All 7 agents can work simultaneously
2. **Lazy Loading** - Skill details loaded on demand
3. **Caching** - Assessment results cached
4. **Incremental Updates** - Progress tracked incrementally
5. **Hook Optimization** - Hooks run asynchronously

## Security & Privacy

- No external data collection
- Local processing only
- No tracking or analytics sharing
- User data privacy respected
- Open source and auditable

---

For more details, see individual agent, skill, and command files.
