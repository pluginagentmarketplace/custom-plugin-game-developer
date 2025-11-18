---
name: security-and-quality-practices
description: Master cybersecurity, QA/testing, code review, security best practices, vulnerability assessment, and compliance. Use when learning security practices, testing strategies, or securing applications.
---

# Security & Quality Practices

## Quick Start Guide

This skill covers security, quality assurance, testing, code review, and compliance frameworks.

### Security & Quality Technology Stack

```
Security & Quality
├── Cybersecurity (1200+ hours)
│   ├── Security Fundamentals
│   │   ├── CIA triad (Confidentiality, Integrity, Availability)
│   │   ├── Threat modeling
│   │   ├── Risk assessment
│   │   ├── Vulnerability assessment
│   │   └── Attack vectors and exploitation
│   │
│   ├── OWASP Top 10
│   │   ├── SQL Injection prevention
│   │   ├── Cross-Site Scripting (XSS) prevention
│   │   ├── Cross-Site Request Forgery (CSRF) prevention
│   │   ├── Insecure Deserialization handling
│   │   ├── Broken Authentication fixes
│   │   ├── Sensitive Data Exposure prevention
│   │   ├── XML External Entities (XXE) prevention
│   │   ├── Broken Access Control
│   │   ├── Using Components with Known Vulnerabilities
│   │   └── Insufficient Logging & Monitoring
│   │
│   ├── Authentication & Authorization
│   │   ├── JWT (JSON Web Tokens)
│   │   ├── OAuth 2.0
│   │   ├── OpenID Connect
│   │   ├── SAML
│   │   ├── Multi-factor authentication
│   │   ├── Password hashing (bcrypt, Argon2)
│   │   ├── Session management
│   │   └── Role-based access control (RBAC)
│   │
│   ├── Cryptography
│   │   ├── Symmetric encryption (AES)
│   │   ├── Asymmetric encryption (RSA)
│   │   ├── Hashing algorithms (SHA-256)
│   │   ├── Digital signatures
│   │   ├── SSL/TLS
│   │   ├── Certificate management
│   │   └── Key management
│   │
│   ├── Secure Development
│   │   ├── Secure coding practices
│   │   ├── Input validation
│   │   ├── Output encoding
│   │   ├── Command injection prevention
│   │   ├── Path traversal prevention
│   │   ├── Race conditions
│   │   └── Security testing in SDLC
│   │
│   ├── Penetration Testing
│   │   ├── Reconnaissance
│   │   ├── Scanning and enumeration
│   │   ├── Vulnerability identification
│   │   ├── Exploitation techniques
│   │   ├── Post-exploitation
│   │   ├── Report writing
│   │   └── Remediation guidance
│   │
│   └── Tools & Platforms
│       ├── Burp Suite
│       ├── OWASP ZAP
│       ├── Metasploit
│       ├── Nmap
│       ├── Wireshark
│       ├── SQLmap
│       └── Static analysis tools
│
├── QA & Testing (1200+ hours)
│   ├── Testing Fundamentals
│   │   ├── Test planning
│   │   ├── Test design
│   │   ├── Test execution
│   │   ├── Test reporting
│   │   ├── Defect tracking
│   │   └── Test metrics
│   │
│   ├── Testing Types
│   │   ├── Unit testing
│   │   ├── Integration testing
│   │   ├── System testing
│   │   ├── Acceptance testing
│   │   ├── End-to-end (E2E) testing
│   │   ├── Performance testing
│   │   ├── Load testing
│   │   ├── Stress testing
│   │   ├── Penetration testing
│   │   ├── Security testing
│   │   ├── Usability testing
│   │   └── Regression testing
│   │
│   ├── Test Automation
│   │   ├── Framework selection
│   │   ├── Test automation pyramid
│   │   ├── Data-driven testing
│   │   ├── Page object model
│   │   ├── CI/CD integration
│   │   ├── Test parallelization
│   │   └── Flakiness handling
│   │
│   ├── Testing Frameworks
│   │   ├── JavaScript: Jest, Mocha, Jasmine, Cypress
│   │   ├── Python: Pytest, unittest, nose2
│   │   ├── Java: JUnit, TestNG, Mockito
│   │   ├── .NET: NUnit, xUnit, Moq
│   │   ├── Go: testing package, testify
│   │   ├── Selenium for browser automation
│   │   ├── Playwright for cross-browser testing
│   │   └── Appium for mobile testing
│   │
│   ├── Test Data Management
│   │   ├── Test data creation
│   │   ├── Test data maintenance
│   │   ├── Data masking for privacy
│   │   ├── Data generation tools
│   │   └── Test environment management
│   │
│   └── Performance Testing
│       ├── Load testing
│       ├── Stress testing
│       ├── Spike testing
│       ├── Soak testing
│       ├── Tools (JMeter, LoadRunner, Gatling)
│       └── Analysis and optimization
│
├── Code Review (800+ hours)
│   ├── Code Review Fundamentals
│   │   ├── Purpose and benefits
│   │   ├── Types of reviews
│   │   ├── Review processes
│   │   ├── Tools and platforms
│   │   └── Best practices
│   │
│   ├── What to Review
│   │   ├── Code quality
│   │   ├── Design patterns
│   │   ├── Performance implications
│   │   ├── Security vulnerabilities
│   │   ├── Test coverage
│   │   ├── Documentation
│   │   └── Maintainability
│   │
│   ├── Code Review Tools
│   │   ├── GitHub pull requests
│   │   ├── GitLab merge requests
│   │   ├── Gerrit
│   │   ├── Phabricator
│   │   ├── Code review bots
│   │   └── Automated analysis
│   │
│   └── Effective Feedback
│       ├── Constructive comments
│       ├── Approving code
│       ├── Requesting changes
│       ├── Communication skills
│       └── Building trust
│
├── Compliance & Governance (1000+ hours)
│   ├── Regulatory Frameworks
│   │   ├── GDPR (General Data Protection Regulation)
│   │   ├── HIPAA (Healthcare)
│   │   ├── PCI DSS (Payment Card Industry)
│   │   ├── SOC 2 (Service Organization Control)
│   │   ├── ISO 27001 (Information Security)
│   │   ├── CCPA (California Privacy)
│   │   └── Other regional regulations
│   │
│   ├── GDPR Compliance
│   │   ├── Data protection principles
│   │   ├── Lawful basis for processing
│   │   ├── Data subject rights
│   │   ├── DPIA (Data Protection Impact Assessment)
│   │   ├── DPA (Data Processing Agreement)
│   │   ├── Breach notification
│   │   └── Privacy by design
│   │
│   ├── Security Governance
│   │   ├── Security policies
│   │   ├── Access controls
│   │   ├── Audit trails
│   │   ├── Incident response
│   │   ├── Business continuity
│   │   ├── Disaster recovery
│   │   └── Security training
│   │
│   └── Documentation & Audits
│       ├── Security documentation
│       ├── Audit preparation
│       ├── Compliance monitoring
│       ├── Remediation tracking
│       └── Evidence collection
│
└── Secure Development Lifecycle (700+ hours)
    ├── Planning Phase
    │   ├── Threat modeling
    │   ├── Risk assessment
    │   ├── Security requirements
    │   └── Compliance requirements
    │
    ├── Development Phase
    │   ├── Secure coding standards
    │   ├── Code review with security focus
    │   ├── Static analysis
    │   ├── Dependency scanning
    │   └── Secret management
    │
    ├── Testing Phase
    │   ├── Security testing
    │   ├── Penetration testing
    │   ├── Vulnerability scanning
    │   ├── DAST (Dynamic Application Security Testing)
    │   └── SAST (Static Application Security Testing)
    │
    ├── Deployment Phase
    │   ├── Secure deployment
    │   ├── Configuration hardening
    │   ├── Secret rotation
    │   ├── Monitoring setup
    │   └── Incident response plan
    │
    └── Monitoring Phase
        ├── Security monitoring
        ├── Log analysis
        ├── Alert management
        ├── Threat detection
        └── Continuous improvement
```

## Deep Dive Topics

### OWASP Top 10 Prevention
- **SQL Injection**: Parameterized queries, input validation
- **XSS (Cross-Site Scripting)**: Output encoding, CSP headers
- **CSRF (Cross-Site Request Forgery)**: Tokens, same-site cookies
- **Broken Authentication**: Strong password policies, MFA
- **Sensitive Data Exposure**: Encryption, secure communication
- **Insecure Deserialization**: Safe deserialization methods
- **Broken Access Control**: RBAC, proper authorization checks
- **XML External Entities (XXE)**: Disable XML features
- **Using Components with Known Vulnerabilities**: Dependency scanning
- **Insufficient Logging & Monitoring**: Comprehensive logging

### Testing Best Practices
- **Test Pyramid**: Unit tests at base, integration in middle, E2E at top
- **Test Coverage**: Aiming for meaningful coverage (70%+ typically)
- **Test Isolation**: Independent tests without side effects
- **Mock and Stub**: Isolating components for unit testing
- **Continuous Integration**: Running tests automatically
- **Performance Baselines**: Tracking performance over time

### Code Review Excellence
- **What Makes Good Code**: Readability, maintainability, performance
- **Security in Reviews**: Identifying security issues early
- **Design Patterns**: Recognizing and suggesting patterns
- **Testing**: Ensuring adequate test coverage
- **Documentation**: Clear, helpful comments
- **Constructive Feedback**: Balancing criticism with encouragement

### Compliance Implementation
- **Privacy by Design**: Building privacy into systems
- **Data Inventory**: Understanding what data is collected
- **Consent Management**: Getting proper user consent
- **Data Retention**: Knowing when to delete data
- **Access Controls**: Who can access what data
- **Incident Response**: Handling security breaches

## 66 Development Roles Using Security & Quality Skills

**QA & Testing Roles**:
- QA Engineer
- Test Automation Engineer
- Test Lead
- Performance Tester
- Penetration Tester
- Security Researcher

**Security Roles**:
- Cybersecurity Engineer
- Security Architect
- Application Security Engineer
- Compliance Officer
- Security Analyst

**Code Review & Quality Roles**:
- Senior Developer / Architect (Code Review)
- Code Quality Manager
- Technical Lead

## Quick Learning Paths

### QA Engineer Path (6-9 months)
1. Testing fundamentals - 1 month
2. Test automation basics - 1 month
3. Automation framework mastery - 2 months
4. Advanced testing types - 1 month
5. Performance testing - 1 month
6. Projects and specialization - ongoing

### Security Engineer Path (12-18 months)
1. Security fundamentals - 2 months
2. OWASP Top 10 - 1 month
3. Secure coding practices - 1 month
4. Cryptography and authentication - 2 months
5. Penetration testing - 2 months
6. Compliance frameworks - 1 month
7. Real-world projects - ongoing

### Penetration Tester Path (12-18 months)
1. Networking and systems - 2 months
2. Security fundamentals - 2 months
3. Penetration testing tools - 2 months
4. Exploitation techniques - 2 months
5. Report writing - 1 month
6. Certifications (CEH, OSCP) - ongoing

## Key Learning Resources

- [roadmap.sh Cyber Security Roadmap](https://roadmap.sh/cyber-security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- Official security frameworks
- Testing tools documentation
- Hands-on labs (HackTheBox, TryHackMe, OWASP WebGoat)
- Security certifications (CEH, CISSP, OSCP, etc.)

---

**When to use this skill**: Learning security practices, improving testing strategies, conducting code reviews, implementing compliance, or securing applications against vulnerabilities.
