---
name: memory-management
description: Game memory optimization, pooling, garbage collection tuning, and efficient resource management for target platforms.
sasmp_version: "1.3.0"
bonded_agent: 01-game-designer
bond_type: PRIMARY_BOND
---

# Memory Management

## Techniques

- **Object Pooling**: Reuse objects instead of allocating
- **Garbage Collection**: Understanding and tuning GC
- **Memory Profiling**: Identifying leaks and inefficiency
- **Resource Streaming**: Loading/unloading assets dynamically

## Per-Platform

- **PC**: Generous memory, watch for fragmentation
- **Console**: Fixed memory budgets, optimization critical
- **Mobile**: Severe constraints, careful management
- **VR**: Tight timing requirements

## Tools

- Memory profilers (Unity, Unreal)
- Heap analysis
- Performance monitoring

---

**Use this skill**: When optimizing memory usage, reducing frame stutters, or supporting mobile platforms.
