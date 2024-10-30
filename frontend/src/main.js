import {createApp} from 'vue'
import DataTable from "@/components/DataTable.vue";
import GroupDetails from "@/components/GroupDetails.vue";



// Create Vue Instance
const app = createApp({});

// Create Components
app.component('data-table', DataTable);
app.component('group-details', GroupDetails);


import {
    AdminCreateComponent,
    AdminListComponent,
} from '../../apps/admin/assets/js/app'

// Admin Component
app.component('admin-list', AdminListComponent);
app.component('admin-create', AdminCreateComponent);


import {
    CreateInstenceComponent,
} from '../../apps/cloud/assets/js/app'

// Admin Component
app.component('instence-create', CreateInstenceComponent);


// mounted components
app.mount('#top');



