# githubTest

This repository demonstrates a simple collision avoidance routine for cranes.
The `crane_collision.py` file implements a Python function to detect when two
cranes are traveling toward one another along the same axis and adjusts the
preemption priority accordingly. Unit tests in `test_crane_collision.py` show how
the logic behaves when cranes move in opposite directions versus unrelated
movement.

The repository also contains `crane_collision.cpp`, a small C++ example that
illustrates the same heading-toward-each-other logic for environments where a
C++ implementation is preferred.
