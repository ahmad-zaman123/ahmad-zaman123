# 👋 Hi, I'm Ahmad Zaman

🚀 **Backend Engineer · Python & Django · Cloud and endpoint security**

Building production **Python APIs (Django, DRF, Flask)**, 1+ years in.

- 🔐 **Now:** endpoint-security tooling and a cloud and SaaS identity scanner across AWS, Azure, GCP, Okta and more
- ⚡ **Before:** async, real-time systems (Celery, WebSockets, Redis) and OpenAI integrations at Barq
- 🧠 **On the side:** RAG and API projects, such as Unfurl and Paper-Mind

I care about clean, scalable, production-ready backends.

---

## 🤝 Connect With Me

[![Portfolio](https://img.shields.io/badge/Portfolio-ahmad--zaman--portfolio-2447D6?style=for-the-badge&logo=vercel&logoColor=white)](https://ahmad-zaman-portfolio.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ahmad--zaman-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmad-zaman-dev/)
[![GitHub](https://img.shields.io/badge/GitHub-ahmad--zaman123-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123)
[![Email](https://img.shields.io/badge/Email-ahmadzamannn@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ahmadzamannn@gmail.com)

---

## 📊 GitHub Activity

<!-- Heatmap + stats are regenerated daily by .github/workflows/update-profile-art.yml.
     whoami.svg is static: edit scripts/render_whoami_svg.py and re-run it.
     Both card SVGs are 840x880, so equal widths give equal heights. -->

<div align="center">

<img src="./contrib-heatmap.svg" width="860" alt="Ahmad's GitHub contribution graph — auto-refreshed daily" />

<br><br>

<table>
<tr>
<td valign="top"><img src="./whoami.svg" width="420" alt="Ahmad Zaman — whoami terminal card" /></td>
<td valign="top"><img src="./stats.svg" width="420" alt="Ahmad's GitHub streak and contribution stats — auto-refreshed daily" /></td>
</tr>
</table>

</div>

---

## 🧑‍💻 Experience

### Backend Engineer — Broadstone Technologies, LLC · Aug 2026 – Present

**Tech:** Python, Flask, Wazuh, AWS, GCP, Azure, Microsoft Graph, Okta

* Built the **Flask endpoint** that receives device-offline notifications from **Wazuh** and emails alerts to customers, covering **nearly 700 monitored devices** and replacing a legacy integration. Alerts show the last keep-alive as the disconnect time and pass DKIM
* Extended the **cloud identity scanner** across AWS, Azure, Microsoft Graph, GCP, Google Workspace, Slack, GitHub, Dropbox, Zoom and Okta with MFA, last-login, access-key, group and policy fields
* Added **device-vs-cloud identity matching** and fixed failed scans being reported as empty
* Added search, filtering, and live-query retry and timeout handling to the **EDR host-management API**, plus host cleanup rules

### Associate Software Engineer — Barq Dev · Aug 2025 – Jul 2026

**Tech:** Python, Django, Django REST Framework, PostgreSQL, Redis, Celery, Django Channels, WebSockets, OpenAI, Piper TTS, FCM

* Designed and shipped **scalable REST APIs** serving a React client, with token authentication, granular permissions, filtering and pagination
* Architected **relational schemas** and transactional workflows on **PostgreSQL**, modelling core product domains (recipes, cart, pantry) and enforcing data integrity at the database layer
* Eliminated **N+1 patterns across four modules** using reusable ORM optimization patterns, **cutting multiple endpoints from 250+ queries to under 10**, and added **Redis caching** to cut repeat response times
* Built a **real-time notification service** using WebSockets, Redis and Celery with **JWT authentication** and user presence tracking
* Implemented **asynchronous pipelines** with Celery for background jobs, ETL workflows, image scanning and URL-to-recipe ingestion, and improved observability with structured logging and custom middleware
* Integrated the **OpenAI API** and Piper TTS for intelligent automation and audio-based user experiences, with caching and asynchronous processing

---

## 🚀 Featured Projects

### 🔗 Unfurl — Social Preview Cards as an API

*An API that turns any URL into a social preview image, with signed URLs, API keys and rate limiting.*

**Tech:** Django REST Framework, PostgreSQL (Neon), Redis (Upstash), React, Pillow

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://unfurl-one.vercel.app/) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Unfurl)

- Designed a **create/serve split** — an authenticated endpoint mints a signed URL, while the actual `og:image` is served from a public, unauthenticated, crawler-friendly endpoint
- Implemented **HMAC-signed URLs** that double as cache keys — any tampered parameter is rejected with a 403, and identical requests are served from cache
- Built a **Stripe-style API key system** with SHA-256 hashed keys, showing the raw key only once, alongside a custom DRF auth class for `Bearer` token support
- Added **per-key rate limiting and plan-based quotas** (fixed-window, Redis-backed) with standard `X-RateLimit-*` / `Retry-After` headers, plus usage analytics for API consumers
- Hardened the logo-fetch feature against **SSRF** — blocks private IP ranges and cloud metadata endpoints, disallows redirects, and enforces size/time limits

---

### 📄 Paper-Mind — Chat With Your Documents (RAG)

*Upload documents and chat with them. Every answer is cited to the exact passage it came from.*

**Tech:** Django REST Framework, PostgreSQL + pgvector, Google Gemini, React (Vite)

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://paper-mind-sage.vercel.app) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Paper-Mind)

- Built a **retrieval-augmented generation (RAG) pipeline** — uploaded PDFs, Word docs, and text files are extracted, chunked, and embedded automatically
- Implemented **vector similarity search** using PostgreSQL + pgvector (Neon in production) for fast nearest-neighbour retrieval over document chunks
- Integrated **Google Gemini** for both embeddings (`gemini-embedding-001`) and answer generation (`gemini-2.5-flash`), with every answer **cited back to the exact source passage**
- Added **multi-turn conversations** — the system retains prior context so follow-up questions resolve correctly against the same document
- Secured the app with **JWT auth** so each user's documents and chats stay private by default

---

### 🛒 Blissful — Full-Stack E-commerce Storefront

*A full-stack skincare storefront with cart, checkout and live card payments.*

**Tech:** Node.js, Express, MongoDB (Mongoose), React, Safepay

[![Live Demo](https://img.shields.io/badge/Live_Demo-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](https://blissful-template.vercel.app/) [![Source Code](https://img.shields.io/badge/Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahmad-zaman123/Blissful-Template)

- Designed and built a **REST API** (Express + Mongoose) covering products, cart, orders, and payments
- Integrated **Safepay** card payments with **HMAC-verified webhooks** that update order status server-side with no client polling, plus a **Cash-on-Delivery fallback**
- Built a **session-based cart** so customers can check out without an account, with server-side search, category and skin-concern filters, price-range queries and real-time stock toggles

---

## 🛠 Tech Stack

### 🚀 Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=flat&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express.js-000000?style=flat&logo=express&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat&logo=celery&logoColor=white)

### ☁️ Cloud & Security
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Microsoft Graph](https://img.shields.io/badge/Microsoft_Graph-0078D4?style=flat&logo=microsoft&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat&logo=powershell&logoColor=white)
![HMAC](https://img.shields.io/badge/HMAC-Signing-444444?style=flat)

### 🤖 AI
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat&logo=googlegemini&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Pipelines-444444?style=flat)

### 🎨 Frontend
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

### 🗄 Databases & Caching
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![FalkorDB](https://img.shields.io/badge/FalkorDB-Graph_DB-B22222?style=flat)

### ⚙️ DevOps & Tools
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)

---

## 🌱 Currently Exploring

- Endpoint security tooling
- Identity and access security across cloud and SaaS platforms
- System design for scalable backend architectures
- Async processing, background workers, and AI-powered backends
