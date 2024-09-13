## Checkbox
A control that allows the user to toggle between checked and not checked.
Install: `npx shadcn-svelte@latest add checkbox`

```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 let checked = false;
</script>
 
<div class="flex items-center space-x-2">
 <Checkbox id="terms" bind:checked aria-labelledby="terms-label" />
 <Label
  id="terms-label"
  for="terms"
  class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
 >
  Accept terms and conditions
 </Label>
</div>
```

#### Usage
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox";
</script>
```
```svelte
<Checkbox />
```

#### Examples
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<div class="items-top flex space-x-2">
 <Checkbox id="terms1" />
 <div class="grid gap-1.5 leading-none">
  <Label
   for="terms1"
   class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
  >
   Accept terms and conditions
  </Label>
  <p class="text-muted-foreground text-sm">
   You agree to our Terms of Service and Privacy Policy.
  </p>
 </div>
</div>
```

#### Disabled
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<div class="flex items-center space-x-2">
 <Checkbox id="terms" disabled />
 <Label
  for="terms2"
  class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 peer-data-[disabled=true]:cursor-not-allowed peer-data-[disabled=true]:opacity-70"
 >
  Accept terms and conditions
 </Label>
</div>
```

#### Form
```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 export const formSchema = z.object({
  mobile: z.boolean().default(false)
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
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 let data: SuperValidated<Infer<FormSchema>> = $page.data.checkboxSingle;
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
 
<form action="/?/checkboxSingle" method="POST" class="space-y-6" use:enhance>
 <Form.Field
  {form}
  name="mobile"
  class="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4"
 >
  <Form.Control let:attrs>
   <Checkbox {...attrs} bind:checked={$formData.mobile} />
   <div class="space-y-1 leading-none">
    <Form.Label>Use different settings for my mobile devices</Form.Label>
    <Form.Description>
     You can manage your mobile notifications in the <a
      href="/examples/forms">mobile settings</a
     > page.
    </Form.Description>
   </div>
   <input name={attrs.name} value={$formData.mobile} hidden />
  </Form.Control>
 </Form.Field>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```

```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 
 const items = [
  {
   id: "recents",
   label: "Recents"
  },
  {
   id: "home",
   label: "Home"
  },
  {
   id: "applications",
   label: "Applications"
  },
  {
   id: "desktop",
   label: "Desktop"
  },
  {
   id: "downloads",
   label: "Downloads"
  },
  {
   id: "documents",
   label: "Documents"
  }
 ] as const;
 
 export const formSchema = z.object({
  items: z.array(z.string()).refine((value) => value.some((item) => item), {
   message: "You have to select at least one item."
  })
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
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.checkboxMultiple;
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
 
 function addItem(id: string) {
  $formData.items = [...$formData.items, id];
 }
 
 function removeItem(id: string) {
  $formData.items = $formData.items.filter((i) => i !== id);
 }
</script>
 
<form action="/?/checkboxMultiple" method="POST" class="space-y-8" use:enhance>
 <Form.Fieldset {form} name="items" class="space-y-0">
  <div class="mb-4">
   <Form.Legend class="text-base">Sidebar</Form.Legend>
   <Form.Description>
    Select the items you want to display in the sidebar.
   </Form.Description>
  </div>
  <div class="space-y-2">
   {#each items as item}
    {@const checked = $formData.items.includes(item.id)}
    <div class="flex flex-row items-start space-x-3">
     <Form.Control let:attrs>
      <Checkbox
       {...attrs}
       {checked}
       onCheckedChange={(v) => {
        if (v) {
         addItem(item.id);
        } else {
         removeItem(item.id);
        }
       }}
      />
      <Form.Label class="font-normal">
       {item.label}
      </Form.Label>
      <input
       hidden
       type="checkbox"
       name={attrs.name}
       value={item.id}
       {checked}
      />
     </Form.Control>
    </div>
   {/each}
   <Form.FieldErrors />
  </div>
 </Form.Fieldset>
 <Form.Button>Update display</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```