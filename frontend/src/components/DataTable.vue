<template>
  <div class="row">
    <div class="col-md-12">
      <div class="card">
        <div class="card-header d-flex">
          <div class="card-title">
            <i class="fas fa-table me-2"></i>
            {{ config?.title }}
          </div>
          <div class="card-options ms-auto" v-if="config?.control?.add_button">
            <a class="btn btn-sm btn-primary" :href="config?.control?.add_button_url">
              <span class="fas fa-plus me-2"></span>
              Add
            </a>
          </div>
        </div>

        <div class="card-body bg-light">
          <div class="row g-0">
            <div class="col-auto ms-0 me-2 px-0" v-if="config?.control?.bulk_delete_button && selectedIds.length > 0">
              <button class="btn btn-sm btn-outline-danger" type="button" @click="deleteSelected()">
                <span class="fas fa-trash me-2"></span>
                Delete ({{ selectedIds.length }}) Selected
              </button>

            </div>

            <div class="col-auto col-sm-3 mb-3" v-if="ajaxLoading">
              <div class="d-flex justify-content-start align-items-center">
                <div class="spinner-border spinner-border-sm" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
            </div>

            <div class="col-auto col-sm-3 mb-3 ms-auto" v-if="config?.control?.search">
              <div class="input-group">
                <input class="form-control shadow-none search" type="search"
                       @keyup="makeSearch($event.target.value)"
                       placeholder="Search..." aria-label="search"/>
                <div class="input-group-text bg-transparent">
                  <span class="fa fa-search fs--1 text-600"></span>
                </div>
              </div>
            </div>
          </div>

          <div class="table-responsive scrollbar">
            <table class="table table-bordered table-striped fs--1 mb-0">
              <thead class="bg-200 text-900">
              <tr>
                <th v-for="column in config?.columns"
                    :key="column?.name"
                    :width="column?.width"
                    @click="makeSort((column?.sortable) ? column?.source : null)"
                    :align="['boolean', 'image', 'action'].includes(column?.type) ? 'center' : 'left'"
                    :class="{
                      'cursor-pointer': column?.sortable,
                      'text-center': ['boolean', 'image', 'action'].includes(column?.type),
                      'bg-info': filters?.sort_by === column?.source,
                    }"
                >
                  <div :class="{
                    'd-flex flex-nowrap' : true,
                    'text-align-center': ['boolean', 'image', 'action'].includes(column?.type),
                  }">

                    <div class="me-auto"> {{ column?.title }}</div>

                    <span v-if="column?.sortable" class="float-end align-center">
                    <span v-if="filters?.sort_by === column?.source && filters?.order_by === 'asc'">
                      <span class="fas fa-sort-up"></span>
                    </span>

                    <span v-if="filters?.sort_by === column?.source && filters?.order_by === 'desc'">
                      <span class="fas fa-sort-down"></span>
                    </span>

                    <span v-if="filters?.sort_by !== column?.source">
                      <span class="fas fa-sort"></span>
                    </span>
                  </span>
                  </div>
                </th>
              </tr>
              </thead>


              <tbody class="list">
              <tr v-for="item in data" :key="item.id">
                <td v-for="column in config?.columns" :key="column?.name"
                    valign="middle"
                    :align="['boolean', 'image', 'action'].includes(column?.type) ? 'center' : 'left'"
                    :class="{
                      'cursor-pointer': column?.sortable,
                      'text-center': ['boolean', 'image', 'action'].includes(column?.type),

                    }"
                >

                  <template v-if="column?.source === 'id'">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" :value="item[column?.source]"
                             v-model="selectedIds"
                             id="id-{{ item.id }}">
                      <label class="form-check-label" for="id-{{ item.id }}">
                        {{ item[column?.source] }}
                      </label>
                    </div>
                  </template>

                  <template v-else-if="column?.type === 'link'">
                    <a :href="item[column?.source]">
                      {{ item[column?.source] }}
                    </a>
                  </template>


                  <template v-else-if="column?.type === 'image'">
                    <div v-if="item[column?.source]">
                      <img :src="item[column?.source]" alt="..." style="height: 3rem"
                           @click="imgPreview(item[column?.source])"
                           class="img-thumbnail img-previewable"/>
                    </div>
                    <div v-else>
                      <span class="fas fa-image"></span>
                    </div>
                  </template>


                  <template v-else-if="column?.type === 'boolean'">
                    <div class="form-check form-switch">
                      <input class="form-check-input" type="checkbox" role="switch" :id="'switch-' + item.id"
                             :checked="item[column?.source] === true"
                             :disabled="booleanActionName(column?.source) === null"
                             @change="makeAction(
                                 booleanActionName(column?.source),
                                 column?.source,
                                  item.id
                            )"
                      >
                      <label class="form-check-label" :for="'switch-' + item.id">
                        <!--                        {{ item[column?.source] === true ? 'Yes' : 'No' }}-->
                      </label>
                    </div>
                  </template>


                  <template v-else-if="column?.type === 'action'">
                    <div class="d-flex flex-nowrap justify-content-center">
                      <button type="button" data-bs-toggle="tooltip" data-bs-placement="top"
                              aria-label="Edit" data-bs-original-title="Edit"
                              v-for="acc in actionsItems"
                              :class="{
                                'btn btn-link p-0 mx-1': true,
                                'text-primary': acc.type === 'edit',
                                'text-danger': acc.type === 'delete'
                              }"
                              @click="makeAction(acc.type, acc.route, item.id)"
                              :key="acc.type"
                      >
                        <span class="fas fa-eye" v-if="acc.type === 'view'"></span>
                        <span class="fas fa-edit" v-if="acc.type === 'edit'"></span>
                        <span class="fas fa-trash" v-if="acc.type === 'delete'"></span>
                      </button>
                    </div>
                  </template>


                  <template v-else>
                    {{ str_limit(item[column?.source], 65) }}
                    <br/>
                    <small class="text-muted bg-200 p-1"
                           v-if="column?.secondary_source && item[column?.secondary_source]">
                      {{ str_limit(item[column?.secondary_source], 65) }}
                    </small>
                  </template>
                </td>
              </tr>


              <tr v-if="loading">
                <td :colspan="config?.columns?.length">
                  <div class="d-flex justify-content-center">
                    <div class="spinner-border" role="status">
                      <span class="visually-hidden">Loading...</span>
                    </div>
                  </div>
                </td>
              </tr>
              <tr v-if="data.length === 0 && !loading">
                <td :colspan="config?.columns?.length">
                  <div class="d-flex justify-content-center">
                    <div class="text-center">
                      <span class="fas fa-exclamation-circle fs-1"></span>
                      <p class="fs-1">No data found!</p>
                    </div>
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="card-footer d-flex">
          <div class="d-flex">
            <label class="me-2 align-self-center">Showing</label>
            <select class="form-control form-control-sm" @change="makeLimit($event.target.value)">
              <option value="10">10</option>
              <option value="25">25</option>
              <option value="50">50</option>
            </select>
          </div>

          <nav class="ms-auto  d-flex">
            <button
                :class="{
                  'btn btn-sm btn-falcon-default me-1 ':true,
                  'disabled': pagination.has_prev === false
                }"
                type="button"
                title="Previous"
                :disabled="pagination.has_prev === false"
                @click="makePage(pagination?.current_page - 1)"
            >
              <span class="fas fa-chevron-left"></span>
            </button>

            <ul class="pagination  pagination-sm mb-0">
              <li v-for="page in pagination?.pages"
                  :key="page"
                  :class="{
                    'page-item': true,
                    'active': page === pagination?.current_page,
                  }"
              >
                <button
                    class="page-link"
                    type="button"
                    @click="makePage(page)"
                    :disabled="pagination?.current_page === page || page === '...'"
                >
                  {{ page }}
                </button>
              </li>
            </ul>

            <button
                :class="{
                  'btn btn-sm btn-falcon-default ms-1':true,
                  'disabled': pagination.has_next === false
                }"
                type="button"
                title="Next"
                :disabled="pagination.has_next === false"
                @click="makePage(pagination?.current_page + 1)"
            >
              <span class="fas fa-chevron-right"> </span>
            </button>
          </nav>
        </div>

      </div>

      <div class="modal fade" id="imagePreviewModel" tabindex="-1" role="dialog"
           aria-labelledby="imagePreviewModelLabel"
           aria-hidden="true">
        <div class="modal-dialog modal-lg  modal-dialog-centered rounded" role="document">
          <div class="modal-content">
            <button type="button" class="btn-close position-absolute" data-bs-dismiss="modal"
                    aria-label="Close"></button>

            <img :src="imagePreviewUrl" :alt="imagePreviewUrl" class="img-fluid"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import get_csrf from "@/utils/get_csrf";
import str_limit from "@/utils/str";

export default {
  props: {
    url: String,
  },

  data() {
    return {
      data: [],
      loading: true,
      error: null,
      configLoading: true,
      ajaxLoading: false,
      config: {},
      filters: {
        search: '',
        sort_by: '',
        order_by: 'asc',
        page: 1,
        limit: 10,
      },
      selectedIds: [],
      imagePreviewUrl: '',
      pagination: {
        current_page: 1,
        pages: [],
        has_next: false,
        has_prev: false,
        total: 0,
      },
      actionsItems: [],
    }
  },

  mounted() {
    this.getConfig();

  },

  methods: {
    str_limit,
    imgPreview(url) {
      this.imagePreviewUrl = url;
      window.$('#imagePreviewModel').modal('show');
    },
    booleanActionName(source) {
      if (source === 'is_active') {
        return 'status';
      } else if (source === 'is_featured') {
        return 'featured';
      } else {
        return null;
      }
    },
    getConfig() {
      fetch(this.url + 'config/').then(response => response.json()).then(data => {
        this.config = data;
        const actionColumn = data.columns.find(column => column.type === 'action');
        if (typeof actionColumn !== 'undefined') {
          this.actionsItems = actionColumn.actions;
        }
        this.configLoading = false;
        this.getData();
      }).catch(error => {
        this.error = error;
        this.configLoading = false;
      });
    },

    getData() {
      const url = new URL(window.location.origin + this.url + 'data/');

      url.searchParams.append('search', this.filters?.search);
      url.searchParams.append('sort_by', this.filters?.sort_by);
      url.searchParams.append('order_by', this.filters?.order_by);
      url.searchParams.append('page', this.filters?.page);
      url.searchParams.append('limit', this.filters?.limit);

      this.ajaxLoading = true;
      fetch(url).then(response => response.json()).then(data => {
        this.data = data.data;
        this.setPagination(data.total)


        this.ajaxLoading = false;
        this.loading = false;
      }).catch(error => {
        this.error = error;
        this.loading = false;
        this.ajaxLoading = false;
      });
    },

    makeSort(column) {
      if (column === null) {
        return;
      }
      if (this.filters.sort_by === column) {
        this.filters.order_by = this.filters.order_by === 'asc' ? 'desc' : 'asc';
      } else {
        this.filters.sort_by = column;
        this.filters.order_by = 'asc';
      }
    },
    makePage(page) {
      this.filters.page = page;
    },
    makeLimit(limit) {
      this.filters.limit = limit;
      this.filters.page = 1;
    },

    makeSearch(search) {
      // debounce
      this.filters.search = search;
      this.filters.page = 1;
    },

    makeAction(type, redirector_route, id) {
      if (type == 'delete' && !confirm('Are you sure?')) {
        return;
      }

      const url = new URL(window.location.origin + this.url + 'action/')

      const form = new FormData();
      form.append('id', id);
      form.append('route', redirector_route);
      form.append('type', type);

      this.ajaxLoading = true;
      fetch(url, {
        method: 'POST',
        body: form,
        headers: {
          "X-CSRFToken": get_csrf(),
        },
      }).then(response => response.json()).then(data => {
        if (data.type == 'redirect') {
          window.location.href = data.url;
        } else {
          this.ajaxLoading = false;
          this.getData();
        }
      }).catch(error => {
        this.error = error;
      });
    },

    deleteSelected() {
      if (!confirm('Are you sure?')) {
        return;
      }

      const url = new URL(window.location.origin + this.url + 'action/')

      const form = new FormData();
      form.append('ids', this.selectedIds);
      form.append('route', 'delete');
      form.append('type', 'bulk_delete');

      this.ajaxLoading = true;
      fetch(url, {
        method: 'POST',
        body: form,
        headers: {
          "X-CSRFToken": get_csrf(),
        },
      }).then(response => response.json()).then(data => {
        if (data.type == 'redirect') {
          window.location.href = data.url;
        } else {
          this.ajaxLoading = false;
          this.getData();
          this.selectedIds = [];
        }
      }).catch(error => {
        this.error = error;
      });
    },

    setPagination(total) {
      const limit = this.filters.limit;
      const current_page = this.filters.page;
      const total_pages = Math.ceil(total / limit || 1);
      let has_next = false;
      let has_prev = false;


      const pages = [];
      for (let i = 1; i <= total_pages; i++) {
        if (i <= 2 || i >= total_pages - 1 || (i >= current_page - 2 && i <= current_page + 2)) {
          pages.push(i);
        }
        if (i === 3 && current_page - 4 > 2) {
          pages.push('...');
        }
        if (i === total_pages - 2 && current_page + 4 < total_pages - 1) {
          pages.push('...');
        }

        if (i === 1 && current_page !== 1) {
          has_prev = true;
        }
        if (i === total_pages && current_page !== total_pages) {
          has_next = true;
        }
      }


      this.pagination = {
        current_page: current_page,
        pages: pages,
        has_next: has_next,
        has_prev: has_prev,
        total: total,
      }
    }

  },


  watch: {
    filters: {
      handler() {
        this.getData();
      },
      deep: true,
    },

    selectedIds() {
      console.log(this.selectedIds);
    }
  },


};
</script>


<style scoped lang="scss">
.form-switch {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-left: 0 !important;

  & .form-check-input {
    height: 1.2rem !important;
    width: 2.5rem !important;
    padding-left: 0;
    margin: 0 !important;

    &:checked {
      background-color: #2aa200;
    }

    &:focus {
      box-shadow: none;
    }

    &:focus-visible {
      box-shadow: none;
    }
  }

}


.btn-close {
  top: .5rem;
  right: .5rem;
  padding: .7rem;
  background-color: rgba(255, 0, 8, 0.5);
  border-radius: 50%;
}
</style>