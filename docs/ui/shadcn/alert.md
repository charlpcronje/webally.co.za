# Alert
Displays a callout for user attention.
**Install:** `npx shadcn-svelte@latest add alert`

```svelte
<script lang="ts">
  import Terminal from "lucide-svelte/icons/terminal";
  import * as Alert from "$lib/components/ui/alert/index.js";
</script>
 
<Alert.Root>
  <Terminal class="h-4 w-4" />
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description
    >You can add components to your app using the cli.</Alert.Description
  >
</Alert.Root>
```

## Usage
```svelte
<script lang="ts">
 import * as Alert from "$lib/components/ui/alert";
</script>
 
<Alert.Root>
 <Alert.Title>Heads up!</Alert.Title>
 <Alert.Description>
  You can add components to your app using the cli.
 </Alert.Description>
</Alert.Root>
```

## Examples

### Default 
```svelte
<script lang="ts">
 import Terminal from "lucide-svelte/icons/terminal";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
 
<Alert.Root>
 <Terminal class="h-4 w-4" />
 <Alert.Title>Heads up!</Alert.Title>
 <Alert.Description
  >You can add components to your app using the cli.</Alert.Description
 >
</Alert.Root>
```

### Destructive
```svelte
<script lang="ts">
 import CircleAlert from "lucide-svelte/icons/circle-alert";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
 
<Alert.Root variant="destructive">
 <CircleAlert class="h-4 w-4" />
 <Alert.Title>Error</Alert.Title>
 <Alert.Description
  >Your session has expired. Please login again.</Alert.Description
 >
</Alert.Root>
```