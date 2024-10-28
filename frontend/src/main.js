import {createApp} from 'vue'
import DataTable from "@/components/DataTable.vue";
import GroupDetails from "@/components/GroupDetails.vue";

import {
    AdminCreateComponent,
    AdminListComponent,
} from '../../apps/admin/assets/js/app'


// Create Vue Instance
const app = createApp({});



// Create Components
app.component('data-table', DataTable);
app.component('group-details', GroupDetails);

// Admin Component
app.component('admin-list', AdminListComponent);
app.component('admin-create', AdminCreateComponent);







// mounted components
app.mount('#top');



