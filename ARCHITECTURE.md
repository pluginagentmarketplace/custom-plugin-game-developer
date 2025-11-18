# Game Developer Plugin - Technical Architecture

## System Overview

```
User → Commands → Plugin.json → Agents ↔ Skills ↔ Hooks
                      ↓
                  7 Experts
                 (Parallel)
```

## Components

### 1. Plugin Manifest (plugin.json)

Registry for:
- 7 Game Dev Agents
- 4 Slash Commands
- 7 Skill Categories
- 10 Automation Hooks

### 2. Seven Agents (Specialized)

| Agent | Specialty |
|-------|-----------|
| Game Designer | Mechanics, levels, UX/UI |
| Game Programmer | C#/C++, systems, code |
| Graphics & Rendering | Shaders, VFX, optimization |
| Audio & Sound Design | Audio systems, music, voice |
| Networking & Multiplayer | Netcode, servers, sync |
| Tools & Pipeline | Build systems, automation |
| Game Publishing | Platforms, monetization, live ops |

**Routing**:
- `/learn-gamedev` → Route by specialization
- User question → Analyze → Route to relevant agent(s)

### 3. Seven Skills

Each SKILL.md covers 1000+ hours:

1. **Game Engines** - Unity, Unreal, Godot
2. **Languages** - C#, C++, GDScript
3. **Graphics** - Shaders, VFX, lighting
4. **Audio** - Audio programming, music
5. **Networking** - Multiplayer, servers
6. **Optimization** - Performance, profiling
7. **Tools & Workflows** - Pipelines, CI/CD

### 4. Four Commands

- `/learn-gamedev` - Learning paths
- `/explore-gamedev` - Browse content
- `/game-profile` - Assessments
- `/gamedev-projects` - Projects

### 5. Ten Hooks

Automation for:
- Progress tracking
- Portfolio building
- Engine specialization
- Role progression
- Community networking
- Project roadmaps
- Game jam prep
- Publishing guides
- Performance optimization
- Industry insights

## Data Flow

```
Learning Path:
  User → /learn-gamedev → Choose Specialization →
  Get Personalized Path → Track Progress →
  Recommend Projects → Build Portfolio

Assessment:
  User → /game-profile → Questions →
  Score Calculation → Gap Analysis →
  Recommendations

Project Flow:
  User → /gamedev-projects → Filter →
  Select Project → Get Resources →
  Complete → Add to Portfolio
```

## Extension Points

### Adding Agents
1. Create `agents/XX-new-agent.md`
2. Add YAML frontmatter
3. Register in plugin.json

### Adding Skills
1. Create `skills/category/SKILL.md`
2. Include comprehensive content
3. Register in plugin.json

### Adding Hooks
1. Define in `hooks/hooks.json`
2. Specify triggers and actions
3. Enable/disable as needed

---

For detailed role-specific paths, see LEARNING-PATHS.md
