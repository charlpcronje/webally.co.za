# Dropdown Menu
Displays a menu to the user — such as a set of actions or functions — triggered by a button.

```svelte
<script lang="ts">
 import CirclePlus from "lucide-svelte/icons/circle-plus";
 import Cloud from "lucide-svelte/icons/cloud";
 import CreditCard from "lucide-svelte/icons/credit-card";
 import Github from "lucide-svelte/icons/github";
 import Keyboard from "lucide-svelte/icons/keyboard";
 import LifeBuoy from "lucide-svelte/icons/life-buoy";
 import LogOut from "lucide-svelte/icons/log-out";
 import Mail from "lucide-svelte/icons/mail";
 import MessageSquare from "lucide-svelte/icons/message-square";
 import Plus from "lucide-svelte/icons/plus";
 import Settings from "lucide-svelte/icons/settings";
 import User from "lucide-svelte/icons/user";
 import UserPlus from "lucide-svelte/icons/user-plus";
 import Users from "lucide-svelte/icons/users";
 
 import { Button } from "$lib/components/ui/button/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button builders={[builder]} variant="outline">Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>My Account</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.Group>
   <DropdownMenu.Item>
    <User class="mr-2 h-4 w-4" />
    <span>Profile</span>
    <DropdownMenu.Shortcut>⇧⌘P</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <CreditCard class="mr-2 h-4 w-4" />
    <span>Billing</span>
    <DropdownMenu.Shortcut>⌘B</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <Settings class="mr-2 h-4 w-4" />
    <span>Settings</span>
    <DropdownMenu.Shortcut>⌘S</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <Keyboard class="mr-2 h-4 w-4" />
    <span>Keyboard shortcuts</span>
    <DropdownMenu.Shortcut>⌘K</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
  </DropdownMenu.Group>
  <DropdownMenu.Separator />
  <DropdownMenu.Group>
   <DropdownMenu.Item>
    <Users class="mr-2 h-4 w-4" />
    <span>Team</span>
   </DropdownMenu.Item>
   <DropdownMenu.Sub>
    <DropdownMenu.SubTrigger>
     <UserPlus class="mr-2 h-4 w-4" />
     <span>Invite users</span>
    </DropdownMenu.SubTrigger>
    <DropdownMenu.SubContent>
     <DropdownMenu.Item>
      <Mail class="mr-2 h-4 w-4" />
      <span>Email</span>
     </DropdownMenu.Item>
     <DropdownMenu.Item>
      <MessageSquare class="mr-2 h-4 w-4" />
      <span>Message</span>
     </DropdownMenu.Item>
     <DropdownMenu.Item>
      <CirclePlus class="mr-2 h-4 w-4" />
      <span>More...</span>
     </DropdownMenu.Item>
    </DropdownMenu.SubContent>
   </DropdownMenu.Sub>
   <DropdownMenu.Item>
    <Plus class="mr-2 h-4 w-4" />
    <span>New Team</span>
    <DropdownMenu.Shortcut>⌘+T</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
  </DropdownMenu.Group>
  <DropdownMenu.Separator />
  <DropdownMenu.Item>
   <Github class="mr-2 h-4 w-4" />
   <span>GitHub</span>
  </DropdownMenu.Item>
  <DropdownMenu.Item>
   <LifeBuoy class="mr-2 h-4 w-4" />
   <span>Support</span>
  </DropdownMenu.Item>
  <DropdownMenu.Item>
   <Cloud class="mr-2 h-4 w-4" />
   <span>API</span>
  </DropdownMenu.Item>
  <DropdownMenu.Separator />
  <DropdownMenu.Item>
   <LogOut class="mr-2 h-4 w-4" />
   <span>Log out</span>
   <DropdownMenu.Shortcut>⇧⌘Q</DropdownMenu.Shortcut>
  </DropdownMenu.Item>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

**Install:** `npx shadcn-svelte@latest add dropdown-menu`

## Usage
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger>Open</DropdownMenu.Trigger>
 <DropdownMenu.Content>
  <DropdownMenu.Group>
   <DropdownMenu.Label>My Account</DropdownMenu.Label>
   <DropdownMenu.Separator />
   <DropdownMenu.Item>Profile</DropdownMenu.Item>
   <DropdownMenu.Item>Billing</DropdownMenu.Item>
   <DropdownMenu.Item>Team</DropdownMenu.Item>
   <DropdownMenu.Item>Subscription</DropdownMenu.Item>
  </DropdownMenu.Group>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

### Checkboxes
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 
 let showStatusBar = true;
 let showActivityBar = false;
 let showPanel = false;
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button variant="outline" builders={[builder]}>Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>Appearance</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.CheckboxItem bind:checked={showStatusBar}>
   Status Bar
  </DropdownMenu.CheckboxItem>
  <DropdownMenu.CheckboxItem bind:checked={showActivityBar} disabled>
   Activity Bar
  </DropdownMenu.CheckboxItem>
  <DropdownMenu.CheckboxItem bind:checked={showPanel}
   >Panel</DropdownMenu.CheckboxItem
  >
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

### Radio Group
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 
 let position = "bottom";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button variant="outline" builders={[builder]}>Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>Panel Position</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.RadioGroup bind:value={position}>
   <DropdownMenu.RadioItem value="top">Top</DropdownMenu.RadioItem>
   <DropdownMenu.RadioItem value="bottom">Bottom</DropdownMenu.RadioItem>
   <DropdownMenu.RadioItem value="right">Right</DropdownMenu.RadioItem>
  </DropdownMenu.RadioGroup>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```