# RepSense
Your Reps, Sensibly Counted                               


## Overview

RepSense is an innovative fitness tool that leverages advanced pose estimation technology to make your workouts more effective and convenient. Say goodbye to manual rep counting and hello to automated, precise tracking. The project is a fully open-source tracker for fitness tests. ~~It is created because we can't pass our fitness tests~~ 


It is created **to democratize the motion senors used in national fitness tests and make objectively counting reps accessible to all**

With RepSense, you can check your pushups/situps form anywhere, anytime! 

## Features

- **Smart Rep Counting**: RepSense uses cutting-edge pose estimation to intelligently track your workout movements and count reps accurately.

- **Choose Your Workout**: Select from a variety of pre-defined workouts or create your custom routines.

- **Real-time Feedback**: Get instant feedback on your form and performance to improve your workouts.

- **Progress Tracking**: RepSense keeps a record of your workout history, helping you monitor your fitness progress over time.

- **Easy-to-Use GUI**: The intuitive graphical user interface makes it effortless to get started.

## The magic of ~meth~ math
We exploit trigonometry to find the magnitude of the angle between the forearm and bicep from the [normalized](https://en.wikipedia.org/wiki/Normalization_(statistics)) window coordinates of elbow, shoulder and hand. Following which, we render the real-time angle at the upscaled coordinates (directly proportional to the size of the video capture) of the elbow.

## How It Works

1. Launch the RepSense application.
2. Select your desired workout from the list.
3. Position your camera to capture your workout area.
4. Start your workout, and RepSense will automatically count your reps based on your movements.

## Installation

1. Clone this repository.
2. Install the required dependencies.
3. Run RepSense.py to launch the application.

## Requirements

- Python 3.7+
- OpenCV
- Pose Estimation Library (e.g., OpenPose)

## Usage

- Launch the RepSense application.
- Select a workout from the available options.
- Follow the on-screen instructions for camera setup.
- Begin your workout, and RepSense will track and count your reps.

## Contributing

We welcome contributions to enhance RepSense. Please review our [contribution guidelines](CONTRIBUTING.md) for more details.

## Feedback and Support

If you encounter any issues or have suggestions for improvement, please [submit an issue](https://github.com/takatoshilee/RepSense/issues) or [contact us](mailto:tka767@gmail.com).

## License

RepSense is released under the [MIT License](LICENSE).


![Real-Time Demostration](https://github.com/.gif)
