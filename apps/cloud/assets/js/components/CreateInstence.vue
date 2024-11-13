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
            <form class="row g-3" @submit.prevent="submitPayment">
                <div class="col-md-8">
                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="input_label col-form-label" for="rule">
                                Project Name
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <input type="text" class="form-control" placeholder="Write you project name..."
                                    v-model="project_name" required>
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
                                    v-model="name" required>
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
                                <select class="form-select" v-model="availabilityZone" required>
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
                                RAM (GB)
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="ram" required>
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
                                CPU (Core)
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <select class="form-select" v-model="cpu" required>
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
                                Storage (GB)
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <div class="storage-field">
                                    <select class="form-select" v-model="storageType" required>
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
                                Bandwidth (MB)
                                <span class="text-danger">*</span>
                            </label>
                            <div class="input_field">
                                <input type="text" class="form-control" placeholder="Write bandwidth amount..."
                                    v-model="bandwidth" required>
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
                                <select class="form-select" v-model="ipType" required>
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
                                    <td>{{ ram || 'N/A' }} * {{ RamPrice }} GB</td>
                                    <td>{{ calculatedRamPrice }}</td>
                                </tr>
                                <tr>
                                    <td><strong>CPU:</strong></td>
                                    <td>{{ cpu || 'N/A' }} * {{ CpuPrice }} Core</td>
                                    <td>{{ calculatedCpuPrice }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Storage:</strong></td>
                                    <td>{{ storageSize || 'N/A' }} * {{ StoragePrice }} GB ({{ storageType }})</td>
                                    <td>{{ calculatedStoragePrice }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Bandwidth:</strong></td>
                                    <td>{{ bandwidth || 'N/A' }} * {{ BandwidthPrice }}</td>
                                    <td>{{ calculatedBandwidthPrice }}</td>
                                </tr>
                                <tr>
                                    <td><strong>IP:</strong></td>
                                    <td>{{ ipType || 'N/A' }}</td>
                                    <td>{{ calculatedIpPrice }}</td>
                                </tr>
                                <tr>
                                    <td><strong>Total:</strong></td>
                                    <td colspan="2">{{ calculatedTotal }}/-</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="card-footer bg-200 d-flex" style="justify-content: end;">
                    <button class="btn btn-outline-primary btn-sm" style="width: 200px;" type="submit">Payment</button>
                </div>
            </form>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

import get_csrf from "../../../../../frontend/src/utils/get_csrf";

import { ServiceListAPI, SSLCommerzAPI } from "../../js/routes";

export default {
    data() {
        return {
            // User input fields
            project_name: '',
            name: '',
            availabilityZone: '',
            ram: '',
            cpu: '',
            storageType: '',
            storageSize: '',
            bandwidth: '',
            ipType: '',
            serviceDetails: [],

            // Prices from API
            RamPrice: 0,
            CpuPrice: 0,
            StoragePrice: 0, // Dynamic price based on selected storage type
            BandwidthPrice: 0,
            IpPrice: 0,

            // CSRF token
            csrfToken: '',
        };
    },

    computed: {
        // Calculate each price based on the user input and the API-provided price
        calculatedRamPrice() {
            return this.ram * this.RamPrice || 0;
        },
        calculatedCpuPrice() {
            return this.cpu * this.CpuPrice || 0;
        },
        calculatedStoragePrice() {
            return this.storageSize * this.StoragePrice || 0;
        },
        calculatedBandwidthPrice() {
            return this.bandwidth * this.BandwidthPrice || 0;
        },
        calculatedIpPrice() {
            return this.IpPrice || 0;
        },
        calculatedTotal() {
            // Sum up all calculated prices for the total
            return this.calculatedRamPrice + this.calculatedCpuPrice + this.calculatedStoragePrice + this.calculatedBandwidthPrice + this.calculatedIpPrice;
        }
    },

    mounted() {
        // this.csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    },

    methods: {
        async fetchServiceDetails() {
            try {
                const response = await axios.get(ServiceListAPI);
                this.serviceDetails = response.data;

                // Map prices from the API to data properties
                const ramDetail = this.serviceDetails.find(service => service.name === 'RAM');
                const cpuDetail = this.serviceDetails.find(service => service.name === 'CPU');
                const storageDetail = this.serviceDetails.find(service => service.name === 'Storage');
                // const bandwidthDetail = this.serviceDetails.find(service => service.name === 'Bandwidth');
                const bandwidthDetail = this.serviceDetails.find(service => service.name === 'Bandwith');
                const ipDetail = this.serviceDetails.find(service => service.name === 'IP');

                if (ramDetail) this.RamPrice = ramDetail.details[0].price;
                if (cpuDetail) this.CpuPrice = cpuDetail.details[0].price;
                if (bandwidthDetail) this.BandwidthPrice = bandwidthDetail.details[0].price;

                // Set Storage Price based on the selected storage type
                this.setStoragePrice();

            } catch (error) {
                console.error('Error fetching service details:', error);
            }
        },

        setStoragePrice() {
            // Find storage detail that matches the selected type and set the price
            const storageDetail = this.serviceDetails.find(service => service.name === 'Storage');
            if (storageDetail) {
                const selectedStorage = storageDetail.details.find(item => item.storage_type === this.storageType);
                this.StoragePrice = selectedStorage ? selectedStorage.price : 0;
            }
        },

        async submitPayment() {
            // console.log("Payment");
            const data = {
                project_name: this.project_name,
                instence_name: this.name,
                availability_zone: this.availabilityZone,
                ram: this.ram,
                cpu: this.cpu,
                storage_type: this.storageType,
                storage_size: this.storageSize,
                bandwidth: this.bandwidth,
                ip_type: this.ipType,
                total_amount: this.calculatedTotal,
                customer_info: {
                    name: "Customer Name",
                    email: "customer@example.com",
                    phone: "017XXXXXXXX",
                    address1: "Customer Address",
                    city: "Dhaka",
                    postcode: "1216",
                    country: "Bangladesh",
                }
            };


            console.log({
                project_name: this.project_name,
                instence_name: this.name,
                availability_zone: this.availabilityZone,
                ram: this.ram,
                cpu: this.cpu,
                storage_type: this.storageType,
                storage_size: this.storageSize,
                bandwidth: this.bandwidth,
                ip_type: this.ipType,
                total_amount: this.calculatedTotal
            });


            try {
                const response = await axios.post(SSLCommerzAPI, data, {
                    headers: {
                        "X-CSRFToken": get_csrf(),
                        'Content-Type': 'application/json'
                    }
                });

                // Redirect to SSLCommerz GatewayPageURL if provided
                if (response.data && response.data.GatewayPageURL) {
                    window.location.href = response.data.GatewayPageURL;
                } else {
                    toast.error("Failed to initiate payment.");
                }
            } catch (error) {
                console.error("Payment initiation error:", error);
                toast.error("Payment initiation failed. Please try again.");
            }
        }

    },


    watch: {
        // Watch for changes in storageType and update the price accordingly
        storageType() {
            this.setStoragePrice();
        },
        // Watch for changes in ipType and set price based on selection
        ipType(newType) {
            // this.IpPrice = newType === 'Private' ? 250 : 0;
            this.IpPrice = newType === 'Public' ? 250 : 0;
        }
    },
    mounted() {
        this.fetchServiceDetails();
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
