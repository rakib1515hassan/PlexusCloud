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
                            <label class="col-md-2 col-form-label" for="rule">RAM</label>
                            <div class="col-md-9">
                                <input type="text" class="form-control" placeholder="">
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="col-md-2 col-form-label" for="rule">CPU</label>
                            <div class="col-md-9">
                                <input type="text" class="form-control" placeholder="">
                            </div>
                        </div>
                    </div>

                    <div class="show_item">
                        <div class="form-group row mb-3">
                            <label class="col-md-2 col-form-label" for="rule">CPU</label>
                            <div class="col-md-9">
                                <input type="text" class="form-control" placeholder="">
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                gender: '',
                dob: '',
                joining: '',
                user_salary: '',
                is_verified: false,
                address: '',
                profile_image: null,
            },
            formErrors: [],
        };
    },
    methods: {
        async submitForm() {
            this.formErrors = [];
            // Clear any previous errors

            // Here you would make your API call to submit the form data
            try {
                const formData = new FormData();
                Object.entries(this.form).forEach(([key, value]) => {
                    formData.append(key, value);
                });

                // Make sure to handle the API endpoint correctly
                await this.$http.post('/api/employee/create/', formData);
                // Redirect or perform any other actions on success
            } catch (error) {
                if (error.response && error.response.data) {
                    // Assume the API returns an object with field-specific errors
                    this.formErrors = Object.values(error.response.data);
                } else {
                    console.error(error);
                }
            }
        },
        handleFileUpload(event) {
            this.form.profile_image = event.target.files[0];
        },
        cancel() {
            // Handle cancel action, e.g., redirect or clear form
            this.$router.push({ name: 'employee_list' });
        },
    },
};
</script>

<style scoped>
.error-message {
    color: red;
}
</style>
