<template>
    <div class="row mt-5 mt-lg-0 mt-xl-5 mt-xxl-0">
        <div class="col-lg-6 col-xl-12 col-xxl-6 h-100">
            <div class="card theme-wizard mb-5 mb-lg-0 mb-xl-5 mb-xxl-0 h-100">
                <div class="card-header bg-light pt-3 pb-2">
                    <ul class="nav nav-pills mb-3" role="tablist" id="pill-tab2">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active" data-wizard-step="data-wizard-step" data-bs-toggle="pill"
                                data-bs-target="#form-wizard-progress-tab1" type="button" role="tab"
                                aria-controls="form-wizard-progress-tab1" aria-selected="true"><span
                                    class="fas fa-lock me-2" data-fa-transform="shrink-2"></span><span
                                    class="d-none d-md-inline-block fs--1">Account</span></button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" data-wizard-step="data-wizard-step" data-bs-toggle="pill"
                                data-bs-target="#form-wizard-progress-tab2" type="button" role="tab"
                                aria-controls="form-wizard-progress-tab2" aria-selected="false"><span
                                    class="fas fa-user me-2" data-fa-transform="shrink-2"></span><span
                                    class="d-none d-md-inline-block fs--1">Personal</span></button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" data-wizard-step="data-wizard-step" data-bs-toggle="pill"
                                data-bs-target="#form-wizard-progress-tab3" type="button" role="tab"
                                aria-controls="form-wizard-progress-tab3" aria-selected="false"><span
                                    class="fas fa-dollar-sign me-2" data-fa-transform="down-2 shrink-2"></span><span
                                    class="d-none d-md-inline-block fs--1">Billing</span></button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" data-wizard-step="data-wizard-step" data-bs-toggle="pill"
                                data-bs-target="#form-wizard-progress-tab4" type="button" role="tab"
                                aria-controls="form-wizard-progress-tab4" aria-selected="false"><span
                                    class="fas fa-thumbs-up me-2" data-fa-transform="shrink-2"></span><span
                                    class="d-none d-md-inline-block fs--1">Done</span></button>
                        </li>
                    </ul>
                </div>
                <div class="progress" style="height: 2px;">
                    <div class="progress-bar" role="progressbar" aria-valuenow="33" aria-valuemin="0"
                        aria-valuemax="100"></div>
                </div>
                <div class="card-body py-4">
                    <div class="tab-content">
                        <div class="tab-pane active px-sm-3 px-md-5" role="tabpanel"
                            aria-labelledby="form-wizard-progress-tab1" id="form-wizard-progress-tab1">
                            <form novalidate="novalidate">
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-wizard-name">Name</label>
                                    <input class="form-control" type="text" name="name" placeholder="John Smith"
                                        id="form-wizard-progress-wizard-name" />
                                </div>
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-wizard-email">Email*</label>
                                    <input class="form-control" type="email" name="email" placeholder="Email address"
                                        pattern="^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$"
                                        required="required" id="form-wizard-progress-wizard-email"
                                        data-wizard-validate-email="true" />
                                    <div class="invalid-feedback">You must add email</div>
                                </div>
                                <div class="row g-2">
                                    <div class="col-6">
                                        <div class="mb-3">
                                            <label class="form-label"
                                                for="form-wizard-progress-wizard-password">Password*</label>
                                            <input class="form-control" type="password" name="password"
                                                placeholder="Password" required="required"
                                                id="form-wizard-progress-wizard-password"
                                                data-wizard-validate-password="true" />
                                            <div class="invalid-feedback">Please enter password</div>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="mb-3">
                                            <label class="form-label"
                                                for="form-wizard-progress-wizard-confirm-password">Confirm
                                                Password*</label>
                                            <input class="form-control" type="password" name="confirmPassword"
                                                placeholder="Confirm Password" required="required"
                                                id="form-wizard-progress-wizard-confirm-password"
                                                data-wizard-validate-confirm-password="true" />
                                            <div class="invalid-feedback">Passwords need to match</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" name="terms" required="required"
                                        checked="checked" id="form-wizard-progress-wizard-checkbox" />
                                    <label class="form-check-label" for="form-wizard-progress-wizard-checkbox">I
                                        accept the <a href="#!">terms </a>and <a href="#!">privacy
                                            policy</a></label>
                                </div>
                            </form>
                        </div>
                        <div class="tab-pane px-sm-3 px-md-5" role="tabpanel"
                            aria-labelledby="form-wizard-progress-tab2" id="form-wizard-progress-tab2">
                            <form>
                                <div class="mb-3">
                                    <div class="row" data-dropzone="data-dropzone" data-options=''>
                                        <div class="fallback">
                                            <input type="file" name="file" />
                                        </div>
                                        <div class="col-md-auto">
                                            <div class="dz-preview dz-preview-single">
                                                <div
                                                    class="dz-preview-cover d-flex align-items-center justify-content-center mb-3 mb-md-0">
                                                    <div class="avatar avatar-4xl"><img class="rounded-circle" src=""
                                                            alt="..." data-dz-thumbnail="data-dz-thumbnail" /></div>
                                                    <div class="dz-progress"><span class="dz-upload"
                                                            data-dz-uploadprogress=""></span></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md">
                                            <div class="dz-message dropzone-area px-2 py-3"
                                                data-dz-message="data-dz-message">
                                                <div class="text-center"><img class="me-2" src="" width="25"
                                                        alt="" />Upload your profile picture
                                                    <p class="mb-0 fs--1 text-400">Upload a 300x300 jpg image
                                                        with
                                                        <br />a maximum size of 400KB
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-gender">Gender</label>
                                    <select class="form-select" name="gender" id="form-wizard-progress-gender">
                                        <option value="">Select your gender ...</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Other">Other</option>
                                    </select>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-wizard-phone">Phone</label>
                                    <input class="form-control" type="text" name="phone" placeholder="Phone"
                                        id="form-wizard-progress-wizard-phone" />
                                </div>
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-wizard-datepicker">Date
                                        of
                                        Birth</label>
                                    <input class="form-control datetimepicker" type="text" placeholder="d/m/y"
                                        data-options='{"dateFormat":"d/m/y","disableMobile":true}'
                                        id="form-wizard-progress-wizard-datepicker" />
                                </div>
                                <div class="mb-3">
                                    <label class="form-label" for="form-wizard-progress-wizard-address">Address</label>
                                    <textarea class="form-control" rows="4"
                                        id="form-wizard-progress-wizard-address"></textarea>
                                </div>
                            </form>
                        </div>
                        <div class="tab-pane px-sm-3 px-md-5" role="tabpanel"
                            aria-labelledby="form-wizard-progress-tab3" id="form-wizard-progress-tab3">
                            <form class="form-validation">
                                <div class="row g-2">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label" for="form-wizard-progress-card-number">Card
                                                Number</label>
                                            <input class="form-control" placeholder="XXXX XXXX XXXX XXXX" type="text"
                                                id="form-wizard-progress-card-number" />
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label" for="form-wizard-progress-card-name">Name
                                                on
                                                Card</label>
                                            <input class="form-control" placeholder="John Doe" name="cardName"
                                                type="text" id="form-wizard-progress-card-name" />
                                        </div>
                                    </div>
                                </div>
                                <div class="row g-2">
                                    <div class="col-6">
                                        <div class="mb-3">
                                            <label class="form-label"
                                                for="form-wizard-progress-card-holder-country">Country</label>
                                            <select class="form-select" name="customSelectCountry"
                                                id="form-wizard-progress-card-holder-country">
                                                <option value="">Select your country ...</option>
                                                <option value="Afghanistan">Afghanistan</option>
                                                <option value="Albania">Albania</option>
                                                <option value="Algeria">Algeria</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="mb-3">
                                            <label class="form-label"
                                                for="form-wizard-progress-card-holder-zip-code">Zip Code</label>
                                            <input class="form-control" placeholder="1234" name="zipCode" type="text"
                                                id="form-wizard-progress-card-holder-zip-code" />
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="form-group mb-0">
                                            <label class="form-label" for="form-wizard-progress-card-exp-date">Exp
                                                Date</label>
                                            <input class="form-control" placeholder="15/2024" name="expDate" type="text"
                                                id="form-wizard-progress-card-exp-date" />
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="form-group mb-0">
                                            <label class="form-label"
                                                for="form-wizard-progress-card-cvv">CVV</label><span class="ms-1"
                                                data-bs-toggle="tooltip" data-bs-placement="top"
                                                title="Card verification value"><span
                                                    class="fa fa-question-circle"></span></span>
                                            <input class="form-control" placeholder="123" name="cvv" maxlength="3"
                                                pattern="[0-9]{3}" type="text" id="form-wizard-progress-card-cvv" />
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div class="tab-pane text-center px-sm-3 px-md-5" role="tabpanel"
                            aria-labelledby="form-wizard-progress-tab4" id="form-wizard-progress-tab4">
                            <div class="wizard-lottie-wrapper">
                                <div class="lottie wizard-lottie mx-auto my-3" data-options=''>
                                </div>
                            </div>
                            <h4 class="mb-1">Your account is all set!</h4>
                            <p>Now you can access to your account</p><a class="btn btn-primary px-5 my-3" href="">Start
                                Over</a>
                        </div>
                    </div>
                </div>
                <div class="card-footer bg-light">
                    <div class="px-sm-3 px-md-5">
                        <ul class="pager wizard list-inline mb-0">
                            <li class="previous">
                                <button class="btn btn-link ps-0" type="button"><span class="fas fa-chevron-left me-2"
                                        data-fa-transform="shrink-3"></span>Prev</button>
                            </li>
                            <li class="next">
                                <button class="btn btn-primary px-5 px-sm-6" type="submit">Next<span
                                        class="fas fa-chevron-right ms-2" data-fa-transform="shrink-3">
                                    </span></button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
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
