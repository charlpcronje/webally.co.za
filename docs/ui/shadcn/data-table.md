# Data Table
Powerful table and data grids built using Svelte Headless Table.
Install: `npx shadcn-svelte@latest add data-table`

```svelte
<script lang="ts">
 import {
  Render,
  Subscribe,
  createRender,
  createTable
 } from "svelte-headless-table";
 import {
  addHiddenColumns,
  addPagination,
  addSelectedRows,
  addSortBy,
  addTableFilter
 } from "svelte-headless-table/plugins";
 import { readable } from "svelte/store";
 import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
 import ChevronDown from "lucide-svelte/icons/chevron-down";
 import Actions from "./data-table/data-table-actions.svelte";
 import DataTableCheckbox from "./data-table/data-table-checkbox.svelte";
 import * as Table from "$lib/components/ui/table/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { cn } from "$lib/utils.js";
 import { Input } from "$lib/components/ui/input/index.js";
 
 type Payment = {
  id: string;
  amount: number;
  status: "Pending" | "Processing" | "Success" | "Failed";
  email: string;
 };
 
 const data: Payment[] = [
  {
   id: "m5gr84i9",
   amount: 316,
   status: "Success",
   email: "ken99@yahoo.com"
  },
  {
   id: "3u1reuv4",
   amount: 242,
   status: "Success",
   email: "Abe45@gmail.com"
  },
  {
   id: "derv1ws0",
   amount: 837,
   status: "Processing",
   email: "Monserrat44@gmail.com"
  },
  {
   id: "5kma53ae",
   amount: 874,
   status: "Success",
   email: "Silas22@gmail.com"
  },
  {
   id: "bhqecj4p",
   amount: 721,
   status: "Failed",
   email: "carmella@hotmail.com"
  }
 ];
 
 const table = createTable(readable(data), {
  sort: addSortBy({ disableMultiSort: true }),
  page: addPagination(),
  filter: addTableFilter({
   fn: ({ filterValue, value }) => value.includes(filterValue)
  }),
  select: addSelectedRows(),
  hide: addHiddenColumns()
 });
 
 const columns = table.createColumns([
  table.column({
   header: (_, { pluginStates }) => {
    const { allPageRowsSelected } = pluginStates.select;
    return createRender(DataTableCheckbox, {
     checked: allPageRowsSelected
    });
   },
   accessor: "id",
   cell: ({ row }, { pluginStates }) => {
    const { getRowState } = pluginStates.select;
    const { isSelected } = getRowState(row);
 
    return createRender(DataTableCheckbox, {
     checked: isSelected
    });
   },
   plugins: {
    sort: {
     disable: true
    },
    filter: {
     exclude: true
    }
   }
  }),
  table.column({
   header: "Status",
   accessor: "status",
   plugins: { sort: { disable: true }, filter: { exclude: true } }
  }),
  table.column({
   header: "Email",
   accessor: "email",
   cell: ({ value }) => value.toLowerCase(),
   plugins: {
    filter: {
     getFilterValue(value) {
      return value.toLowerCase();
     }
    }
   }
  }),
  table.column({
   header: "Amount",
   accessor: "amount",
   cell: ({ value }) => {
    const formatted = new Intl.NumberFormat("en-US", {
     style: "currency",
     currency: "USD"
    }).format(value);
    return formatted;
   },
   plugins: {
    sort: {
     disable: true
    },
    filter: {
     exclude: true
    }
   }
  }),
  table.column({
   header: "",
   accessor: ({ id }) => id,
   cell: (item) => {
    return createRender(Actions, { id: item.value });
   },
   plugins: {
    sort: {
     disable: true
    }
   }
  })
 ]);
 
 const {
  headerRows,
  pageRows,
  tableAttrs,
  tableBodyAttrs,
  flatColumns,
  pluginStates,
  rows
 } = table.createViewModel(columns);
 
 const { sortKeys } = pluginStates.sort;
 
 const { hiddenColumnIds } = pluginStates.hide;
 const ids = flatColumns.map((c) => c.id);
 let hideForId = Object.fromEntries(ids.map((id) => [id, true]));
 
 $: $hiddenColumnIds = Object.entries(hideForId)
  .filter(([, hide]) => !hide)
  .map(([id]) => id);
 
 const { hasNextPage, hasPreviousPage, pageIndex } = pluginStates.page;
 const { filterValue } = pluginStates.filter;
 
 const { selectedDataIds } = pluginStates.select;
 
 const hideableCols = ["status", "email", "amount"];
</script>
 
<div class="w-full">
 <div class="flex items-center py-4">
  <Input
   class="max-w-sm"
   placeholder="Filter emails..."
   type="text"
   bind:value={$filterValue}
  />
  <DropdownMenu.Root>
   <DropdownMenu.Trigger asChild let:builder>
    <Button variant="outline" class="ml-auto" builders={[builder]}>
     Columns <ChevronDown class="ml-2 h-4 w-4" />
    </Button>
   </DropdownMenu.Trigger>
   <DropdownMenu.Content>
    {#each flatColumns as col}
     {#if hideableCols.includes(col.id)}
      <DropdownMenu.CheckboxItem bind:checked={hideForId[col.id]}>
       {col.header}
      </DropdownMenu.CheckboxItem>
     {/if}
    {/each}
   </DropdownMenu.Content>
  </DropdownMenu.Root>
 </div>
 <div class="rounded-md border">
  <Table.Root {...$tableAttrs}>
   <Table.Header>
    {#each $headerRows as headerRow}
     <Subscribe rowAttrs={headerRow.attrs()}>
      <Table.Row>
       {#each headerRow.cells as cell (cell.id)}
        <Subscribe
         attrs={cell.attrs()}
         let:attrs
         props={cell.props()}
         let:props
        >
         <Table.Head
          {...attrs}
          class={cn("[&:has([role=checkbox])]:pl-3")}
         >
          {#if cell.id === "amount"}
           <div class="text-right font-medium">
            <Render of={cell.render()} />
           </div>
          {:else if cell.id === "email"}
           <Button variant="ghost" on:click={props.sort.toggle}>
            <Render of={cell.render()} />
            <ArrowUpDown
             class={cn(
              $sortKeys[0]?.id === cell.id && "text-foreground",
              "ml-2 h-4 w-4"
             )}
            />
           </Button>
          {:else}
           <Render of={cell.render()} />
          {/if}
         </Table.Head>
        </Subscribe>
       {/each}
      </Table.Row>
     </Subscribe>
    {/each}
   </Table.Header>
   <Table.Body {...$tableBodyAttrs}>
    {#each $pageRows as row (row.id)}
     <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
      <Table.Row
       {...rowAttrs}
       data-state={$selectedDataIds[row.id] && "selected"}
      >
       {#each row.cells as cell (cell.id)}
        <Subscribe attrs={cell.attrs()} let:attrs>
         <Table.Cell class="[&:has([role=checkbox])]:pl-3" {...attrs}>
          {#if cell.id === "amount"}
           <div class="text-right font-medium">
            <Render of={cell.render()} />
           </div>
          {:else if cell.id === "status"}
           <div class="capitalize">
            <Render of={cell.render()} />
           </div>
          {:else}
           <Render of={cell.render()} />
          {/if}
         </Table.Cell>
        </Subscribe>
       {/each}
      </Table.Row>
     </Subscribe>
    {/each}
   </Table.Body>
  </Table.Root>
 </div>
 <div class="flex items-center justify-end space-x-2 py-4">
  <div class="text-muted-foreground flex-1 text-sm">
   {Object.keys($selectedDataIds).length} of {$rows.length} row(s) selected.
  </div>
  <Button
   variant="outline"
   size="sm"
   on:click={() => ($pageIndex = $pageIndex - 1)}
   disabled={!$hasPreviousPage}>Previous</Button
  >
  <Button
   variant="outline"
   size="sm"
   disabled={!$hasNextPage}
   on:click={() => ($pageIndex = $pageIndex + 1)}>Next</Button
  >
 </div>
</div>
```

### Introduction
Data tables are difficult to componentize because of the wide variety of features they support, and the uniqueness of every data set.

So instead of trying to create a one-size-fits-all solution, we've created a guide to help you build your own data tables.

We'll start with the basic `<Table />` component, and work our way up to a fully-featured data table.

>> Tip: If you find yourself using the same table in multiple places, you can always extract it into a reusable component.


### Table of Contents
This guide will show you how to use Svelte Headless Table and the <Table /> component to build your own custom data table. We'll cover the following topics:

- Basic Table
- Row Actions
- Pagination
- Sorting
- Filtering
- Visibility
- Row Selection
- Reusable Components

### Installation
Add the <Table /> component to your project:
```sh
npx  shadcn-svelte@latest add table
```

Add svelte-headless-table as a dependency:
```sh
npm install  svelte-headless-table
```

#### Prerequisites
We're going to build a table to show recent payments. Here's what our data looks like:

```ts
type Payment = {
  id: string;
  amount: number;
  status: "pending" | "processing" | "success" | "failed";
  email: string;
};
 
export const data: Payment[] = [
  {
    id: "728ed52f",
    amount: 100,
    status: "pending",
    email: "m@example.com",
  },
  {
    id: "489e1d42",
    amount: 125,
    status: "processing",
    email: "example@gmail.com",
  },
  // ...
];
```

### Project Structure
Start by creating a route where your data table will live (we'll call ours payments), along with the following files:

```sh
routes
└── payments
    ├── data-table.svelte
    ├── data-table-actions.svelte
    ├── data-table-checkbox.svelte
    └── +page.svelte
```

- **data-table.svelte** will contain the `<Table />` component all of our data table logic.
- **data-table-actions.svelte** will contain the actions menu for each row.
- **data-table-checkbox.svelte** will contain the checkbox for each row.
- **+page.svelte** is where we'll render and access `<DataTable />` component.

### Basic Table
Let's start by building a basic table.

#### Get/Add Data
Before we can initialize a table, we need to get our data. You can retrieve your data from anywhere, but for this example we'll use a `payments` array.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
</script>
```

#### Initialize Table
Next, we'll initialize a new table using svelte-headless-table.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  import { createTable } from "svelte-headless-table";
  import { readable } from "svelte/store";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data));
</script>
```

#### Create Columns
Now that we have a table, we can define our columns.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  import { createTable } from "svelte-headless-table";
  import { readable } from "svelte/store";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data));
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
    }),
    table.column({
      accessor: "status",
      header: "Status",
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
    }),
  ]);
</script>
```

The last column is where we'll render a menu of actions for each row.

#### Create View Model & Render Table
Finally, we'll create a view model which we'll use to build our table.

- routes/payments/data-table.svelte

```svelte
<script lang="ts">
  import { createTable, Render, Subscribe } from "svelte-headless-table";
  import { readable } from "svelte/store";
  import * as Table from "$lib/components/ui/table";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data));
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
    }),
    table.column({
      accessor: "status",
      header: "Status",
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
    }),
  ]);
 
  const { headerRows, pageRows, tableAttrs, tableBodyAttrs } =
    table.createViewModel(columns);
</script>
 
<div class="rounded-md border">
  <Table.Root {...$tableAttrs}>
    <Table.Header>
      {#each $headerRows as headerRow}
        <Subscribe rowAttrs={headerRow.attrs()}>
          <Table.Row>
            {#each headerRow.cells as cell (cell.id)}
              <Subscribe attrs={cell.attrs()} let:attrs props={cell.props()}>
                <Table.Head {...attrs}>
                  <Render of={cell.render()} />
                </Table.Head>
              </Subscribe>
            {/each}
          </Table.Row>
        </Subscribe>
      {/each}
    </Table.Header>
    <Table.Body {...$tableBodyAttrs}>
      {#each $pageRows as row (row.id)}
        <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
          <Table.Row {...rowAttrs}>
            {#each row.cells as cell (cell.id)}
              <Subscribe attrs={cell.attrs()} let:attrs>
                <Table.Cell {...attrs}>
                  <Render of={cell.render()} />
                </Table.Cell>
              </Subscribe>
            {/each}
          </Table.Row>
        </Subscribe>
      {/each}
    </Table.Body>
  </Table.Root>
</div>
```

#### Render the table
Finally, we'll render our table in our +page.svelte file.

- routes/payments/+page.svelte
```svelte
<script lang="ts">
  import DataTable from "./data-table.svelte";
</script>
 
<div class="container mx-auto py-10">
  <DataTable />
</div>
```

#### Cell Formatting
Now that we have a basic table, let's format the amount cell to display the dollar amount. We'll also align the cell to the right.

#### Update columns definition
First, we'll update our columns definition for the amount column to return a formatted string.

- routes/payments/data-table.svelte
```svelte
const columns = table.createColumns([
  table.column({
    accessor: "id",
    header: "ID",
  }),
  table.column({
    accessor: "status",
    header: "Status",
  }),
  table.column({
    accessor: "email",
    header: "Email",
  }),
  table.column({
    accessor: "amount",
    header: "Amount",
    cell: ({ value }) => {
      const formatted = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(value);
      return formatted;
    },
  }),
  table.column({
    accessor: ({ id }) => id,
    header: "",
  }),
]);
```

#### Update styles
Now that we're returning a formatted string, let's now align the amount header and cell to the right. We'll also capitalize our status cell values.

- routes/payments/data-table.svelte
```svelte
<div class="rounded-md border">
  <Table.Root {...$tableAttrs}>
    <Table.Header>
      {#each $headerRows as headerRow}
        <Subscribe rowAttrs={headerRow.attrs()}>
          <Table.Row>
            {#each headerRow.cells as cell (cell.id)}
              <Subscribe attrs={cell.attrs()} let:attrs props={cell.props()}>
                <Table.Head {...attrs}>
                  {#if cell.id === "amount"}
                    <div class="text-right">
                      <Render of={cell.render()} />
                    </div>
                  {:else}
                    <Render of={cell.render()} />
                  {/if}
                </Table.Head>
              </Subscribe>
            {/each}
          </Table.Row>
        </Subscribe>
      {/each}
    </Table.Header>
    <Table.Body {...$tableBodyAttrs}>
      {#each $pageRows as row (row.id)}
        <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
          <Table.Row {...rowAttrs}>
            {#each row.cells as cell (cell.id)}
              <Subscribe attrs={cell.attrs()} let:attrs>
                <Table.Cell {...attrs}>
                  {#if cell.id === "amount"}
                    <div class="text-right font-medium">
                      <Render of={cell.render()} />
                    </div>
                  {:else if cell.id === "status"}
                    <div class="capitalize">
                      <Render of={cell.render()} />
                    </div>
                  {:else}
                    <Render of={cell.render()} />
                  {/if}
                </Table.Cell>
              </Subscribe>
            {/each}
          </Table.Row>
        </Subscribe>
      {/each}
    </Table.Body>
  </Table.Root>
</div>
```

You can use this approach to customize the styles of any cell in your table. In the following sections, we'll demonstrate how you can use a component to render a cell as well.

#### Row Actions
Let's now add row actions to our table. We'll use a <DropdownMenu /> and <Button /> component for this.

#### Create actions component
We'll start by creating a new component called data-table-actions.svelte which will contain our actions menu. It's going to receive an id prop, which we'll use to identify and perform specific actions on the row.

- routes/payments/data-table-actions.svelte
````svelte
<script lang="ts">
  import Ellipsis from "lucide-svelte/icons/ellipsis";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
  import { Button } from "$lib/components/ui/button";
 
  export let id: string;
</script>
 
<DropdownMenu.Root>
  <DropdownMenu.Trigger asChild let:builder>
    <Button
      variant="ghost"
      builders={[builder]}
      size="icon"
      class="relative h-8 w-8 p-0"
    >
      <span class="sr-only">Open menu</span>
      <Ellipsis class="h-4 w-4" />
    </Button>
  </DropdownMenu.Trigger>
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>Actions</DropdownMenu.Label>
      <DropdownMenu.Item on:click={() => navigator.clipboard.writeText(id)}>
        Copy payment ID
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Item>View customer</DropdownMenu.Item>
    <DropdownMenu.Item>View payment details</DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

#### Update columns definition
Now that we've defined our actions component, let's update our actions column definition to use 

- routes/payments/data-table.svelte
````svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import { readable } from "svelte/store";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    //...
  ];
 
  const table = createTable(readable(data));
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
    }),
    table.column({
      accessor: "status",
      header: "Status",
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
    }),
  ]);
 
  const { headerRows, pageRows, tableAttrs, tableBodyAttrs } =
    table.createViewModel(columns);
</script>
```

We're just passing the id to our actions component, but you could pass whatever information you need to perform actions on the row. In this example, we could use the id to make a DELETE request to our API to delete the payment.

#### Pagination
Next, we'll add pagination to our table

Enable the `addPagination` plugin
- routes/payments/data-table.svelte
````svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import { addPagination } from "svelte-headless-table/plugins";
  import { readable } from "svelte/store";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
  import { Button } from "$lib/components/ui/button";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    //...
  ];
 
  const table = createTable(readable(data), {
    page: addPagination(),
  });
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
    }),
    table.column({
      accessor: "status",
      header: "Status",
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
    }),
  ]);
 
  const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates } =
    table.createViewModel(columns);
 
  const { hasNextPage, hasPreviousPage, pageIndex } = pluginStates.page;
</script>
```

#### Add pagination controls
We can add pagination controls to our table using the <Button /> component and the hasNextPage, hasPreviousPage, and pageIndex variables.

- routes/payments/data-table.svelte
```svelte
<div>
  <div class="rounded-md border">
    <Table.Root {...$tableAttrs}>
      <!-- .... -->
    </Table.Root>
  </div>
  <div class="flex items-center justify-end space-x-4 py-4">
    <Button
      variant="outline"
      size="sm"
      on:click={() => ($pageIndex = $pageIndex - 1)}
      disabled={!$hasPreviousPage}>Previous</Button
    >
    <Button
      variant="outline"
      size="sm"
      disabled={!$hasNextPage}
      on:click={() => ($pageIndex = $pageIndex + 1)}>Next</Button
    >
  </div>
</div>
```

See the pagination docs for more information on how to customize the pagination behavior.

#### Sorting
Let's make the email column sortable.

#### Enable the `addSortBy` plugin
Let's enable the addSortBy plugin and import the <ArrowUpDown /> icon which we'll use to indicate the sort option for the column.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import { addPagination, addSortBy } from "svelte-headless-table/plugins";
  import { readable } from "svelte/store";
  import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
  import { Button } from "$lib/components/ui/button";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    //...
  ];
 
  const table = createTable(readable(data), {
    page: addPagination(),
    sort: addSortBy(),
  });
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
      plugins: {
        sort: {
          disable: true,
        },
      },
    }),
    table.column({
      accessor: "status",
      header: "Status",
      plugins: {
        sort: {
          disable: true,
        },
      },
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
      plugins: {
        sort: {
          disable: true,
        },
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
      plugins: {
        sort: {
          disable: true,
        },
      },
    }),
  ]);
 
  const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates } =
    table.createViewModel(columns);
 
  const { hasNextPage, hasPreviousPage, pageIndex } = pluginStates.page;
</script>
```

#### Make header cell sortable
We can now update the email header cell to add sorting controls.

- routes/payments/data-table.svelte
```svelte
<Table.Root {...$tableAttrs}>
  <Table.Header>
    {#each $headerRows as headerRow}
      <Subscribe rowAttrs={headerRow.attrs()}>
        <Table.Row>
          {#each headerRow.cells as cell (cell.id)}
            <Subscribe
              attrs={cell.attrs()}
              let:attrs
              props={cell.props()}
              let:props
            >
              <Table.Head {...attrs}>
                {#if cell.id === "amount"}
                  <div class="text-right">
                    <Render of={cell.render()} />
                  </div>
                {:else if cell.id === "email"}
                  <Button variant="ghost" on:click={props.sort.toggle}>
                    <Render of={cell.render()} />
                    <ArrowUpDown class={"ml-2 h-4 w-4"} />
                  </Button>
                {:else}
                  <Render of={cell.render()} />
                {/if}
              </Table.Head>
            </Subscribe>
          {/each}
        </Table.Row>
      </Subscribe>
    {/each}
  </Table.Header>
  <Table.Body {...$tableBodyAttrs}>
    <!-- ... -->
  </Table.Body>
</Table.Root>
```

See the sort docs for more information on how to customize the sort behavior.

#### Filtering
Let's add a search input to filter emails in our table.

#### Enable the addTableFilter plugin
We'll start by enabling the addTableFilter plugin and importing the <Input /> component we'll use for the search input.

- routes/payments/data-table.svelte
````svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import {
    addPagination,
    addSortBy,
    addTableFilter,
  } from "svelte-headless-table/plugins";
  import { readable } from "svelte/store";
  import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data), {
    page: addPagination(),
    sort: addSortBy(),
    filter: addTableFilter({
      fn: ({ filterValue, value }) =>
        value.toLowerCase().includes(filterValue.toLowerCase()),
    }),
  });
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "status",
      header: "Status",
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
  ]);
 
  const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates } =
    table.createViewModel(columns);
 
  const { pageIndex, hasNextPage, hasPreviousPage } = pluginStates.page;
  const { filterValue } = pluginStates.filter;
</script>
```

We're excluding all columns except for email from the filter plugin, and we're using a case-insensitive filter function to match the email value.

#### Add search input
Now that our table is configured to filter by email, let's add a search input on top of our table.

- routes/payments/data-table.svelte
```svelte
<div>
  <div class="flex items-center py-4">
    <Input
      class="max-w-sm"
      placeholder="Filter emails..."
      type="text"
      bind:value={$filterValue}
    />
  </div>
  <div class="rounded-md border">
    <Table.Root>
      <!-- ... -->
    </Table.Root>
  </div>
  <div class="flex items-center justify-end space-x-4 py-4">
    <!-- ... -->
  </div>
</div>
```

Since filterValue is a store, we can bind it to the input value and it will automatically update as the user types.

See the filter docs for more information on how to customize the filtering behavior.

#### Visibility
Let's add the ability to control which columns are visible in our table.

- Enable `addHiddenColumns` plugin
We'll start by enabling the addHiddenColumns plugin. We'll also need a <ChevronDown /> icon and the `<DropdownMenu />` component in the next step.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import {
    addPagination,
    addSortBy,
    addTableFilter,
    addHiddenColumns,
  } from "svelte-headless-table/plugins";
  import { readable } from "svelte/store";
  import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
  import ChevronDown from "lucide-svelte/icons/chevron-down";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data), {
    page: addPagination(),
    sort: addSortBy({ disableMultiSort: true }),
    filter: addTableFilter({
      fn: ({ filterValue, value }) => value.includes(filterValue),
    }),
    hide: addHiddenColumns(),
  });
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: "ID",
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "status",
      header: "Status",
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
  ]);
 
  const {
    headerRows,
    pageRows,
    tableAttrs,
    tableBodyAttrs,
    pluginStates,
    flatColumns,
  } = table.createViewModel(columns);
 
  const { pageIndex, hasNextPage, hasPreviousPage } = pluginStates.page;
  const { filterValue } = pluginStates.filter;
  const { hiddenColumnIds } = pluginStates.hide;
 
  const ids = flatColumns.map((col) => col.id);
  let hideForId = Object.fromEntries(ids.map((id) => [id, true]));
 
  $: $hiddenColumnIds = Object.entries(hideForId)
    .filter(([, hide]) => !hide)
    .map(([id]) => id);
 
  const hidableCols = ["status", "email", "amount"];
</script>
```

We're setting the hiddenColumnIds store from the plugin whenever hideForId changes to reflect our newly chosen hidden/shown columns.

### Add column visibility controls
Now we'll use the icon and <DropdownMenu /> we imported in the previous step to render a menu of columns that can be hidden.

- routes/payments/data-table.svelte
```svelte
<div>
  <div class="flex items-center py-4">
    <Input
      class="max-w-sm"
      placeholder="Filter emails..."
      type="text"
      bind:value={$filterValue}
    />
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild let:builder>
        <Button variant="outline" class="ml-auto" builders={[builder]}>
          Columns <ChevronDown class="ml-2 h-4 w-4" />
        </Button>
      </DropdownMenu.Trigger>
      <DropdownMenu.Content>
        {#each flatColumns as col}
          {#if hidableCols.includes(col.id)}
            <DropdownMenu.CheckboxItem bind:checked={hideForId[col.id]}>
              {col.header}
            </DropdownMenu.CheckboxItem>
          {/if}
        {/each}
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </div>
  <div class="rounded-md border">
    <Table.Root>
      <!-- ... -->
    </Table.Root>
  </div>
  <div class="flex items-center justify-end space-x-4 py-4">
    <!-- .... -->
  </div>
</div>
```

See the hidden columns docs for more information.

#### Row Selection
Next, we're going to add row selection to our table.

#### Create checkbox component
We'll start by creating a new component called data-table-checkbox.svelte which will be used to render a checkbox for each row.

- routes/payments/data-table-checkbox.svelte
```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox";
  import type { Writable } from "svelte/store";
 
  export let checked: Writable<boolean>;

<Checkbox bind:checked={$checked} />
```

#### Enable addSelectedRows plugin
Next, we'll enable the addSelectedRows plugin and import the <Checkbox /> component we just created.

- routes/payments/data-table.svelte
```svelte
<script lang="ts">
  import {
    createTable,
    Render,
    Subscribe,
    createRender,
  } from "svelte-headless-table";
  import {
    addPagination,
    addSortBy,
    addTableFilter,
    addHiddenColumns,
    addSelectedRows,
  } from "svelte-headless-table/plugins";
  import { readable } from "svelte/store";
  import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
  import ChevronDown from "lucide-svelte/icons/chevron-down";
  import * as Table from "$lib/components/ui/table";
  import DataTableActions from "./data-table-actions.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Input } from "$lib/components/ui/input";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
  import DataTableCheckbox from "./data-table-checkbox.svelte";
 
  type Payment = {
    id: string;
    amount: number;
    status: "pending" | "processing" | "success" | "failed";
    email: string;
  };
 
  const data: Payment[] = [
    {
      id: "m5gr84i9",
      amount: 316,
      status: "success",
      email: "ken99@yahoo.com",
    },
    // ...
  ];
 
  const table = createTable(readable(data), {
    page: addPagination(),
    sort: addSortBy({ disableMultiSort: true }),
    filter: addTableFilter({
      includeHiddenColumns: true,
      fn: ({ filterValue, value }) => value.includes(filterValue),
    }),
    hide: addHiddenColumns(),
    select: addSelectedRows(),
  });
 
  const columns = table.createColumns([
    table.column({
      accessor: "id",
      header: (_, { pluginStates }) => {
        const { allPageRowsSelected } = pluginStates.select;
        return createRender(DataTableCheckbox, {
          checked: allPageRowsSelected,
        });
      },
      cell: ({ row }, { pluginStates }) => {
        const { getRowState } = pluginStates.select;
        const { isSelected } = getRowState(row);
 
        return createRender(DataTableCheckbox, {
          checked: isSelected,
        });
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "status",
      header: "Status",
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "amount",
      header: "Amount",
      cell: ({ value }) => {
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
        }).format(value);
        return formatted;
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
    table.column({
      accessor: ({ id }) => id,
      header: "",
      cell: ({ value }) => {
        return createRender(DataTableActions, { id: value });
      },
      plugins: {
        sort: {
          disable: true,
        },
        filter: {
          exclude: true,
        },
      },
    }),
  ]);
 
  const {
    headerRows,
    pageRows,
    tableAttrs,
    tableBodyAttrs,
    pluginStates,
    flatColumns,
    rows,
  } = table.createViewModel(columns);
 
  const { pageIndex, hasNextPage, hasPreviousPage } = pluginStates.page;
  const { filterValue } = pluginStates.filter;
  const { hiddenColumnIds } = pluginStates.hide;
  const { selectedDataIds } = pluginStates.select;
 
  const ids = flatColumns.map((col) => col.id);
  let hideForId = Object.fromEntries(ids.map((id) => [id, true]));
 
  $: $hiddenColumnIds = Object.entries(hideForId)
    .filter(([, hide]) => !hide)
    .map(([id]) => id);
 
  const hidableCols = ["status", "email", "amount"];
</script>
```


#### Update styles & show selected rows
To accommodate the checkbox, we'll need to update our table styles. We'll also add a message to show how many rows are selected.

- routes/payments/data-table.svelte
```svelte
<div>
  <div class="flex items-center py-4">
    <Input
      class="max-w-sm"
      placeholder="Filter emails..."
      type="text"
      bind:value={$filterValue}
    />
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild let:builder>
        <Button variant="outline" class="ml-auto" builders={[builder]}>
          Columns <ChevronDown class="ml-2 h-4 w-4" />
        </Button>
      </DropdownMenu.Trigger>
      <DropdownMenu.Content>
        {#each flatColumns as col}
          {#if hidableCols.includes(col.id)}
            <DropdownMenu.CheckboxItem bind:checked={hideForId[col.id]}>
              {col.header}
            </DropdownMenu.CheckboxItem>
          {/if}
        {/each}
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </div>
  <div class="rounded-md border">
    <Table.Root {...$tableAttrs}>
      <Table.Header>
        {#each $headerRows as headerRow}
          <Subscribe rowAttrs={headerRow.attrs()}>
            <Table.Row>
              {#each headerRow.cells as cell (cell.id)}
                <Subscribe
                  attrs={cell.attrs()}
                  let:attrs
                  props={cell.props()}
                  let:props
                >
                  <Table.Head {...attrs} class="[&:has([role=checkbox])]:pl-3">
                    {#if cell.id === "amount"}
                      <div class="text-right">
                        <Render of={cell.render()} />
                      </div>
                    {:else if cell.id === "email"}
                      <Button variant="ghost" on:click={props.sort.toggle}>
                        <Render of={cell.render()} />
                        <ArrowUpDown class={"ml-2 h-4 w-4"} />
                      </Button>
                    {:else}
                      <Render of={cell.render()} />
                    {/if}
                  </Table.Head>
                </Subscribe>
              {/each}
            </Table.Row>
          </Subscribe>
        {/each}
      </Table.Header>
      <Table.Body {...$tableBodyAttrs}>
        {#each $pageRows as row (row.id)}
          <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
            <Table.Row
              {...rowAttrs}
              data-state={$selectedDataIds[row.id] && "selected"}
            >
              {#each row.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs>
                  <Table.Cell {...attrs} class="[&:has([role=checkbox])]:pl-3">
                    {#if cell.id === "amount"}
                      <div class="text-right font-medium">
                        <Render of={cell.render()} />
                      </div>
                    {:else if cell.id === "status"}
                      <div class="capitalize">
                        <Render of={cell.render()} />
                      </div>
                    {:else}
                      <Render of={cell.render()} />
                    {/if}
                  </Table.Cell>
                </Subscribe>
              {/each}
            </Table.Row>
          </Subscribe>
        {/each}
      </Table.Body>
    </Table.Root>
  </div>
  <div class="flex items-center justify-end space-x-4 py-4">
    <div class="text-muted-foreground flex-1 text-sm">
      {Object.keys($selectedDataIds).length} of{" "}
      {$rows.length} row(s) selected.
    </div>
    <Button
      variant="outline"
      size="sm"
      on:click={() => ($pageIndex = $pageIndex - 1)}
      disabled={!$hasPreviousPage}>Previous</Button
    >
    <Button
      variant="outline"
      size="sm"
      disabled={!$hasNextPage}
      on:click={() => ($pageIndex = $pageIndex + 1)}>Next</Button
    >
  </div>
</div>
```