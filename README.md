# AWS DeepRacer Training Models

This repository contains multiple AWS DeepRacer reward function implementations and training data for autonomous racing experiments.

## Project Structure

```
├── default.py              # Basic center-line following reward function
├── final.py                # Final optimized reward function
├── parameters.png           # Parameter visualization
├── firstModel/             # First training attempt
├── secondModel/            # Second training iteration
├── thirdModel/             # Third training iteration
├── fourthModel/            # Fourth training iteration
├── fifthModel/             # Fifth training iteration
├── sixthModel/             # Sixth training iteration
└── README.md               # This file
```

## Model Directories

Each model directory contains:
- `main.py` - The reward function implementation
- `conf.png` - Configuration screenshot
- Training logs, metrics, and simulation traces (when available)

## Reward Functions

### Default Model
- Simple center-line following approach
- Uses distance markers at 10%, 25%, and 50% of track width
- Provides graduated rewards based on distance from center

### First Model
- Enhanced with speed rewards
- Includes steering angle penalties
- On-track validation
- Hyperparameter configuration included

## Training Data

The repository includes comprehensive training data:
- **Logs**: SageMaker and RoboMaker training logs
- **Metrics**: Training performance metrics in JSON format
- **Simulation Traces**: CSV files with iteration-by-iteration performance data

## Usage

1. Use the reward functions in AWS DeepRacer console
2. Adjust hyperparameters as needed
3. Monitor training through the provided logs and metrics
4. Analyze performance using simulation trace data

## Training Hyperparameters

Key hyperparameters used across models:
- Gradient Descent Batch Size: 64
- Entropy: 0.01
- Discount Factor: 0.99
- Loss Type: Huber
- Learning Rate: 0.0003
- Experience Episodes: 20
- Epochs: 10

## Getting Started

1. Clone this repository
2. Review the reward functions in each model directory
3. Copy the desired reward function to AWS DeepRacer console
4. Configure hyperparameters based on the provided examples
5. Start training and monitor progress

## AWS DeepRacer

AWS DeepRacer is a 1/18th scale race car that gives you an interesting and fun way to get started with reinforcement learning (RL). This repository documents the iterative process of developing and refining reward functions for optimal racing performance.
