### Button
Install: `npx  shadcn-svelte@latest add button`

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button";
</script>
 
<Button>Click me</Button>
```

### Link
You can convert the <button> into an <a> element by simply passing an href as a prop.`
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button";
</script>
 
<Button href="/dashboard">Dashboard</Button>
```

Alternatively, you can use the buttonVariants helper to create a link that looks like a button.
```svelte
<script lang="ts">
 import { buttonVariants } from "$lib/components/ui/button";
</script>
 
<a href="/dashboard" class={buttonVariants({ variant: "outline" })}>
 Dashboard
</a>
```

## Examples

### Primary
```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button>Button</Button>
```

### Secondary
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="secondary">Secondary</Button>
```

### Destructive
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="destructive">Destructive</Button>
```

### Outline
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="outline">Outline</Button>
```

### Ghost
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="ghost">Ghost</Button>
```

### Link
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="link">Link</Button>
```

### With Icon
```svelte
<script lang="ts">
 import Mail from "lucide-svelte/icons/mail";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button>
 <Mail class="mr-2 h-4 w-4" />
 Login with Email
</Button>
```

### Icon
```svelte
<script lang="ts">
 import ChevronRight from "lucide-svelte/icons/chevron-right";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button variant="outline" size="icon">
 <ChevronRight class="h-4 w-4" />
</Button>
```

### Loading
```svelte
<script lang="ts">
 import LoaderCircle from "lucide-svelte/icons/loader-circle";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button disabled>
 <LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
 Please wait
</Button>
```