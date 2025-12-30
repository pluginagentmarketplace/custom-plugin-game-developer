---
name: projects
version: "2.0.0"
description: Game Development Project Ideas and Tutorials
sasmp_version: "1.3.0"
allowed-tools: Read

parameters:
  - name: difficulty
    type: string
    required: false
    validation:
      enum: [beginner, intermediate, advanced, professional]
  - name: engine
    type: string
    required: false
    validation:
      enum: [unity, unreal, godot]
  - name: genre
    type: string
    required: false
    validation:
      enum: [platformer, rpg, fps, puzzle, multiplayer, mobile]
---

# /gamedev-projects - Game Development Projects

Discover hands-on game development projects from beginner to professional level.

## Usage

```bash
/gamedev-projects
/gamedev-projects beginner
/gamedev-projects unity intermediate
/gamedev-projects multiplayer advanced
/gamedev-projects graphics
```

## Project Categories

### Beginner Projects (1-2 weeks)

| Project | Skills Learned | Engine |
|---------|----------------|--------|
| Pong Clone | Input, physics, UI | Any |
| Breakout | Collision, spawning | Any |
| Endless Runner | Procedural generation | Any |
| Memory Card Game | UI, state management | Any |
| Simple Platformer | Physics, animation | Any |

**Example: Simple Platformer**
```
SCOPE:
├─ Player movement (walk, jump)
├─ Simple physics
├─ 3-5 levels
├─ Collectibles
├─ Win/lose conditions
└─ Basic UI (score, lives)

TIME: 1-2 weeks
SKILLS: Physics, input, scenes, UI
AGENTS: 02-game-programmer, 01-game-designer
```

---

### Intermediate Projects (2-4 weeks)

| Project | Skills Learned | Engine |
|---------|----------------|--------|
| Top-Down Shooter | Combat, AI, spawning | Any |
| Puzzle Game | Logic, level design | Any |
| RPG Prototype | Inventory, dialogue | Any |
| Tower Defense | Pathfinding, waves | Any |
| Racing Game | Vehicle physics, tracks | Any |

**Example: Top-Down Shooter**
```
SCOPE:
├─ Player movement (8-directional)
├─ Shooting mechanics
├─ Enemy AI (chase, attack)
├─ Wave-based spawning
├─ Health/damage systems
├─ Power-ups
├─ Audio (SFX, music)
└─ Polish (particles, juice)

TIME: 2-4 weeks
SKILLS: AI, combat, audio, VFX
AGENTS: 02-game-programmer, 04-audio-sound-design
```

---

### Advanced Projects (4-8 weeks)

| Project | Skills Learned | Engine |
|---------|----------------|--------|
| Multiplayer Game | Networking, sync | Any |
| 3D Platformer | 3D physics, camera | Unity/Unreal |
| Roguelike | Procedural, save/load | Any |
| Strategy Game | RTS mechanics, AI | Any |
| VR Experience | VR interaction | Unity/Unreal |

**Example: Multiplayer Game**
```
SCOPE:
├─ Client-server architecture
├─ Player synchronization
├─ Lag compensation
├─ Lobby/matchmaking
├─ Chat system
├─ Leaderboards
├─ Anti-cheat basics
└─ Deployment

TIME: 4-8 weeks
SKILLS: Networking, security, cloud
AGENTS: 05-networking-multiplayer, 02-game-programmer
```

---

### Professional Projects (8+ weeks)

| Project | Skills Learned | Engine |
|---------|----------------|--------|
| Commercial Indie Game | Full production | Any |
| Mobile F2P Game | Monetization, UA | Unity |
| Cross-Platform Game | Build systems | Any |
| Game Engine Feature | Low-level systems | Custom |
| AAA-Style Demo | Polish, optimization | Unreal |

**Example: Commercial Indie Game**
```
SCOPE:
├─ Complete gameplay loop
├─ 10+ hours content
├─ Full audio/music
├─ Localization
├─ Accessibility options
├─ Platform certification
├─ Marketing materials
├─ Launch strategy
└─ Post-launch support

TIME: 8-24 weeks
SKILLS: Full stack, publishing
AGENTS: All agents
```

---

## Project Templates

### Game Jam Project (48-72 hours)
```
CONSTRAINTS:
├─ Theme-based design
├─ Minimal scope
├─ Complete experience
└─ Polished feel

CHECKLIST:
□ Core mechanic (hour 1-4)
□ Playable prototype (hour 4-12)
□ Content creation (hour 12-36)
□ Polish pass (hour 36-48)
□ Final testing (hour 48-72)
```

### Portfolio Project
```
REQUIREMENTS:
├─ Demonstrates specific skills
├─ Polished presentation
├─ Playable build
├─ Source code available
├─ Documentation
└─ Development breakdown

STRUCTURE:
├─ README with overview
├─ Screenshots/GIFs
├─ Playable link
├─ Technical breakdown
└─ Lessons learned
```

---

## Features Per Project

### What Every Project Should Have
- Clear win/lose conditions
- Audio feedback
- Visual polish (particles, animations)
- Responsive controls
- Performance optimization
- Build for target platform

### Optional Enhancements
- Save/load system
- Settings menu
- Achievements
- Analytics integration
- Accessibility options

---

## Output

When you run this command, you'll receive:
- Project list filtered by your criteria
- Detailed scope and requirements
- Step-by-step implementation guide
- Resource links and assets
- Learning outcomes
- Time estimates

---

**Use this command**: To find projects that match your skill level and interests!
