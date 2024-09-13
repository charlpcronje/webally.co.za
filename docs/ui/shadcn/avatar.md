# Avatar
An image element with a fallback for representing the user.
Install: npx shadcn-svelte@latest add avatar

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
 
<Avatar.Root>
 <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
 <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```
