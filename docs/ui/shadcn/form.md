# Formsnap & Superforms  
Building forms with Formsnap, Superforms, & Zod.

Forms are tricky. They are one of the most common things you'll build in a web application, but also one of the most complex.

Well-designed HTML forms are:
- Well-structured and semantically correct.
- Easy to use and navigate (keyboard).
- Accessible with ARIA attributes and proper labels.
- Supported by client- and server-side validation.
- Well-styled and consistent with the rest of the application.

In this guide, we will take a look at building forms with **Formsnap**, **SvelteKit-Superforms**, and **Zod**.

---

## Features

The form components offered by `shadcn-svelte` are wrappers around **Formsnap** and **SvelteKit-Superforms** which provide a few benefits:

- Composable components for building forms.
- Form field components for scoping form state.
- Form validation using Zod or any other validation library supported by Superforms.
- Applies the correct ARIA attributes to form fields based on their states.
- Enables you to easily use components like `Select`, `RadioGroup`, `Switch`, `Checkbox`, and other form components with Formsnap.

If you're unfamiliar with **Superforms** & **Formsnap**, check out their documentation first, as this guide assumes you have a basic understanding of how they work together.

---

## Anatomy

```html
<form>
  <Form.Field>
    <Form.Control>
      <Form.Label />
      <!-- Any Form input component -->
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>
</form>
```

### Example

```html
<form method="POST" use:enhance>
  <Form.Field {form} name="email">
    <Form.Control let:attrs>
      <Form.Label>Email</Form.Label>
      <Input {...attrs} bind:value={$formData.email} />
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>
</form>
```

---

## Installation

```bash
npx shadcn-svelte@latest add form
```

Select package manager: `npm`

---

## Usage

### 1. Create a Form Schema

Define the shape of your form using a **Zod** schema. We’ll define it in a file called `schema.ts` in the same directory as our page component.

```ts
// src/routes/settings/schema.ts
import { z } from "zod";

export const formSchema = z.object({
  username: z.string().min(2).max(50),
});

export type FormSchema = typeof formSchema;
```

### 2. Return the Form from the Route's Load Function

```ts
// src/routes/settings/+page.server.ts
import type { PageServerLoad } from "./$types.js";
import { superValidate } from "sveltekit-superforms";
import { formSchema } from "./schema";
import { zod } from "sveltekit-superforms/adapters";

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema)),
  };
};
```

### 3. Create a Form Component

In this example, we'll pass the form returned from the load function as a prop to this component.

```svelte
<!-- src/routes/settings/settings-form.svelte -->
<script lang="ts">
  import * as Form from "$lib/components/ui/form";
  import { Input } from "$lib/components/ui/input";
  import { formSchema, type FormSchema } from "./schema";
  import {
    type SuperValidated,
    type Infer,
    superForm,
  } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";

  export let data: SuperValidated<Infer<FormSchema>>;

  const form = superForm(data, {
    validators: zodClient(formSchema),
  });

  const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
  <Form.Field {form} name="username">
    <Form.Control let:attrs>
      <Form.Label>Username</Form.Label>
      <Input {...attrs} bind:value={$formData.username} />
    </Form.Control>
    <Form.Description>This is your public display name.</Form.Description>
    <Form.FieldErrors />
  </Form.Field>
  <Form.Button>Submit</Form.Button>
</form>
```

The name, id, and all accessibility attributes are applied to the input by spreading the `attrs` object from the `Form.Control` component. The `Form.Label` will automatically associate with the input using the `for` attribute.

### 4. Create a Page Component

Pass the form data from the load function to the form component.

```svelte
<!-- src/routes/settings/+page.svelte -->
<script lang="ts">
  import type { PageData } from "./$types.js";
  import SettingsForm from "./settings-form.svelte";
  export let data: PageData;
</script>

<SettingsForm data={data.form} />
```

### 5. Create an Action to Handle Form Submission

```ts
// src/routes/settings/+page.server.ts
import type { PageServerLoad, Actions } from "./$types.js";
import { fail } from "@sveltejs/kit";
import { superValidate } from "sveltekit-superforms";
import { zod } from "sveltekit-superforms/adapters";
import { formSchema } from "./schema";

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema)),
  };
};

export const actions: Actions = {
  default: async (event) => {
    const form = await superValidate(event, zod(formSchema));
    if (!form.valid) {
      return fail(400, { form });
    }
    return { form };
  },
};
```

---

## Done

That's it! You now have a fully accessible form that is type-safe with client- and server-side validation.

### Example Form

```html
<form method="POST" use:enhance>
  <Form.Field {form} name="username">
    <Form.Control let:attrs>
      <Form.Label>Username</Form.Label>
      <Input {...attrs} bind:value={$formData.username} />
    </Form.Control>
    <Form.Description>This is your public display name.</Form.Description>
    <Form.FieldErrors />
  </Form.Field>
  <Form.Button>Submit</Form.Button>
</form>
```

---

## Next Steps

Be sure to check out the **Formsnap** and **Superforms** documentation for more information on how to use them effectively.