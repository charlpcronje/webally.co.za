# Radio Group
A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

**Install:** `npx shadcn-svelte@latest add radio-group`

## Preview
```svelte
<script lang="ts">
 import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<RadioGroup.Root value="comfortable">
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="default" id="r1" />
  <Label for="r1">Default</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="comfortable" id="r2" />
  <Label for="r2">Comfortable</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="compact" id="r3" />
  <Label for="r3">Compact</Label>
 </div>
 <RadioGroup.Input name="spacing" />
</RadioGroup.Root>
```

## Usage
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label";
 import * as RadioGroup from "$lib/components/ui/radio-group";
</script>
 
<RadioGroup.Root value="option-one">
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="option-one" id="option-one" />
  <Label for="option-one">Option One</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="option-two" id="option-two" />
  <Label for="option-two">Option Two</Label>
 </div>
</RadioGroup.Root>
```

## Examples
```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 
 export const formSchema = z.object({
  type: z.enum(["all", "mentions", "none"], {
   required_error: "You need to select a notification type"
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
 import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.radioGroup;
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
 
<form method="POST" action="/?/radioGroup" class="w-2/3 space-y-6" use:enhance>
 <Form.Fieldset {form} name="type" class="space-y-3">
  <Form.Legend>Notify me about...</Form.Legend>
  <RadioGroup.Root
   bind:value={$formData.type}
   class="flex flex-col space-y-1"
  >
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="all" {...attrs} />
     <Form.Label class="font-normal">All new messages</Form.Label>
    </Form.Control>
   </div>
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="mentions" {...attrs} />
     <Form.Label class="font-normal"
      >Direction messages and mentions</Form.Label
     >
    </Form.Control>
   </div>
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="none" {...attrs} />
     <Form.Label class="font-normal">Nothing</Form.Label>
    </Form.Control>
   </div>
   <RadioGroup.Input name="type" />
  </RadioGroup.Root>
  <Form.FieldErrors />
 </Form.Fieldset>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```
