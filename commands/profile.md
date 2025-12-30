---
name: profile
version: "2.0.0"
description: Assess Game Development Skills and Get Recommendations
sasmp_version: "1.3.0"
allowed-tools: Read

parameters:
  - name: specialization
    type: string
    required: false
    validation:
      enum: [designer, programmer, graphics, audio, networking, tools, publisher]
  - name: engine
    type: string
    required: false
    validation:
      enum: [unity, unreal, godot]
---

# /game-profile - Assess Game Development Skills

Evaluate your game development expertise and get personalized recommendations.

## Usage

```bash
/game-profile
/game-profile programmer
/game-profile designer unity
/game-profile graphics unreal
```

## What It Does

- Assess your game development knowledge
- Calculate proficiency scores (0-100%)
- Identify skill gaps
- Generate personalized learning recommendations
- Compare your skills to role requirements

## Assessment Areas

### 🎨 Game Design
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Mechanics Design | Core loops | System design | Meta progression |
| Level Design | Layout basics | Pacing | Environmental narrative |
| Balance | Number tuning | Economy design | Live balance |
| UX/UI | Basic layouts | User flows | Accessibility |

### 💻 Game Programming
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Engine Proficiency | Basics | Systems | Engine extension |
| Architecture | Scripts | Patterns | Large-scale |
| Optimization | Basics | Profiling | Platform-specific |
| Debugging | Console | Profilers | Low-level |

### 🎨 Graphics & Rendering
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Shaders | Surface | Custom | Pipeline |
| VFX | Particles | Complex | GPU-driven |
| Lighting | Baked | Real-time | GI systems |
| Optimization | LOD | Culling | GPU profiling |

### 🎵 Audio & Sound
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Sound Design | SFX basics | Layering | Procedural |
| Music | Loops | Adaptive | Full scores |
| Implementation | Engine audio | Middleware | Custom systems |
| Mixing | Basics | Spatial | Mastering |

### 🌐 Networking & Multiplayer
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Netcode | Basics | Prediction | Rollback |
| Servers | Local | Cloud | Distributed |
| Security | Validation | Anti-cheat | Encryption |
| Scaling | Single server | Auto-scale | Global |

### 🛠️ Tools & Pipeline
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Version Control | Git basics | Branching | LFS/Perforce |
| CI/CD | Manual | Automated | Full pipeline |
| Editor Tools | Built-in | Extensions | Custom |
| Asset Pipeline | Import | Processing | Streaming |

### 🚀 Publishing & Business
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| Platforms | One platform | Multi-platform | Console cert |
| Marketing | Social media | Campaigns | UA strategy |
| Monetization | Premium | F2P basics | Live ops |
| Analytics | Basic KPIs | Funnels | Predictive |

---

## Proficiency Levels

```
SKILL LEVEL DEFINITIONS:
┌─────────────────────────────────────────────────────────────┐
│  0-20%   │ NOVICE       │ Just starting, learning basics   │
├──────────┼──────────────┼──────────────────────────────────┤
│  21-40%  │ BEGINNER     │ Can follow tutorials, basic work │
├──────────┼──────────────┼──────────────────────────────────┤
│  41-60%  │ INTERMEDIATE │ Independent work, some expertise │
├──────────┼──────────────┼──────────────────────────────────┤
│  61-80%  │ ADVANCED     │ Mentor others, complex systems   │
├──────────┼──────────────┼──────────────────────────────────┤
│  81-100% │ EXPERT       │ Industry leader, push boundaries │
└──────────┴──────────────┴──────────────────────────────────┘
```

---

## Role Requirements

### Junior Game Designer
```
Required Skills:
├─ Game Design Theory: 40%+
├─ Level Design: 30%+
├─ Documentation: 50%+
└─ Communication: 50%+

Nice to Have:
├─ Engine Basics: 20%+
├─ UI/UX: 30%+
└─ Playtesting: 40%+
```

### Junior Gameplay Programmer
```
Required Skills:
├─ Engine Proficiency: 50%+
├─ Programming (C#/C++): 50%+
├─ Debugging: 40%+
└─ Version Control: 40%+

Nice to Have:
├─ Optimization: 30%+
├─ Patterns: 30%+
└─ Networking: 20%+
```

### Junior Graphics Programmer
```
Required Skills:
├─ Shader Programming: 40%+
├─ Linear Algebra: 50%+
├─ Rendering Concepts: 50%+
└─ GPU Profiling: 30%+

Nice to Have:
├─ VFX: 30%+
├─ Post-Processing: 30%+
└─ Engine Internals: 20%+
```

---

## Output

When you run this command, you'll receive:

1. **Overall Proficiency Score**
   - Aggregate score across all areas
   - Breakdown by specialization

2. **Skill Radar Chart**
   - Visual representation of strengths/weaknesses
   - Comparison to role requirements

3. **Gap Analysis**
   - Skills needing improvement
   - Priority recommendations
   - Estimated time to close gaps

4. **Learning Recommendations**
   - Personalized resource list
   - Project suggestions
   - Agent recommendations

5. **Career Readiness**
   - Roles you're ready for
   - Roles within reach
   - Long-term goals

---

**Use this command**: To assess your skills and plan your learning journey!
