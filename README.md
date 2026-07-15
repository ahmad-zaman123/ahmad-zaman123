# 👋 Hi, I'm Ahmad Zaman

🚀 **Backend Engineer | Django & REST APIs | MERN Stack | Scalable Systems**

Backend-focused software engineer with hands-on experience in **Django, Django REST Framework, and MERN stack development**. Passionate about building **clean, scalable, and production-ready APIs**, optimizing database queries, and designing maintainable backend systems that scale in real-world environments.

---

## 🛠 Tech Stack

### 🚀 Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=flat&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express.js-000000?style=flat&logo=express&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat&logo=celery&logoColor=white)

### 🎨 Frontend
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

### 🗄 Databases & Caching
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

### ⚙️ DevOps & Tools
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=flat&logo=pycharm&logoColor=white)

---

## 💼 What I Do

- Design & build RESTful APIs using Django REST Framework and Express
- Build ETL pipelines and async / background workflows with Celery
- Integrate third-party services — payment gateways, messaging APIs, OpenAI LLMs
- Optimize ORM queries and resolve performance bottlenecks
- Implement authentication, authorization, and webhook signature verification
- Write clean, testable, and maintainable backend code

---

## 🧑‍💻 Experience

### Associate Software Engineer — Barq Dev · Nov 2025 – Present

**Tech:** Python, Django, Django REST Framework, PostgreSQL, Redis, Celery, Django Channels, WebSockets, OpenAI, FCM

* Designed and developed **scalable RESTful APIs** using Python, Django, and Django REST Framework (DRF), implementing authentication, permissions, filtering, and pagination
* Built **backend business logic and transactional workflows** with optimized ORM queries on PostgreSQL, improving API response times, database efficiency, and scalability
* Implemented **asynchronous task processing** and background jobs using Celery, and developed ETL pipelines for efficient data extraction, transformation, and loading
* Integrated **OpenAI Large Language Models (LLMs)** and Text-to-Speech (TTS) services to deliver AI-powered automation, intelligent features, and audio-based user interactions
* Applied **Redis caching, logging, and custom middleware** to enhance system performance, observability, and reliability
* Developed a **real-time notification platform** using Django Channels, WebSockets, Redis, Celery, and FCM push notifications, with JWT authentication and user presence tracking
* Collaborated within an **Agile development team** using Git and GitHub for version control, code reviews, and feature-branch workflows

---

## 🚀 Featured Projects

### 🔗 Unfurl — Social Preview Cards as an API

**Tech:** Django REST Framework, PostgreSQL (Neon), Redis (Upstash), React, Pillow

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://unfurl-one.vercel.app/) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Unfurl)

- Designed a **create/serve split** — an authenticated endpoint mints a signed URL, while the actual `og:image` is served from a public, unauthenticated, crawler-friendly endpoint
- Implemented **HMAC-signed URLs** that double as cache keys — any tampered parameter is rejected with a 403, and identical requests are served from cache
- Built a **Stripe-style API key system** with SHA-256 hashed keys, showing the raw key only once, alongside a custom DRF auth class for `Bearer` token support
- Added **per-key rate limiting and plan-based quotas** (fixed-window, Redis-backed) with standard `X-RateLimit-*` / `Retry-After` headers
- Hardened the logo-fetch feature against **SSRF** — blocks private IP ranges and cloud metadata endpoints, disallows redirects, and enforces size/time limits

--- 

### 📄 Paper-Mind — Chat With Your Documents (RAG)

**Tech:** Django REST Framework, PostgreSQL + pgvector, Google Gemini, React (Vite)

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://paper-mind-sage.vercel.app) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Paper-Mind)

- Built a **retrieval-augmented generation (RAG) pipeline** — uploaded PDFs, Word docs, and text files are extracted, chunked, and embedded automatically
- Implemented **vector similarity search** using PostgreSQL + pgvector (Neon in production) for fast nearest-neighbour retrieval over document chunks
- Integrated **Google Gemini** for both embeddings (`gemini-embedding-001`) and answer generation (`gemini-2.5-flash`), with every answer **cited back to the exact source passage**
- Added **multi-turn conversations** — the system retains prior context so follow-up questions resolve correctly against the same document
- Secured the app with **JWT auth** so each user's documents and chats stay private by default

---

### 🛒 Blissful — Full-Stack E-commerce Storefront

**Tech:** Node.js, Express, MongoDB (Mongoose), React, Safepay

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://blissful-template.vercel.app/) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Blissful-Template)

- Designed and built a **REST API** (Express + Mongoose) covering products, cart, orders, and payments for a beauty/skincare storefront
- Integrated **Safepay** for live card payments with **HMAC-verified webhooks** that auto-update order status server-side — no client polling required
- Implemented a **Cash-on-Delivery fallback** and a **session-based MongoDB cart**, so customers can shop and check out without creating an account
- Built **server-side product search** (regex-based), category and skin-concern filtering, and price-range queries with real-time stock toggles
- Delivered the full flow **end-to-end** — catalog, cart, checkout, and payment confirmation — as a single deployable full-stack app

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=ahmad-zaman123&show_icons=true&count_private=true&include_all_commits=true&theme=tokyonight&hide_border=true&cb=3" height="180"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=ahmad-zaman123&theme=tokyonight&hide_border=true&cb=3" height="180"/>
</p>

---

## 🌱 Currently Exploring

- Advanced Django performance optimization
- System design for scalable backend architectures
- Async processing, background workers, and AI-powered backends

---

## 🤝 Connect With Me

- 💼 LinkedIn: https://www.linkedin.com/in/ahmad-zaman-228879285/
- 🐙 GitHub: https://github.com/ahmad-zaman123
- 📧 Email: ahmadzamannn@gmail.com

---

⭐️ **If you find my work useful, feel free to follow or star my repositories!**
