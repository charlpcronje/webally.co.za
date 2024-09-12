# Tech Stack Installation

Here is a comprehensive guide for setting up a SvelteKit project with Shadcn UI, Tailwind CSS, a flat icon set, a MySQL ORM, executing Python scripts, and rendering Markdown content with additional features:

I created an automated installer that should work of all the Prerequisites are installed
- [Automated Install Script](./installScript.md)

## Prerequisites

- Node.js (v14 or higher)
- npm or pnpm package manager

## 1. **Create a New SvelteKit Project**

```bash
npm create svelte@latest my-app
cd my-app
npm install
```

During project creation, select the following options:

- **Add TypeScript support?** Yes
- **Add ESLint for code linting?** No
- **Add Prettier for code formatting?** Yes
- **Add Playwright for browser testing?** No

## 2. **Install Required Dependencies**

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```bash
npm install @shadcn/ui
```

```bash
npm install -D vite-plugin-svelte-icons
```

```bash
npm install prisma --save-dev
npx prisma init
```

```bash
npm install @prisma/client
```

## 3. **Configure SvelteKit**

In `svelte.config.js`, add the Shadcn UI and Svelte Icons plugins:

```js
import { vitePreprocess } from '@sveltejs/kit/vite';
import { svelteIconsPreprocess } from 'vite-plugin-svelte-icons/preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    alias: {
      $src: 'src',
      $lib: 'src/lib',
      $components: 'src/lib/components',
      $utils: 'src/lib/utils',
      $styles: 'src/lib/styles'
    }
  },
  preprocess: [
    vitePreprocess(),
    svelteIconsPreprocess()
  ]
};
```

## 4. **Set Up Tailwind CSS**

In `tailwind.config.cjs`, add the following content:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: []
};
```

In `src/app.css`, add the Tailwind directives:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Import the CSS file in `src/routes/+layout.svelte`:

```html
<script>
  import '../app.css';
</script>

<slot />
```

## 5. **Integrate Shadcn UI**

In `src/routes/+layout.svelte`, import the Shadcn UI styles:

```html
<script>
  import '@shadcn/ui/styles.css';
</script>

<slot />
```

## 6. **Set Up Prisma ORM**

In `prisma/schema.prisma`, define your MySQL database schema.

Run the following command to generate the Prisma client:

```bash
npx prisma generate
```

## 7. **Execute Python Scripts**

Create a Python script, e.g., `src/lib/utils/python_script.py`, and define your functionality.

In your SvelteKit component, use the `child_process` module to execute the Python script and retrieve the output:

```js
import { spawn } from 'child_process';

const pythonScript = async () => {
  const python = spawn('python3', ['src/lib/utils/python_script.py']);

  let data = '';

  for await (const chunk of python.stdout) {
    data += chunk.toString();
  }

  await new Promise((resolve) => {
    python.on('close', resolve);
  });

  return data.trim();
};
```

## 8. **Render Markdown Content**

Install the `marked` library:

```bash
npm install marked
```

Create a Markdown file, e.g., `src/lib/content/example.md`.

In your SvelteKit component, read the Markdown file and render it using `marked`:

```js
import { marked } from 'marked';
import exampleMarkdown from '$lib/content/example.md';

const html = marked.parse(exampleMarkdown);
```

```html
<div class="prose" set:html={html}></div>
```

## 9. **Additional Features**

- **Accordions**: Use the `Accordion` component from Shadcn UI.
- **Tabs**: Use the `Tabs` component from Shadcn UI.
- **Icons**: Use the `Icon` component from `vite-plugin-svelte-icons` and import your desired icon set.

## 10. **Start the Development Server**

```bash
npm run dev
```

Your SvelteKit application is now set up with Shadcn UI, Tailwind CSS, a flat icon set, a MySQL ORM, Python script execution, and Markdown content rendering with additional features like accordions and tabs.

## Citations:
[1] https://cloudcannon.com/tutorials/sveltekit-beginner-tutorial/
[2] https://kit.svelte.dev/docs/introduction
[3] https://tailwindcss.com/docs/guides/sveltekit
[4] https://www.sitepoint.com/a-beginners-guide-to-sveltekit/
[5] https://kit.svelte.dev/docs/creating-a-project
[6] https://gist.github.com/OllieJT/54aaaec97c0e77be0a755f8d9f8cc2d8
[7] https://kit.svelte.dev
[8] https://blog.logrocket.com/exploring-astro-svelte-vs-sveltekit/