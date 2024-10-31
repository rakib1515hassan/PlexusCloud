<template>
    <div class="card mb-3">
        <div class="card-header">
            <div class="row flex-between-end">
                <div class="col-auto align-self-center">
                    <h5 class="mb-0">Instance Create</h5>
                </div>
            </div>
        </div>
        <div class="card-body bg-light">
            <form class="row g-3" @submit.prevent="submitForm" enctype="multipart/form-data">
                <div class="col-md-8">
                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Project Name
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <input type="text" class="form-control" placeholder="Write you project name..."
                                    v-model="project_name">
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Instance Name
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <input type="text" class="form-control" placeholder="Write you instance name..."
                                    v-model="name">
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Availability Zone
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="availabilityZone">
                                    <option value="">Select area...</option>
                                    <option value="Khulna">Khulna</option>
                                    <option value="Dhaka">Dhaka</option>
                                    <option value="Rajshai">Rajshai</option>
                                    <option value="Chitogong">Chitogong</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                RAM
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="ram">
                                    <option value="">Select RAM...</option>
                                    <option value="1">1 GB</option>
                                    <option value="2">2 GB</option>
                                    <option value="3">3 GB</option>
                                    <option value="4">4 GB</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                CPU
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="cpu">
                                    <option value="">Select CPU...</option>
                                    <option value="1">1 Core</option>
                                    <option value="2">2 Core</option>
                                    <option value="3">3 Core</option>
                                    <option value="4">4 Core</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Storage Type
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <div class="storage-field">
                                    <select class="form-select" v-model="storageType">
                                        <option value="">Select Type...</option>
                                        <option value="SSD">SSD</option>
                                        <option value="HDD">HDD</option>
                                        <option value="NVME">NVME</option>
                                    </select>
                                </div>
                                <div class="storage-field">
                                    <input type="number" class="form-control" placeholder="Write storage size"
                                        v-model="storageSize">
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Bandwidth
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <input type="text" class="form-control" placeholder="Write bandwidth amount..."
                                    v-model="bandwidth">
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                IP
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="ipType">
                                    <option value="">Select Type...</option>
                                    <option value="Public">Public</option>
                                    <option value="Private">Private</option>
                                </select>
                            </div>
                        </div>
                    </div>

                </div>

                <div class="col-md-4">
                    <span class="fw-bold">Your Config:</span>
                    <div class="ms-4">
                        <table class="table table-bordered">
                            <tbody>
                                <tr>
                                    <td><strong>RAM:</strong></td>
                                    <td>{{ ram || 'N/A' }}</td>
                                </tr>
                                <tr>
                                    <td><strong>CPU:</strong></td>
                                    <td>{{ cpu || 'N/A' }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Storage:</strong></td>
                                    <td>{{ storageSize || 'N/A' }} GB</td>
                                </tr>
                                <tr>
                                    <td><strong>Bandwidth:</strong></td>
                                    <td>{{ bandwidth || 'N/A' }}</td>
                                </tr>
                                <tr>
                                    <td><strong>IP:</strong></td>
                                    <td>{{ ipType || 'N/A' }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Total:</strong></td>
                                    <td>{{ calculatedTotal }}/-</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>


                <div class="card-footer bg-200 d-flex" style="justify-content: end;">
                    <button class="btn btn-outline-primary btn-sm" style="width: 200px;">Next</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            project_name: '',
            name: '',
            availabilityZone: '',
            ram: '',
            cpu: '',
            storageType: '',
            storageSize: '',
            bandwidth: '',
            ipType: '',
            total: 5000, // Example base price
        };
    },
    computed: {
        // Dynamically calculate total based on selections, adjust logic as needed.
        calculatedTotal() {
            let total = 5000;
            if (this.ram) total += parseInt(this.ram) * 1000;
            if (this.cpu) total += parseInt(this.cpu) * 2000;
            if (this.storageSize) total += parseInt(this.storageSize) * 500;
            return total;
        }
    },
    methods: {
        submitForm() {
            // Form submission logic here
            console.log("Form Submitted:", this.$data);
        }
    }
};
</script>


<style scoped>
.error-message {
    color: red;
}

.input_label {
    width: 25%;
}

.input_field {
    width: 75%;
    display: flex;
    gap: 10px;
    /* Adds a 10px gap between fields */
}

.storage-field {
    flex: 1;
    /* Makes both fields take up 50% each */
}
</style>
