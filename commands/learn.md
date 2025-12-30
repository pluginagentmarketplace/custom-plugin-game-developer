---
name: learn
version: "2.0.0"
description: Personalized Game Development Learning Paths
sasmp_version: "1.3.0"
allowed-tools: Read, WebSearch

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
  - name: milestone
    type: string
    required: false
---

# /learn-gamedev - Personalized Game Development Learning Paths

Begin your game development journey with expert-designed learning paths tailored to your specialization, engine choice, and experience level.

## Quick Start

```bash
# Start interactive learning path selection
/learn-gamedev

# Choose specific specialization
/learn-gamedev designer
/learn-gamedev programmer
/learn-gamedev graphics

# Choose specialization with engine
/learn-gamedev designer unity
/learn-gamedev programmer unreal
/learn-gamedev graphics godot

# View specific milestone in learning path
/learn-gamedev designer unity month-3
/learn-gamedev programmer month-6
```

## What This Command Does

### 1. Personalized Learning Paths
- Customized 8-18 month roadmap based on your specialization
- Beginner → Intermediate → Advanced progression
- Clear milestones and checkpoints
- Estimated time commitments
- Success metrics for each phase

### 2. Resource Recommendations
- Curated learning materials for each topic
- Book recommendations with summaries
- Online course suggestions
- YouTube channels and tutorials
- Community resources and forums
- Tools and software recommendations

### 3. Project-Based Learning
- Suggested projects for each skill level
- Step-by-step project walkthroughs
- Portfolio-building guidance
- Real-world project examples
- Project difficulty and time estimates

### 4. Progress Tracking
- Mark completed topics and projects
- Track learning milestones
- Monitor time spent
- Compare progress with peers
- Certificate of completion

## Specialization Paths

### 🎨 Game Designer Path

**Overview**: Create engaging gameplay experiences through mechanics design, level design, and player psychology.

**Prerequisites**:
- Comfortable with creative thinking
- Basic understanding of game principles
- No programming required initially

**Timeline**: 8-12 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Game design theory and MDA framework
- Core mechanics and feedback loops
- Balance and difficulty design
- Introduction to level design
- Game Design Document (GDD) creation
- Project: Simple game concept and GDD

**Phase 2: Intermediate (Months 4-9)**
- Advanced level design techniques
- Player psychology and engagement
- Economy and progression systems
- Narrative integration
- UI/UX design principles
- Playtesting and iteration
- Project: Design a complete game vertical slice with documentation

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Level Design, Systems Design, or Narrative
- Leadership and team dynamics
- Production pipeline understanding
- Publishing and player acquisition basics
- Portfolio development
- Project: Lead design on significant game project

**Related Agents**: 01-game-designer

---

### 💻 Game Programmer Path

**Overview**: Build the technical systems that power games through engine mastery, clean architecture, and performance optimization.

**Prerequisites**:
- Programming experience (any language)
- Math basics (vectors, physics concepts)
- Problem-solving mindset

**Timeline**: 10-18 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Choose engine (Unity with C#, Unreal with C++, or Godot with GDScript)
- Engine editor navigation and scene setup
- Basic scripting and components
- Input handling and player control
- Introduction to game loops
- Project: Build simple 2D platformer with basic mechanics

**Phase 2: Intermediate (Months 4-9)**
- Advanced OOP and design patterns
- State machines and gameplay systems
- Physics engine integration
- Debugging and profiling tools
- Performance optimization basics
- Multiplayer fundamentals
- Project: Implement complete gameplay system with multiple mechanics

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Gameplay, Engine, Tools, or Graphics programming
- Advanced architecture and large-scale systems
- Technical leadership and mentoring
- Performance optimization advanced techniques
- Build systems and CI/CD
- Project: Complex multiplayer system or engine feature

**Related Agents**: 02-game-programmer

---

### 🎨 Graphics Programmer Path

**Overview**: Create stunning visuals through shader programming, particle systems, and rendering optimization.

**Timeline**: 12-18 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Graphics fundamentals (vertices, textures, UV mapping)
- Introduction to shaders (HLSL, GLSL, ShaderLab)
- Basic material creation
- Lighting fundamentals
- Introduction to particle systems
- Project: Create custom materials and visual effects

**Phase 2: Intermediate (Months 4-9)**
- Advanced shader techniques (normal mapping, parallax)
- Particle system design and optimization
- Lighting systems (baked, real-time, global illumination)
- GPU profiling and optimization
- Post-processing effects
- Project: Build complex visual effects showcase

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Shaders, VFX, or Rendering optimization
- Custom rendering pipelines
- Advanced optimization techniques
- Technical art and material systems
- Performance budgeting
- Project: Implement graphics-intensive game feature

**Related Agents**: 03-graphics-rendering

---

### 🎵 Audio Specialist Path

**Overview**: Create immersive audio experiences through sound design, music composition, and audio programming.

**Timeline**: 12-18 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Audio fundamentals (frequency, amplitude, dynamics)
- DAW basics (choosing and learning tools)
- Sound design fundamentals
- Music composition basics
- Game audio systems (Wwise, FMOD basics)
- Project: Create SFX library and simple music track

**Phase 2: Intermediate (Months 4-9)**
- Advanced sound design techniques
- Music composition for games
- Interactive music systems
- Spatial audio and 3D sound
- Audio implementation in engines
- Optimization and compression
- Project: Design audio for game level or scene

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Sound Design, Composition, or Audio Engineering
- Professional recording techniques
- Advanced middleware systems
- Audio strategy and direction
- Leadership and team collaboration
- Project: Compose complete soundtrack or design audio vertical slice

**Related Agents**: 04-audio-sound-design

---

### 🌐 Network Programmer Path

**Overview**: Build multiplayer systems and scalable game servers for connected gaming.

**Timeline**: 14-18 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Network fundamentals (TCP, UDP, protocols)
- Client-server architecture basics
- Netcode fundamentals (client prediction, lag compensation)
- Introduction to game servers
- Synchronization basics
- Project: Simple networked game prototype

**Phase 2: Intermediate (Months 4-9)**
- Advanced netcode techniques
- Server architecture and scaling
- State replication and synchronization
- Anti-cheat system design
- Player authentication and security
- Load balancing concepts
- Project: Implement networked multiplayer game feature

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Netcode, Servers, or Anti-Cheat
- Cloud infrastructure and deployment
- Advanced optimization techniques
- Matchmaking and server selection
- Analytics and monitoring
- Project: Deploy scalable multiplayer system

**Related Agents**: 05-networking-multiplayer

---

### 🛠️ Tools Programmer Path

**Overview**: Streamline development through tools, pipelines, and automation.

**Timeline**: 10-15 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Build systems basics (CMake, Gradle, MSBuild)
- Version control (Git, branching strategies)
- Scripting fundamentals (Python, C#)
- Editor extension basics
- Introduction to CI/CD
- Project: Create simple editor tool or build script

**Phase 2: Intermediate (Months 4-9)**
- Advanced editor extensions
- Asset pipeline design and implementation
- Automation scripting
- Testing frameworks
- CI/CD pipeline setup
- Workflow optimization
- Project: Build custom tool or asset pipeline

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Build Systems, Pipelines, or DevOps
- Large-scale infrastructure
- Performance profiling and optimization
- Team tool ecosystems
- Documentation and training
- Project: Implement comprehensive dev infrastructure

**Related Agents**: 06-tools-pipeline

---

### 🚀 Game Publisher Path

**Overview**: Bring games to market and manage live operations and communities.

**Timeline**: 8-12 months to junior level

**Phase 1: Fundamentals (Months 1-3)**
- Game development process overview
- Platform knowledge (Steam, consoles, mobile)
- Publishing fundamentals
- Community basics
- Monetization overview
- Project: Analyze published game business model

**Phase 2: Intermediate (Months 4-9)**
- Platform-specific certification requirements
- Marketing and launch strategy
- Community management at scale
- Monetization system design
- Analytics and KPIs
- Live operations planning
- Project: Create publishing and marketing plan for game

**Phase 3: Advanced (Months 10-18)**
- Specialization: Choose Publishing, Live Ops, Marketing, or Community
- Regional and international considerations
- Advanced analytics
- Team leadership
- Risk management
- Project: Manage live game operations

**Related Agents**: 07-game-publishing

---

## Learning Methodologies

### Structured Learning
1. **Learn**: Study concept through resources
2. **Practice**: Apply knowledge in exercises
3. **Build**: Create project using skills
4. **Review**: Reflect on learning and gaps
5. **Iterate**: Refine understanding through repetition

### Project-Based Learning
- Select meaningful projects
- Break into milestones
- Share and get feedback
- Build portfolio pieces
- Learn through doing

## Tips for Success

- **Consistency**: Learn daily, even 30 minutes helps
- **Projects**: Build real projects, not just tutorials
- **Feedback**: Share work and seek feedback early
- **Community**: Find local game dev groups or online communities
- **Mentorship**: Find experienced developers to learn from
- **Specialization**: Pick a path and go deep vs. learning everything
- **Portfolio**: Document and showcase your best work
- **Networking**: Build relationships in game development community

---

**Start Your Learning Journey**: Choose your specialization and get a personalized roadmap to game development mastery!
