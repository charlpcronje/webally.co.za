# Sonner
An opinionated toast component for Svelte.
**Install:** `npx shadcn-svelte@latest add sonner`

```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button
 variant="outline"
 on:click={() =>
  toast.success("Event has been created", {
   description: "Sunday, December 03, 2023 at 9:00 AM",
   action: {
    label: "Undo",
    onClick: () => console.info("Undo")
   }
  })}
>
 Show Toast
</Button>
```

### Setup theme support
```svelte
By default, Sonner will use the user's system preferences to determine whether to show the light or dark theme. To get around this, you can either pass in a custom theme prop to the component, or simply use mode-watcher which you can hardcode to dark or light mode should you wish.

You can learn more about setting up Dark Mode support here.

If you wish to opt out of Dark Mode support, you can uninstall mode-watcher and remove the theme prop from the component after installing via CLI, or manually install the component and don't include mode-watcher
```

### Add the Toaster component:
Note: Make sure you are adding the import from the path "$lib/components/ui/sonner" not "svelte-sonner".

#### +layout.svelte`
```svelte
<script lang="ts">
 import { Toaster } from "$lib/components/ui/sonner";
</script>
 
<Toaster />
 
<slot />
```

### Usage
```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import { Button } from "$lib/components/ui/button";
</script>
 
<Button on:click={() => toast("Hello world")}>Show toast</Button>
```