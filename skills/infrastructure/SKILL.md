---
name: infrastructure-and-devops-tools
description: Master DevOps and infrastructure tools - Docker, Kubernetes, Terraform, AWS, Azure, GCP, Linux, CI/CD pipelines. Use when learning infrastructure automation, containerization, orchestration, or cloud deployment.
---

# Infrastructure & DevOps Tools

## Quick Start Guide

This skill covers modern infrastructure automation, containerization, orchestration, and cloud platform mastery.

### DevOps Technology Stack

```
DevOps & Infrastructure
├── Containerization (1000+ hours)
│   ├── Docker Fundamentals
│   │   ├── Images and containers
│   │   ├── Dockerfiles and best practices
│   │   ├── Container networking
│   │   ├── Volume management
│   │   └── Docker Compose
│   │
│   ├── Container Registries
│   │   ├── Docker Hub
│   │   ├── ECR (Elastic Container Registry)
│   │   ├── GCR (Google Container Registry)
│   │   └── Private registries
│   │
│   └── Image Best Practices
│       ├── Multi-stage builds
│       ├── Layer optimization
│       ├── Security scanning
│       └── Image signing
│
├── Orchestration (1200+ hours)
│   ├── Kubernetes Fundamentals
│   │   ├── Pods and containers
│   │   ├── Services and networking
│   │   ├── Deployments and StatefulSets
│   │   ├── ConfigMaps and Secrets
│   │   └── Volumes and persistent storage
│   │
│   ├── Advanced Kubernetes
│   │   ├── Operators and CRDs
│   │   ├── Service mesh (Istio)
│   │   ├── Helm for templating
│   │   ├── GitOps (ArgoCD, Flux)
│   │   └── Security policies
│   │
│   └── Kubernetes Distributions
│       ├── EKS (AWS Kubernetes)
│       ├── GKE (Google Kubernetes Engine)
│       ├── AKS (Azure Kubernetes Service)
│       └── Self-managed clusters
│
├── Infrastructure as Code (800+ hours)
│   ├── Terraform
│   │   ├── HCL syntax
│   │   ├── Providers and resources
│   │   ├── Modules for reusability
│   │   ├── State management
│   │   ├── Workspaces
│   │   └── Remote backends
│   │
│   ├── CloudFormation (AWS)
│   │   ├── YAML/JSON templates
│   │   ├── Stack management
│   │   ├── Change sets
│   │   └── Nested stacks
│   │
│   ├── Other IaC Tools
│   │   ├── Ansible for configuration
│   │   ├── Pulumi for programming languages
│   │   ├── Chef and Puppet
│   │   └── CDK (AWS/Terraform)
│   │
│   └── Version Control Integration
│       ├── Git-based workflows
│       ├── Infrastructure versioning
│       ├── Change tracking
│       └── Collaboration practices
│
├── Cloud Platforms (1500+ hours total)
│   ├── AWS (Most Popular)
│   │   ├── EC2 (compute)
│   │   ├── RDS (databases)
│   │   ├── S3 (storage)
│   │   ├── Lambda (serverless)
│   │   ├── VPC and networking
│   │   ├── Load Balancers
│   │   ├── CloudFront CDN
│   │   ├── IAM and security
│   │   ├── CloudWatch monitoring
│   │   ├── Auto Scaling
│   │   └── Cost optimization
│   │
│   ├── Google Cloud Platform
│   │   ├── Compute Engine (VMs)
│   │   ├── App Engine (PaaS)
│   │   ├── Cloud Functions (FaaS)
│   │   ├── BigQuery (data warehouse)
│   │   ├── Cloud Storage
│   │   ├── Cloud SQL
│   │   ├── AI/ML services
│   │   └── Networking
│   │
│   ├── Microsoft Azure
│   │   ├── Virtual Machines
│   │   ├── App Services
│   │   ├── Azure Functions
│   │   ├── Azure SQL Database
│   │   ├── Blob Storage
│   │   ├── CosmosDB
│   │   └── Azure DevOps
│   │
│   └── Alternative Clouds
│       ├── DigitalOcean
│       ├── Heroku
│       ├── Linode
│       └── Oracle Cloud
│
├── CI/CD Pipelines (900+ hours)
│   ├── GitHub Actions
│   │   ├── Workflows and jobs
│   │   ├── Actions and marketplace
│   │   ├── Secrets management
│   │   └── Environments and deployments
│   │
│   ├── GitLab CI/CD
│   │   ├── Runners
│   │   ├── Pipelines and stages
│   │   ├── Variables and artifacts
│   │   └── Auto DevOps
│   │
│   ├── Jenkins
│   │   ├── Pipelines as Code
│   │   ├── Agents and distributed
│   │   ├── Integration with tools
│   │   └── Blue-green deployments
│   │
│   ├── CircleCI
│   │   ├── Workflows
│   │   ├── Orbs and reuse
│   │   └── Contexts and environment variables
│   │
│   └── General Practices
│       ├── Build automation
│       ├── Test automation
│       ├── Deployment strategies
│       ├── Release management
│       └── Artifact management
│
├── Monitoring & Logging (700+ hours)
│   ├── Metrics Collection
│   │   ├── Prometheus
│   │   ├── InfluxDB
│   │   ├── CloudWatch (AWS)
│   │   ├── Stackdriver (GCP)
│   │   └── Azure Monitor
│   │
│   ├── Visualization
│   │   ├── Grafana
│   │   ├── Kibana
│   │   ├── DataDog
│   │   ├── New Relic
│   │   └── Splunk
│   │
│   ├── Logging
│   │   ├── ELK Stack (Elasticsearch, Logstash, Kibana)
│   │   ├── Splunk
│   │   ├── CloudWatch Logs
│   │   ├── Stackdriver Logging
│   │   └── ELK alternatives (Loki)
│   │
│   ├── Alerting
│   │   ├── AlertManager
│   │   ├── PagerDuty
│   │   ├── OpsGenie
│   │   └── Slack integration
│   │
│   └── APM (Application Performance)
│       ├── Datadog APM
│       ├── New Relic APM
│       ├── Elastic APM
│       └── Jaeger (distributed tracing)
│
└── Linux & Operating Systems (1000+ hours)
    ├── Linux Fundamentals
    │   ├── File system
    │   ├── User and permissions
    │   ├── Package management
    │   ├── System services
    │   └── Shell scripting
    │
    ├── Linux Server Administration
    │   ├── User management
    │   ├── Disk management
    │   ├── Network configuration
    │   ├── SSH and remote access
    │   ├── Firewall (iptables/firewalld)
    │   └── SELinux/AppArmor
    │
    └── Common Distributions
        ├── Ubuntu
        ├── CentOS/RHEL
        ├── Debian
        ├── Alpine
        └── Amazon Linux
```

## Deep Dive Topics

### Docker Mastery
- **Image Creation**: Dockerfile optimization, multi-stage builds, minimal images
- **Container Runtime**: Container lifecycle, volume mounting, networking
- **Best Practices**: Security scanning, image signing, registry management
- **Development Workflow**: Docker Compose for local development

### Kubernetes Expertise
- **Architecture**: Control plane, nodes, kubelet, kube-proxy
- **Core Concepts**: Pods, Services, Deployments, StatefulSets, DaemonSets
- **Storage**: PersistentVolumes, PersistentVolumeClaims, storage classes
- **Networking**: Service discovery, ingress, network policies
- **Operators**: Extending Kubernetes with custom resources
- **Security**: RBAC, network policies, pod security policies
- **Scaling**: HPA (Horizontal Pod Autoscaler), VPA (Vertical Pod Autoscaler)

### Terraform Infrastructure
- **Modules**: Creating reusable infrastructure components
- **State Management**: Remote backends, locking, version control
- **Provider Configuration**: Managing credentials securely
- **Workspaces**: Multiple environments management
- **Testing**: Terratest for infrastructure testing

### AWS Services Deep Dive
- **Compute**: EC2, Lambda, ECS, Fargate, Elastic Beanstalk
- **Networking**: VPC, subnets, security groups, NACLs, route tables
- **Databases**: RDS, DynamoDB, ElastiCache, Redshift
- **Storage**: S3, EBS, EFS, Glacier
- **Messaging**: SQS, SNS, Kinesis
- **Monitoring**: CloudWatch, X-Ray, EventBridge

### CI/CD Pipeline Patterns
- **Build Automation**: Compilation, linting, security scanning
- **Test Automation**: Unit tests, integration tests, end-to-end tests
- **Artifact Management**: Docker images, binaries, packages
- **Deployment Strategies**: Blue-green, canary, rolling deployments
- **Rollback Strategies**: Handling failed deployments

### Monitoring Best Practices
- **SLI/SLO/SLA**: Defining reliability objectives
- **Alerting**: Threshold-based and anomaly detection
- **Dashboards**: Real-time visualization and insights
- **Log Aggregation**: Centralized logging from all services
- **Distributed Tracing**: Understanding request flows

## 66 Development Roles Using DevOps Skills

**Core DevOps Roles**:
- DevOps Engineer (Beginner, Advanced)
- Site Reliability Engineer (SRE)
- Cloud Engineer
- Infrastructure Engineer
- Platform Engineer
- Solutions Architect

**Specialized Roles**:
- Kubernetes Administrator
- Docker Specialist
- Terraform Expert
- AWS Solutions Architect
- Linux System Administrator
- CI/CD Engineer
- Cloud Security Engineer
- Database Administrator

## Quick Learning Paths

### DevOps Engineer Path (6-12 months)
1. Linux fundamentals - 2 months
2. Docker containerization - 2 months
3. Kubernetes orchestration - 2 months
4. Terraform IaC - 1-2 months
5. AWS or GCP - 2 months
6. CI/CD pipelines - 1-2 months
7. Monitoring and logging - 1-2 months
8. Real-world projects - ongoing

### Kubernetes Path (4-8 months)
1. Docker fundamentals - 2 months
2. Kubernetes core concepts - 2 months
3. Advanced Kubernetes - 2 months
4. Helm and operators - 1-2 months
5. Production patterns - ongoing

### Terraform Path (2-4 months)
1. HCL fundamentals - 1 month
2. Providers and resources - 1 month
3. Modules and best practices - 1 month
4. State management - 1 month
5. Real-world infrastructure - ongoing

### AWS Solutions Architect (4-8 months)
1. AWS fundamentals - 1 month
2. Compute services - 1 month
3. Networking and databases - 2 months
4. Advanced topics - 1-2 months
5. Solutions design - ongoing

## Key Learning Resources

- [roadmap.sh DevOps Roadmap](https://roadmap.sh/devops)
- [roadmap.sh Docker Guide](https://roadmap.sh/docker)
- [roadmap.sh Kubernetes Guide](https://roadmap.sh/kubernetes)
- [roadmap.sh Terraform Guide](https://roadmap.sh/terraform)
- [roadmap.sh AWS Guide](https://roadmap.sh/aws)
- Official documentation (Docker, Kubernetes, Terraform, AWS, GCP, Azure)
- Hands-on labs and certifications
- Community practices and patterns

## Certifications

- **Docker**: Docker Certified Associate
- **Kubernetes**: CKA, CKAD, CKS
- **AWS**: Solutions Architect, Developer, SysOps
- **Terraform**: HashiCorp Certified: Terraform Associate
- **Cloud Platforms**: GCP Professional, Azure Administrator

---

**When to use this skill**: Learning DevOps practices, containerizing applications, orchestrating infrastructure, implementing automation, optimizing cloud costs, or managing production systems.
