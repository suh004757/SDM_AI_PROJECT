# SDM Technical Skillset Framework: Microsoft Technology Stack

## 📋 Overview

Based on the SDM Job Description requirements:
- **Microsoft Technology Stack** experience
- **Microsoft Azure Cloud** experience  
- **Microsoft M365 & Security** exposure
- **15+ resources** team management

This framework defines the technical competencies required for effective Service Delivery Management in Microsoft-centric environments.

---

## 🎯 Skill Proficiency Levels

| Level | Description | Expectation |
|-------|-------------|-------------|
| **L1 - Awareness** | Understands concepts, can discuss intelligently | Can explain to stakeholders |
| **L2 - Practitioner** | Can perform tasks with guidance | Hands-on with documentation |
| **L3 - Proficient** | Independent execution, troubleshooting | Day-to-day operational capability |
| **L4 - Expert** | Deep knowledge, architecture decisions | Design and optimization |
| **L5 - Authority** | Industry recognition, strategic direction | Thought leadership |

**SDM Target Level: L3-L4** (Proficient to Expert for core areas)

---

## ☁️ PART 1: MICROSOFT AZURE

### 1.1 Core Infrastructure Services

#### Compute Services

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Azure Virtual Machines** | IaaS compute | Sizing, cost optimization, availability | L4 |
| **VM Scale Sets** | Auto-scaling VM groups | Capacity planning, scaling policies | L3 |
| **Azure Kubernetes Service (AKS)** | Managed Kubernetes | Container workload delivery | L3 |
| **Azure App Service** | PaaS web hosting | Web app deployment, scaling | L3 |
| **Azure Functions** | Serverless compute | Event-driven workloads, cost model | L2 |
| **Azure Batch** | Large-scale parallel jobs | HPC workload management | L2 |

**Key Knowledge Areas:**
```
□ VM Series selection (D, E, F, M, N series) and use cases
□ Availability Sets vs Availability Zones vs Region Pairs
□ Reserved Instances vs Pay-as-you-go vs Spot pricing
□ VM sizing methodology (CPU, memory, storage, network)
□ Hybrid Benefit licensing (Windows Server, SQL Server)
□ Update Management and patching strategies
□ Backup and disaster recovery configurations
```

#### Storage Services

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Azure Blob Storage** | Object storage | Data tiering, lifecycle management | L4 |
| **Azure Files** | Managed file shares | SMB/NFS workloads, hybrid scenarios | L3 |
| **Azure Disk Storage** | Block storage for VMs | Performance tiers, encryption | L4 |
| **Azure Data Lake** | Big data storage | Analytics workload support | L2 |
| **Azure NetApp Files** | Enterprise NAS | High-performance file workloads | L2 |

**Key Knowledge Areas:**
```
□ Storage account types (GPv2, Premium, Blob)
□ Access tiers (Hot, Cool, Archive) and lifecycle policies
□ Redundancy options (LRS, ZRS, GRS, RA-GRS, GZRS)
□ Performance tiers (Standard, Premium, Ultra)
□ Storage security (encryption, private endpoints, SAS tokens)
□ Cost optimization strategies
```

#### Networking Services

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Virtual Network (VNet)** | Software-defined networking | Network architecture, segmentation | L4 |
| **Azure Load Balancer** | L4 load balancing | High availability design | L3 |
| **Application Gateway** | L7 load balancer + WAF | Web application delivery | L3 |
| **Azure Firewall** | Managed firewall service | Network security policies | L3 |
| **ExpressRoute** | Private connectivity | Hybrid connectivity | L3 |
| **VPN Gateway** | Site-to-site/P2S VPN | Remote access, hybrid | L3 |
| **Azure Front Door** | Global load balancer + CDN | Global application delivery | L3 |
| **Azure DNS** | DNS hosting | Domain management | L2 |

**Key Knowledge Areas:**
```
□ VNet design (address spaces, subnets, NSGs)
□ Hub-spoke topology and VNet peering
□ Network security groups (NSG) and Application Security Groups (ASG)
□ Private endpoints and service endpoints
□ ExpressRoute vs VPN decision criteria
□ Traffic Manager routing methods
□ DDoS Protection Standard
```

### 1.2 Azure Identity & Security

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Microsoft Entra ID** (Azure AD) | Identity management | Authentication, SSO, MFA | L4 |
| **Conditional Access** | Risk-based access policies | Security posture management | L4 |
| **Privileged Identity Management (PIM)** | Just-in-time access | Admin access governance | L3 |
| **Azure Key Vault** | Secrets management | Certificate, key, secret storage | L3 |
| **Microsoft Defender for Cloud** | Cloud security posture | Security monitoring, compliance | L4 |
| **Azure Sentinel** | SIEM/SOAR | Security operations | L3 |
| **Azure Policy** | Governance at scale | Compliance enforcement | L3 |

**Key Knowledge Areas:**
```
□ Entra ID tenant architecture and licensing (P1, P2)
□ Authentication methods (passwordless, FIDO2, Windows Hello)
□ Conditional Access policy design
□ RBAC role assignments and custom roles
□ Security Center secure score optimization
□ Compliance standards (ISO 27001, SOC 2, GDPR, HIPAA)
□ Zero Trust architecture principles
```

### 1.3 Azure Management & Governance

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Azure Resource Manager (ARM)** | Resource deployment | Infrastructure as Code | L3 |
| **Azure Monitor** | Observability platform | Performance monitoring | L4 |
| **Log Analytics** | Log aggregation & query | Operational insights | L4 |
| **Azure Automation** | Runbook automation | Operational automation | L3 |
| **Azure Cost Management** | Cost analysis & optimization | Budget management | L4 |
| **Azure Advisor** | Best practice recommendations | Optimization guidance | L3 |
| **Azure Blueprints** | Environment templates | Standardized deployments | L2 |

**Key Knowledge Areas:**
```
□ Management group and subscription hierarchy
□ Tagging strategy for cost allocation and governance
□ Azure Monitor metrics, logs, and alerts
□ KQL (Kusto Query Language) for Log Analytics
□ Cost Management budgets and alerts
□ Reservation recommendations and purchasing
□ Azure Landing Zone architecture
```

### 1.4 Azure Data Services

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Azure SQL Database** | Managed SQL | Database delivery, HA/DR | L3 |
| **Azure SQL Managed Instance** | SQL Server compatible PaaS | Migration, hybrid | L3 |
| **Azure Cosmos DB** | Global NoSQL database | Modern app backends | L2 |
| **Azure Database for MySQL/PostgreSQL** | Open source managed DB | OSS database delivery | L2 |
| **Azure Synapse Analytics** | Analytics platform | Data warehouse delivery | L2 |
| **Azure Data Factory** | Data integration | ETL/ELT pipelines | L2 |

**Key Knowledge Areas:**
```
□ SQL Database service tiers (Basic, Standard, Premium, Hyperscale)
□ DTU vs vCore purchasing models
□ High availability options (Zone redundant, Geo-replication)
□ Backup and point-in-time restore
□ Database migration strategies (DMS, offline, online)
□ Performance tuning and query optimization
```

---

## 💼 PART 2: MICROSOFT 365

### 2.1 Core Productivity Services

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Exchange Online** | Cloud email | Mail flow, compliance, migration | L4 |
| **SharePoint Online** | Content collaboration | Site architecture, governance | L3 |
| **OneDrive for Business** | Personal cloud storage | Data protection, sync | L3 |
| **Microsoft Teams** | Collaboration hub | Deployment, governance, voice | L4 |
| **Microsoft 365 Apps** | Office applications | Deployment, update channels | L3 |
| **Power Platform** | Low-code platform | Citizen development governance | L2 |

**Key Knowledge Areas:**
```
□ M365 licensing (E3, E5, F1, F3) and feature mapping
□ Exchange Online Protection and Defender for Office 365
□ Teams deployment and governance policies
□ SharePoint site architecture (Hub sites, Communication sites)
□ OneDrive Known Folder Move (KFM)
□ Microsoft 365 Apps deployment (CDN, SCCM, Intune)
□ Update channels (Current, Monthly Enterprise, Semi-Annual)
```

### 2.2 Microsoft 365 Security & Compliance

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Microsoft Defender for Office 365** | Email security | Threat protection | L4 |
| **Microsoft Defender for Endpoint** | Endpoint protection | EDR, threat hunting | L3 |
| **Microsoft Defender for Identity** | Identity threat detection | AD security | L3 |
| **Microsoft Defender for Cloud Apps** | CASB | Shadow IT, app governance | L3 |
| **Microsoft Purview** | Data governance | Classification, DLP, retention | L3 |
| **Insider Risk Management** | Insider threat detection | Risk monitoring | L2 |

**Key Knowledge Areas:**
```
□ Microsoft 365 Defender portal and unified incidents
□ Safe Attachments and Safe Links policies
□ Attack simulation training
□ Data Loss Prevention (DLP) policies
□ Sensitivity labels and Information Protection
□ Retention policies and eDiscovery
□ Compliance Manager and compliance score
```

### 2.3 Endpoint Management

| Service | Description | SDM Relevance | Target Level |
|---------|-------------|---------------|--------------|
| **Microsoft Intune** | Unified endpoint management | Device management, app deployment | L4 |
| **Configuration Manager (MECM)** | On-premises management | Legacy management, co-management | L3 |
| **Windows Autopilot** | Zero-touch deployment | Device provisioning | L3 |
| **Windows Update for Business** | Update management | Patch compliance | L3 |
| **Endpoint Analytics** | Endpoint insights | User experience monitoring | L3 |

**Key Knowledge Areas:**
```
□ Intune enrollment methods (Autopilot, bulk, user-driven)
□ Device compliance policies
□ Configuration profiles (device restrictions, Wi-Fi, VPN)
□ App deployment (Win32, MSI, Store apps, LOB)
□ Conditional Access integration
□ Co-management with Configuration Manager
□ Windows 365 Cloud PC management
```

---

## 🔒 PART 3: MICROSOFT SECURITY

### 3.1 Security Architecture

| Domain | Components | SDM Relevance | Target Level |
|--------|------------|---------------|--------------|
| **Identity Security** | Entra ID, PIM, Identity Protection | Zero Trust foundation | L4 |
| **Endpoint Security** | Defender for Endpoint, Intune | Device protection | L4 |
| **Data Security** | Purview, DLP, Encryption | Data protection | L3 |
| **Application Security** | Defender for Cloud Apps, App Proxy | App protection | L3 |
| **Infrastructure Security** | Defender for Cloud, Firewall, NSG | Cloud security | L3 |
| **Security Operations** | Sentinel, Defender XDR | Threat detection & response | L3 |

### 3.2 Zero Trust Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    ZERO TRUST ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│   │  IDENTITY   │    │  ENDPOINTS  │    │    DATA     │        │
│   │             │    │             │    │             │        │
│   │ • Entra ID  │    │ • Intune    │    │ • Purview   │        │
│   │ • MFA       │    │ • Defender  │    │ • DLP       │        │
│   │ • PIM       │    │ • Compliance│    │ • Encryption│        │
│   │ • Cond.Acc. │    │ • Autopilot │    │ • Labels    │        │
│   └─────────────┘    └─────────────┘    └─────────────┘        │
│          │                  │                  │                │
│          └──────────────────┼──────────────────┘                │
│                             │                                    │
│                    ┌────────▼────────┐                          │
│                    │   VISIBILITY    │                          │
│                    │   & ANALYTICS   │                          │
│                    │                 │                          │
│                    │ • Sentinel      │                          │
│                    │ • Defender XDR  │                          │
│                    │ • Log Analytics │                          │
│                    └─────────────────┘                          │
│                                                                  │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│   │    APPS     │    │ INFRASTRUCTURE│   │  NETWORK   │        │
│   │             │    │             │    │             │        │
│   │ • MCAS      │    │ • Defender  │    │ • Firewall  │        │
│   │ • App Proxy │    │   for Cloud │    │ • NSG       │        │
│   │ • OAuth     │    │ • Policy    │    │ • Private   │        │
│   │   Controls  │    │ • Blueprints│    │   Link      │        │
│   └─────────────┘    └─────────────┘    └─────────────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Security Operations

| Capability | Tools | SDM Relevance | Target Level |
|------------|-------|---------------|--------------|
| **Threat Detection** | Sentinel, Defender XDR | Incident awareness | L3 |
| **Investigation** | Advanced Hunting, KQL | Root cause analysis | L3 |
| **Response** | Automated playbooks, SOAR | Incident management | L3 |
| **Posture Management** | Secure Score, Compliance Score | Security improvement | L4 |
| **Threat Intelligence** | Defender TI, MITRE ATT&CK | Threat awareness | L2 |

**Key Knowledge Areas:**
```
□ Microsoft 365 Defender portal navigation
□ Incident and alert management workflow
□ KQL queries for threat hunting
□ Automated investigation and response (AIR)
□ Secure Score recommendations and remediation
□ Security baseline configurations
□ Incident response procedures
```

---

## 📊 PART 4: SKILL ASSESSMENT MATRIX

### 4.1 Self-Assessment Template

```
┌─────────────────────────────────────────────────────────────────┐
│              SDM TECHNICAL SKILL ASSESSMENT                      │
├─────────────────────────────────────────────────────────────────┤
│ Name: _____________________  Date: _______________              │
│ Current Role: _____________  Experience: _____ years            │
├─────────────────────────────────────────────────────────────────┤
│ Rating Scale: 1=Awareness, 2=Practitioner, 3=Proficient,        │
│               4=Expert, 5=Authority                              │
├─────────────────────────────────────────────────────────────────┤
│ MICROSOFT AZURE                          Current │ Target │ Gap │
│ ├─ Compute (VMs, AKS, App Service)      [  ]    │ [  ]  │[  ]│
│ ├─ Storage (Blob, Files, Disks)         [  ]    │ [  ]  │[  ]│
│ ├─ Networking (VNet, LB, Firewall)      [  ]    │ [  ]  │[  ]│
│ ├─ Identity (Entra ID, PIM)             [  ]    │ [  ]  │[  ]│
│ ├─ Security (Defender, Sentinel)        [  ]    │ [  ]  │[  ]│
│ ├─ Management (Monitor, Cost Mgmt)      [  ]    │ [  ]  │[  ]│
│ └─ Data (SQL, Cosmos, Synapse)          [  ]    │ [  ]  │[  ]│
├─────────────────────────────────────────────────────────────────┤
│ MICROSOFT 365                            Current │ Target │ Gap │
│ ├─ Exchange Online                      [  ]    │ [  ]  │[  ]│
│ ├─ SharePoint Online                    [  ]    │ [  ]  │[  ]│
│ ├─ Microsoft Teams                      [  ]    │ [  ]  │[  ]│
│ ├─ Intune/Endpoint Manager              [  ]    │ [  ]  │[  ]│
│ ├─ Security & Compliance                [  ]    │ [  ]  │[  ]│
│ └─ Power Platform                       [  ]    │ [  ]  │[  ]│
├─────────────────────────────────────────────────────────────────┤
│ SECURITY                                 Current │ Target │ Gap │
│ ├─ Zero Trust Architecture              [  ]    │ [  ]  │[  ]│
│ ├─ Microsoft Defender Suite             [  ]    │ [  ]  │[  ]│
│ ├─ Security Operations (SOC)            [  ]    │ [  ]  │[  ]│
│ ├─ Compliance & Governance              [  ]    │ [  ]  │[  ]│
│ └─ Incident Response                    [  ]    │ [  ]  │[  ]│
├─────────────────────────────────────────────────────────────────┤
│ AVERAGE SCORE                           [    ]  │ [    ] │    │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Certification Roadmap

| Level | Certification | Focus Area | Recommended For |
|-------|--------------|------------|-----------------|
| **Foundational** | AZ-900 | Azure Fundamentals | All SDMs |
| **Foundational** | SC-900 | Security Fundamentals | All SDMs |
| **Foundational** | MS-900 | M365 Fundamentals | All SDMs |
| **Associate** | AZ-104 | Azure Administrator | Infrastructure SDMs |
| **Associate** | AZ-500 | Azure Security Engineer | Security-focused SDMs |
| **Associate** | MS-102 | M365 Administrator | M365-focused SDMs |
| **Associate** | SC-200 | Security Operations Analyst | SOC-integrated SDMs |
| **Associate** | MD-102 | Endpoint Administrator | Endpoint-focused SDMs |
| **Expert** | AZ-305 | Azure Solutions Architect | Senior SDMs |
| **Expert** | SC-100 | Cybersecurity Architect | Security Lead SDMs |

**Recommended Path for SDM:**
```
Year 1: AZ-900 → SC-900 → MS-900 → AZ-104
Year 2: AZ-500 → MS-102 → SC-200
Year 3: AZ-305 or SC-100 (based on specialization)
```

### 4.3 Learning Resources

| Resource | Type | Cost | Best For |
|----------|------|------|----------|
| **Microsoft Learn** | Self-paced modules | Free | Fundamentals, hands-on |
| **Microsoft Docs** | Documentation | Free | Reference, deep dives |
| **Azure Portal** | Hands-on practice | Pay-as-you-go | Practical experience |
| **Pluralsight** | Video courses | $29-45/mo | Structured learning |
| **A Cloud Guru** | Video + labs | $35/mo | Certification prep |
| **Whizlabs** | Practice exams | $20-30/exam | Exam preparation |
| **Microsoft Events** | Webinars, Ignite | Free | Updates, announcements |

---

## 📋 PART 5: TECHNICAL INTERVIEW QUESTIONS

### Azure Infrastructure

```
1. Explain the difference between Availability Sets, Availability Zones, 
   and Region Pairs. When would you use each?

2. A customer needs 99.99% SLA for a web application. Design the Azure 
   architecture to achieve this.

3. Compare Azure Reserved Instances, Savings Plans, and Spot VMs. 
   When is each appropriate?

4. How would you design a hub-spoke network topology in Azure? 
   What are the key components?

5. Explain the Azure Storage redundancy options and their use cases.

6. A VM is experiencing performance issues. Walk through your 
   troubleshooting methodology using Azure Monitor.

7. How do you implement a Zero Trust network architecture in Azure?

8. Explain the difference between Azure Policy and Azure RBAC. 
   Give examples of when to use each.
```

### Microsoft 365

```
1. A company is migrating from on-premises Exchange to Exchange Online. 
   What migration methods are available and when would you use each?

2. How would you design a Microsoft Teams governance strategy for a 
   10,000-user organization?

3. Explain Microsoft Defender for Office 365 Plan 1 vs Plan 2. 
   What are the key differences?

4. A user reports they cannot access SharePoint. Walk through your 
   troubleshooting steps.

5. How do you implement Data Loss Prevention (DLP) across M365 workloads?

6. Explain the Microsoft 365 update channels. How would you configure 
   them for an enterprise?

7. What is Co-management with Intune and MECM? When is it beneficial?

8. How do you implement Conditional Access policies for a Zero Trust model?
```

### Security

```
1. Explain the Microsoft Defender XDR architecture. How do the 
   components work together?

2. A security alert indicates potential ransomware activity. 
   Walk through your incident response process.

3. How would you improve an organization's Microsoft Secure Score 
   from 45% to 75%?

4. Explain the difference between Microsoft Sentinel and 
   Microsoft Defender for Cloud.

5. How do you implement Privileged Identity Management (PIM) 
   for Azure resource access?

6. What is Microsoft Purview and how does it help with data governance?

7. Design a security monitoring architecture using Microsoft tools 
   for a hybrid environment.

8. How do you investigate a compromised user account using 
   Microsoft 365 Defender?
```

---

## 🎯 PART 6: COMPETENCY FRAMEWORK

### SDM Technical Competency Model

| Competency | Description | Behaviors |
|------------|-------------|-----------|
| **Technical Breadth** | Wide knowledge across Microsoft stack | Can discuss any M365/Azure topic intelligently |
| **Technical Depth** | Deep expertise in core areas | Can architect and troubleshoot complex issues |
| **Solution Design** | Translate requirements to architecture | Creates viable technical solutions |
| **Cost Optimization** | Financial awareness in technical decisions | Considers TCO in all recommendations |
| **Security Mindset** | Security-first approach | Embeds security in all designs |
| **Operational Excellence** | Focus on reliability and efficiency | Designs for manageability |
| **Continuous Learning** | Stays current with technology | Regularly updates skills |

### Competency Development Plan

```
┌─────────────────────────────────────────────────────────────────┐
│              TECHNICAL DEVELOPMENT PLAN                          │
├─────────────────────────────────────────────────────────────────┤
│ Name: _____________________  Manager: _______________           │
│ Review Period: _____________  Next Review: _______________      │
├─────────────────────────────────────────────────────────────────┤
│ SKILL GAP PRIORITIES (Top 3)                                     │
│ 1. _________________________________ Target Date: ___________   │
│ 2. _________________________________ Target Date: ___________   │
│ 3. _________________________________ Target Date: ___________   │
├─────────────────────────────────────────────────────────────────┤
│ CERTIFICATION GOALS                                              │
│ Q1: ________________________________                             │
│ Q2: ________________________________                             │
│ Q3: ________________________________                             │
│ Q4: ________________________________                             │
├─────────────────────────────────────────────────────────────────┤
│ LEARNING ACTIVITIES                                              │
│ □ Microsoft Learn Path: _________________________________       │
│ □ Hands-on Lab Project: _________________________________       │
│ □ Mentoring/Shadowing: _________________________________        │
│ □ Conference/Training: _________________________________        │
├─────────────────────────────────────────────────────────────────┤
│ SUCCESS METRICS                                                  │
│ □ Certification achieved: Y/N                                    │
│ □ Skill assessment improvement: _____ points                    │
│ □ Project application: _________________________________        │
└─────────────────────────────────────────────────────────────────┘
```

---

*This framework ensures SDMs have the technical depth to make informed decisions, communicate effectively with technical teams, and deliver Microsoft-based solutions that meet business requirements.*