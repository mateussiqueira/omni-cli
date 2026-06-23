# Omni Memory Deep Dive

Complete guide to understanding and optimizing macOS memory with Omni CLI and Thunderbolt 4 SSD.

## Table of Contents

- [How macOS Manages Memory](#how-macos-manages-memory)
- [Why Use an External SSD](#why-use-an-external-ssd)
- [Thunderbolt 4 vs Other Interfaces](#thunderbolt-4-vs-other-interfaces)
- [Setup Strategies](#setup-strategies)
- [Recommended SSD Specifications](#recommended-ssd-specifications)
- [Monitoring Memory Pressure](#monitoring-memory-pressure)
- [Moving App Caches](#moving-app-caches)
- [macOS Settings for Best Performance](#macos-settings-for-best-performance)
- [When Not to Use External Swap](#when-not-to-use-external-swap)

## How macOS Manages Memory

macOS uses several memory management techniques:

- **Compressed Memory**: Compresses inactive RAM to free space
- **Swap**: Moves inactive data to disk when RAM is full
- **Memory Pressure**: Indicator of how hard the system is working to free RAM

You can check current status with:

```bash
omni memory status
memory_pressure
vm_stat
```

## Why Use an External SSD

When memory pressure is high, macOS writes swap to the internal SSD. This can:

- Slow down the system
- Wear out the internal SSD faster
- Reduce available internal storage

A fast external Thunderbolt 4 SSD can:

- Offload swap and cache from internal storage
- Provide nearly internal-SSD speeds
- Extend internal SSD lifespan
- Keep more free space on the main drive

## Thunderbolt 4 vs Other Interfaces

| Interface | Theoretical Speed | Real-world Speed | Good for Swap? |
|-----------|------------------|------------------|----------------|
| Thunderbolt 4 | 40 Gbps | ~2,800 MB/s | ✅ Excellent |
| Thunderbolt 3 | 40 Gbps | ~2,500 MB/s | ✅ Excellent |
| USB4 | 40 Gbps | ~2,000 MB/s | ✅ Very Good |
| USB 3.2 Gen 2 | 10 Gbps | ~900 MB/s | ⚠️ Acceptable |
| USB 3.0 | 5 Gbps | ~400 MB/s | ❌ Too slow |

## Setup Strategies

### Strategy 1: App Caches on External SSD

Best for most users. Move heavy app caches without modifying system swap:

```bash
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm
omni memory cache-move xcode
```

### Strategy 2: Full Memory Extension

For advanced users with sustained memory pressure:

```bash
omni memory setup --disk /Volumes/ThunderboltSSD
```

This configures monitoring, logging, and prepares the SSD for swap/cache use.

### Strategy 3: Developer Workstation

Combine both strategies for maximum benefit:

```bash
# Move all dev caches
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm
omni memory cache-move xcode

# Setup monitoring
omni memory setup --disk /Volumes/ThunderboltSSD
omni memory monitor
```

## Recommended SSD Specifications

For optimal results, use an SSD with:

- **Interface**: Thunderbolt 4 or Thunderbolt 3
- **Capacity**: At least 1 TB (2 TB recommended for dev workloads)
- **Read/Write Speed**: 2,000 MB/s+ sustained
- **DRAM Cache**: Yes, for better sustained performance
- **Endurance**: 600 TBW or higher for 1 TB models
- **Cooling**: Passive or active heatsink for sustained loads

## Monitoring Memory Pressure

Use Omni CLI to monitor memory continuously:

```bash
omni memory monitor
```

The log file shows:

```text
[2026-06-22 10:00:00] MEM: ... | SWAP: ... | PRESSURE: ... | DISK: ...
```

Interpret pressure levels:

| Free RAM | Status | Action |
|----------|--------|--------|
| > 50% | 🟢 Low | None needed |
| 20-50% | 🟡 Medium | Consider closing apps |
| 10-20% | 🟠 High | Move caches, reduce workload |
| < 10% | 🔴 Critical | Immediate action needed |

## Moving App Caches

### Docker Desktop

```bash
# In Docker Desktop settings:
# Resources > Advanced > Disk image location
# Set to: /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/docker
```

### Xcode DerivedData

```bash
# In Xcode: Preferences > Locations > DerivedData
# Set to: /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/Xcode/DerivedData
```

### Gradle

```bash
export GRADLE_USER_HOME=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/gradle
```

### npm

```bash
npm config set cache /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/npm-cache
```

## macOS Settings for Best Performance

1. **Disable "Put hard disks to sleep when possible"**
   - System Settings > Energy Saver
   - This keeps the external SSD responsive

2. **Enable Trim if supported**
   - Modern APFS handles this automatically on Apple Silicon

3. **Keep 20% internal SSD free**
   - macOS needs free space for temporary files and native swap

4. **Eject properly**
   - Always eject the Thunderbolt SSD before disconnecting to avoid data loss

## When Not to Use External Swap

Avoid relying entirely on external SSD if:

- Your SSD is USB 3.0 or slower
- You frequently disconnect the SSD
- Your SSD has low endurance (TBW)
- You work with highly sensitive data on portable drives

In these cases, focus on app cache relocation and RAM upgrade instead.
