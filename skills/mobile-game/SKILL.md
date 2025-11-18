---
name: mobile-and-game-development
description: Master mobile development (iOS, Android, React Native, Flutter) and game development (client-side, server-side game architecture, game engines). Use when learning mobile or game development.
---

# Mobile & Game Development

## Quick Start Guide

This skill covers native and cross-platform mobile development, plus game development for various platforms.

### Mobile & Game Development Stack

```
Mobile & Game Development
├── iOS Development (1200+ hours)
│   ├── Fundamentals
│   │   ├── Swift language basics
│   │   ├── Xcode IDE
│   │   ├── iOS SDKs and frameworks
│   │   ├── App lifecycle
│   │   ├── Memory management (ARC)
│   │   └── Testing in iOS
│   │
│   ├── UIKit (Traditional)
│   │   ├── View controllers
│   │   ├── Views and layers
│   │   ├── Navigation and storyboards
│   │   ├── Gestures and touches
│   │   ├── Table and collection views
│   │   ├── Network requests
│   │   └── Data persistence
│   │
│   ├── SwiftUI (Modern)
│   │   ├── Declarative syntax
│   │   ├── Views and modifiers
│   │   ├── State management (@State, @StateObject)
│   │   ├── Data binding (@Binding)
│   │   ├── Navigation
│   │   ├── List and forms
│   │   ├── Animations
│   │   └── Combine framework
│   │
│   ├── Advanced Topics
│   │   ├── Networking (URLSession, Alamofire)
│   │   ├── JSON parsing (Codable)
│   │   ├── Core Data for persistence
│   │   ├── CloudKit for cloud sync
│   │   ├── Push notifications
│   │   ├── Background tasks
│   │   ├── Performance optimization
│   │   └── Security (Keychain, certificates)
│   │
│   ├── iOS Testing
│   │   ├── XCTest framework
│   │   ├── Unit testing
│   │   ├── UI testing
│   │   ├── Mocking and dependency injection
│   │   └── Test coverage
│   │
│   └── App Store
│       ├── App Store Connect
│       ├── App submission process
│       ├── Certificates and provisioning
│       ├── App Store Optimization (ASO)
│       ├── Analytics
│       └── User reviews and ratings
│
├── Android Development (1200+ hours)
│   ├── Fundamentals
│   │   ├── Kotlin language
│   │   ├── Android Studio
│   │   ├── Gradle build system
│   │   ├── Android SDK and APIs
│   │   ├── App lifecycle
│   │   ├── Activities, fragments
│   │   └── Services and background work
│   │
│   ├── Jetpack & Architecture
│   │   ├── ViewModel for state
│   │   ├── LiveData and StateFlow
│   │   ├── Navigation component
│   │   ├── Room database
│   │   ├── DataStore for preferences
│   │   ├── Work Scheduler
│   │   ├── MVVM architecture
│   │   └── Repository pattern
│   │
│   ├── UI Development
│   │   ├── Compose (Modern declarative)
│   │   ├── Traditional layouts (XML)
│   │   ├── Material Design 3
│   │   ├── RecyclerView lists
│   │   ├── Fragments
│   │   ├── Animations
│   │   └── Gestures
│   │
│   ├── Advanced Features
│   │   ├── Networking (Retrofit, OkHttp)
│   │   ├── JSON parsing (Gson, Moshi)
│   │   ├── Dependency injection (Hilt, Dagger)
│   │   ├── Push notifications (FCM)
│   │   ├── Media and camera
│   │   ├── Location services
│   │   ├── Sensors and hardware
│   │   └── Background processing
│   │
│   ├── Android Testing
│   │   ├── JUnit for unit tests
│   │   ├── Espresso for UI testing
│   │   ├── Robolectric for fast testing
│   │   ├── Mocking with Mockito
│   │   └── Test coverage
│   │
│   └── Google Play
│       ├── Play Developer Console
│       ├── APK and App Bundle
│       ├── Release management
│       ├── Beta testing
│       ├── Play Store Optimization (ASO)
│       ├── Analytics and crashes
│       └── User feedback
│
├── Cross-Platform: React Native (1000+ hours)
│   ├── Fundamentals
│   │   ├── JavaScript/TypeScript
│   │   ├── React concepts
│   │   ├── Native modules
│   │   ├── Bridge architecture
│   │   ├── Platform-specific code
│   │   └── Performance considerations
│   │
│   ├── Development
│   │   ├── Expo (easy) vs bare (full control)
│   │   ├── React Navigation
│   │   ├── State management (Redux, Context)
│   │   ├── Networking (Fetch API)
│   │   ├── Storage (AsyncStorage, Realm)
│   │   ├── UI libraries (React Native Paper, NativeBase)
│   │   └── Animations
│   │
│   ├── Platform Integration
│   │   ├── Native modules development
│   │   ├── Platform differences handling
│   │   ├── Camera, location, sensors
│   │   ├── Background tasks
│   │   ├── App signing and release
│   │   └── Performance optimization
│   │
│   └── Deployment
│       ├── iOS build and signing
│       ├── Android APK/AAB build
│       ├── Expo publishing
│       ├── Over-the-air updates
│       └── App store submission
│
├── Cross-Platform: Flutter (1000+ hours)
│   ├── Fundamentals
│   │   ├── Dart language
│   │   ├── Flutter SDK
│   │   ├── Widgets and composition
│   │   ├── Widget lifecycle
│   │   ├── Hot reload
│   │   └── Testing
│   │
│   ├── UI Development
│   │   ├── Material Design widgets
│   │   ├── Cupertino (iOS) widgets
│   │   ├── Layouts (Column, Row, Stack)
│   │   ├── Navigation and routing
│   │   ├── Themes and styling
│   │   ├── Animations
│   │   └── Custom widgets
│   │
│   ├── State Management
│   │   ├── setState
│   │   ├── Provider package
│   │   ├── GetX
│   │   ├── BLoC pattern
│   │   ├── Riverpod
│   │   └── State management comparison
│   │
│   ├── Advanced Features
│   │   ├── Networking (Dio, http)
│   │   ├── Local storage (Hive, SharedPreferences)
│   │   ├── JSON serialization
│   │   ├── Platform channels for native code
│   │   ├── Plugins ecosystem
│   │   ├── Camera and media
│   │   ├── Background work
│   │   └── Push notifications
│   │
│   ├── Flutter Testing
│   │   ├── Unit tests
│   │   ├── Widget tests
│   │   ├── Integration tests
│   │   ├── Test coverage
│   │   └── Performance profiling
│   │
│   └── Deployment
│       ├── iOS build and signing
│       ├── Android APK/AAB build
│       ├── Play Store and App Store
│       ├── Fastlane automation
│       └── CI/CD for Flutter
│
└── Game Development (1500+ hours)
    ├── Game Engines
    │   ├── Unity (Most Popular)
    │   │   ├── C# scripting
    │   │   ├── Scene and GameObject
    │   │   ├── Prefabs and components
    │   │   ├── Physics 2D and 3D
    │   │   ├── Animation system
    │   │   ├── Particle effects
    │   │   ├── Lighting and rendering
    │   │   ├── UI Canvas system
    │   │   ├── Asset Store
    │   │   └── Cross-platform build
    │   │
    │   ├── Unreal Engine
    │   │   ├── C++ programming
    │   │   ├── Blueprint visual scripting
    │   │   ├── Actor and component system
    │   │   ├── Physics engine (Havok)
    │   │   ├── Animation system (Sequencer)
    │   │   ├── Material system
    │   │   ├── Level design
    │   │   ├── Networking (replication)
    │   │   └── Plugin development
    │   │
    │   ├── Godot
    │   │   ├── GDScript language
    │   │   ├── Node-based system
    │   │   ├── Scene system
    │   │   ├── 2D and 3D physics
    │   │   ├── AnimationPlayer
    │   │   ├── Tile system
    │   │   ├── Shader language
    │   │   ├── Export and deployment
    │   │   └── Free and open source
    │   │
    │   └── Other Engines
    │       ├── Cocos2d
    │       ├── GameMaker
    │       ├── LibGDX
    │       └── Custom engines
    │
    ├── Game Design & Mechanics
    │   ├── Game design document
    │   ├── Game mechanics
    │   ├── Level design
    │   ├── Game balance
    │   ├── Player progression
    │   ├── Difficulty curves
    │   ├── Playtesting
    │   └── Feedback loops
    │
    ├── Graphics & Audio
    │   ├── 2D graphics
    │   ├── 3D modeling (Blender)
    │   ├── Texturing and materials
    │   ├── Lighting
    │   ├── Visual effects
    │   ├── Audio design
    │   ├── Music integration
    │   └── Sound effects
    │
    ├── Game Programming
    │   ├── Game loop architecture
    │   ├── Input handling
    │   ├── Collision detection
    │   ├── Physics simulation
    │   ├── AI and pathfinding
    │   ├── Animation systems
    │   ├── Particle systems
    │   └── Optimization
    │
    ├── Client-Side Game Dev
    │   ├── Single-player games
    │   ├── Local multiplayer
    │   ├── Performance optimization
    │   ├── Asset management
    │   ├── Save/load systems
    │   ├── UI implementation
    │   └── Deployment platforms
    │
    ├── Server-Side Game Dev
    │   ├── Game server architecture
    │   ├── Multiplayer synchronization
    │   ├── Player state management
    │   ├── Game logic server
    │   ├── Session management
    │   ├── Anti-cheat systems
    │   ├── Database design for games
    │   ├── Matchmaking systems
    │   ├── Scaling for many players
    │   └── Monitoring and analytics
    │
    ├── Game Publishing
    │   ├── Steam
    │   ├── Epic Games Store
    │   ├── Console platforms
    │   ├── Mobile platforms
    │   ├── Web platforms
    │   ├── Localization
    │   ├── Marketing
    │   └── Post-launch support
    │
    └── Tools & Ecosystem
        ├── Version control (Git)
        ├── 3D modeling (Blender, Maya)
        ├── Sprite editors (Aseprite)
        ├── Audio tools (Audacity, FL Studio)
        ├── Build automation
        ├── CI/CD for games
        └── Analytics and telemetry
```

## Deep Dive Topics

### iOS Development Excellence
- **SwiftUI Modern Approach**: Declarative UI, state management, combining with UIKit
- **Performance**: Memory profiling, battery optimization, smooth animations
- **Networking**: REST APIs, caching, offline support
- **Persistence**: Core Data, CloudKit, file system
- **App Store**: Submission process, marketing, analytics

### Android Development Excellence
- **Jetpack Architecture**: Modern best practices, MVVM, clean architecture
- **Compose**: Modern declarative UI approach
- **Performance**: ANR prevention, memory management, battery optimization
- **Networking**: Efficient data transfer, caching strategies
- **Play Store**: Distribution, versioning, analytics

### React Native Mastery
- **Cross-platform**: Sharing code between iOS and Android
- **Performance**: Native modules for demanding tasks
- **Navigation**: Complex navigation patterns
- **Native Integration**: Camera, location, sensors
- **Testing**: Debugging and performance profiling

### Flutter Mastery
- **Dart Language**: Understanding Dart's strengths
- **Widget System**: Building custom, performant widgets
- **State Management**: Choosing the right approach
- **Platform Channels**: Integrating with native code
- **Performance**: Building 60/120 FPS apps

### Game Development Expertise
- **Game Design**: Creating engaging, balanced games
- **Physics**: Realistic or arcade physics as needed
- **Networking**: Real-time multiplayer synchronization
- **Optimization**: Running smoothly on target hardware
- **Monetization**: In-app purchases, ads, premium pricing

## 66 Development Roles Using Mobile & Game Skills

**iOS Roles**:
- iOS Developer (Swift/SwiftUI)
- iOS Engineer
- Senior iOS Developer
- iOS Architect

**Android Roles**:
- Android Developer (Kotlin)
- Android Engineer
- Senior Android Developer
- Android Architect

**Cross-Platform Roles**:
- React Native Developer
- Flutter Developer
- Cross-platform Mobile Engineer
- Mobile Architect

**Game Development Roles**:
- Game Developer
- Game Programmer
- Game Engine Programmer
- Game Architect
- Graphics Programmer
- Gameplay Programmer
- AI Programmer
- Physics Programmer
- Tools Programmer
- Server-Side Game Developer
- Multiplayer Game Programmer

## Quick Learning Paths

### iOS Developer Path (9-12 months)
1. Swift fundamentals - 1 month
2. UIKit or SwiftUI basics - 1 month
3. Navigation and architecture - 1 month
4. Networking and data - 1 month
5. Advanced features (push, background) - 1 month
6. Publishing to App Store - 1 month
7. Real-world projects - ongoing

### Android Developer Path (9-12 months)
1. Kotlin fundamentals - 1 month
2. Activity/Fragment basics - 1 month
3. Modern Jetpack components - 1 month
4. Architecture patterns - 1 month
5. Networking and storage - 1 month
6. Publishing to Play Store - 1 month
7. Real-world projects - ongoing

### React Native Path (6-9 months)
1. React fundamentals - 1 month
2. React Native basics - 1 month
3. Navigation and state - 1 month
4. Networking and storage - 1 month
5. Native modules and platform-specific - 1 month
6. Deployment and publishing - 1 month
7. Real-world projects - ongoing

### Flutter Path (6-9 months)
1. Dart language - 1 month
2. Flutter widget system - 1 month
3. Navigation and routing - 1 month
4. State management - 1 month
5. Networking and storage - 1 month
6. Advanced features - 1 month
7. Real-world projects - ongoing

### Game Developer Path (12-18 months)
1. Game design fundamentals - 1 month
2. Choose engine (Unity/Unreal) - 1 month
3. Engine basics - 2 months
4. Game mechanics and programming - 2 months
5. Graphics and audio - 1 month
6. Multiplayer/networking (optional) - 2 months
7. Published game portfolio - ongoing

## Key Learning Resources

- [roadmap.sh iOS Roadmap](https://roadmap.sh/ios)
- [roadmap.sh Android Roadmap](https://roadmap.sh/android)
- [roadmap.sh React Native Roadmap](https://roadmap.sh/react-native)
- [roadmap.sh Flutter Roadmap](https://roadmap.sh/flutter)
- [roadmap.sh Game Developer Roadmap](https://roadmap.sh/game-developer)
- Official documentation (Apple, Google, React Native, Flutter, Unity, Unreal)
- YouTube tutorials and courses
- Hands-on projects and game jams
- Community forums and Discord servers

## Certifications & Recognition

- **Apple**: Developer Program
- **Google**: Google Developer Certification
- **Flutter**: Google Flutter certification
- **Game Development**: Published games, portfolio
- **Community**: Open source contributions, GitHub projects

---

**When to use this skill**: Learning iOS or Android development, building cross-platform apps, creating games, optimizing mobile performance, or designing game architectures.
