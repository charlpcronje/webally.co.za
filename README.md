# webAlly Project

## Overview

webAlly is a comprehensive website showcasing the services, portfolio, tools, and research of a full-stack web development company. Built with modern web technologies, it offers an interactive and responsive user experience.

## Tech Stack 

- [SvelteKit](https://kit.svelte.dev) - App framework
- [Tailwind CSS](https://tailwindcss.com) - Utility-first CSS framework
- [Shadcn UI](https://ui.shadcn.com/) - UI component library
- [Prisma ORM](https://www.prisma.io) - Database toolkit
- [Marked](https://marked.js.org/) - Markdown parser and compiler
- Node.js - For executing Python scripts
- [Flat Icons](https://www.flaticon.com) - Icon set

## Documentation
- **Development Docs**
  - [Index](./docs/README.md)

- **Tech Stack**
  - [Considerations](./docs/stack/considerations.md)
  - [More information](./docs/stack/moreInfo.md)
  - [Installation](./docs/stack/install.md)
  - [AI Assistance Prompts](./docs/ai/prompts.md)


## Project Structure

```sh
webAlly/
├── src/
│   ├── components/
│   │   ├── Header.svelte
│   │   ├── Footer.svelte
│   │   ├── HeroSlider.svelte
│   │   ├── FeaturePanel.svelte
│   │   ├── SplitContent.svelte
│   │   ├── BenefitCard.svelte
│   │   ├── ServiceCard.svelte
│   │   ├── SkillLevelIndicator.svelte
│   │   ├── PortfolioItem.svelte
│   │   ├── PortfolioFilter.svelte
│   │   ├── ToolCard.svelte
│   │   ├── ToolExecutor.svelte
│   │   ├── ResearchArticle.svelte
│   │   ├── SearchBar.svelte
│   │   ├── TagCloud.svelte
│   │   ├── ContactForm.svelte
│   │   ├── ContactInfo.svelte
│   │   └── Map.svelte
│   ├── routes/
│   │   ├── +layout.svelte
│   │   ├── +page.svelte
│   │   ├── services/
│   │   │   └── +page.svelte
│   │   ├── portfolio/
│   │   │   └── +page.svelte
│   │   ├── tools/
│   │   │   └── +page.svelte
│   │   ├── research/
│   │   │   └── +page.svelte
│   │   └── contact/
│   │       └── +page.svelte
│   ├── lib/
│   │   └── utils.ts
│   └── styles/
│       └── global.css
├── static/
├── prisma/
│   └── schema.prisma
├── package.json
├── svelte.config.js
├── tailwind.config.cjs
└── README.md
```

## Setup and Installation

1. Clone the repository:
```sh
git clone git@github.com:charlpcronje/webally.co.za.git
cd webally.co.za
```

2. Install dependencies:
```sh
npm install
```

3. Set up environment variables:
   Create a `.env` file in the root directory and add necessary environment variables.

4. Set up the database:
```sh
npx prisma migrate dev
```

5. Run the development server:
```sh
npm run dev
```

6. Open your browser and navigate to `http://localhost:5173` to view the application.

## Available Scripts

- `npm run dev` - Starts the development server
- `npm run build` - Builds the app for production
- `npm run preview` - Previews the built app
- `npm run lint` - Runs the linter
- `npm run format` - Formats the code using Prettier

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

Charl Cronje - charl@webally.co.za

Project Link: [https://github.com/charlpcronje/webally.co.za](https://github.com/charlpcronje/webally.co.za)