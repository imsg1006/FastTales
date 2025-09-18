FastTales

FastTales is an interactive story generator where users can create, explore, and experience immersive stories. The app features a smooth UI built with React + Vite and a backend powered by Python and FASTAPI, delivering real-time storytelling with a unique Mystic Night color scheme.It is a multiple level story game based on the input by the user.

✨ Features

🎭 Interactive Story Generator – Generate dynamic stories with AI.

⚡ Modern Frontend – Built with React, TailwindCSS, ShadCN UI, and Vite for speed.

🔧 Backend with Python and FASTAPI – Scalable APIs for story logic.

🖊 Typewriter Text Effects – Smooth animated text rendering.


🛠️ Tech Stack

Frontend

React + Vite

TailwindCSS

ShadCN UI

Aceternity Typewriter Effect

Backend

Python
FASTAPI

Tools

Git & GitHub for version control

VS Code  

🚀 Getting Started
1️⃣ Clone the repo
git clone https://github.com/your-username/FastTales.git
cd FastTales

2️⃣ Setup frontend (React + Vite)
cd frontend
npm install
npm run dev

3️⃣ Setup backend (FASTAPI)
cd backend
uv run uvicorn main:app --reload

4️⃣ Add Gemini API Key
Create a .env file inside the backend directory and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here


🎨 Theme System

FastTales comes with a color scheme inspired by Mystic Night:

Blue (#3B82F6)

Purple (#9333EA)

Neon Pink (#EC4899)

Usage in Tailwind for gradient text:

<span class="bg-gradient-to-r from-[#3B82F6] via-[#9333EA] to-[#EC4899] bg-clip-text text-transparent">
  FastTales
</span>

📸 Screenshots (Optional)


Add screenshots of your landing page, story generator, and theme input boxes here.

🤝 Contributing

Fork the repo

Create a feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Added feature")

Push to branch (git push origin feature-name)

Open a Pull Request

📜 License

This project is licensed under the MIT License – free to use and modify.
