---
name: optimization-performance
description: Game optimization, performance profiling, multi-platform support, frame rate optimization.
sasmp_version: "1.3.0"
bonded_agent: 01-game-designer
bond_type: PRIMARY_BOND
---

# Optimization & Performance

## Performance Metrics

- **Frame Rate**: Targeting 60 FPS (or 30 FPS for consoles)
- **Memory**: RAM, VRAM limits per platform
- **CPU**: Processing time per frame (frame budget)
- **GPU**: Draw calls, fill rate, bandwidth
- **Storage**: Build size, loading times

## Profiling Tools

- **CPU Profiling**: Identify slow code sections
- **Memory Profiling**: Find memory leaks
- **GPU Profiling**: Shader bottlenecks
- **Frame Analysis**: Timeline profiling
- **Platform Tools**: Console-specific profilers

## Optimization Techniques

- **Code Optimization**: Algorithms, caching, pooling
- **Rendering**: Batching, LOD, culling
- **Physics**: Optimization levels, sleeping bodies
- **Audio**: Compression, streaming
- **Memory**: Streaming, unloading, pooling
- **Networking**: Bandwidth reduction, compression

## Multi-Platform Support

- **PC**: High-end specs, flexible scaling
- **Console**: Fixed hardware, optimization critical
- **Mobile**: Limited RAM/CPU/GPU, battery
- **Web**: Browser limitations, loading times
- **VR**: Consistent 90 FPS requirement

## Best Practices

- **Profile First**: Measure before optimizing
- **Target Bottleneck**: Find and fix slowest part
- **Platform Specific**: Different optimizations per platform
- **Iterate**: Measure, optimize, repeat
- **Quality vs Performance**: Balance visual quality with speed

---

**Use this skill**: When optimizing games, profiling performance, supporting multiple platforms.
