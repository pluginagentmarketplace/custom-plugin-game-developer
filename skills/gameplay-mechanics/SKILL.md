---
name: gameplay-mechanics
description: Master implementation of core gameplay mechanics, system interactions, feedback loops, and iterative balance refinement. Learn to build responsive, engaging systems that transform design concepts into playable experiences through clean architecture and rapid iteration.
sasmp_version: "1.3.0"
bonded_agent: 01-game-designer
bond_type: PRIMARY_BOND
---

# Gameplay Mechanics Implementation

Gameplay mechanics are the interactive systems that form the core of player experience. This skill focuses on implementing mechanics cleanly, making them balanceable, and iterating rapidly based on playtesting feedback.

## Core Principles

### 1. Action Systems: Input to Effect

The foundation of mechanics is the action system - converting player input into game world effects.

**Input Handling**:
- Capture player input (keyboard, gamepad, mouse, touch)
- Queue inputs during processing
- Handle simultaneous inputs appropriately
- Consume inputs at correct time

**Processing**:
- Validate inputs (can player perform this action now?)
- Calculate effects (what happens as result?)
- Update game state
- Generate feedback (what should player see/hear?)

**Feedback**:
- Immediate visual response (animation, particles)
- Audio response (sound effects, feedback)
- Screen shake or haptic feedback
- UI updates showing results

**Example: Attack Mechanic**
```
Input: Player presses attack button
→ Validation: Check if player not in recovery, has stamina
→ Processing: Check if enemy in range, calculate damage
→ Effect: Deal damage, start recovery timer, reduce stamina
→ Feedback: Attack animation, damage number, hit sound
→ State Change: Enemy HP reduced, visual health bar update
```

### 2. Feedback Loops: Making Actions Feel Good

Feedback loops connect player actions to observable game changes, making mechanics feel responsive.

**Immediate Feedback** (< 100ms):
- Essential for feeling responsive
- Audio/visual indication action was registered
- Must happen even if processing takes longer

**Short-term Feedback** (100ms - 1 second):
- Direct result of action (damage dealt, resource collected)
- Visible state changes (health bar changes)
- Score/progress updates

**Long-term Feedback** (seconds - minutes):
- Accumulated effects (leveling up, progression)
- New abilities unlocked
- Story progress
- Environmental changes

**Feedback Design Principles**:
- **Clarity**: Obvious what happened
- **Intensity**: Match importance (small action = small feedback)
- **Frequency**: Provide frequent feedback, not just final results
- **Variety**: Avoid feedback fatigue through variation
- **Consistency**: Similar actions produce consistent feedback
- **Layering**: Combine visual, audio, haptic feedback

### 3. Resource Economy Systems

Resource management creates interesting decisions and progression.

**Resource Types**:
- **Health**: Player durability and challenge
- **Currency**: Purchasing and economic decisions
- **Energy/Stamina**: Gating repeated actions
- **Cooldowns**: Preventing ability spam
- **Inventory Slots**: Forcing resource management
- **Crafting Materials**: Multi-step progression

**Economy Principles**:
- **Balance Scarcity**: Not too abundant, not too scarce
- **Multiple Uses**: Resources valuable for multiple purposes
- **Trade-offs**: Spending resource on one thing means not spending elsewhere
- **Regeneration**: How fast resources restore
- **Loss Consequences**: What happens when resource depleted?

**Example: Stamina Economy**
```
Max Stamina: 100
Actions consume:
  - Light attack: 10 stamina
  - Heavy attack: 25 stamina
  - Dodge: 15 stamina
  - Run: 5 stamina/second
Regeneration: 20 stamina/second when not acting

This creates interesting decisions:
- Use stamina for defense or offense?
- When to stop and recover?
- Balance of risk/reward
```

### 4. Progression Systems

Progression keeps players motivated by providing measurable growth.

**Progression Types**:

**Linear Progression**:
- Unlock features in predetermined order
- Good for learning curves
- Less player agency

**Branching Progression**:
- Multiple paths to advancement
- Player choice and specialization
- More complex to balance

**Skill Trees**:
- Visual representation of options
- Clear cost/benefit decisions
- Multiple viable build paths

**Seasonal/Episodic**:
- Content resets between seasons
- New challenges each cycle
- Sustained engagement

**Progression Mechanics**:
- **Experience Points**: Earn from activities, unlock on milestones
- **Levels**: Visible progression markers
- **Unlocks**: New abilities, areas, cosmetics
- **Skill Points**: Flexible progression choice
- **Equipment**: Gear progression and itemization

**Balancing Progression**:
- Early progression should be fast (engagement hook)
- Mid progression steady (maintaining interest)
- Late progression slower (giving aspirational goals)
- Avoid progression walls (sudden difficulty spikes)

## System Architecture

### Clean Separation of Concerns

Well-architected mechanics systems are easier to balance and iterate on.

**System Components**:

**Input System**:
```
Captures and queues player input
Converts to game-agnostic action commands
Handles input validation and conflicts
```

**Action Execution**:
```
Processes action commands
Checks preconditions (can action execute?)
Calculates effects
Updates game state
Generates feedback
```

**Feedback System**:
```
Audio effects playback
Visual effects (particles, animations)
UI updates
Camera/screen effects
```

**Separation Benefits**:
- Change feedback without changing mechanics
- Reuse mechanics with different feedback
- Easy to iterate on balance numbers
- Easy to implement new mechanics
- Easier testing and debugging

### Event-Driven Architecture

Events decouple systems, allowing clean communication.

**Event-Based Pattern**:
```
Player Action → Action Executed → Events Fired → Systems React

Example: Enemy Takes Damage
  Player attacks → Action executes →
    Events:
      - DamageDealt(amount, position)
      - HealthChanged(old, new)
      - EnemyStaggered()
    Systems respond:
      - VFX system: Show damage numbers
      - Audio system: Play hit sound
      - AI system: Interrupt attack
      - UI system: Update health bar
```

**Event-Driven Benefits**:
- Systems don't need direct references
- Easy to add observers (new effects)
- Same mechanic triggers multiple consequences
- Easy to disable/enable features
- Better for networking (easy to replicate events)

### Parameter Tuning for Balance

Mechanics need to be easily adjustable for balance iteration.

**Data-Driven Design**:
- Store mechanic numbers in configuration files
- Change values without code recompilation
- Quick balance iteration
- Designer-friendly balance changes

**Parameters to Expose**:
```
Combat System Parameters:
  - Attack damage
  - Attack speed
  - Range
  - Stamina cost
  - Knockback amount

Movement Parameters:
  - Walk speed
  - Run speed
  - Jump height
  - Air control

Enemy Parameters:
  - HP
  - Damage
  - Aggro range
  - Attack frequency
```

**Balance Feedback Loop**:
1. Observe playtesting data
2. Identify imbalance (too weak, too strong, frustrating)
3. Adjust parameters
4. Test quickly
5. Repeat

## Implementation Patterns

### State Machines for Action Flow

State machines cleanly handle transitions between actions.

```
States:
  Idle ↔ Running ↔ Falling
  Idle → Attacking → Recovery → Idle

Example: Attack State Machine
  Idle:
    Input.Attack → Attacking state
    Input.Move → Running state

  Attacking:
    Frame 5: Hit active (can damage enemies)
    Frame 15: Hit window closes
    Frame 25: Recovery ends → Idle state

  Recovery:
    Cannot act
    Cannot take new inputs
    Timer counts down
```

### Component-Based Systems

Components modularize mechanic behavior.

```
Weapon Component:
  - Damage value
  - Attack speed
  - Range
  - AttackSound
  - HitEffect

Player Component:
  - Has HealthComponent
  - Has WeaponComponent
  - Has MovementComponent
  - Has AnimationComponent
```

## Playtesting for Mechanics

Playtesting reveals how mechanics actually play vs. how they were designed.

### Identifying Friction Points

**Friction**: Anything preventing smooth, fun gameplay

**Common Friction Sources**:
- **Unresponsive Controls**: Input doesn't immediately feel good
- **Unclear Feedback**: Player doesn't understand what happened
- **Tedium**: Repetitive actions without reward
- **Unbalanced Difficulty**: Too easy or too hard for player skill
- **Unfair Mechanics**: Consequences seem random or unfair
- **Poor Pacing**: Actions feel too slow or clunky

**Identifying Friction**:
- Watch player faces and body language
- Listen to player complaints
- Note where players hesitate or repeat actions
- Track time spent on tasks
- Record what players do without instruction

### Measuring Engagement

**Quantitative Metrics**:
- **Session Length**: How long do players stay?
- **Retention**: Do players come back?
- **Progression Speed**: How quickly do players progress?
- **Action Frequency**: How often do players repeat actions?
- **Failure Rate**: What percentage fail at challenges?

**Qualitative Feedback**:
- What felt good?
- What was frustrating?
- Was challenge appropriate?
- What would improve it?
- Would you play again?

### Rapid Iteration Cycles

Quick iteration on mechanics is essential.

**Iteration Process**:
1. **Playtest** (15-30 minutes)
2. **Gather Feedback** (qualitative + quantitative)
3. **Analyze** (5-15 minutes, identify patterns)
4. **Adjust** (change parameters or design)
5. **Repeat** (test change immediately)

**Time Target**: Full cycle in 1-2 hours

**Benefits of Speed**:
- Fresh perspective each iteration
- Multiple design approaches tested quickly
- Find dead ends fast (early pivot)
- Avoid over-polishing broken mechanics
- Team stays excited with visible progress

## Common Pitfalls

- **Unresponsive Feel**: Delays between input and feedback
- **Unbalanced**: Some options trivially better/worse
- **Unclear Mechanics**: Players don't understand how things work
- **Tedious Execution**: Mechanics require tedious repeated actions
- **No Clear Progression**: Players don't see advancement
- **Feedback Overload**: Too much visual/audio feedback
- **Unfair Difficulty**: Challenge feels random or impossible
- **No Decision Making**: Only one viable approach

## Related Resources

**Game Feel**: Action games focus on responsive, satisfying mechanics
**Balancing**: Spreadsheet systems for tracking mechanic numbers
**Playtesting**: Methodology for gathering feedback
**Architecture**: Code patterns for clean systems

## Related Agents & Skills

**Consult the Game Programmer Agent** when:
- Implementing mechanics architecturally
- Performance optimization
- Debugging complex systems
- Engine-specific implementation

**Related Skills**:
- **game-design-theory**: Theoretical foundations
- **level-design**: Applying mechanics in level context
- **game-engines**: Implementation on specific engines

---

**Master gameplay mechanics to transform design concepts into responsive, engaging, balanceable systems that players love.**
