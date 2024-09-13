# Card
Displays a card with header, content, and footer.

Install: `npx shadcn-svelte@latest add card`
```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card";
</script>
 
<Card.Root>
 <Card.Header>
  <Card.Title>Card Title</Card.Title>
  <Card.Description>Card Description</Card.Description>
 </Card.Header>
 <Card.Content>
  <p>Card Content</p>
 </Card.Content>
 <Card.Footer>
  <p>Card Footer</p>
 </Card.Footer>
</Card.Root>
```

- Modify the heading level
By default, the `<Card.Title>` component renders an `<h3>` element. You can change this by passing a tag prop to the component.

- For example:
```svelte
<Card.Title tag="h1">This will render an H1</Card.Title>
```
...
```svelte
<Card.Title tag="h6">This will render an H6</Card.Title>
```
#### Examples
```svelte
<script lang="ts">
 import BellRing from "lucide-svelte/icons/bell-ring";
 import Check from "lucide-svelte/icons/check";
 import { Button } from "$lib/components/ui/button/index.js";
 import * as Card from "$lib/components/ui/card/index.js";
 import { Switch } from "$lib/components/ui/switch/index.js";
 
 const notifications = [
  {
   title: "Your call has been confirmed.",
   description: "1 hour ago"
  },
  {
   title: "You have a new message!",
   description: "1 hour ago"
  },
  {
   title: "Your subscription is expiring soon!",
   description: "2 hours ago"
  }
 ];
</script>
 
<Card.Root class="w-[380px]">
 <Card.Header>
  <Card.Title>Notifications</Card.Title>
  <Card.Description>You have 3 unread messages.</Card.Description>
 </Card.Header>
 <Card.Content class="grid gap-4">
  <div class=" flex items-center space-x-4 rounded-md border p-4">
   <BellRing />
   <div class="flex-1 space-y-1">
    <p class="text-sm font-medium leading-none">Push Notifications</p>
    <p class="text-muted-foreground text-sm">
     Send notifications to device.
    </p>
   </div>
   <Switch />
  </div>
  <div>
   {#each notifications as notification, idx (idx)}
    <div
     class="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
    >
     <span class="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
     <div class="space-y-1">
      <p class="text-sm font-medium leading-none">
       {notification.title}
      </p>
      <p class="text-muted-foreground text-sm">
       {notification.description}
      </p>
     </div>
    </div>
   {/each}
  </div>
 </Card.Content>
 <Card.Footer>
  <Button class="w-full">
   <Check class="mr-2 h-4 w-4" /> Mark all as read
  </Button>
 </Card.Footer>
</Card.Root>
```