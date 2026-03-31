#  Cyber-Threat Hunter (RL-Powered)

[![Live Demo](https://img.shields.io/badge/Demo-HuggingFace-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/rishabh-dwivedi22/Cyber-Threat-Hunter)
[![GitHub License](https://img.shields.io/github/license/rishabh-dwivedi22/Cyber-Threat-Hunter)](https://github.com/rishabh-dwivedi22/Cyber-Threat-Hunter)

> **Cyber-Threat Hunter** is an AI-driven security monitoring dashboard that uses **Reinforcement Learning (RL)** to simulate and automate threat patching in real-time environments.

---

## Key Features
* **AI-Driven Response:** Uses a custom Gymnasium-based environment for RL agents to learn optimal patching strategies.
* **Real-time Dashboard:** Built with **React + Vite** for a lag-free, modern UI experience.
* **Containerized Architecture:** Fully Dockerized for seamless deployment on Hugging Face Spaces.
* **RESTful API:** Flask backend handles the communication between the AI agent and the frontend.

## Tech Stack
| Category | Tools/Technologies |
| :--- | :--- |
| **Frontend** | React.js, Vite, Tailwind CSS |
| **Backend** | Python, Flask |
| **AI/ML** | OpenAI Gymnasium (Custom Environment), Reinforcement Learning |
| **Deployment** | Docker, Hugging Face Spaces |

## Architecture
The system follows a Client-Server architecture where the **React** frontend requests the current network state from the **Flask** backend. The backend runs a **CyberThreatEnv** (RL Environment) that calculates rewards and next states based on simulated threats.



##  Local Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/rishabh-dwivedi22/Cyber-Threat-Hunter.git](https://github.com/rishabh-dwivedi22/Cyber-Threat-Hunter.git)
   cd Cyber-Threat-Hunter
