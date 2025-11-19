---
name: synchronization-algorithms
description: Network synchronization, lag compensation, client prediction, and state consistency for multiplayer games.
---

# Multiplayer Synchronization

## Techniques

- **Client Prediction**: Predict movement based on input
- **Lag Compensation**: Rollback and reconciliation
- **Interpolation**: Smooth movement between states
- **Extrapolation**: Predict future positions

## Authority Models

- **Server Authoritative**: Server validates all actions
- **Client Authoritative**: Lighter server load (risky)
- **Hybrid**: Best of both

## Network Optimization

- **Delta Compression**: Send only changes
- **Priority**: Important updates first
- **Bandwidth Management**: Reduce packet size
- **Frequency**: Balance latency vs bandwidth

---

**Use this skill**: When building multiplayer systems, optimizing netcode, or fixing desync issues.
