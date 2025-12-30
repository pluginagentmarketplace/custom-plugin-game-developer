---
name: explore
version: "2.0.0"
description: Explore Game Development Careers and Specializations
sasmp_version: "1.3.0"
allowed-tools: Read, WebSearch

parameters:
  - name: topic
    type: string
    required: false
    validation:
      enum: [designers, programmers, graphics, audio, networking, tools, publishing, engines, careers]
  - name: engine
    type: string
    required: false
    validation:
      enum: [unity, unreal, godot]
---

# /explore-gamedev - Explore Game Development

Discover game development careers, specializations, and industry paths.

## Usage

```bash
/explore-gamedev
/explore-gamedev designers
/explore-gamedev programmers
/explore-gamedev graphics
/explore-gamedev networking
/explore-gamedev engines
/explore-gamedev unreal
```

## What It Does

- Browse all game development roles and specializations
- Understand required skills for each role
- See career progression paths
- Explore different game engines
- Learn about industry trends and job market

## Roles & Specializations

### Design Roles
| Role | Focus | Agents |
|------|-------|--------|
| Game Designer | Mechanics, systems, balance | 01-game-designer |
| Level Designer | Spatial design, pacing | 01-game-designer |
| Systems Designer | Economy, progression | 01-game-designer |
| Narrative Designer | Story, dialogue | 01-game-designer |

### Programming Roles
| Role | Focus | Agents |
|------|-------|--------|
| Gameplay Programmer | Core mechanics, systems | 02-game-programmer |
| Engine Programmer | Low-level systems | 02-game-programmer |
| Graphics Programmer | Rendering, shaders | 03-graphics-rendering |
| Network Programmer | Multiplayer, servers | 05-networking-multiplayer |
| Tools Programmer | Pipelines, automation | 06-tools-pipeline |
| Audio Programmer | Sound systems, middleware | 04-audio-sound-design |

### Technical Art Roles
| Role | Focus | Agents |
|------|-------|--------|
| Technical Artist | Art/code bridge | 03-graphics-rendering |
| VFX Artist | Particle systems, effects | 03-graphics-rendering |
| Shader Artist | Material creation | 03-graphics-rendering |

### Business Roles
| Role | Focus | Agents |
|------|-------|--------|
| Producer | Project management | 08-project-coordinator |
| Publisher | Release, marketing | 07-game-publishing |
| Community Manager | Player engagement | 07-game-publishing |

## Game Engines

### Unity (C#)
- **Best for**: Mobile, indie, VR/AR, 2D games
- **Market share**: 70%+ mobile games
- **Learning curve**: Moderate
- **Related agents**: All agents support Unity

### Unreal Engine (C++/Blueprints)
- **Best for**: AAA, high-end graphics, large teams
- **Market share**: Major console/PC titles
- **Learning curve**: Steep (C++) / Easy (Blueprints)
- **Related agents**: All agents support Unreal

### Godot (GDScript/C#)
- **Best for**: 2D games, learning, open source
- **Market share**: Growing indie scene
- **Learning curve**: Easy
- **Related agents**: All agents support Godot

## Career Progression

```
TYPICAL CAREER PATH:
┌─────────────────────────────────────────────────────────────┐
│  ENTRY LEVEL (0-2 years)                                    │
│  Junior Designer / Programmer / Artist                      │
│  • Learning fundamentals                                    │
│  • Working on features                                      │
│  • Building portfolio                                       │
├─────────────────────────────────────────────────────────────┤
│  MID LEVEL (2-5 years)                                      │
│  Designer / Programmer / Artist                             │
│  • Owning systems                                           │
│  • Mentoring juniors                                        │
│  • Cross-team collaboration                                 │
├─────────────────────────────────────────────────────────────┤
│  SENIOR LEVEL (5-10 years)                                  │
│  Senior / Lead                                              │
│  • Technical leadership                                     │
│  • Architecture decisions                                   │
│  • Team guidance                                            │
├─────────────────────────────────────────────────────────────┤
│  PRINCIPAL/DIRECTOR (10+ years)                             │
│  Principal / Director / VP                                  │
│  • Studio-wide impact                                       │
│  • Strategy and vision                                      │
│  • Industry thought leadership                              │
└─────────────────────────────────────────────────────────────┘
```

## Industry Trends

- **Cloud Gaming**: Streaming, distributed computing
- **AI in Games**: Procedural content, NPCs
- **Cross-Platform**: Play anywhere
- **Live Services**: GaaS models
- **VR/AR**: Immersive experiences
- **Indie Growth**: Solo/small team success stories

## Output

When you run this command, you'll receive:
- Role descriptions with responsibilities
- Required skills and experience levels
- Salary ranges by region
- Job market demand analysis
- Learning resources for each path
- Related roles and progression options

---

**Use this command**: To explore game development careers and opportunities!
