# Performance and Benchmarks

Performance expectations and benchmarking for Omni CLI features.

## Table of Contents

- [Thunderbolt 4 SSD Performance](#thunderbolt-4-ssd-performance)
- [Internal vs External SSD](#internal-vs-external-ssd)
- [Benchmarking Your Setup](#benchmarking-your-setup)
- [Memory Optimization Impact](#memory-optimization-impact)
- [Expected Improvements](#expected-improvements)

## Thunderbolt 4 SSD Performance

Thunderbolt 4 provides up to 40 Gbps bandwidth. Real-world SSD performance depends on the drive quality.

### Typical speeds

| SSD Type | Read Speed | Write Speed | Notes |
|----------|-----------|-------------|-------|
| High-end Thunderbolt 4 NVMe | 2,800 MB/s | 2,300 MB/s | Best for swap/cache |
| Mid-range Thunderbolt 3 NVMe | 2,000 MB/s | 1,800 MB/s | Very good |
| USB4 NVMe | 1,800 MB/s | 1,500 MB/s | Good |
| USB 3.2 Gen 2 NVMe | 900 MB/s | 800 MB/s | Acceptable for light use |
| SATA SSD (USB) | 500 MB/s | 400 MB/s | Not recommended for swap |

## Internal vs External SSD

Modern Macs use very fast internal SSDs. A good Thunderbolt 4 external SSD can come close.

| Metric | Internal Mac SSD | Thunderbolt 4 SSD | Difference |
|--------|------------------|-------------------|------------|
| Read | ~5,000 MB/s | ~2,800 MB/s | ~44% slower |
| Write | ~4,000 MB/s | ~2,300 MB/s | ~43% slower |
| Latency | Very low | Low | Slightly higher |
| Endurance impact on internal SSD | High | Reduced | Significant benefit |

## Benchmarking Your Setup

### Test disk speed

On macOS:

```bash
diskutil info /Volumes/ThunderboltSSD | grep "Protocol"

# Simple write test
time dd if=/dev/zero of=/Volumes/ThunderboltSSD/test-file bs=1m count=1024
rm /Volumes/ThunderboltSSD/test-file
```

### Test memory pressure impact

1. Run a memory-heavy workload
2. Monitor with Omni CLI:

```bash
omni memory monitor
```

3. Compare performance with and without external cache

### Test swap speed

```bash
# Create memory pressure and measure swap usage
stress-ng --vm 4 --vm-bytes 2G --timeout 60s
```

Monitor swap usage during the test.

## Memory Optimization Impact

Moving app caches to Thunderbolt SSD can free significant internal storage:

| Cache Type | Typical Size | Internal SSD Saved |
|------------|-------------|-------------------|
| Docker Desktop | 10-100 GB | High |
| Xcode DerivedData | 5-50 GB | High |
| Gradle | 1-10 GB | Medium |
| npm | 1-5 GB | Medium |
| Python pip | 0.5-2 GB | Low-Medium |

## Expected Improvements

### For developers

- More free space on internal SSD
- Reduced wear on internal SSD
- Better sustained performance under memory pressure
- Faster Docker builds when cache is on fast external SSD

### For content creators

- More room for project files on internal SSD
- Reduced risk of running out of disk space

### Caveats

- Initial cache migration takes time
- External SSD must remain connected during use
- First access to moved caches may be slightly slower than internal SSD
- Not a replacement for insufficient RAM in all cases
