<template>
    <div class="card mb-3">
        <!-- Header Content -->
        <div class="card-header bg-light">
            <div class="row flex-between-center">
                <div class="col-4 col-sm-auto d-flex align-items-center pe-0">
                    <h5 class="fs-0 mb-0 text-nowrap py-2 py-xl-0">
                        <span class="fas fa-user-friends fs-1 me-2"></span>Admin List
                    </h5>
                </div>
                <div class="col-8 col-sm-auto ms-auto text-end ps-0">
                    <div class="d-flex flex-row" id="orders-actions">
                        <a href="" class="btn btn-konnect-default btn-sm">
                            <span class="fas fa-plus"></span>
                            <span class="d-none d-sm-inline-block ms-1">New</span>
                        </a>
                        <button class="btn btn-konnect-default btn-sm mx-2" @click="openFilterModal">
                            <span class="fas fa-filter"></span>
                            <span class="d-none d-sm-inline-block ms-1">Filter</span>
                        </button>
                        <button class="btn btn-konnect-default btn-sm" @click="exportData">
                            <span class="fas fa-external-link-alt"></span>
                            <span class="d-none d-sm-inline-block ms-1">Export All</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Body Content -->
        <div class="card-body p-4">

            <!-- Show, Bulk Delete, and Search -->
            <div class="row mb-3 align-items-center">
                <!-- Show Entries Dropdown -->
                <div class="col-12 col-md-3">
                    <div class="d-flex align-items-center">
                        <label class="d-flex align-items-center mb-0">Showing
                            <select class="form-select form-select-sm mx-2" v-model="itemsPerPage"
                                @change="changeItemsPerPage" style="width: 80px;">
                                <option value="10">10</option>
                                <option value="25">25</option>
                                <option value="50">50</option>
                            </select>
                            Entries
                        </label>
                    </div>
                </div>

                <!-- Bulk Delete Action -->
                <div class="col-12 col-md-6 mt-2 mt-md-0">
                    <form method="post" id="delete_form">
                        <div v-if="selectedAdmins.length > 0" class="ms-3">
                            <input type="hidden" name="delete_id_list" id="delete_id_list" v-model="deleteIdList">
                            <button class="btn btn-outline-danger me-1 mb-1" @click="handleDeleteButtonClick">
                                <span class="fas fa-trash me-2 btn-icon"></span>
                                Delete <span>({{ selectedAdmins.length }}) Selected</span>
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Search -->
                <div class="col-12 col-md-3 mt-2 mt-md-0">
                    <form class="d-flex justify-content-between mb-3" @submit.prevent="search">
                        <div class="input-group">
                            <input class="form-control" type="search" v-model="searchQuery" placeholder="Search..." />
                            <button class="btn btn-outline-secondary" type="submit">
                                <i class="fas fa-search"></i>
                            </button>
                        </div>
                    </form>
                </div>
            </div>


            <!-- Table -->
            <div class="table-responsive">
                <table width="100%" class="table table-bordered table-striped fs--1 mb-0">
                    <thead class="bg-200 text-900">
                        <tr>
                            <th>
                                <div class="form-check mb-0">
                                    <input class="form-check-input me-2" type="checkbox" @change="selectAll($event)" />
                                    S/N
                                </div>
                            </th>
                            <th>Avatar</th>
                            <th>Name/Gender</th>
                            <th>Email/Phone</th>
                            <th>Date of Birth</th>
                            <th class="text-center">Super Admin</th>
                            <th class="text-center">Joining/Enroll</th>
                            <th class="text-center">Active</th>
                            <th class="text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(admin, index) in paginatedAdmins" :key="admin.id">
                            <td>
                                <div class="form-check mb-0">
                                    <input class="form-check-input me-2" type="checkbox" :value="admin.id"
                                        v-model="selectedAdmins" />
                                    {{ startIndex + index + 1 }}
                                </div>
                            </td>
                            <td><img :src="admin.avatar" class="img-fluid rounded" width="50" /></td>
                            <td>
                                <span :class="admin.is_superuser ? 'badge bg-danger' : 'badge badge-soft-dark'">
                                    {{ admin.name }}
                                </span>
                                <br />
                                <span class="badge badge-soft-light">{{ admin.gender }}</span>
                            </td>
                            <td>
                                <span class="badge bg-light text-dark">{{ admin.email }}</span><br />
                                <span class="badge bg-light text-dark">{{ admin.phone }}</span>
                            </td>
                            <td>
                                <span class="badge bg-light text-dark">{{ admin.dob }}</span><br />
                                <span v-if="admin.age" class="badge bg-light text-dark">Age: {{ admin.age }}</span>
                            </td>
                            <td class="text-center">
                                <i
                                    :class="admin.is_superuser ? 'fa-solid fa-check text-success' : 'fa-solid fa-xmark text-danger'"></i>
                            </td>
                            <td class="text-center">
                                <span class="badge badge-soft-info">{{ admin.joining }}</span><br />
                                <span class="badge badge-soft-light">{{ admin.created_at }}</span><br />
                                <span class="badge badge-soft-light">{{ admin.created_time }}</span>
                            </td>
                            <td class="text-center">
                                <i
                                    :class="admin.is_active ? 'fa-solid fa-check text-success' : 'fa-solid fa-xmark text-danger'"></i>
                            </td>
                            <td class="text-center">
                                <a class="text-primary" href=""><span class="fas fa-eye text-primary"></span></a>
                                <a class="text-warning" href=""><span class="fas fa-edit text-warning"></span></a>
                                <a class="text-danger cursor-pointer" @click="deleteAdmin(admin.id)"><span
                                        class="fas fa-trash text-danger"></span></a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Pagination and Counting -->
        <div class="card-footer bg-light">
            <div class="row justify-content-between">
                <!-- Counting -->
                <div class="col-md-6 ms-3">
                    <strong>Showing
                        <span class="text-primary">{{ startIndex + 1 }}</span>
                        To
                        <span class="text-primary">{{ endIndex }}</span>
                        Out Of
                        <span class="text-primary">{{ querysetCount }}</span>
                    </strong>
                </div>

                <!-- Pagination -->
                <div class="col-md-2 me-3">
                    <nav aria-label="Page navigation example">
                        <div class="d-flex align-items-center justify-content-end">
                            <button class="btn btn-sm btn-falcon-default me-1" :disabled="!hasPrevious"
                                @click="goToFirstPage">
                                <i class="fa-solid fa-angles-left"></i>
                            </button>
                            <button class="btn btn-sm btn-falcon-default me-1" :disabled="!hasPrevious"
                                @click="goToPreviousPage">
                                <span class="fas fa-chevron-left"></span>
                            </button>
                            <span>{{ currentPage }}</span>
                            <button class="btn btn-sm btn-falcon-default ms-1" :disabled="!hasNext"
                                @click="goToNextPage">
                                <span class="fas fa-chevron-right"></span>
                            </button>
                            <button class="btn btn-sm btn-falcon-default ms-1" :disabled="!hasNext"
                                @click="goToLastPage">
                                <i class="fa-solid fa-angles-right"></i>
                            </button>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            itemsPerPage: 10,
            admins: [], 
            selectedAdmins: [],
            searchQuery: '',
            currentPage: 1,
            pageSize: 10,
            querysetCount: 0, // Total count of admins
        };
    },
    computed: {
        filteredAdmins() {
            return this.admins.filter((admin) =>
                admin.name.toLowerCase().includes(this.searchQuery.toLowerCase())
            );
        },
        paginatedAdmins() {
            const start = (this.currentPage - 1) * this.pageSize;
            const end = start + this.pageSize;
            return this.filteredAdmins.slice(start, end);
        },
        startIndex() {
            return (this.currentPage - 1) * this.pageSize;
        },
        endIndex() {
            return Math.min(this.startIndex + this.pageSize, this.querysetCount);
        },
        hasPrevious() {
            return this.currentPage > 1;
        },
        hasNext() {
            return this.currentPage * this.pageSize < this.querysetCount;
        },
    },
    methods: {
        changeItemsPerPage() {
            // Adjust the number of items shown per page
            this.fetchData();
        },
        search() {
            this.currentPage = 1; // Reset to the first page after search
        },
        goToFirstPage() {
            this.currentPage = 1;
        },
        goToPreviousPage() {
            if (this.hasPrevious) {
                this.currentPage -= 1;
            }
        },
        goToNextPage() {
            if (this.hasNext) {
                this.currentPage += 1;
            }
        },
        goToLastPage() {
            const totalPages = Math.ceil(this.querysetCount / this.pageSize);
            this.currentPage = totalPages;
        },
        selectAll(event) {
            this.selectedAdmins = event.target.checked
                ? this.paginatedAdmins.map((admin) => admin.id)
                : [];
        },
        handleDeleteButtonClick() {
            console.log('Selected admins for deletion:', this.selectedAdmins);
            // Perform the bulk delete action
        },
        deleteAdmin(id) {
            console.log('Delete admin with id:', id);
            // Perform the delete action for a single admin
        },
        openFilterModal() {
            // Handle filter modal opening
        },
        exportData() {
            console.log('Exporting data');
            // Handle data export
        },
    },
    mounted() {
        // Assume this data comes from your Django backend
        this.admins = [
            // Example data...
        ];
        this.querysetCount = this.admins.length;
    },
};
</script>


<style scoped>
.action li {
    display: inline;
}

.action li a {
    color: #fff;
    display: inline-block;
    font-size: 14px;
    margin-right: 5px;
    line-height: 1.5;
    border-radius: 3px;
    transition: all 0.3s ease;
}
li .page {
    background-color: #d9dce0 !important;
    color: #0b0b0b !important;
}

li.active .page {
    background-color: #2c7be5 !important;
    color: #efeff5 !important;
}

.page {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
}

.btn-falcon-default .page {
    color: var(--falcon-btn-falcon-default-color);
    background-color: var(--falcon-btn-falcon-background);
    border-color: var(--falcon-btn-falcon-background);
    -webkit-box-shadow: var(--falcon-btn-falcon-box-shadow);
    box-shadow: var(--falcon-btn-falcon-box-shadow);
}

.font_text {
    font-family: "Poppins", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}


.filter_input {
    height: 45px;
}

.btn_hober:hover {
    background-color: #2c7be5 !important;
    color: white !important;
}
</style>