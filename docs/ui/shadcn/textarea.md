# Textarea
Displays a form textarea or a component that looks like a textarea.
Install: `npx shadcn-svelte@latest add textarea`

```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea placeholder="Type your message here." />
```

## Usage
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea";
</script>
```
```svelte
<Textarea />
```

## Examples
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea placeholder="Type your message here." />
```

### Disabled
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea disabled placeholder="Type your message here." />
```

### With Label
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-1.5">
 <Label for="message">Your message</Label>
 <Textarea placeholder="Type your message here." id="message" />
</div>
```

### With Text
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-1.5">
 <Label for="message-2">Your Message</Label>
 <Textarea placeholder="Type your message here." id="message-2" />
 <p class="text-muted-foreground text-sm">
  Your message will be copied to the support team.
 </p>
</div>
```

### With Button
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-2">
 <Textarea placeholder="Type your message here." />
 <Button>Send message</Button>
</div>
```

### Form`
``svelte
<script lang="ts" context="module">
 import { z } from "zod";
 export const formSchema = z.object({
  bio: z
   .string()
   .min(10, "Bio must be at least 10 characters.")
   .max(160, "Bio must be at most 160 characters.")
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.textarea;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
</script>
 
<form method="POST" action="/?/textarea" class="w-2/3 space-y-6" use:enhance>
 <Form.Field {form} name="bio">
  <Form.Control let:attrs>
   <Form.Label>Bio</Form.Label>
   <Textarea
    {...attrs}
    placeholder="Tell us a little bit about yourself"
    class="resize-none"
    bind:value={$formData.bio}
   />
   <Form.Description>
    You can <span>@mention</span> other users and organizations.
   </Form.Description>
  </Form.Control>
  <Form.FieldErrors />
 </Form.Field>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```

 
<Textarea placeholder="Type your message here." />