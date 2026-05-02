# Asteroids Clone

## Project Overview
This project is a simplified clone of the classic arcade game Asteroids, developed in Python using the Pygame library. It features a real-time game loop where the player controls a 2D spaceship capable of movement, rotation, and firing projectiles to destroy incoming asteroids. 

This project was built primarily as a learning exercise focused on object-oriented programming (OOP), game loop architecture, collision detection, and vector mathematics.

## Core Gameplay Mechanics
The gameplay loop is built on real-time rendering and continuous user input handling.

*   **Player Control:** The player commands a ship that can rotate, move across the screen, and fire projectiles.
*   **Asteroid Dynamics:** Asteroids spawn dynamically and travel with independent velocities across the play area.
*   **Collision System:** The game constantly checks for overlaps between circular objects (e.g., shots colliding with asteroids, or the player colliding with asteroids).
*   **Asteroid Splitting:** A central mechanic where destroying an asteroid results in fragmentation rather than immediate removal:
    *   Large asteroids split into two medium asteroids.
    *   Medium asteroids split into two small asteroids.
    *   Small asteroids are removed entirely upon impact.
    *   *Fragmentation physics:* New asteroid fragments spawn at the point of destruction, move at higher velocities, and travel in randomized directions based on the original velocity vector.

## Technical Concepts & Skills Demonstrated
The codebase demonstrates several foundational software engineering and game development principles:

*   **Object-Oriented Programming (OOP):** Utilizing separate, modular classes for distinct game entities (player, asteroids, shots) and shared behaviors (circle-based collision).
*   **Game Loop Architecture:** Implementing a standard frame-by-frame loop that continuously updates entity states, processes user input, and renders graphics to the screen.
*   **Vector Mathematics:** Utilizing vectors to handle precise entity positioning, movement, velocity, and rotation mechanics.
*   **Modular Architecture:** Organizing logic across multiple specialized files rather than a single script.

## Project Structure
The repository is organized into distinct modules, separating concerns for better maintainability:

*   `main.py`: The entry point. Initializes Pygame, contains the core game loop, manages object collections, handles overarching collision logic (e.g., triggering the splitting mechanic), and renders updates.
*   `player.py`: Defines the player ship entity, encapsulating logic for keyboard input response, movement, rotation, shooting cooldowns, and position tracking.
*   `asteroid.py`: Defines asteroid behavior, including size states, velocity tracking, and the mathematical logic for randomized splitting trajectories.
*   `asteroidfield.py`: Manages the spawning logic, controlling frequency and positioning to populate the game with threats.
*   `shot.py`: Defines projectile behavior, tracking trajectory and handling off-screen removal or collision states.
*   `circleshape.py`: A base class providing shared logic for circular game entities, centralizing position tracking, radius data, and collision detection logic.
*   `constants.py`: Centralized configuration file storing reusable values (screen dimensions, entity speeds, spawn rates).
*   `logger.py`: Provides event logging support for gameplay actions (e.g., recording splits) to assist in debugging and execution tracing.

## Limitations & Scope
As an educational project focused on core architecture, the scope is intentionally constrained:
*   Visuals rely on simple geometric shapes rather than complex sprite artwork.
*   Does not include sound effects, persistent scoring, save systems, or advanced menu UI.
*   Lacks external polish systems like particle effects or advanced animations.