# 🧩 3DHub.am

**3DHub.am** is an interactive web platform for creating, viewing, sharing, printing, and scanning 3D models. Designed for designers, engineers, students, and technology enthusiasts.

---

## 📌 Product Info

- **Product Name:** 3DHub.am  
- **Author:** Hrant Mikaelyan  
- **Start Date:** April 25, 2025  
- **Goal:** Provide an all-in-one 3D modeling, printing, and scanning platform with user collaboration features.

---

## 🌐 General Overview

3DHub.am brings together tools and services related to 3D modeling, 3D printing, and 3D scanning. The platform encourages creativity, collaboration, and access to modern 3D services.

### 🔧 Main Features

- 📂 Upload, view, and manage 3D models
- 🔍 Interactive 3D model previews via browser (Three.js)
- 🖨️ Submit 3D printing requests with material and size options
- 📷 Book 3D scanning services (online or in-person)
- 💬 Chat system for users and admins
- 🛡️ Manage private/public profiles and projects

---

## 🧩 Core Functionality

### 1. User Login / Registration

- Register via email or social media
- Secure login system with validation

### 2. Model Management

- Supported formats: `.STL`, `.OBJ`, `.GLTF`
- Preview 3D models in browser
- Like, comment, and manage visibility

### 3. 3D Printing

- Select model, material, scale, and quantity
- Estimate costs automatically
- Payments integrated with Idram and Telcell

### 4. 3D Scanning

- Choose equipment and service type
- Schedule time slots online

### 5. Chat System

- One-on-one and project-based conversations
- Mentions, notes, and notifications

---

## 🗂️ Website Pages

| Page                | Description                                         |
|---------------------|-----------------------------------------------------|
| 🏠 Home             | Latest models and platform introduction             |
| 📚 Models Gallery   | Browse and view public 3D models                    |
| 🖨️ Print Order      | Choose model and place a printing order            |
| 📷 Scan Service     | Info on scanning options and request form          |
| 👤 My Profile       | Personal dashboard for projects, models, settings  |
| 💬 Chat             | Messaging system for collaboration                 |
| 🔑 Login/Register   | Authentication pages                               |

---

## 🛠️ Technologies

- 🎨 **Frontend:** HTML, CSS, JavaScript, [Three.js](https://threejs.org/)
- ⚙️ **Backend:** Python / Django
- 🗄️ **Database:** PostgreSQL or SQLite

---

## 🎨 UX/UI Requirements

- Clean and minimalist design
- Support for dark and light themes
- Fully responsive layout for mobile and desktop

---

## 🚀 Future Enhancements

- 📱 AR support for real-world model placement
- 🏆 User/author rating and review system
- 🌍 Multilingual interface (Armenian, English, etc.)

---

## 🐳 Run Locally with Docker

```bash
git clone https://github.com/yourusername/3dhub.am.git
cd 3dhub.am
docker-compose up --build
Access the app at http://localhost:8000

🤝 Contributing
Contributions are welcome! Please open an issue before submitting major changes.
Pull requests are appreciated.

📄 License
Licensed under the MIT License.