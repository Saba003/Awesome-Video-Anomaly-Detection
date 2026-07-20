# Decision Tree

```text
Do you have anomaly labels?
├── Yes, frame/segment-level
│   └── Supervised temporal model or transformer
├── Yes, video-level only
│   └── Weakly supervised MIL or vision-language model
└── No
    ├── Only normal training video
    │   └── Semi-supervised reconstruction, prediction, memory, or teacher-student
    └── No task-specific training
        └── Training-free vision-language/LLM pipeline
```
